
from django.conf.urls import url
from . import views


urlpatterns = [
   url(r'^$', views.DatamodelAPIView.as_view(), name='datamodel'),
]


