from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()#it hashs the password
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

class customLogout(LogoutView):
    def dispatch(self, request, *args, **kwargs):#* adds additional positional arguments`(func(a,b))` and ** adds keyword arguments like id=4
        messages.success(request,f'You have been logged out.')
        return super().dispatch(request, *args, **kwargs)