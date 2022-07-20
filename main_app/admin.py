from django.contrib import admin
from .models import Game, Comment, Genre, Photo, Profile

# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Photo)
admin.site.register(Profile)