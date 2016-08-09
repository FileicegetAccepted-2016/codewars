from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime


class Contest(models.Model):
    name = models.CharField(max_length=200)
    contest_start_date = models.DateField()
    contest_end_date = models.DateField()

    def __str__(self):
        return self.name


class Question(models.Model):
    contest = models.ForeignKey(Contest)
    question_code = models.CharField(max_length=100)
    question_name = models.CharField(max_length=250)

    def __str__(self):
        return self.user + ' - ' + self.question_code


class Submission(models.Model):
    user = models.ForeignKey(User)
    question_code = models.CharField(max_length=20)
    source = models.TextField()
    result = models.CharField(max_length=20)
    complete_pass = models.BooleanField(default=False)
    submission_time = models.DateTimeField()

    def __str__(self):
        return self.question_code + ": " + self.result
