from django.shortcuts import render

from django.utils import timezone

#add the Post model from the current directory
from .models import Post



#post_list function takes in request
#returns render of the 'blog/post_list.html' template
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
	return render(request, 'blog/post_list.html', {'posts': posts})
