from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime


class Contest(models.Model):
    name = models.CharField(max_length=200)
    contest_start_date = models.DateTimeField
    contest_end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Question(models.Model):
    contest = models.ForeignKey(Contest)
    question_code = models.CharField(max_length=100)
    question_name = models.CharField(max_length=250)

    def __str__(self):
        return self.user + ' - ' + self.question_code


class Submission(models.Model):
    contest = models.ForeignKey(Contest)
    user = models.ForeignKey(User)
    question_code = models.CharField(max_length=20)
    submission_id = models.BigIntegerField()
    source = models.TextField()
    result = models.CharField(max_length=20)
    complete_pass = models.BooleanField(default=False)
    submission_time = models.DateTimeField()

    def __str__(self):
        return self.question_code + ": " + self.result
