from django.db import models
from django import forms
from problems.models import problems,test_cases 
from django.contrib.admin import widgets

DIFFICULTY =[
	("easy"),
	("medium"),
	("hard"),
]

class problems_form(forms.ModelForm):

	#diff = forms.ChoiceField(choices= DIFFICULTY )
	class Meta:

		model=problems
		fields=['problem_code','problem_description','diff']


class testcases(forms.ModelForm):

	class Meta:
		model=test_cases
		fields=['problem_code','test_input','test_output']

	def __init__(self,*args,**kwargs):
		super(testcases,self).__init__(*args,**kwargs)
		self.fields['problem_code']=forms.ChoiceField(choices=get_list())



def get_list() :
	tup=((x,x) for x in problems.objects.values_list('problem_code',flat=True))
	return tup