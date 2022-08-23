"""NearEvent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events import views as events
from Details import views as Details
from login import  views as login
from register import views as register
from Search import views as search
from user import views as user
from location import views as location
from myEvents import views as myEvents
from eventDetails import views as eventDetails
from addEvents import views as addEvents
from Calendar import views as calendar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events', events.index, name="index"),
    path('', Details.events, name="events"),
    path('login/',login.login,name="Login"),
    path('register/',register.register),
    path('search/',search.search),
    path('user/',user.user),
    path('location/',location.location),
    path('myEvents/',myEvents.myEvents),
    path('event/Details',eventDetails.eventsDetails,name='eventsDetails'),
    path('addEvents', addEvents.addEvents, name='addEvents'),
    path('addV', addEvents.addVenue, name='addVenue'),
    path('calendar/<int:year>/<str:month>/',calendar.calendarData,name="calendar"),
    path('calendar/', calendar.calendarData, name="calendar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_URL+""+settings.MEDIA_ROOT)
