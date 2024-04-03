import requestPromise from './request_promise.mjs'


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/tree/data-proof?tree_name=teste_545&index=2',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/tree/inclusion-proof?tree_name=teste_545&index=2',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/tree/all-consistency-proof?tree_name=teste_545',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});
