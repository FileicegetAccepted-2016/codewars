from django.conf.urls import url
from RITCSE_codeWars import views

urlpatterns = [
    url(r'^$', views.index, name="Index"),
    url(r'^questions/(?P<contest_list_id>[0-9]+)/$', views.questions_list, name="Questions"),
    url(r'^questions/solve/(?P<question_code>.+)/$', views.problem, name="Problem"),
    url(r'^yoursubmission', views.your_submissions, name="YourSubmissions"),
    url(r'^code', views.your_code, name="YourCode"),
    url(r'^registration', views.register_user, name="Registration"),
    url(r'^login/$', views.login_user, name="Login"),
    url(r'authenticate/$', views.authenticate_user, name="AuthenticateUser"),
    url(r'logout', views.logout_user, name="Logout"),
    url(r'questions/solve/(?P<question_code>.+)/verify', views.verify_submission, name="VerifyResult"),
    url(r'createuser/$', views.create_user, name="CreateUser")
]
