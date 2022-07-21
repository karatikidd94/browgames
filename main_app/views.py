from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from . models import Game, Genre, Comment, Photo, Profile
from .forms import CommentForm
from django.db.models.signals import post_save
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import uuid
import boto3


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  id_list = game.genres.all().values_list('id')
  genres_game_doesnt_have = Genre.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  print(genres_game_doesnt_have)
  return render(request, 'games/detail.html', {
<<<<<<< HEAD
    'game': game,
    'comment_form': comment_form,
    'genres': genres_game_doesnt_have
  })

def assoc_genre(request, game_id, genre_id):
  Game.objects.get(id=game_id).genres.add(genre_id)
  return redirect('detail', game_id=game_id)

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['title', 'description', 'link', 'creator']
  success_url = '/games/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['title', 'description', 'link', 'creator']
  
class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'
  
@login_required
def add_comment(request, game_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.game_id = game_id
        new_comment.save()
    return redirect('detail', game_id=game_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = '__all__'

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/games/'

class GenreList(LoginRequiredMixin, ListView):
    model = Genre

class GenreCreate(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    success_url = '/genres/'

def profiles_index(request):
  profiles = Profile.objects.all()
  return render(request, 'profiles/index.html', { 'profiles': profiles })

def profile_detail(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  return render(request, 'profiles/detail.html', { 'profile': profile })
  
class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['username', 'bio', 'contact_info']
  success_url = '/profiles/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['username', 'bio', 'contact_info']
  success_url = '/profiles/'

class ProfileDelete(LoginRequiredMixin, DeleteView):
  model = Profile
  success_url = '/profiles/'

@login_required
def add_photo(request, game_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, game_id=game_id)
    except Exception as e:
      print('An error occured uploading file to S3')
      print(e)
  return redirect('detail', game_id=game_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_create')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
=======
    'game': game
  }) 
>>>>>>> c4e9473c994e565af92128c63db97ab40617d49c
