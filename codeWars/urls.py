
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^codewars/', include('RITCSE_codeWars.urls')),
    url(r'^admin/', admin.site.urls)
]
