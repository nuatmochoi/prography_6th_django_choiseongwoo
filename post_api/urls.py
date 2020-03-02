from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi


schema_url_v1_patterns = [
    url(r'^post/v1', include(('post.urls','post'), namespace='post')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="POST API",
        default_version='v1',
        description=
        '''
        프로그라피 6기 Django 사전과제입니다.
        
        Post API를 구현하였습니다.
        ''',
        contact=openapi.Contact(email="tjddn8770@ajou.com"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('post.urls')),

    url(r'^/v1/', include(('post.urls','post'), namespace='post_api')),
    # API document generation with  drf_yasg
    path('swagger<str:format>', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/',  schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1')
]
