from django.contrib import admin
from .models import StudentInfo,StudentAcadmics
# Register your models here.
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('id','Roll','Name','Clas','School','Mobile','Address')

@admin.register(StudentAcadmics)
class StudentAcadmicsAdmin(admin.ModelAdmin):
    list_display = ('id','Roll_no','Maths','Physics','Chemistry','Biology','English')
