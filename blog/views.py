from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from . forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group

# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# About
def about(request):
    return render(request, 'blog/about.html')

# Contact
def contact(request):
    return render(request, 'blog/contact.html')

# Signup
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congratulations! You havbe become an Author!')
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                return HttpResponseRedirect('/login/')
        else:
            form = SignUpForm()
        return render(request, 'blog/signup.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html',{'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

# Logout
def user_logout(request):
	logout(request)
	messages.warning(request,'Logout Successfully!!')
	return HttpResponseRedirect('/login/')


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        fname = user.get_full_name()
        authgroups = user.groups.all
        return render(request, 'blog/dashboard.html', {'posts':posts,'fname':fname, 'groups':authgroups})
    else:
        return HttpResponseRedirect('/login/')

# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                messages.success(request,'Add post successfull!')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')



# Update Post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                messages.warning(request,'Data update successful!')
                form.save()
        else:
            post = Post.objects.get(pk=id)
            form = PostForm(instance=post)
        return render (request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


# Delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            messages.error(request,'Delete Successfully!!',post)
            post.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        fname = user.get_full_name()
        authgroups = user.groups.all
        return render(request, 'blog/profile.html',{'fname':fname, 'groups':authgroups})
    else:
        return HttpResponseRedirect('/login/')