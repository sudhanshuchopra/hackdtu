from .views import HistoryViewSet
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
history_create = HistoryViewSet.as_view({
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    url(r'^history/$', history_create, name='history-create'),
    url(r'^history_records/$',views.HistoryList.as_view(),name='history-list')])