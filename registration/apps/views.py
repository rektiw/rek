from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .form import *


# Create your views here.
	
def success(request):
	return render (request, 'success.html')

def home(request):
	return render (request, 'home.html')

def Gmail(request):
	return render (request, 'Gmail.html')

def index(request):
	return render (request, 'index.html')

def main(request):
	return render (request, 'main.html')

#def Registration(request):
    #return render (request, 'Registration.html')
def form():
 	obj.object.all()
	#return request(request, 'form.html')
	
def Newuser(request):
	formdata= Newuser_form()

	if request.method == 'POST':
		formdata = Newuser_form(request.POST)
		if formdata.is_valid():
			formdata.save()
			return HttpResponse("your form submit successfully")  
	print(form)
	return render(request, 'Registration.html', {'form': formdata})
