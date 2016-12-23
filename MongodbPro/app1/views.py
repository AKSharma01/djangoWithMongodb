from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt	
from .models import *
import re

# Create your views here.

def insertData(request):
	return render(request,"app1/insertData.html")

@csrf_exempt
def viewData(request):
	val=post = ''
	if request.method == 'POST':
		text = request.POST['key']
		if text:
			text = re.escape(text)
			post = MongoModel.objects.filter(msg__iregex='%s'%text)
		else: 
			if request.POST['submit']=='All':
				post = MongoModel.objects.all()
			else:
				val = 'Enter Key First'
	
	return render(request,"app1/viewData.html",{'post': post, 'value':val })#Listview.as_list(queryset))

def indexHtml(request):
	return render(request,'app1/index.html')

@csrf_exempt
def insertInto(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		msg = request.POST['msg']
		post = MongoModel.objects.create(name=name, email=email, msg=msg)
		# post.save()
		return render(request,"app1/insertData.html",{'status' : 'successfully inserted!'})
	else:
		return render(request,"app1/insertData.html",{'status' : 'Insertion Fail!'})