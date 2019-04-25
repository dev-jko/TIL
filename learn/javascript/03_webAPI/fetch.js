// browser에서 실행해야됨

const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'posts';
const QUERY_STRING = '?postId=1';

const getRequest = URL => {
    fetch(URL)
        .then(response => response.json())
        .then(parseData => console.log(parseData));
};

const postRequest = URL => {
    fetch(URL, {
        method: 'POST',
        body: JSON.stringify({
            title: 'new post',
            content: 'new content',
            userId: 1
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
        .then(response => response.json())
        .then(parseData => console.log(parseData));
};

getRequest(DOMAIN + RESOURCE + QUERY_STRING);
postRequest(DOMAIN + RESOURCE + QUERY_STRING);

