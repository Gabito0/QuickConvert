from django.urls import path
from . import views

app_name = "QuickConvert"
urlpatterns = [
    path('convert/', views.convert, name="convert"),
    path('data-form/', views.data_form, name="data_form")
]


