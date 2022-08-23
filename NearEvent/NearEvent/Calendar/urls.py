from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Calendar'

urlpatterns=[
    path('calendar/<int:year>/<str:month>/',views.calendarData, name='calendar')
]

urlpatterns += staticfiles_urlpatterns()