from __future__ import unicode_literals
from djangotoolbox.fields import EmbeddedModelField
from django.db import models
from djangotoolbox.fields import ListField
# from mongoengine import *

# Create your models here.

class MongoModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True, null=True)
	name = models.CharField(max_length=200)
	email = models.EmailField()
	msg = models.TextField()
	