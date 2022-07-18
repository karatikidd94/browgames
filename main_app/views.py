from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Game
from .forms import CommentForm



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  comment_form = CommentForm()
  return render(request, 'games/detail.html', {
    'game': game,
    'comment_form': comment_form
  })

class GameCreate(CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'
  
class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def add_comment(request, game_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.game_id = game_id
        new_comment.save()
    return redirect('detail', game_id=game_id)