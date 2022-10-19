from django.urls import path


from . import views


urlpatterns = [
    # Гдавная страница
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
]