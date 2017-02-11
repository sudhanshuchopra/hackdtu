from django.shortcuts import render
from django.http import JsonResponse
from medhistory.models import History
from accounts.models import MyUser
# Create your views here.
def PercentageOfPeople(request):
	k=MyUser.objects.count()
	d=History.objects.all()
	m=set()
	for each in d:
		if each.blood_sugar_level !=None:
			v=int(each.blood_sugar_level)
			if v > 130:
				m.append(each.user)
	m=m.count()
	p=(m/d)*100
	JsonResponse({"percentage":p})



