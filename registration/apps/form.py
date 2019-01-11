from django import forms
from django.forms import ModelForm
from .models import *

class Newuser_form(ModelForm):
	class Meta:
		model = Newuser
		fields = '__all__'
