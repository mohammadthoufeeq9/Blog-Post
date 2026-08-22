from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #Ensures that only logged-in users can access a class-based view. If the user isn't logged in, Django redirects them to the login page.
# userPassesTestMixin-Allows access to a class-based view only if a condition define returns True.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
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

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False