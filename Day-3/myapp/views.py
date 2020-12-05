from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(req):
	return HttpResponse('<h1>Welcome</h1>')

def abt(req):
	return HttpResponse('<h4 style=color:blue;>welcome abt<h4>')

def myname(req,name):
	return HttpResponse("<h1 style=color:green>Welcome %s </h1>" %(name))



def table(req,num):
	l = ''
	for i in range(1, 10+1):
		l+="%s *%s = %s"%(num,i,num*i)+"<br>"
		# print(l)
	return HttpResponse(l)



def names(req,name,age):
	return render(req, 'data.html',{'name':name,'age':age})


def login(req):
	return render(req,'login.html')

def register(req):
	return render(req,'register.html')