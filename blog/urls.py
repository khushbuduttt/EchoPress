from django.urls import path,include
from .views import TagListView, CategoryListView, PostListView, PostDetailView, PostDetailSlugView

urlpatterns = [
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>/', PostDetailSlugView.as_view(), name='post-detail-slug'),
    path('post-detail/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
]
