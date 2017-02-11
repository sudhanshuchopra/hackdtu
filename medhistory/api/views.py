from rest_framework import viewsets,mixins
from medhistory.models import History
from .serializers import HistorySerializer,HistoryUploadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from django.views.decorators.csrf import csrf_exempt
class HistoryViewSet(mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    
    queryset = History.objects.all()
    serializer_class = HistoryUploadSerializer
    #authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly,)
    @csrf_exempt
    def perform_create(self,serializer):
        #print("$$$$$$$$$$$",se.request.user)
        serializer.save(user=self.request.user)

class HistoryList(APIView):
    def get(self, request, format=None):
        historyobjs = History.objects.filter(user=request.user)
        serializer = HistorySerializer(historyobjs, many=True)
        return Response(serializer.data)