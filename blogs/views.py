from django.shortcuts import render

# .'tanın bitişik olup olmaması birşey değiştirmiyor sanırım.
from .models import BlogPost

def index(request):
    """Blog projesi için home page"""
    blog_post = BlogPost.objects.order_by('date_added')
    context = {'index': blog_post}
    return render(request, 'blogs/index.html', context)