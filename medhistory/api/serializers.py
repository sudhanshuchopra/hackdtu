from rest_framework import serializers
from medhistory.models import History
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# Turn off CSRF
class CsrfExemptSessionAuthentication(BasicAuthentication):
    def enforce_csrf(self, request):
        return

class HistorySerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.adhaar_card')
	class Meta:
		model = History
		fields = ('history_pic', 'user', 'time', 'image_title', 'Disease','blood_sugar_level')

class HistoryUploadSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.adhaar_card')
	history_pic=serializers.ImageField(required=False)
	class Meta:
		model = History
		fields = ('history_pic', 'user', 'time', 'image_title')