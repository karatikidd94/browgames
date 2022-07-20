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
    path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
    path('games/<int:game_id>/assoc_genre/<int:genre_id>/', views.assoc_genre, name='assoc_genre'),
    path('games/<int:game_id>/comment_update/<int:comment_id>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('games/<int:game_id>/comment_delete/<int:comment_id>/', views.CommentDelete.as_view(), name='comment_delete'),
    path('genres/', views.GenreList.as_view(), name='genres_index'),
    path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profiles/', views.profiles_index, name='profile_index'),
    path('profiles/create/', views.ProfileCreate.as_view(), name="profile_create"),
    path('profiles/<int:profile_id>/', views.profile_detail, name='profile_detail'),
]