from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class StaticQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technology=models.CharField(max_length=100,default=True)
    question=RichTextField()
    answer=RichTextField()
    created_at=models.DateTimeField(blank=True,null=True)
