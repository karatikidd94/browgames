from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name="detail"),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_comment/', views.add_comment, name='add_comment'),
    path('games/<int:game_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name='assoc_genre'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('accounts/signup/', views.signup, name='signup'),
]