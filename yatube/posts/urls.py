from django.urls import path


from . import views


app_name = 'posts'


urlpatterns = [
    # Гдавная страница
    path('', views.index, name='index'),
    path('group/', views.group_posts, name='group_list'),
]