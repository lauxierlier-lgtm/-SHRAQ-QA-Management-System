from django import forms
from .models import Project, Bug, TestCase


# ==============================
# PROJECT FORM
# ==============================

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'name',
            'description',
            'status'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter project name'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your testing project',
                'rows': 4
            }),

            'status': forms.Select()
        }


# ==============================
# BUG REGISTRATION FORM
# ==============================

class BugForm(forms.ModelForm):

    class Meta:
        model = Bug

        fields = [
            'project',
            'title',
            'description',
            'severity',
            'status'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter bug title'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Explain the bug and steps to reproduce it',
                'rows': 5
            }),

            'severity': forms.Select(),

            'status': forms.Select()
        }


# ==============================
# TEST CASE FORM
# ==============================

class TestCaseForm(forms.ModelForm):

    class Meta:
        model = TestCase

        fields = [
            'project',
            'title',
            'test_steps',
            'expected_result',
            'actual_result',
            'status'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter test case title'
            }),

            'test_steps': forms.Textarea(attrs={
                'placeholder': 'Enter step-by-step testing instructions',
                'rows': 4
            }),

            'expected_result': forms.Textarea(attrs={
                'placeholder': 'What should happen?',
                'rows': 3
            }),

            'actual_result': forms.Textarea(attrs={
                'placeholder': 'What actually happened?',
                'rows': 3
            }),

            'status': forms.Select()
        }