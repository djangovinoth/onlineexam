from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def javalevel(request):
    return render(request,'tech/javalevel.html')

def javaexam(request):
    return render(request,'tech/java.html')
