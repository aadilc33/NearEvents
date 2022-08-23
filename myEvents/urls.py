from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Search'

urlpatterns=[
    path('/',views.myEvents, name='myEvents')
]

urlpatterns += staticfiles_urlpatterns()