from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
        category = request.POST['category']

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        login(request, user)
        return redirect('explore')  # 👈 after register, go to explore

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('explore')  # 👈 after login, go to explore
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def explore(request):
    posts = Post.objects.select_related('user').order_by('-created_at')
    return render(request, 'explore.html', {'posts': posts})

@login_required
def events(request):
    return render(request, 'events.html')

@login_required
def post_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption') or ''  # ✅ prevent None

        if image:
            Post.objects.create(user=request.user, image=image, caption=caption)
            return redirect('explore')
        else:
            return render(request, 'post_create.html', {'error': 'Image is required'})
    
    return render(request, 'post_create.html')



def about(request):
    return render(request, 'about.html')
