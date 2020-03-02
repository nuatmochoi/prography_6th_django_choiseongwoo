from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer
from .serializers import UserSerializer
from .models import Post
from django.contrib.auth.models import User
from rest_framework import permissions
from .permission import IsUserOrReadOnly
from rest_framework.pagination import PageNumberPagination

class PostPageNumberPagination(PageNumberPagination):
    page_size = 2

class Post_list(ListAPIView):
    '''
    게시물 목록을 반환하는 API

    ---
    ## `/post/`
    ## 내용
        - id: 게시물 고유번호
        - user: 작성한 유저
        - title: 게시물 제목
        - contents: 게시물 내용
        - create_data: 게시물 생성 날짜
        - update_date: 게시물 최종 수정 날짜
        - url: 각 게시물의 url
        - update_url: 게시물 수정 url
        - delete_url: 게시물 삭제 url
    '''
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    pagination_class = PostPageNumberPagination

class Post_detail(RetrieveAPIView):
    '''
    게시물 세부사항을 반환하는 API

    ---
    ## `/post/<int:pk>/`
    ## 내용
        - id: 게시물 고유번호
        - user: 작성한 유저
        - title: 게시물 제목
        - contents: 게시물 내용
        - create_data: 게시물 생성 날짜
        - update_date: 게시물 최종 수정 날짜
        - url: 각 게시물의 url
        - update_url: 게시물 수정 url
        - delete_url: 게시물 삭제 url
    '''
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class Post_update(UpdateAPIView):
    '''
    게시물을 수정하는 API

    ---
    ## `/post/<int:pk>/update/`
    ## 내용
        - title: 수정된 게시물 제목
        - contents: 수정된 게시물 내용
    ## 세부사항
        - 게시물을 작성한 사람만 수정 가능
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,IsUserOrReadOnly)

class Post_delete(DestroyAPIView):
    '''
    게시물을 삭제하는 API

    ---
    ## `/post/<int:pk>/delete/`
    ## 세부사항
        - 게시물을 작성한 사람만 삭제 가능
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,IsUserOrReadOnly)

class Post_create(CreateAPIView):
    '''
    게시물을 작성하는 api

    ---
    ## `/post/create/`
    ## 세부사항
        - 로그인한 상황에서만 작성 가능
    '''
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserList(ListAPIView):
    '''
    전체 유저의 목록을 반환하는 API

    ---
    ## `/user/`
    ## 내용
        - id: 유저 고유번호
        - username: 유저 닉네임
        - posts: 유저가 작성한 게시물 목록
    ## 세부사항
        - `/rest-auth/registration/` : 회원가입 API
        - `/rest-auth/login/` : 로그인 API
        - `/rest-auth/logout/` : 로그아웃 API
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    '''
    유저 세부사항을 반환하는 API

    ---
    ## `/user/<int:pk>/`
    ## 내용
        - id: 유저 고유번호
        - username: 유저 닉네임
        - posts: 유저가 작성한 게시물 목록
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer