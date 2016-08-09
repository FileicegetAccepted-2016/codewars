from django.conf.urls import url
from RITCSE_codeWars import views

urlpatterns = [
    url(r'^$', views.index, name="Index"),
    url(r'^allsubmissions', views.all_submission, name="AllSubmissions"),
    url(r'^yoursubmission', views.your_submissions, name="YourSubmissions"),
    url(r'^code', views.your_code, name="YourCode"),
    url(r'^registration', views.UserFormView.as_view(), name="Registration"),
    url(r'^login/$', views.login_user, name="Login"),
    url(r'authenticate/$', views.authenticate_user, name="AuthenticateUser"),
]
