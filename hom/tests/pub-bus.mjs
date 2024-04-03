import requestPromise from './request_promise.mjs'


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/find_by_merkletree_index_range?initial_index=2&final_index=4&election_id=545',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/find_by_info?UF=AC&zona=2&secao=88',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/distinct_eleicoes',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/distinct_uf?id_eleicao=545',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/distinct_municipio?id_eleicao=545&UF=AC',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/distinct_zona?id_eleicao=545&UF=AC&municipio=BUJARI',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});


var options = {
    'method': 'GET',
    'url': 'http://127.0.0.1:8080/bu/distinct_secao?id_eleicao=545&UF=AC&zona=9&municipio=BUJARI',
    'headers': {
    }
};
await requestPromise(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
});
