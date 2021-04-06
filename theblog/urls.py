from django.urls import path
from .views import PostListView, PostDetailView, AddPostView, PostUpdateView, DeletePostView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('edit_post/<int:pk>', PostUpdateView.as_view(), name='edit-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
]