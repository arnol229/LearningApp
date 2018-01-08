from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Course(models.Model):
	course_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	length = models.IntegerField()
	subject = models.CharField(max_length=255)
	