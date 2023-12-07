from django.contrib import admin

from api.models import Student
#@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','score']
admin.site.register(Student, StudentAdmin)
