from django.shortcuts import render

# Create your views here.

#post_list function takes in request
#returns render of the 'blog/post_list.html' template
def post_list(request):
	return render(request, 'blog/post_list.html', {})