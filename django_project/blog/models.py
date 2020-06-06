from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level=models.CharField(max_length=100,default=True)
    technology=models.CharField(max_length=100,default=True)
    qid=models.CharField(max_length=100,default=True)
    # question=models.CharField(max_length=100,default=True)
    question=RichTextField()
    answera=RichTextField()
    answerb=RichTextField()
    answerc=RichTextField()
    answerd=RichTextField()

    correctanswer=models.CharField(max_length=100,default=True)

class Answers(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attemptid=models.CharField(max_length=100,default=True)
    level=models.CharField(max_length=100,default=True)
    technology=models.CharField(max_length=100,default=True)
    qid=models.CharField(max_length=100,default=True)
    stdanswer=models.CharField(max_length=100,default=True)
