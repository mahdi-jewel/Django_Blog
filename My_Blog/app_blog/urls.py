from django.urls import path
from . import views 

app_name = 'app_blog'

urlpatterns = [
    path('',views.blog_list.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unlike, name='unliked'),
    path('my_blog/', views.myBlog.as_view(), name='my_blog'),
    path('update_blog/<pk>/', views.updateBlog.as_view(), name='update_blog'),
    path('delete_blog/<pk>/',views.deleteBlog.as_view(), name='delete_blog')
]
