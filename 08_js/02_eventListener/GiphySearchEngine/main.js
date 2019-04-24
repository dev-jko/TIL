const imgRequest = keyword => {
    const result = document.querySelector('#result-area');
    const KEY = 'FhdniIjsJyo3DmrgHbVZk67LkwYFeohf';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;
    const AJAXCall = new XMLHttpRequest();
    AJAXCall.open('GET', URL);
    AJAXCall.send();
    AJAXCall.addEventListener('load', e => {
        const rowData = e.target.response;
        const parsedData = JSON.parse(rowData);
        result.innerHTML = null;
        for (d of parsedData.data) {
            const element = document.createElement('img');
            element.classList.add('container-image');
            element.src = d.images.fixed_height.url;
            element.alt = d.title;
            result.appendChild(element);
        }
    });
};

const init = () => {
    const inputArea = document.querySelector('#js-userinput');
    const button = document.querySelector('#js-go');

    inputArea.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            imgRequest(inputArea.value);
        }
    });

    button.addEventListener('click', e => {
        imgRequest(inputArea.value);
    });
};


init();

