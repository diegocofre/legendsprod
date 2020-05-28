from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    bio = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    time_zone = models.SmallIntegerField()
    max_attendants = models.SmallIntegerField()
    curr_attendants = models.SmallIntegerField(null=True, blank=True)
    id_teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="courses")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=settings.CURRENCY_CHOICES)
    duration_minutes = models.IntegerField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class CourseDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="days")
    week_day = models.SmallIntegerField(choices=settings.WEEK_DAYS)
    from_time = models.TimeField()
    to_time = models.TimeField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return ("{} {}/{}").format(settings.WEEK_DAYS[self.week_day], self.from_time, self.to_time)


class CourseClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="classes")
    attendant = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.datetime.tostring()
