from django import forms
from submit.models import submission

LANGUAGE_CHOICES = [
("C","c"),
("cpp","cpp"),
("py","python")
]

class submissionform (forms.ModelForm):
    language = forms.ChoiceField(choices= LANGUAGE_CHOICES)
    
    class Meta:
        model = submission
        fields = ["language","code","input_data"]
