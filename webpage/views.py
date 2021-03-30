from django.shortcuts import render, redirect
from django.views import generic
from .models import CourseSpecialist, Course, Post, RegisterStudent, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from webpage.forms import AdminPostForm, PostForm, CourseSpecialistForm, CourseForm, RegisterStudentForm, UserForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime

def home_page(request):
    if request.user.is_authenticated:
      course_specialist = CourseSpecialist.objects.get(name=request.user)
    else:
      user_id = User.objects.get(is_superuser=1)
      course_specialist = CourseSpecialist.objects.get(name=user_id)
    context = {
      'course_specialist': course_specialist,
    }

    return render(request, 'webpage/home_page.html', context=context)

# admin post create
def admin_post_create(request):
  if request.method == 'POST':
    form = AdminPostForm(request.POST, request.FILES)
    if form.is_valid():
      admin_post = Post()
      admin_post.content = form.cleaned_data['content']
      admin_post.photo = form.cleaned_data['photo']
      admin_post.post_creator = CourseSpecialist.objects.get(name = request.user.pk)
      admin_post.save()

      return HttpResponseRedirect(reverse('home-page'))

  else:
    form = AdminPostForm()

  context = {
    'form': form,
  }

  return render(request, 'webpage/adminpost_form.html', context)

# admin post delete
def post_delete(request, pk):
  query = Post.objects.get(pk=pk)
  query.delete()
  return HttpResponseRedirect(reverse('home-page'))

# admin post update
def post_update(request, pk): 
  instance = get_object_or_404(Post, pk=pk)
  form = PostForm(request.POST or None, instance=instance)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('home-page'))
  return render(request, 'webpage/post_form.html', {'form': form}) 

# course specialist list
class CourseSpecialistListView(generic.ListView):
  model = CourseSpecialist

# course_specialist_create
def course_specialist_create(request):
  if request.method == 'POST':
    form = CourseSpecialistForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect(reverse('course-specialist-list'))

  else:
    form = CourseSpecialistForm()

  context = {
    'form': form,
  }

  return render(request, 'webpage/coursespecialist_form.html', context)

# course_create
def course_create(request):
  if request.method == 'POST':
    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect(reverse('course-list'))

  else:
    form = CourseForm()

  context = {
    'form': form,
  }

  return render(request, 'webpage/course_form.html', context)

# update course specialist
def course_specialist_update(request, pk): 
  instance = get_object_or_404(CourseSpecialist, pk=pk)
  form = CourseSpecialistForm(request.POST or None, instance=instance)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('course-specialist-list'))
  return render(request, 'webpage/coursespecialist_form.html', {'form': form}) 

# delete course specialist
def course_specialist_delete(request, pk):
  query = CourseSpecialist.objects.get(pk=pk)
  query.delete()
  return HttpResponseRedirect(reverse('course-specialist-list'))

# course specialist list
class CourseSpecialistListView(generic.ListView):
  model = CourseSpecialist

# course list
class CourseListView(generic.ListView):
  model = Course

# update course
def course_update(request, pk): 
  instance = get_object_or_404(Course, pk=pk)
  form = CourseForm(request.POST or None, instance=instance)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('course-list'))
  return render(request, 'webpage/course_form.html', {'form': form}) 

# course delete
def course_delete(request, pk):
  query = Course.objects.get(pk=pk)
  query.delete()
  return HttpResponseRedirect(reverse('course-list'))

# register
def create_account(request):
  if request.method == 'POST':
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
      user = User()
      user.username = form.cleaned_data['username']
      user.email = form.cleaned_data['email']
      user.set_password(form.cleaned_data['password'])
      user.save()

      return HttpResponseRedirect(reverse('home-page'))

  else:
    form = UserForm()

  context = {
    'form': form,
  }

  return render(request, 'webpage/user_form.html', context)

# register
def register_student(request):
  if request.method == 'POST':
    form = RegisterStudentForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect(reverse('home-page'))

  else:
    form = RegisterStudentForm()

  context = {
    'form': form,
  }

  return render(request, 'webpage/register_form.html', context)