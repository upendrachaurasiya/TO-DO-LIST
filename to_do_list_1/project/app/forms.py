from django import forms
from .models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ["name"]
        widgets = {"name":forms.TextInput(attrs={"rows":3,"cols":30,'class':'form-control'})}
        labels = {"name":"Add Task here"}