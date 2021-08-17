from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Departmentbranch)
class DepBranch(admin.ModelAdmin):
    list_display=['branch']

@admin.register(Studentdata)
class StuBranch(admin.ModelAdmin):
    list_display=['name','city','marks','dept']

@admin.register(Lecturer)
class LectBranch(admin.ModelAdmin):
    list_display=['Lecturer_name']