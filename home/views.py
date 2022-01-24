from django.shortcuts import render ,HttpResponseRedirect
from .forms import StudentRegistration,Student
from .models import StudentInfo,StudentAcadmics

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            ro=fm.cleaned_data['  Roll   ']
            nm=fm.cleaned_data['Name   ']
            cl=fm.cleaned_data['Clas   ']
            sc=fm.cleaned_data['School ']
            mo=fm.cleaned_data['Mobile ']
            ad=fm.cleaned_data['Address']
            reg=StudentInfo(Roll=ro, Name=nm,Clas=cl,School=sc,Mobile=mo,Address=ad)
            reg.save()
        fm=StudentRegistration()
    else:
        fm= StudentRegistration()
    stud = StudentInfo.objects.all()
    return render(request, 'create.html', {'form': fm,'stu':stud})


# This function will delete data
def delete(request,id):

 if request.method=='POST':

    pi = StudentInfo.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')


def update(request,id):
    if request.method=='POST':
        pi = StudentInfo.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = StudentInfo.objects.get(pk=id)
    fm = StudentRegistration( instance=pi)
    return render(request,'update.html',{'form':fm})
