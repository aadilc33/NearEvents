from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Login'

urlpatterns=[
    path('',views.addEvents, name='events'),
]

urlpatterns += staticfiles_urlpatterns()