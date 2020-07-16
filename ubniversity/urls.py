from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^course-details/$', views.course_details, name='course-details'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^shoot/(\w+)$', views.shoot, name='shoot'),
]