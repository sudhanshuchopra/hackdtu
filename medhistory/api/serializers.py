from rest_framework import serializers
from medhistory.models import History
class HistorySerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.adhaar_card')
	class Meta:
		model = History
		fields = ('history_pic', 'user', 'time', 'image_title', 'Disease','blood_sugar_level')