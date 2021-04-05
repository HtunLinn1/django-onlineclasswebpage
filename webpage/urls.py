from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.home_page, name='home-page'),
  path('admin-post-create', views.AdminPostCreate.as_view(), name='admin-post-create'),
  path('<int:pk>/post-delete', views.post_delete, name='post-delete'),
  path('<int:pk>/update', views.post_update, name='post-update'),

  path('course-specialists', views.CourseSpecialistListView.as_view(), name='course-specialist-list'),
  path('course-specialist-create', views.course_specialist_create, name='course-specialist-create'),
  path('course-specialists/<int:pk>/update', views.course_specialist_update, name='course-specialist-update'),
  path('course-specialists/<int:pk>/delete', views.course_specialist_delete, name='course-specialist-delete'),
  path('<int:pk>/course-specialist-detail', views.CourseSpecialistDetail.as_view(), name='course-specialist-detail'),

  path('courses', views.CourseListView.as_view(), name='course-list'),
  path('course-create', views.course_create, name='course-create'),
  path('<int:pk>/course-detail', views.CourseDetail.as_view(), name='course-detail'),
  path('courses/<int:pk>/update', views.course_update, name='course-update'),
  path('courses/<int:pk>/delete', views.course_delete, name='course-delete'),

  path('create-account', views.create_account, name='create-account'),
  path('register/<int:pk>', views.RegisterStudentCreate.as_view(), name='register-with-course'),
  path('register', views.RegisterStudentCreate.as_view(), name='register'),

  path('<int:pk>/course-post-list', views.course_post_list, name='course-post-list'),
  path('course/<int:pk>/specialist-post-create', views.specialist_post_create, name='specialist-post-create'),

  path('course/<int:pk>/course-question-create', views.course_question_create, name='course-question-create'),
  path('course/<int:course_id>/question/<int:qus_id>/delete', views.question_delete, name='qus-delete'),
  path('course/<int:course_id>/question/<int:qus_id>/answer', views.question_answer, name='qus-answer'),
  path('student/<int:student_id>/course/<int:course_id>/delete', views.course_delete_by_student, name='course-delete-by-student'),
]
