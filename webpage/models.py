from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class CourseSpecialist(models.Model):
  """ course specialist """
  name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name="course specialist")
  photo = models.ImageField(upload_to='images/', default='defo')
  bio = models.TextField(max_length=1000, help_text="Enter your bio details here.")
  
  class Meta:
    ordering = ["name", "bio"]

  def get_absolute_url(self):
    pass

  def __str__(self):
    return self.name.username

class Course(models.Model):
  """ Course """
  name = models.CharField(max_length=200)
  course_specialist = models.ForeignKey(CourseSpecialist, on_delete=models.SET_NULL, null=True)
  photo = models.ImageField(upload_to='images/', default='defo')
  duration = models.IntegerField()
  limit_student = models.IntegerField()
  payment = models.IntegerField()
  description = models.TextField(max_length=1000)
  
  class Meta:
    ordering = ["name"]
    unique_together = (('name'),)

  def get_absolute_url(self):
    pass

  def __str__(self):
    return self.name

class Post(models.Model):
  """ Post """
  content = models.TextField(max_length=1000)
  photo = models.ImageField(upload_to='images/', default='defo')
  course = models.ForeignKey(Course, verbose_name='course', on_delete=models.SET_NULL, null=True)
  post_creator= models.ForeignKey(CourseSpecialist, on_delete=models.CASCADE)
  post_date = models.DateTimeField(default=datetime.datetime.now())
  
  class Meta:
    ordering = ["post_date"]

  def get_absolute_url(self):
    pass

  def __str__(self):
    return self.content

class RegisterStudent(models.Model):
  """ register student """
  name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  course = models.ForeignKey(Course, verbose_name='course', on_delete=models.SET_NULL, null=True)
  start_date = models.DateTimeField(default=datetime.datetime.now())
  
  class Meta:
    ordering = ["start_date"]
    unique_together = (('name', 'course'),)

  def get_absolute_url(self):
    pass

  def __str__(self):
    return self.name.username

class CourseQuestion(models.Model):
  """ Course Question """
  student = models.ForeignKey(RegisterStudent, verbose_name='student', on_delete=models.SET_NULL, null=True)
  course = models.ForeignKey(Course, verbose_name='course', on_delete=models.SET_NULL, null=True)
  question = models.TextField(max_length=1000)
  is_answered = models.BooleanField(default=False)
  start_date = models.DateTimeField(default=datetime.datetime.now())
  
  class Meta:
    ordering = ["start_date"]

  def get_absolute_url(self):
    pass

  def __str__(self):
    return self.question