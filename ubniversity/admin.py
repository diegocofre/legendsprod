from django.contrib import admin
from .models import Organization, Teacher, Course, CourseDay, CourseClass, Level

# Register your models here.
admin.site.register(Organization)
admin.site.register(Teacher)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(CourseDay)
admin.site.register(CourseClass)