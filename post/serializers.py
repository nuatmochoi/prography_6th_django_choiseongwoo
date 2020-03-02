from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, PrimaryKeyRelatedField, DateTimeField
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','contents','create_date','update_date')

class PostDetailSerializer(ModelSerializer):
    create_date = DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')
    update_date = DateTimeField(format='%Y-%m-%d %H:%M:%S.%f')
    url = HyperlinkedIdentityField(
        view_name='post_detail',
        lookup_field='pk'
    )

    update_url = HyperlinkedIdentityField(
        view_name='post_update',
        lookup_field='pk'
    )

    delete_url = HyperlinkedIdentityField(
        view_name='post_delete',
        lookup_field='pk'
    )

    class Meta:
        model = Post
        fields = ('id','user','title','contents','create_date','update_date','url','update_url','delete_url')

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','contents','create_date')

class UserSerializer(ModelSerializer):
    posts = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username','posts')