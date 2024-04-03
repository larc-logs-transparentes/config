import requestPromise from './request_promise.mjs'
import fs from 'fs';


var options = {
    'method': 'POST',
    'url': 'http://127.0.0.1:9090/bu/create',
    'headers': {
    },
    formData: {
        'file': {
            'value': fs.createReadStream('o00407-0101500020065.bu'),
            'options': {
                'filename': 'o00407-0101500020065.bu',
                'contentType': null
            }
        }
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'POST',
    'url': 'http://127.0.0.1:9090/tree/commit-all-trees',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});

