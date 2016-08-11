from sqlite3 import IntegrityError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils import timezone
from django.views.generic import View

from RITCSE_codeWars import CodeChef
from RITCSE_codeWars.models import Submission, Contest, Question
from .form import UserForm, UploadFileForm

c = CodeChef.API('buildrit', 'CSEdepartment')
#c.login()


def index(request):
    now = timezone.now()
    contest_list = Contest.objects.all()
    contests = []
    for contest in contest_list:
        if contest.contest_start_date < now < contest.contest_end_date:
            contests.append(contest)
    if not request.user.is_authenticated():
        return render(request, 'RITCSE_codeWars/ContestList_not_auth.html', {
            "contest_list": contests
        })

    return render(request, 'RITCSE_codeWars/ContestList.html', {
        "contest_list": contests,
        "user": request.user.is_authenticated()

    })


def your_submissions(request):
    if request.user.is_authenticated:
        user = request.user
        submision_list = Submission.objects.all().filter(user=user)
        return render(request, 'RITCSE_codeWars/YourSubmissions.html', {
            "submission_list": submision_list
        })
    else:
        return HttpResponseRedirect(reverse('Login') + "?error=true")


def your_code(request):
    try:
        id = request.GET['submission_id']
    except KeyError:
        return HttpResponseRedirect(reverse('YourSubmissions'))
    user = request.user
    submission = Submission.objects.all().filter(submission_id=id)

    if submission[0].user.username != user.username:
        return render(request, 'RITCSE_codeWars/YourCode.html', {
            "submission": "You are not authorised"
        })

    return render(request, 'RITCSE_codeWars/YourCode.html', {
        "submission": submission
    })


def login_user(request):
    try:
        error = request.GET['error']
        if error == 'incorrect':
            context = {'error_message': "Username and password does not match"}
        else:
            context = {'error_message': "Login required"}
    except KeyError:
        context = {}
    return render(request, 'RITCSE_codeWars/Login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Index'))


def authenticate_user(request):
    try:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
    except KeyError:
        return HttpResponseRedirect(reverse('Login'))
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('Login') + '?error=incorrect')
    login(request, user)
    return HttpResponseRedirect(reverse('Index'))


def questions_list(request, contest_list_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('Login') + "?error=true")
    try:
        contest_obj = Contest.objects.all().filter(pk=contest_list_id)
    except Contest.DoesNotExist:
        return HttpResponseRedirect(reverse('Index'))
    questions = Question.objects.all().filter(contest=contest_obj)
    print questions
    return render(request, 'RITCSE_codeWars/QuestionList.html', {
        'username': request.user.username,
        'contest': contest_obj,
        'question_list': questions,
    })


def problem(request, question_code):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('Login') + "?error=true")
    try:
        question = Question.objects.all().filter(question_code=question_code)[0]
    except Question.DoesNotExist:
        return HttpResponseRedirect('Index')

    submission_list = Submission.objects.all().filter(question_code=question_code).order_by('-submission_time')
    submission_accepted = submission_list.filter(complete_pass=True).order_by('-submission_time')
    print submission_accepted
    return render(request, 'RITCSE_codeWars/Home.html', {
        'username': request.user.username,
        'question': question,
        'submission_list': submission_list,
        'submission_accepted': submission_accepted
    })


def verify_submission(request, question_code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Login') + "?error=true")
    try:
        language = request.POST['Language']
        if str(language) == 'none':
            return HttpResponseRedirect(reverse('Problem', kwargs={'question_code': question_code}) + "?error=true")
        source = request.FILES['source']
        print source.name
    except KeyError:
        return HttpResponseRedirect(reverse('Problem', kwargs={'question_code': question_code}) + "?error=true")
    submission = Submission(user=request.user)
    q_obj = Question.objects.get(question_code=question_code)
    submission.contest = q_obj.contest
    submission.question_code = question_code
    submission.source = source.read()
    submission.submission_time = timezone.now()
    submission.language = language
    submission.submission_id = c.submit(question_code, submission.source, language)
    submission.result = c.check_result(submission.submission_id, question_code)
    if submission.result.find('accepted') != -1:
        submission.complete_pass = True
    else:
        submission.complete_pass = False
    submission.save()
    return HttpResponseRedirect(reverse('YourSubmissions'))


def create_user(request):
    user = User()
    try:
        user.first_name = request.POST['firstname']
        user.username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['conformpassword']
        if password != re_password:
            return HttpResponseRedirect(reverse('Registration'))
        user.email = request.POST['email']
        user.set_password(password)
    except KeyError:
        return HttpResponseRedirect(reverse('Registration'))
    try:
        user.last_name = request.POST['lastname']
    except KeyError:
        user.last_name = ""
    try:
        user.save()
    except Exception:
        return HttpResponseRedirect(reverse('Registration') + "?error=user")
    return HttpResponseRedirect(reverse('Login'))


def register_user(request):
    try:
        error = request.GET['error']
        if error == 'user':
            context = {'error_message': 'Username already exists'}
        else:  # error == 'pass':
            context = {'error_message': "Password doesn't match"}
    except KeyError:
        context = {}
    return render(request, 'RITCSE_codeWars/registration.html', context)
