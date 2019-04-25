// browser에서 실행해야됨


const init = () => {
    postRequest();
    getRequest();
};

const getRequest = () => {
    const XHR = new XMLHttpRequest();
    XHR.open('GET', 'http://13.125.249.144:8080/ssafy/seoul/3/posts');
    XHR.send();
    XHR.addEventListener('load', e => {
        console.log(JSON.parse(e.target.response));
    });
};

const postRequest = () => {
    const body = {
        post: {
            title: 'ABC',
            content: 'DEF',
            author: 'G',
        }
    };
    const XHR = new XMLHttpRequest();
    XHR.open('POST', 'http://13.125.249.144:8080/ssafy/seoul/3/posts');
    XHR.setRequestHeader(
        'Content-type',
        'application/json;charset=UTF-8'
    );
    XHR.send(JSON.stringify(body));
    XHR.addEventListener('load', e => {
        console.log(JSON.parse(e.target.response));
    });
};

init();