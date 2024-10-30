#!/bin/bash

clktck=$(getconf CLK_TCK)
read_time=$(date +"%T.%3N")

for pid in $(ps -C uvicorn,mongod,node -o pid --no-headers);
do
    stat=$(cat /proc/$pid/stat | awk '{print($2,","($14+$15))}')
    cmd_line=$(tr '\0' ' '  < /proc/$pid/cmdline)
    echo "$read_time,$pid,$stat,$clktck,$cmd_line" | tee -a $1

done