from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# .'tanın bitişik olup olmaması birşey değiştirmiyor sanırım.
from .models import BlogPost
from .forms import BlogForm

def index(request):
    """Blog projesi için home page"""
    blog_post = BlogPost.objects.order_by('date_added')
    context = {'index': blog_post}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
    """Tek bir postu gösterir"""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Add new post"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            #form.save()
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    # Uyarılar hangisi sayesinde çıkıyor?(ör boş form submit)
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an exist post"""
    post = BlogPost.objects.get(id=post_id)
    #post = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    #post = BlogPost.objects.filter(owner=request.user)

    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #form = BlogForm(data=request.GET)#neden böyle değilde aşağıdaki gibi
        form = BlogForm(instance=post)
    else:
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogs:post', post_id=post.id)
            #return redirect('blogs:post', post_id)
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)