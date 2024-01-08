from django.shortcuts import render
from modelapp.forms import EmployeeForm
# Create your views here.
def Employee_view(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("RECORD INSERTED INTO DATABASE SUCCESSFULLY..")
    form=EmployeeForm()
    return render(request,"modelapp/model.html",{"form":form})
