from django.shortcuts import render, get_object_or_404
from blog.models import Bloger

def all_blogs(request):
    blogs = Bloger.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Bloger, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
