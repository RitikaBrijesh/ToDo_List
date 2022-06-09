from dataclasses import field
from operator import mod
from tkinter import Widget
from turtle import title
from urllib import request
from django import forms
from .models import *
from django.forms import TextInput

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','complete')

        a='width:300px; height:35px;border:1px solid; margin-left:70px;padding:5px 5px;'
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'style':a,
                'placeholder':'add items'
            }),

            'complete':forms.CheckboxInput(attrs={
                'style':'margin-left:0px;'
            })
        }
