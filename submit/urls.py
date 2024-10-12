from django.urls import include,path
from submit.views import runfn,submitfn

urlpatterns=[
    path("<problem_code>",runfn,name="submit"),
]