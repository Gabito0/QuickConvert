from django import forms
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
import pandas as pd
import json
from io import StringIO
import csv


def data_form(request):
  return render(request, "Data.html")

@csrf_protect 
def convert(request):
  if request.method == "POST":
    raw_data = request.POST.get("data", " ")
    try:
      csv_file = StringIO(raw_data)  
      reader = csv.DictReader(csv_file)
      json_data = list(reader)
      return render(request, "Data.html", {"json_data":json_data})
    except(ValueError):
      print("Data was not submitted")
  return render(request, "Data.html")
  









