from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Events'

urlpatterns=[
    path('events',views.events, name='events')
]

urlpatterns += staticfiles_urlpatterns()