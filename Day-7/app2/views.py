from django.shortcuts import render

# Create your views here.


def home(req):
	return render(req,'app2/home.html')



def grid(req):
	return render(req,'app2/grid.html')