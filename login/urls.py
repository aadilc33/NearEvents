from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Login'

urlpatterns=[
    path('login',views.login, name='login')
]

urlpatterns += staticfiles_urlpatterns()