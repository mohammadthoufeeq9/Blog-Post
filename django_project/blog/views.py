from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #Ensures that only logged-in users can access a class-based view. If the user isn't logged in, Django redirects them to the login page.
# userPassesTestMixin-Allows access to a class-based view only if a condition define returns True.
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
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
    paginate_by= 5  # Pagination: Splits posts into multiple pages instead of showing all posts at once.Django automatically handles which page to display.

class UserPostListView(ListView):
    model = post
    template_name='blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    paginate_by= 5  # Pagination: Splits posts into multiple pages instead of showing all posts at once.Django automatically handles which page to display.

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')

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
        post=self.get_object() # gets the current post/object
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/'
    def test_func(self):
            post=self.get_object() # gets the current post/object
            if self.request.user == post.author:  #self.request.user-gets the currently logged-in user.
                return True
            else:
                return False