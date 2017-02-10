from django.conf.urls import include, url
from .views import UserLoginAPI
urlpatterns = [
    url(r'^login/$',UserLoginAPI.as_view(),name='login-api')
]