// browser에서 실행해야됨

const DOMAIN = 'https://jsonplaceholder.typicode.com/';
const RESOURCE = 'comments';
const QUERY_STRING = '?postId=1';
const XHR = new XMLHttpRequest();
XHR.open('GET', DOMAIN + RESOURCE + QUERY_STRING);
XHR.send();
XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});



XHR.open('POST', DOMAIN + RESOURCE + QUERY_STRING);
XHR.setRequestHeader(
    'Content-Type',
    'application/json;charset=UTF-8'
);
XHR.send(
    JSON.stringify({
        title: "NewPOST",
        body: "This is New post",
        userId: 1,
    })
);
XHR.addEventListener('load', e => {
    const parseData = JSON.parse(e.target.response);
    console.log(parseData);
});
