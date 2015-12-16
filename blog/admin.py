#this file is like makefiles in C
#declare dependencies of models from relevant files here
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
