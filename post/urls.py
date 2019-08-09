from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('tag/<str:slug>/', views.FilterByTagView.as_view(), name='filter-by-tag'),
]
