from django.contrib import admin
from modelapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["name","sno","email","phn","addr","com","skills"]
admin.site.register(Employee,EmployeeAdmin)
