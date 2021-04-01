from django.shortcuts import render, redirect
from django.views import generic
from .models import CourseSpecialist, Course, Post, RegisterStudent, User, CourseQuestion
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from webpage.forms import AdminPostForm, PostForm, CourseSpecialistForm, CourseForm, UserForm, CourseQuestionForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime

def home_page(request):
    if request.user.is_authenticated:
      co_specialist = CourseSpecialist.objects.filter(name=request.user).count()
      if co_specialist == 1:
        course_specialist = CourseSpecialist.objects.get(name=request.user)
        context = {
          'course_specialist': course_specialist,
        }
      else:
        students = RegisterStudent.objects.filter(name=request.user)
        context = {
          'students': students,
        }
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
  if query.course == None:
    return HttpResponseRedirect(reverse('home-page'))
  else:
    return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': query.course.id}))

# admin post update
def post_update(request, pk): 
  instance = get_object_or_404(Post, pk=pk)
  form = PostForm(request.POST or None, instance=instance)
  if form.is_valid():
    form.save()
    post = Post.objects.get(pk=pk)
    if post.course == None:
      return HttpResponseRedirect(reverse('home-page'))
    else:
      return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': post.course.id}))
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

# course specialist detail
class CourseSpecialistDetail(generic.DetailView):
  model = CourseSpecialist
  template_name ='webpage/coursespecialist_detail.html'

# course list
class CourseListView(generic.ListView):
  model = Course

# course detail
class CourseDetail(generic.DetailView):
  model = Course
  template_name ='webpage/course_detail.html'

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

# create account
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

# registe student
class RegisterStudentCreate(LoginRequiredMixin, CreateView):
  model = RegisterStudent
  fields = ['name', 'course', 'start_date']
  def get_initial(self, **kwargs):
    print(len(self.kwargs))
    if len(self.kwargs) > 0:
      initial = super().get_initial()
      name = self.request.user
      course = Course.objects.get(pk=self.kwargs["pk"])
      initial['course'] = course
      initial['name'] = name
      return initial
    else:
      initial = super().get_initial()
      name = self.request.user
      initial['name'] = name
      return initial
  success_url = reverse_lazy('home-page')

# course post list
def course_post_list(request, pk):
  course_query = get_object_or_404(Course, pk=pk)
  context = {
    'course': course_query,
  }

  return render(request, 'webpage/coursepost_list.html', context=context)

# specialist post create
def specialist_post_create(request, pk):
  course = Course.objects.get(pk = pk)
  if request.method == 'POST':
    form = AdminPostForm(request.POST, request.FILES)
    if form.is_valid():
      specialist_post = Post()
      specialist_post.content = form.cleaned_data['content']
      specialist_post.photo = form.cleaned_data['photo']
      specialist_post.course = Course.objects.get(pk = pk)
      specialist_post.post_creator = CourseSpecialist.objects.get(name = request.user.pk)
      specialist_post.save()

      return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': pk}))

  else:
    form = AdminPostForm()

  context = {
    'form': form,
    'course': course,
  }

  return render(request, 'webpage/adminpost_form.html', context)

# create course question
def course_question_create(request, pk):
  course = Course.objects.get(id = pk)
  if request.method == 'POST':
    form = CourseQuestionForm(request.POST, request.FILES)
    if form.is_valid():
      course_qus = CourseQuestion()
      course_qus.student = RegisterStudent.objects.get(name = request.user, course_id = pk)
      course_qus.course = Course.objects.get(pk = pk)
      course_qus.question = form.cleaned_data['question']
      course_qus.is_answered = False
      course_qus.save()

      return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': pk}))

  else:
    form = CourseQuestionForm()

  context = {
    'form': form,
    'course': course,
  }

  return render(request, 'webpage/coursequestion_form.html', context)

# course question delete
def question_delete(request, course_id, qus_id):
  query = CourseQuestion.objects.get(pk=qus_id)
  query.delete()
  return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': course_id}))

# answer question
def question_answer(request, course_id, qus_id):
  CourseQuestion.objects.filter(pk=qus_id).update(is_answered=1)
  return HttpResponseRedirect(reverse('course-post-list', kwargs={'pk': course_id}))