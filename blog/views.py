from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post, Category

def detail(request, category_slug, slug):
    post =get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    return render(request, 'blog/detail.html', {'post': post})



def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts' : posts})



def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', { 'posts' : posts, 'query': query})
