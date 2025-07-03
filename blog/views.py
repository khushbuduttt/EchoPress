from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from .models import Tag, Category, Post
from .serializers import TagSerializer, CategorySerializer, PostListSerializer, PostDetailSerializer

# ------------- Tag List -------------#
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)

# ------------- Category List -------------#
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('name',)
    search_fields = ('name',)
# ------------- Post List -------------#
class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category','category__slug')
    search_fields = ('title',)
# ------------- Post Detail slug -------------#
class PostDetailSlugView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)

# ------------- Post Detail id -------------#
class PostDetailView(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

