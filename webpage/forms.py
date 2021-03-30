import datetime
from django import forms
from django.forms import ModelForm
from webpage.models import Post, CourseSpecialist, Course, RegisterStudent, User

class AdminPostForm(forms.Form):
  content = forms.CharField(widget=forms.Textarea, help_text="Enter content for post")
  photo = forms.ImageField(help_text="Choose photo")

  def clean_content(self):
    content_data = self.cleaned_data['content']
    return content_data

  def clean_photo(self):
    photo_data = self.cleaned_data['photo']
    return photo_data

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['content', 'photo']

class CourseSpecialistForm(forms.ModelForm):
  class Meta:
    model = CourseSpecialist
    fields = ['name', 'photo', 'bio']

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'course_specialist', 'photo', 'duration', 'limit_student', 'payment', 'description']

class UserForm(forms.Form):
  username = forms.CharField(help_text="Enter your name")
  email = forms.CharField(help_text="Enter your email")
  password = forms.CharField(widget=forms.PasswordInput, help_text="Enter ypur password")

  def clean_username(self):
    username_data = self.cleaned_data['username']
    return username_data

  def clean_email(self):
    email_data = self.cleaned_data['email']
    return email_data

  def clean_password(self):
    password_data = self.cleaned_data['password']
    return password_data

class RegisterStudentForm(forms.ModelForm):
  class Meta:
    model = RegisterStudent
    fields = ['name', 'course', 'start_date']
