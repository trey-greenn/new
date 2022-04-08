from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from blog.models import Post



def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'mysite/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'mysite/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")