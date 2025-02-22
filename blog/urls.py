from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page, name="login"),
    path('register/', register_page, name="register"),    
    path('blog/', home, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:id>/', blog_detail, name='blog_detail'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/<int:id>/update/', blog_update, name='blog_update'),
    path('blog/<int:id>/delete/', blog_delete, name='blog_delete'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/<int:id>/update/', post_update, name='post_update'),
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),
    path('logout/', logout_view, name='logout'),

]