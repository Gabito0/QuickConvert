from django import forms
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import pandas as pd


def data_form(request):
  return render(request, "Data.html")

@csrf_protect
def convert(request):
  try:
    data = request.POST["data"]
    print(data)
  except(ValueError):
    print("Data was not submitted")









