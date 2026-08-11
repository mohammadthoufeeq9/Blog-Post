from django.shortcuts import render
posts=[
    {
        'author':'Thoufeeq',
        'title':'First blog post',
        'context':'Human emotions',
        'date':'24,feb,2020'
    },
    {
        'author':'Mohammad Thoufeeq',
        'title':'human culture',
        'context':'Human emotions and responsibility',
        'date':'18-march-2020'
    }
] 

def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About_pg'})