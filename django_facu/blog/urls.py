from django.urls import path
from .views import PostListView, \
    about, \
    UserPostListView, \
    CategoryPostListView, \
    PostDetailListView, \
    PresentationListView, \
    PresentationDetail, \
    PostDetailUpdateView, \
    PostDetailDeleteView, \
    PostCreateView, \
    PostUpdateView, \
    PostDeleteView, \
    PresentationUpdateView, \
    PresentationDeleteView, \
    PresentationListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('category/<str:get_category_display>', CategoryPostListView.as_view(), name='category-posts'),
    path('post/<int:pk>/', PostDetailListView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('postDetail/<int:pk>/', PresentationListView.as_view(), name='presentation'),
    path('postDetail/<int:pk>/update/', PostDetailUpdateView.as_view(), name='post-detail-update'),
    path('postDetail/<int:pk>/delete/', PostDetailDeleteView.as_view(), name='post-detail-delete'),
    path('presentation/<int:pk>/', PresentationDetail.as_view(), name='presentation-detail'),
    path('presentation/<int:pk>/update/', PresentationUpdateView.as_view(), name='presentation-update'),
    path('presentation/<int:pk>/delete/', PresentationDeleteView.as_view(), name='presentation-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', about, name='blog-about'),
]