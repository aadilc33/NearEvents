from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'register'

urlpatterns=[
    path('/',views.register, name='home')
]

urlpatterns += staticfiles_urlpatterns()