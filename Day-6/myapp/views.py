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


def script(req):
	return render(req,'script.html')

def operations(req):
	return render(req,'operations.html')


def operators(req):
	if req.method=="POST":
		val1=int(req.POST["num1"])
		val2=int(req.POST["num2"])
		a=val1 + val2
		s=val1 - val2
		m=val1 * val2
		d=val1 / val2
	return render(req,'operators.html',{'a':a,'s':s,'m':m,'d':d,'val1':val1,'val2':val2})


def arthe(req):
	return render(req,'arthe.html')