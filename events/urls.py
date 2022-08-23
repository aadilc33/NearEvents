from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ..NearEvent import settings

app_name = 'food'

urlpatterns=[
    path('',RedirectView.as_view(url='', permanent=True)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
