from rest_framework import serializers
from accounts.models import MyUser
from django.core.exceptions import ValidationError 
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# Turn off CSRF
class CsrfExemptSessionAuthentication(BasicAuthentication):
    def enforce_csrf(self, request):
        return

class UserLoginSerializer(serializers.ModelSerializer):
    adhaar_card = serializers.IntegerField(max_value=999999999999, min_value=1)
    class Meta:
        model = MyUser
        fields = ('adhaar_card', 'password')

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
    	login_user = None
    	adhaar_card = data.get('adhaar_card', '')
    	if not adhaar_card:
    		raise ValidationError('Adhaar Card must be provided')
    	users_list = MyUser.objects.filter(adhaar_card=adhaar_card)
    	if users_list.exists() and users_list.count() == 1:
    		login_user = users_list.first()
    	else:
    		raise ValidationError('user does not exist')
    	if login_user:
    		if not login_user.check_password(data.get('password')):
    			raise ValidationError('User/Password doesnt Match' )
    	return data


		
		
