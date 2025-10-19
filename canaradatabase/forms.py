from django import forms
from .models import Student
class AddStudent(forms.ModelForm):
    class Meta:
        model=Student

        fields='__all__'


    

    def clean_gmail(self):
        gmail=self.cleaned_data.get('gmail')

        if Student.objects.filter(gmail=gmail).exists():
             raise forms.ValidationError("email already exists")
        
        return gmail
    

    def clean_rno(self):
        rno=self.cleaned_data.get('rno')

        if Student.objects.filter(rno=rno).exists():
            raise forms.ValidationError("roll no already exitss")
        
        return rno
          

      


