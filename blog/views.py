from django.shortcuts import render
from blog.models import BlogPost

def create_blog_view(request):

    context = {}

    return render(request, 'blog/create_post.html', context)

