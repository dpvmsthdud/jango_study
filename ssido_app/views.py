from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def index(request):
	
	# 이건느 cmd창에서 볼 수 있음
	#print("SSIDO!~!~!")

	members = Member.objects.all()
	#members = Member.objects.filter(name = '김소영', age = 20) 이런식으로 원하는 정보를 얻어올 수 있음
	print(members)

	#html로 뿌려줄거다
	context = {'members' : members}


	return render(request, './a.html', context)


def index2(request):
	
	return render(request, './b.html')

def first(request):
	
	return render(request, './ssido.html')


def login(request):
	return render(request, './login.html')

def check_id(request):
	if request.methon == 'GET':

		print(request.GET.get('user_id', None))
		user_id = request.GET.get('user_id', None)

		try :
			member_list = Member.objects.get(user_id = user_id)
			result = {"result" : 'true'}
		except :
			result = {"result" : 'false'}

		return JsonResponse(result)

def register_member_db(request):
	if request.method == 'POST':

		user_id = request.POST['user_id']
		user_psw = request.POST['user_psw']

		new_member = Member(user_id= user_id, user_psw = user_psw)
		new_member.save()

		return render(request, './login.html')
	