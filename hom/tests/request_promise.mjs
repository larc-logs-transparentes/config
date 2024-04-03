import request from 'request';


async function requesPromise(options, callback) {

    var promise = new Promise((completed) => {
        request(options, function (error, response) {
            callback(error, response);
            completed(true);
        });
    });

    return promise;
}

export default requesPromise;