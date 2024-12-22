from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoModel
from .forms import ToDoForm
# Create your views here.

def addandshow(request):
    if request.method == "POST":
        fd = ToDoForm(request.POST)
        if fd.is_valid():
            fd.save()
            fd = ToDoForm()
    else:
        fd =ToDoForm()
    md = ToDoModel.objects.all()
    return render(request,"app/home.html",{"form":fd,"data":md})

def deletedata(request,id):
    d_data = ToDoModel.objects.get(pk=id)
    d_data.delete()
    return HttpResponseRedirect("/")