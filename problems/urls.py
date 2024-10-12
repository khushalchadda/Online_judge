from django.urls import path,include
from problems.views import problem_add,testcases_add,problem_list,problem_page

urlpatterns=[
path('',problem_add,name="add_problems"),
path('add_cases/',testcases_add,name="add_testcases" ),
path('list/',problem_list, name="problem_list"),
path('prob/<problem_code>',problem_page,name="problem_page"),
]

