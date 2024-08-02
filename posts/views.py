from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all()[:20]
    return render(request, 'posts.html', {'posts': posts})

    
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request, post_id):
    post=Post.objects.get(id=post_id)
    new_value=post.likes+1
    post.likes=new_value
    post.save()
    return HttpResponseRedirect('/')

def cancle(request):
    return HttpResponseRedirect('/')


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

import os

def confirm_delete(request, id):
    post = get_object_or_404(Post, id=id)
    template_path = os.path.join('your_app_name', 'confirm_delete.html')
    print(f"Template Path: {template_path}")
    return render(request, 'confirm_delete.html', {'post': post})


