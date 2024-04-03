import requestPromise from './request_promise.mjs'


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});

var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:9090/',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});

var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8000/',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);

    var obj = JSON.parse(response.body);
    if (obj.status != "ok") throw new Error(`Não veio a resposta esperada: ${obj.status}`);
});
