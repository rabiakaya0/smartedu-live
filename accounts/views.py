from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Hesap aktif değil')
            else:
                messages.info(request, 'Kullanıcı adı veya şifre yanlış')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Hesap oluşturuldu, giriş yapabilirsiniz.')
            return redirect('login')
    else:
        form = RegisterForm()
        
    return render(request, 'register.html', {'form': form})

    # return render(request, 'register.html')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    courses = current_user.courses_joined.all() #coursesdaki related_name
    context = {
        'courses': courses
    }
    return render(request, 'dashboard.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')

def enroll_the_course(request):
    course_id = request.POST['course_id']
    user_id = request.POST['user_id']
    course = Course.objects.get(id = course_id)
    user = User.objects.get(id = user_id)
    course.students.add(user)
    return redirect('dashboard')

def release_the_course(request):
    course = Course.objects.get(id = request.POST['course_id'])
    user = User.objects.get(id = request.POST['user_id'])
    course.students.remove(user)
    return redirect('dashboard')