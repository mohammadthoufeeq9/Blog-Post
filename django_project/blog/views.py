from django.shortcuts import render
from django.views.generic import ListView
from .models import post


def home(request):
    context ={
        'posts':post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About_pg'})

class PostListView(ListView):
    model = post
    template_name='blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']# this will make the order of the posts from new to old.