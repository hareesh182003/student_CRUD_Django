from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_college(request):
    if request.method == 'POST':
        cid = request.POST['c_id']
        cname = request.POST['c_name']
        cadd = request.POST['c_add']
        CO = College.objects.get_or_create(col_id=cid,col_name=cname,col_address=cadd)
        return render(request,'display_college.html',{'College_objects':College.objects.all()})
    return render(request,'insert_college.html')

def display_college(request):
    return render(request,'display_college.html',{'College_objects':College.objects.all()})

def insert_student(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        sname = request.POST['sname']
        syear = request.POST['syear']
        sadd = request.POST['sadd']
        col_id = request.POST['col_id']

        CO = College.objects.get(col_id = col_id)
        SO = Student.objects.get_or_create(stu_id = sid,stu_name = sname,stu_year = syear,stu_address = sadd,col_id=CO)
        return render(request,'display_student.html',{'student_objects':Student.objects.all()})
    return render(request,'insert_student.html',{'College_objects':College.objects.all()})

def display_student(request):
    return render(request,'display_student.html',{'student_objects':Student.objects.all()})

def update_college(request):
    College.objects.filter(col_address='guntur').update(col_address='Guntur')
    return render(request,'display_college.html',{'College_objects':College.objects.all()})

def delete_college(request):
    College.objects.filter(col_id=786).delete()
    return render(request,'display_college.html',{'College_objects':College.objects.all()})