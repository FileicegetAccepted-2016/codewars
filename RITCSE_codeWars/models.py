from django.db import models
from django.utils.timezone import datetime


class Users(models.Model):
    user_name = models.CharField(max_length=100)
    logged_in_time = models.CharField(max_length=250)

    def __str__(self):
        return self.user_name


class Question(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question_code = models.CharField(max_length=100)
    question_name = models.CharField(max_length=250)
    language = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    submitted_time = models.CharField(max_length=100)

    def __str__(self):
        return self.user + ' - ' + self.question_code
