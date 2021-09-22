from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .pagination import PostPagination
from .models import Post, Category, Tag, User
from .serializers import PostSerializer, PostDetailSerializer , CategorySerializer, TagSerializer, AuthorSerializer


class PostApiView(generics.ListAPIView):
    """Get information about all posts"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('title', )
    filterset_fields = ('author__id', 'category__slug', 'tags__slug')

    def get_queryset(self):
        return Post.objects.all() if self.request.user.is_authenticated else Post.objects.filter(for_logged_users_only=False)



class PostDetailApiView(generics.RetrieveAPIView):
    """Get information about current post. Accessible by slug"""
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.all() if self.request.user.is_authenticated else Post.objects.filter(for_logged_users_only=False)


class CategoryApiView(generics.ListAPIView):
    """Get information about all categories"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagApiView(generics.ListAPIView):
    """Get information about all tags"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class AuthorApiView(generics.ListAPIView):
    """Get information about all authors"""
    serializer_class = AuthorSerializer
    queryset = User.objects.all()
