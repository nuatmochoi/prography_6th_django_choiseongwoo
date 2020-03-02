# 프로그라피 6기 Django 사전과제 - Post API 

Django REST Framework를 이용하여 게시물 api를 개발하였습니다.

## 필수 요구사항

- [전체 게시물 목록](http://tjddn8770.pythonanywhere.com/) 
- [게시물 세부 사항](http://tjddn8770.pythonanywhere.com/post/1/)
- [게시물 작성](http://tjddn8770.pythonanywhere.com/post/create/)
- [게시물 수정](http://tjddn8770.pythonanywhere.com/post/1/update/)
- [게시물 삭제](http://tjddn8770.pythonanywhere.com/post/1/delete/)

## 필수 요구사항 외 

- [API 문서](http://tjddn8770.pythonanywhere.com/docs/) - drf-yasg 사용
- Pagination : 게시물은 페이지마다 2개씩 출력
- 게시물 접근 권한
    - 게시물 목록 및 세부 사항 : 모든 User가 접근 가능
    - 게시물 작성 : 로그인한 User만 작성 가능
    - 게시물 수정 및 삭제 : 해당 게시물을 작성한 User만 작성 가능
- 게시물에 포함된 항목
    - 게시물 ID
    - 게시물을 작성한 User
    - 게시물의 제목
    - 게시물의 내용
    - 게시물 생성 날짜
    - 게시물 최종 수정 날짜
    - 게시물 상세 url
    - 게시물 수정 url
    - 게시물 삭제 url
- [회원가입](http://tjddn8770.pythonanywhere.com/rest-auth/registration/)
- [로그인](http://tjddn8770.pythonanywhere.com/rest-auth/login/)
- [로그아웃](http://tjddn8770.pythonanywhere.com/rest-auth/logout/)
- [전체 유저 목록](http://tjddn8770.pythonanywhere.com/user/) - 유저별 작성한 게시물 확인 가능
- [유저 세부 사항](http://tjddn8770.pythonanywhere.com/user/1/)

## API 사용 순서

1. 회원가입
2. 로그인
3. 게시물 작성
4. 게시물 수정 및 삭제