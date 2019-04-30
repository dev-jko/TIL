const getUser = (id, callback) => {
    setTimeout(() => {
        const users = [
            {id: 1, githubId: 'nadarm'},
            {id: 2, githubId: 'nadarm2'}
        ];
        callback(users.find(user => user.id === id));
    }, 2000);
};

function getRepos(user, callback) {
    setTimeout(() => {
        const repos = [
            'TIL',
            'workshop',
            'JS'
        ];
        callback(repos);
    }, 2000);
}

const getCommits = (repo, callback) => {
    setTimeout(() => {
        const commits = [
            'init',
            'index.html'
        ];
        callback(commits);
    }, 2000);
};


console.log('start');
// const user = getUser(1, console.log);
const user = getUser(1, user => {
    console.log(user);
    getRepos(user, repos => {
        console.log(repos);
        getCommits(repos[0], commits => {
            console.log(commits.length);
        });
    });
});
console.log('end');
