from rest_framework import serializers
from .models import Post, Category, Tag, User


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tags', 'category', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
