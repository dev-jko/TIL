# git flow 

## 프로젝트 시작할 때

* 깃허브 저장소 클론하기

    ```bash
    $ git clone <깃허브 저장소 주소>
    ```


## 새로운 작업을 시작할 때

1. `develop`브랜치로 이동

    ```bash
    $ git checkout develop
    ```

2. `새로운 브랜치` 생성하고 이동

    ```bash
    $ git checkout -b <새로운 브랜치 이름>
    ```

3. 작업 하기

    ```bash
    $ git add <파일 이름>
    $ git commit -m '<커밋 메세지>'
    ```
    
    푸시를 처음할 땐 푸시할 원격 저장소를 지정해줘야 한다.

    ```bash
    $ git push -u origin <브랜치 이름>
    ```

    그 후엔 `$ git push` 명령어만 사용하면 된다.

    ```bash
    $ git push
    $ git pull
    ```


## `feature` 브랜치에서 작업을 모두 마치고 `develop` 브랜치로 `merge` 할 때

1. `feature` 브랜치에서의 모든 작업이 완료되면 커밋과 푸시를 했는지 확인한다.

2. Github -> Pull requests로 접속한다.

3. `base: develop <- compare: <브랜치 이름>`을 선택하고 `Create pull request` 버튼을 누른다.

4. 브랜치 관련된 정보를 적고 `pull request`를 생성한다.


## 깃헙 풀리퀘스트 완료하기

1. 나중에 작성할께요