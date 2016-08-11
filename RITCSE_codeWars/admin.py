from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from RITCSE_codeWars.models import Contest, Question, Submission


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1


class ContestAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user','language','submission_time','result','question_code')
    list_filter = ('user', 'result', 'submission_time')

admin.site.register(Contest, ContestAdmin)
admin.site.register(Submission, SubmissionAdmin)
