from django.db import models

# Create your models here.
diff=[
       	("easy","easy"),
	("medium","medium"),
	("hard","hard"),

]
class problems(models.Model):
    problem_description = models.TextField()
    problem_code = models.CharField(max_length=100,unique=True)
    diff= models.CharField(max_length=100,choices=diff,default="easy")
          
    def __str__(self):
            return self.problem_code
    
        
class test_cases(models.Model):
      problem_code=models.CharField(max_length=100,unique=True)
      test_input=models.TextField(blank=False)
      test_output=models.TextField(blank=False)
      
      def __str__(self):
              return self.problem_code
      
 