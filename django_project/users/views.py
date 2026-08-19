from django.shortcuts import render,redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
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

@login_required #profile can open to login user if logout user access profile url it will redirect to login as we did updatedd in settings.py
def profile(request):
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm() 

    con = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',con)

 