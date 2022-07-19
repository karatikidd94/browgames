# from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from . models import Game, Genre, Comment
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)