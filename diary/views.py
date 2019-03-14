from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from .models import Articles
from .forms import PostForm


def posts_list(request):
    search= request.GET.get('search','')
    if search:
        posts=Articles.objects.filter(body__icontains=search)
    else:
        posts = Articles.objects.all().order_by('-date')
    return render(request,'diary/startPage.html',context={'posts':posts})

def post_detail(request, slug):
    post= Articles.objects.get(slug__iexact=slug)
    return render(request, 'diary/post_detail.html', context={'post':post})

class PostUpdate(View):
    def get(self, request,slug):
        post=Articles.objects.get(slug__iexact=slug)
        bound_form= PostForm(instance=post)
        return render(request,'diary/post_update_form.html',context={'form':bound_form,'post':post})
    
    def post (self, request,slug):
        post=Articles.objects.get(slug__iexact=slug)
        bound_form= PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post=bound_form.save()
            return redirect(new_post)
        return render(request, 'diary/post_update_form.html', context={'form':bound_form,'post':post})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request,'diary/post_create_form.html', context={'form':form})
    
    def post(self,request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request,'diary/post_create_form.html', context={'form':bound_form})

class PostDelete(View):
    def get (self, request, slug):
        post=Articles.objects.get(slug__iexact=slug)
        return render(request, 'diary/post_delete_form.html', context={'post':post})

    def post (self, request, slug):
        post = Articles.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('post_list_url'))