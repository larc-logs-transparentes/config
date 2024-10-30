import sys
from datetime import datetime,timedelta,MAXYEAR,timezone
from file_read_backwards import FileReadBackwards


class Node:

    def __init__(self):
        self._stack = list()
        self.startTime:datetime=datetime(year=1, month=1, day=1, tzinfo=timezone.utc)
        self.endTime:datetime=datetime(year=MAXYEAR, month=1, day=1, tzinfo=timezone.utc)
        self.parent = None
        self.logRecord:str = 'ROOT'
        self.serviceTimeMs:int = 0
        self.totalServicetime:int = 0
        self.nginxTimeMs:int = 0
        self.totalNginxTimeMs:int = 0
        self.serviceName:str = 'ROOT'
        self.url:str = ''
        self.baseUrl:str = ''
        self.bytes:int = 0
        self.httpStatus:int = 0
        self.overlapped:bool = False
        self.lastOverlapDurationMs:int = 0
        self.ancientOverlappingNode = None

    def appendNode(self, childNode) -> bool:
        result = False

        # Check if the given node (childNode) is really a child to this node
        if self.startTime < childNode.startTime and self.endTime > childNode.endTime:

            # If first child
            if len(self._stack) == 0:
                self.nginxTimeMs -= childNode.nginxTimeMs
                self.serviceTimeMs -= childNode.nginxTimeMs
                self.ancientOverlappingNode = None

            # Else, check for overlapped child (time intersection)
            elif self._stack[0].startTime < childNode.endTime:
                #print(f'DEBUG {self._stack[0].startTime} < {childNode.endTime} : TRUE')

                # If not previously overlapped
                if not self.ancientOverlappingNode:
                    # Reconstruct nginx and service time
                    self.nginxTimeMs += self._stack[0].nginxTimeMs
                    self.serviceTimeMs += self._stack[0].nginxTimeMs
                    # Calculate new service time
                    duration:timedelta = self._stack[0].endTime - childNode.startTime
                    self.lastOverlapDurationMs = int(duration.total_seconds() * 1000)
                    #print(f'DEBUG duration: {self.lastOverlapDurationMs}')
                    self.nginxTimeMs -= self.lastOverlapDurationMs
                    self.serviceTimeMs -= self.lastOverlapDurationMs
                    self.ancientOverlappingNode = self._stack[0]
                    #Flag overlapping nodes
                    childNode.overlapped = True
                    self._stack[0].overlapped = True
                
                # Currently under overlap situation
                else:
                    # Reconstruct nginx and service time
                    self.nginxTimeMs += self.lastOverlapDurationMs
                    self.serviceTimeMs += self.lastOverlapDurationMs
                    # Calculate new service time
                    duration:timedelta = self.ancientOverlappingNode.endTime - childNode.startTime
                    self.lastOverlapDurationMs = int(duration.total_seconds() * 1000)
                    #print(f'DEBUG NEW duration: {self.lastOverlapDurationMs}')
                    self.nginxTimeMs -= self.lastOverlapDurationMs
                    self.serviceTimeMs -= self.lastOverlapDurationMs
                    #Flag overlapping nodes
                    childNode.overlapped = True

            else:
                self.nginxTimeMs -= childNode.nginxTimeMs
                self.serviceTimeMs -= childNode.nginxTimeMs
                self.ancientOverlappingNode = None

            # Add childNode to stack
            self._stack.insert(0, childNode)
            childNode.parent = self
            result = True


        return result
    
    def loadFromRecord(self, logRecord:str):
        self.logRecord = logRecord
        array = logRecord.split()

        self.serviceName = array[3]
        self.url = f'{array[4]} {array[5]} {array[6]}'
        self.bytes = int(array[8])
        self.httpStatus = int(array[7])

        urlDecoded = array[5].split('?')
        self.baseUrl = urlDecoded[0]

        nginxTimeSecs:float = float(array[len(array)-3])
        self.totalServicetime = self.serviceTimeMs = int(float(array[len(array)-2]) * 1000)
        self.totalNginxTimeMs = self.nginxTimeMs = int(nginxTimeSecs * 1000)

        self.endTime = datetime.fromisoformat(array[0])
        timeDelta = timedelta(seconds=nginxTimeSecs)
        self.startTime = self.endTime - timeDelta

    def info(self) -> str:
        totalServiceTimeStr:str = ''
        totalNginxTimeStr:str = ''
        overlappedStr:str=''

        if len(self._stack) > 0:
            totalServiceTimeStr = f'({self.totalServicetime})'
            totalNginxTimeStr = f'({self.totalNginxTimeMs})'

        if self.overlapped: overlappedStr = '(OvrLpd)'

        return f'Info: {self.startTime} - {self.endTime} {self.serviceName} serviceTime: {self.serviceTimeMs}{totalServiceTimeStr}{overlappedStr} nginxTime: {self.nginxTimeMs}{totalNginxTimeStr} {self.url}'

    def printTreeInfo(self, header:str, file):
        file.write(f'{header}-{self.info()} - children: {len(self._stack)}\n')

        for child in self._stack:
            child.printTreeInfo(header+ '  |', file)


class StatsManager:

    def __init__(self) -> None:
        self._statsDict: dict = dict()
    
    def addNode(self, name:str, node:Node):
        stats = self._statsDict.get(name, None)
        if not stats:
            stats = list()
            self._statsDict[name] = stats
        
        stats.append(node)

    def generateStats(self, file):
        file.write(f'Name,Total(ms)/Samples,AVG (ms)\n')
        for key,value in self._statsDict.items():
            total:int = 0
            samples:int = len(value)
            for node in value:
                total += node.serviceTimeMs
            
            file.write(f'{key},{total}/{samples},{total/samples}\n')


def main():
    if len(sys.argv) < 4:
        print('Missing filename argument')
        print('Usage: python analyze.py <IN:nginx file name> <OUT:tree dump file name> <OUT:Stats file name>')
        exit(1)

    fileName = sys.argv[1]

    rootNode = Node()
    currentParentNode = rootNode
    nodeList:list = list()
    statsMgr:StatsManager = StatsManager()

    with FileReadBackwards(fileName, encoding="utf-8") as file:
        for line in file:
            node = Node()
            node.loadFromRecord(line)
            nodeList.append(node)
            statsMgr.addNode(f'{node.serviceName} ALL', node)
            statsMgr.addNode(f'{node.serviceName} {node.baseUrl} http:{node.httpStatus}', node)

            added = currentParentNode.appendNode(node)

            while not added:
                print(f'Trying parent ...')
                currentParentNode = currentParentNode.parent
                added = currentParentNode.appendNode(node)

            print(f'Added: {node.info()}')
            currentParentNode = node
    
    with open(sys.argv[2], 'w') as treeFile:
        rootNode.printTreeInfo('', treeFile)

    with open(sys.argv[3], 'w') as statsFile:
        statsMgr.generateStats(statsFile)
            

def test():
    if len(sys.argv) < 4:
        print('Missing filename argument')
        print('Usage: python analyze.py <IN:nginx file name> <OUT:tree dump file name> <OUT:Stats file name>')
        exit(1)

    nginxFile = sys.argv[1]
    print(f'Nginx file: {nginxFile}')

    date_str = '2024-08-26T22:35:08.042+00:00'   
    format_str = '%Y-%m-%d'  
    datetime_obj = datetime.fromisoformat(date_str)  
    print(datetime_obj.date())  

    logRecord= "2024-08-26T22:35:08.042+00:00 - 192.168.128.4 TL-MGR \"POST /insert-leaf HTTP/1.1\" 200 120 \"-\" \"python-requests/2.31.0\" 0.002 0.001 ."
    array = logRecord.split()

    #for val in array:
    #    print(f'Val: {val}')
    print(f'First: {array[0]} - start delta: {float(array[len(array)-3])}')

    endTime = datetime.fromisoformat(array[0])
    timeDelta = timedelta(seconds=float(array[len(array)-3]))
    startTime = endTime - timeDelta

    print(f'start: {startTime} - endtime: {endTime} - sooner?: {endTime > startTime}')

    node = Node()
    node.loadFromRecord('2024-08-26T22:35:07.972+00:00 - 192.168.128.4 TL-MGR "POST /insert-leaf HTTP/1.1" 400 50 "-" "python-requests/2.31.0" 0.006 0.006 .')

    print(f'Node endTime é menor ou igual: {node.endTime <= endTime}')
#    with FileReadBackwards("profile-1724711707720-nginx.log", encoding="utf-8") as file:
#        for line in file:
#            print(line)




if __name__ == '__main__':
    #test()
    main()