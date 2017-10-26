from .views import HistoryViewSet
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
history_create = HistoryViewSet.as_view({
    'post': 'create'
})
base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'


urlpatterns = format_suffix_patterns([
    url(r'^history/$', history_create, name='history-create'),
    url(r'^history_records/$',views.HistoryList.as_view(),name='history-list'),
    url(r'^user/(?P<adhaar_card>[0-9]+)/$',views.UserDiseaseList.as_view(),name='user-disease'),
    url(r'^bph/(?P<adhaar_card>[0-9]+)/$',views.BPHistory.as_view(),name='bp-history'),
    #url(r'^checkstring/(?P<image_str>{})'.format(base64_pattern),views.examine),
    url(r'^checkstring/(?P<image_str>.+)/$',views.examine,name='check str'),
    url(r'^checkskin/(?P<image_str>.+)/$',views.examine_skin,name='check str')



    ]
    )
