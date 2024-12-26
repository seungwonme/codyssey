# Conventions

- [Git Convention](#git-convention)
  - [Branch Type Description](#branch-type-description)
  - [Commit Message Convention](#commit-message-convention)
  - [Issue Label Setting](#issue-label-setting)
  - [References](#references)
- [Naming Convention](#naming-convention)
  - [File Naming Convention](#file-naming-convention)
  - [Function/Variable Naming Convention](#functionvariable-naming-convention)
  - [Component Naming Convention](#component-naming-convention)
- [Directory Convention](#directory-convention)
  - [src/app](#srcapp)
  - [src/containers](#srccontainers)
  - [src/components](#srccomponents)
  - [src/constants](#srcconstants)
  - [src/hooks](#srchooks)
  - [src/libs](#srclibs)
  - [src/services](#srcservices)
  - [src/states](#srcstates)
  - [src/types](#srctypes)
  - [References](#references-1)

## Git Convention

- 깃 브랜치 전략은 `GitFlow`를 따르며 이를 기반으로 한 브랜치 네이밍 컨벤션을 사용합니다.
- 브랜치 네이밍 형식: `feat/[기능]/#[이슈번호]`

### Branch Type Description

- feat (feature)  
  새로운 기능을 추가할 때 사용합니다.  
  예: `feat/login/#123`
- fix (bug fix)  
  버그를 수정할 때 사용합니다.  
  예: `fix/button-click/#456`
- refactor
  코드 리팩토링(기능 변경 없이 코드 구조 개선)을 할 때 사용합니다.  
  예: `refactor/auth-service/#102`
- chore
  프로젝트 유지 보수 작업(빌드 설정, 패키지 업데이트 등)을 할 때 사용합니다.  
  예: `chore/dependency-update/#104`
- style  
  코드 스타일(포맷 수정, 세미콜론 추가 등)을 수정할 때 사용합니다. 기능 수정은 포함되지 않습니다.  
  예: `style/css-format/#101`
- build  
  빌드 시스템이나 외부 종속성 변경(npm, yarn 등)에 사용합니다.  
  예: `build/webpack-config/#105`
- test  
  테스트 코드를 추가하거나 수정할 때 사용합니다.  
  예: `test/unit-tests/#103`
- docs (documentation)  
  문서 작업(README, 주석 등)을 할 때 사용합니다.  
  예: `docs/api-docs/#789`
- ci  
  CI 구성파일 및 스크립트 변경에 사용합니다.  
  예: `ci/github-actions/#106`
- perf (performance)  
  성능을 개선할 때 사용합니다.  
  예: `perf/api-speed/#107`
- revert  
  이전 커밋을 되돌릴 때 사용합니다.  
  예: `revert/login-bug/#108`

### Commit Message Convention

`git config --local commit.template .github/.gitmessage` 명령어를 통해 커밋 메시지 템플릿을 설정할 수 있습니다. 컨벤션 내용은 `.gitmessage` 파일에 작성되어 있습니다.

### Issue Label Setting

`github-label-sync --access-token <access_token> --labels .github/labels.json <owner>/<repo>`

### References

- [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [AngularJS Git Commit Message Conventions](https://gist.github.com/stephenparish/9941e89d80e2bc58a153)
- [Conventional Commits](https://www.conventionalcommits.org/ko/v1.0.0/)

## Naming Convention

### File Naming Convention

- `kebab-case` 로 작성합니다.
- `not-found.js`, `date-picker.js` 처럼, 최대한 간결하게 하되, 단어 사이는 [하이픈으로 연결](https://nextjs.org/docs/app/api-reference/file-conventions)합니다.

### Function/Variable Naming Convention

- `camelCase` 로 작성합니다.

### Component Naming Convention

- `PascalCase` 로 작성합니다.

## Directory Convention

nextjs에서는 여러 디렉토리 구조를 사용할 수 있지만, [`app` 외부에 프로젝트 파일 저장](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app)하는 방법을 사용합니다.

### src/app

- 라우팅 용으로 사용한다 (라우팅과 관련된 파일만 넣어놓자)
- e.g., `page.tsx`, `layout.tsx`, `opengraph-image.tsx`

### src/containers

- `page.tsx` 안에서 보여줄 컨텐츠들을 넣어놓는다
- 전역 상태관리 남발하지 말자 (props drilling을 막기 위해서는 `Jotai`를 사용하자)
- states.ts => 작은 단위의 상태관리
- e.g., tsx, css, state, hooks ...

### src/components

- 여러 페이지에서 공통으로 사용할 컴포넌트
- Button, Loading...

### src/constants

- 공통으로 사용 할 상수

### src/hooks

- 페이지 곳곳에서 사용되는 공통 훅

### src/libs

- 외부 라이브러리를 모아둔다. package.json때문에 쓸 일이 많지 않지만 튜닝해서 사용할 경우 발생

### src/services

- 각종 API 요청
- GET, POST, PATCH...

### src/states

- 페이지 곳곳에서 사용되는 state를 모아두는 곳

### src/types

- 각종 타입 스크립트의 정의가 들어가는 곳

### References

- https://miriya.net/blog/cliz752zc000lwb86y5gtxstu
- https://medium.com/@mertenercan/nextjs-13-folder-structure-c3453d780366
