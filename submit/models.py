from django.db import models
from problems.models import test_cases,problems
# Create your models here.
class submission(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    input_data = models.TextField(null=True,blank=True)
    output_data = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    problem_code = problems.problem_code