from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', { 'games': games })