const todoBox = document.querySelector('#todo_box');

const createTodoCard = (inputText, completed = false) => {
    const todoCard = document.createElement('div');
    todoCard.classList.add('ui', 'todo-item', 'segment');
    if (completed) todoCard.classList.add('secondary');
    const wrapper = document.createElement('div');
    wrapper.classList.add('ui', 'checkbox');
    const input = document.createElement('input');
    input.setAttribute('type', 'checkbox');
    input.checked = completed;
    const label = document.createElement('label');
    label.innerHTML = inputText;
    if (completed) label.classList.add('completed-label');
    const deleteIcon = document.createElement('i');
    deleteIcon.classList.add('close', 'icon', 'delete-icon');
    wrapper.appendChild(input);
    wrapper.appendChild(label);
    todoCard.appendChild(wrapper);
    todoCard.appendChild(deleteIcon);
    input.addEventListener('change', e => {
        if (e.target.checked) {
            label.classList.add('completed-label');
            todoCard.classList.add('secondary');
        } else {
            label.classList.remove('completed-label');
            todoCard.classList.remove('secondary');
        }
    });
    deleteIcon.addEventListener('click', e => {
        todoCard.remove();
    });
    return todoCard
};

const inputEvent = (inputText, completed = false) => {
    const todoCard = createTodoCard(inputText, completed);
    todoBox.appendChild(todoCard);
};

const fetchData = URL => {
    fetch(URL)
        .then(res => res.json())
        .then(todos => {
            for (const todo of todos) {
                inputEvent(todo.title, todo.completed);
            }
        });
};

const reverseTodos = () => {
    const todos = Array.from(document.querySelectorAll('.todo-item')).reverse();
    while (todoBox.firstChild) {
        todoBox.removeChild(todoBox.firstChild);
    }
    for (todo of todos) {
        todoBox.appendChild(todo);
    }
};


const input = document.querySelector('#add_todo_input');
input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && input.value) {
        inputEvent(input.value);
        input.value = null;
    }
});

const btn = document.querySelector('#add_todo_btn');
btn.addEventListener('click', e => {
    if (input.value) {
        inputEvent(input.value);
        input.value = null;
    }
});

const reverseBtn = document.querySelector('#reverse_btn');
reverseBtn.addEventListener('click', e => {
    reverseTodos();
});


const fetchBtn = document.querySelector('#fetch_btn');
fetchBtn.addEventListener('click', e => {
    fetchData('https://koreanjson.com/todos');
});
