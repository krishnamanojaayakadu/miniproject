from django.shortcuts import render,redirect
from .models import table
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction

def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            center=request.POST.get('username')
            dates = table.objects.raw("select ROW_NUMBER()OVER(order by Centercode)as id,Centercode,ExamDate,count(htno)Total,sum(case when Attstatus in('p') then 1 else 0 end)'present',sum(case when Attstatus in('a') then 1 else 0 end)'absent',sum(case when Attstatus in('mp') then 1 else 0 end)'malpractise',sum(case when IsBuffer in(1) then 1 else 0 end)buffer,sum(case when IsLocked in(0) then 1 else 0 end)pending from sheets_table where Centercode=%s group by ExamDate,Centercode order by id,right(examdate,4),left(right(examdate,7),2),ExamDate ",[center])
            return render(request,'all_data.html',{"dates":dates})
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request,'login.html')

@login_required(login_url='login')
def dates_page(request,date):
    dates=table.objects.raw("select ROW_NUMBER()OVER(order by Course)as id,Course,CourseName,year,QPaperCode'papercode',SubjectCode,SubjectName,count(htno)Total,sum(case when Attstatus in('p') then 1 else 0 end)present,sum(case when Attstatus in('a') then 1 else 0 end)absent,sum(case when Attstatus in('mp') then 1 else 0 end)malpractise,sum(case when IsBuffer in(1) then 1 else 0 end)buffer,sum(case when IsLocked in(0) then 1 else 0 end)pending from sheets_table where ExamDate = %s group by Course,CourseName,year,QPaperCode,SubjectCode,SubjectName",[date])
    return render(request, 'dates.html', {"dates": dates})

@login_required(login_url='login')
def student_pageedit(request,qp):
    students=table.objects.raw("select ROW_NUMBER()OVER(order by sname)as id,sname,htno,ExamType,Examdate,medium,Barcode,OldBarcode,Attstatus from sheets_table where QPaperCode =%s",[qp])
    return render(request, 'studentsedit.html', {"students": students,"qp":qp})

@login_required(login_url='login')
def student_page(request,qp):
        students=table.objects.raw("select ROW_NUMBER()OVER(order by sname)as id,sname,htno,ExamType,Examdate,medium,Barcode,OldBarcode,Attstatus from sheets_table where QPaperCode =%s",[qp])
        QPCode = table.objects.raw("select ROW_NUMBER()OVER(order by sname)as id,QPaperCode from sheets_table where QPaperCode =%s",[qp])
        date1 = table.objects.filter(QPaperCode=qp)
        return render(request, 'students.html', locals())


@login_required(login_url='login')
def save_page(request):
    if request.method =='POST':
      for i in request.POST.get('barcode'):
          x=table(Attstatus=i)
          x.save()
    return redirect(login_page)


