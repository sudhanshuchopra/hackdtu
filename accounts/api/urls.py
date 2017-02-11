from django.conf.urls import include, url
from .views import UserLoginAPI
from . import views
from accounts.views import PercentageOfPeople
urlpatterns = [
    url(r'^login/$',UserLoginAPI.as_view(),name='login-api'),
    url(r'^user/(?P<adhaar_card>[0-9]+)/$',views.UserDetail.as_view(),name='user-api'),
    url(r'^percentageofbsl/$',PercentageOfPeople,name='bsl')
]