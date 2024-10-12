
from django.shortcuts import render
from django.http import HttpResponse
from problems.forms import problems_form,testcases
from problems.models import problems,test_cases
from django.template import loader

from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path
# Create your views here.
# Create your views here.

def problem_add(request):

    if request.method=='POST': 
        form=problems_form(request.POST)
        if form.is_valid():
            form.save()

            return render(request,'admin_portal.html',{'success':request.POST['problem_code']+' added succesfully'})
        else:
            return render(request,'add_problems.html',{'form':problems_form(),'errors':'problem not added try again'})
    else:
        form=problems_form()
        return render(request,"add_problems.html",{"form":form})
        #return render(request, "index2.html", {"form": form})

def problem_list(request):
    prob_list = problems.objects.all()

    return render(request,"problem_list.html",{"prob_list":prob_list})

def problem_page(request,problem_code):

    selected_problem =problems.objects.get(problem_code=problem_code)
    

    return render(request,"problem_page.html",{"selected_problem":selected_problem})

def testcases_add(request):
    if request.method=='POST':
        form=testcases(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'admin_portal.html',{'success':request.POST['problem_code']+'test case added succesfully'})
        else:
            return render(request,'testcase.html',{'form':testcases(),'error':'testcase not added try again'})
    else:
        return render(request,'testcase.html',{'form':testcases()})
            

