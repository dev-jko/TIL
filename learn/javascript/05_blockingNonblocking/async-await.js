const getUser = id => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const users = [{id: 1, githubId: 'nadarm'}, {id: 2, githubId: 'nadarm2'}];
            if (users) resolve(users.find(user => user.id === id));
            else reject(new Error('ERROR'));
        }, 2000);
    });
};

function getRepos(user) {
    return new Promise(((resolve, reject) => {
        setTimeout(() => {
            const repos = ['TIL', 'workshop', 'JS'];
            if (repos) resolve(repos);
            else reject(new Error('Error'));
        }, 2000);
    }));
}

const getCommits = repo => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const commits = ['init', 'index.html'];
            if (commits) resolve(commits);
            else reject(new Error('Error'));
        }, 2000);
    });
};


async function main() {
    try {
        console.log('start');
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length);
        console.log('end');
    } catch (e) {
        console.error(e);
    }
}

main();