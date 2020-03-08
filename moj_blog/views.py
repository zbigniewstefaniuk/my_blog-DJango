from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from moj_blog.forms import UserRegisterForm

# Create your views here.

def index(request):
    posty = Post.objects.filter(data_publikacji__lte=timezone.now()).order_by(
        "data_publikacji"
    )
    return render(request, "moj_blog/index.html", {"posts": posty})


@login_required
def nowy(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('moj_blog:wpis', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'moj_blog/edycja.html', {'form': form})


def wpis(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'moj_blog/wpis.html', {'post': post})


@login_required
def edycja(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('moj_blog:wpis', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'moj_blog/edycja.html', {'form': form})


def rejestracja_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, "moj_blog/rejestracja.html", context)
