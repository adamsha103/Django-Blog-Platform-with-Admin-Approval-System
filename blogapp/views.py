
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(status='Published').filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = BlogPost.objects.filter(status='Published')
    return render(request, 'home.html', {'posts': posts})

def submit_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'submit_post.html', {'form': form})
