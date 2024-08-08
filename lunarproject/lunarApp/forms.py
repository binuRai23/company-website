# forms.py

from django import forms
from .models import Enroll

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ['firstname', 'lastname', 'email', 'selected_course', 'course_amount']

    selected_course = forms.CharField(widget=forms.HiddenInput())
    course_amount = forms.CharField(widget=forms.HiddenInput())

