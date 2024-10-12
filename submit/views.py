
import difflib
from django.shortcuts import render
from django.http import HttpResponse
from submit.forms import submissionform
from django.template import loader
from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path
from problems.models import problems,test_cases
from difflib import SequenceMatcher as SM
# Create your views here.

def runfn(request,problem_code):
    if request.method == "POST":
        form = submissionform(request.POST)
        if form.is_valid():
            submission = form.save()
            print(submission.language)
            print(submission.code)
            output = run_code(
                submission.language, submission.code, submission.input_data
            )
            submission.output_data = output
            submission.save()
            testcase=test_cases.objects.get(problem_code=problem_code)
            result="running"
            desired_output=testcase.test_output
            sm = difflib.SequenceMatcher(None,output, desired_output)
            ratio = sm.ratio() * 100
            print(f"Similarity: {ratio:.2f}%")


            desired_output=desired_output.splitlines()
            output=output.splitlines()
            
            print(result)
            print("------\n")
#            desired_output.strip()
            print(len(desired_output))
            print(desired_output)
           
            print("------\n")
 #           output.strip()
            print(len(output))
            print(output)
            if(output==desired_output):
                print("accepted")
            else:
                print("wrong answer")            
            return render(request, "result.html", {"submission": submission})
    else:
        form = submissionform()
    return render(request, "index2.html", {"form": form})
 




 

def run_code(language, code, input_data):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]

    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty file

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                        
                    )
    elif language == "py":
        # Code for executing Python script
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python3", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return str(output_data)





def submitfn(request,problem_code):
    if request.method == "POST":
        form = submissionform(request.POST)
        if form.is_valid():
            submission = form.save()
            print(submission.language)
            print(submission.code)
            testcase=test_cases.objects.get(problem_code=problem_code)
            
           # output = run_code_submit(
          #      submission.language, submission.code, problem_code
         #   )
            outputs= run_code( submission.language, submission.code,str(testcase.test_input))
        
        if(str(testcase.test_output)==outputs):


            result = "accepted"
        elif(str(testcase.test_output)!=outputs):
            result="wrong answer"
            submission.output_data = outputs
            submission.save()
            return render(request, "result.html", {"submission": submission},{"result":result})
    else:
        form = submissionform()
    return render(request, "index2.html", {"form": form})
 




















def run_code_submit(language, code, problem_code):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]
    testcase = test_cases.objects.get(problem_code=problem_code)
    expected_output=testcase.test_output
    
    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(str(testcase.test_input))

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty file

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                        stderr=output_file,
                    ) 


    elif language == "py":
        # Code for executing Python script
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python3", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    if(output_data==expected_output):

        result = "Accepted"

    elif(output_data!=expected_output):
        result="Wrong Answer"    

    return result
                


























