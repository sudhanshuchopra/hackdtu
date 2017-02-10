from .views import HistoryViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
history_list = HistoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
history_detail = HistoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^history_records/$', history_list, name='history-list'),
    url(r'^history_records/(?P<pk>[0-9]+)/$', history_detail, name='history-detail'),])