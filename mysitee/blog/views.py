
#blog/views.py

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	allpost=Post.objects.all()
	if 'category' in request.GET:
		#allpost=allpost.filter(category=int(request.GET.get('category')))
		allpost=Category.objects.get(pk=int(request.GET.get('category'))).allpost.all()
	return render(request,'index.html',{'posts': allpost.order_by('-posttime')})

def view_post(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})