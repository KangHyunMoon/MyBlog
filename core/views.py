
from core.models import Post
from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', dict(posts = posts))

def Hello_World(request):
    return HttpResponse("Hello World")

def Bye_World(request):
    return HttpResponse("Bye World")

def article_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'article_detail.html', dict(post=post))
