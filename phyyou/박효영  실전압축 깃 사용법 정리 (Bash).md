# 박효영 : 실전압축 깃 사용법 정리 (Bash)

---

---

## bash 기초 명령어  

- ### 디렉터리 및 파일  
  
  - cd ~ : 홈 디렉터리로 이동  
  - mkdir * : 새 디렉터리 생성  
  - cd .. : 부모 디렉터리로 이동  
  - pwd : 현재 경로 보여주기  
  - ls : 디렉터리 내용 표시  
  - ls -l : 옵션을 사용해 디렉터리 폴더 상세정보 까지 표시  
  - ls -a : 옵션을 사용해 디렉터리의 숨겨진 파일이나 폴더를 표시  
  - rm -rf : 디렉터리의 하위 내용 까지 확인없이 삭제  
  - cat (file) : 터미널 안에 파일 내용을 표시  
  
- ### 터미널

  - clear : 터미널 창의 내용을 지움  
  - exit : 터미널 종료  

---

##  깃 기초  

- ### 환경  

  - git config user.name : 깃 환경에서 이름을 지정  

  - git config user.email : 이메일 지정  

    >--global 추가시 모든 환경에 지정됨  

  - git init : 현재 위치에서 지역 저장소 생성  

  - git status : 깃 상태 확인  

- ### 커밋, 스테이지  

  - git add : 파일을 스테이지에 올림 . 을 넣으면 현재 디렉토리의 모든 파일을 스테이지에 올림  
  - git commit -m "ch01" : 커밋 메시지 "ch01"을 붙여 커밋  
  - git commit -am "ch01" : 커밋 메시지 ch01을 붙여 스테이징과 커밋을 동시에 실행  
  - git log : 커밋 정보를 확인  
  - git diff : 최근 버전과 작업 폴더의 수정 파일 사이 차이를 보여줍니다.  
  - git checkout _커밋 해시_ : 지정한 커밋 해시로 이동  
  - git reset ^HEAD: 가장 최근 커밋을 취소  
  - git reset _커밋 해시_ : 지정한 커밋 해시로 이동하고 이후 커밋은 취소  
  - git revert _커밋 해시_ : 지정한 커밋 해시의 변경 이력 취소  

- ### 브랜치, 머지  

  - git branch : 새로운 브랜치 생성  
  - git checkout : 브랜치로 체크아웃  
  - git log --branches --graph : 커밋 로그에 각 브랜치의 커밋을 그래프로 표시  
  - git merge master : master 브랜치와 다른 브랜치를 병합  
  - git init _디렉터리 이름_ : 디렉터리를 생성함과 동시에 지역 저장소로 생성  
  - git reset _브랜치 이름_ _커밋 해시_ : 현재 커밋을 다른 브랜치에 잇는 c1 커밋으로 되돌림  
  - git branch -d : 병합이 끝난 브랜치를 삭제  
  - git stash : 커밋하지 않을 수정 내용을 따로 보관하여 숨김  
  - git stash pop : 숨겼던 내용을 다시 꺼냄  

- ### 원격 저장소  
  
  - git remote add origin _저장소 주소_ : 원격 저장소에 연결  
  - git remote -v : 연결되었는지 확인  
  - git push -u origin master : 처음으로 푸쉬할때 푸쉬  
  - git push (orign master) : 처음 이후로 푸쉬  
  - git pull : 커밋 가져오기  
  - ssh key-gen : ssh연결에 필요한 ssh키 생성  

- ### 협업  

  - git clone : 원격저장소에 있는 내용 복제  

  - git fetch : 원격 브랜치에 어떤 변화가 있는지 정보만 복제  

  - git checkout FETCH_HEAD : 변화를 설명하는 FETCH_HEAD로 체크아웃  

  - git merge FETCH_HEAD : 페치 내용과 로컬 브랜치 병합  

  - git checkout -b : 만드는 동시에 체크아웃  

***

- 추가로 내가 발생했던 에러에 관한 글을 스크랩 해봤다.

# git push, pull (fatal: refusing to merge unrelated histories) 에러

henry-jo 2018. 1. 14. 17:10

원격 저장소를 remote로 설정하고 바로 push를 하면 몇가지 오류가 발생할 수도 있다.

예를 들어 아래와 같은 오류 메시지이다.

```
 ! [rejected]        master -> master (non-fast-forward)error: failed to push some refs to 'https://github.com/huusz/test.git'
```



**rejected** : push가 거부되었다.

**master -> master** : 로컬 저장소의 master 브랜치의 변경 사항을 원격 저장소의 master 브랜치에 반영하려 했는데

**non-fast-forward** : 원격 저장소의 master 브랜치가 로컬 저장소의 버전보다 이전 버전이 아니다. 라는 의미이다.



즉, 오류가 발생한 원인은 github에서 새로운 프로젝트를 생성하면서 만들어진 원격 저장소의 readme.md

파일때문 일 것이다. 더 정확히 말하면 readme.md 파일의 존재가 문제가 되는 것이 아니고, 원격 저장소에서

이루어진 readme.md를 추가하는 커밋이 로컬 저장소의 커밋 로그에는 없기 때문이다.



push 명령은 로컬 저장소의 commit 목록과 원격 저장소의 commit 목록을 비교한다.

그런 다음 원격 저장소의 마지막 commit id와 동일한 commit id를 가진 로컬 저장소의 commit 시점을

찾아낸 뒤, 원격 저장소의 마지막 커밋과 연결한다.

원격 저장소의 첫번째 commit이자 마지막 commit인 readme를 추가하는 commit이 원격 저장소에는

존재하지 않고, 따라서 **현 상태에서는 둘을 연결할 수 없다.**



이 상황을 해결하는 방법에는

1. 원격 저장소를 삭제하고 다시 만든다. (readme.md 파일을 없애고 다시 저장소를 만든다.)
2. fetch나 pull 명령어로 원격 저장소의 마지막 commit을 로컬 저장소의 commit로그의 맨 앞으로 받아온다.



두번째 방법으로 해결해본다.



하지만 pull 명령어를 실행하면 아래와 같은 오류가 발생한다.

\>> git pull origin master

-- fatal: refusing to merge unrelated histories



에러 내용은 원격 저장소의 master 브랜치에서 로컬 저장소의 FETCH_HEAD를 merge하는 것이 거부되었다.

commit 히스토리가 서로 관련이 없다는 뜻이다. 즉, 서로 관련성이 없기 때문에 merge할 수 없다는 것이다.



pull 명령어는 fetch + merge 작업을 한번에 처리하는 명령어이다. 현 상황은 fetch는 되었지만, merge가

되지 않은 상태이다.

기본적으로 merge는 원격 저장소와 로컬 저장소가 공통으로 가지고 있는 commit지점이 존재해야 한다.

그 지점부터 병합을 시도하기 때문이다. 애초에 공통되는 commit이 없기때문에 pull 명령어를 사용할 수

없는 것이다.



> 해결하기 앞서 상황을 이해하기 위해 pull과 fetch의 개념을 살펴보자.

fetch는 원격 저장소에 있는 내용을 가져오지만 자동으로 내 로컬 저장소에 merge하지 않는다.

원격 저장소의 내용을 확인만 하고 로컬에 merge하고 싶지 않을 때는 fetch를 사용한다.



HEAD에는 가장 마지막에 행해진 commit정보가 담긴다. 마찬가지로 FETCH_HEAD는 원격 저장소의

가장 최신 commit 이력이 담기게 된다.

FETCH_HEAD는 이름 없는 브랜치로 로컬에 가져오게 된다. 이 브랜치는 FETCH_HEAD로 checkout도

가능하다.



pull 명령어는 원격 저장소에 있는 내용을 가져올 뿐만 아니라, 자동으로 로컬 저장소에 merge한다.

즉, git pull 명령어는 git fetch + merge FETCH_HEAD인 셈이다.



> 복잡하고 긴 설명 끝에 결론은 어쨌든 연결되는 **공통된 커밋 포인트가 없다**는 것이다.

이 상황을 해결하기 위한 방법에도 2가지 방법이 존재하는데,

1. git clone 명령어를 통해 원격 저장소를 복제해온다.
2. pull 명령어에 옵션을 추가해 강제로 pull 한다.



두번째 방법을 택해 pull 명령어에 옵션을 줘서 가져오면 간단하게 해결된다.

git pull origin (branchname) --allow-unrelated-histories

※ 출처 : https://huusz.github.io/2017/Git/GIT/01.git-connect-github/