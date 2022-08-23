from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'food'

urlpatterns=[
    path('',views.eventsDetails, name='home')
]

urlpatterns += staticfiles_urlpatterns()