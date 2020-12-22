# 장고(Django) 입문기
* 장고를 처음 공부하면서 만든 간단한 프로젝트입니다.
* Database는 SQLite3를 이용하였습니다.

## 홈(Home)
<ol>
    <li>기본 index 페이지를 myuser/views 의 home() method를 통하여 home.html 에 맵핑(mapping) 시켜놓음.</li>
    <li>로그인이 되어있지 않은 경우 로그인과 회원가입 버튼을 보여줌.</li>
    <li>로그인이 되어있을 경우 로그아웃 버튼만 보여줌.</li>
</ol> 

## 회원가입(Sign up)
<ol>
    <li>아이디와 패스워드 그리고 이메일을 입력 받을 수 있도록 함.</li>
    <li>패스워드의 경우 django.contrib.auth.hashers 의 make_password 메서드를 이용하여 암호화 하여 저장하도록 함.</li>
    <li>장고의 forms를 이용하여 제작함.</li>
</ol>

## 로그인(Login), 로그아웃(Logout)
<ol>
    <li>session 을 이용하여 로그인에 성공했을 시 로그인 상태를 유지시킴</li>

```    
request.session['user'] = form.user_id
```
<li>로그아웃 시 session의 user를 삭제함.</li>

```
del(request.session['user'])
```
</ol>

## 게시글(Board)
<ol>
    <li>session을 확인하여 로그인이 되어있지 않은 경우 게시글을 작성할 수 없으며, 로그인 화면으로 이동됨.</li>
    <li>Paginator를 이용하여 페이지를 관리함.</li>
</ol>

## 태그(Tag)
<ol>
    <li>게시글에 태그를 추가할 수 있음.</li>
    <li>get_or_create() Method를 이용하여 태그가 이미 DB에 있으면 그냥 가져오고 없으면 생성을 한 후 가져옴.</li>

```
Tag.objects.get_or_create(name=tag)
```
    
</ol>