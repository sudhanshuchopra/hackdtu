from rest_framework import viewsets
from medhistory.models import History
from .serializers import HistorySerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly,)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)