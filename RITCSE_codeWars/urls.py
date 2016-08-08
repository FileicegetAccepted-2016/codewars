from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="CodeWars"),
    url(r'^allsubmissions', views.all_submission, name="AllSubmissions"),
    url(r'^yoursubmission', views.your_submissions, name="YourSubmissions"),
    url(r'^code', views.your_code, name="YourCode")
]
