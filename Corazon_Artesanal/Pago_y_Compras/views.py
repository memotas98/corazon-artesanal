from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django import forms
from models import FormaPago
from django.contrib import messages

"""class pagoForm(forms.ModelForm):
    class Meta:"""
