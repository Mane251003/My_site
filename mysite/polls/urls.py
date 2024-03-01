from django.urls import path
from .views import course_list, course_detail, rate_course

#app_name="polls"

urlpatterns=[
    path("courses/", course_list, name="course_list"),
    path("courses/<int:course_id>", course_detail, name="course_detail"),
    path('courses/<int:course_id>/rate/', rate_course, name='rate_course'),
]
