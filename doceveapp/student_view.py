from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import json
from doceveapp.serializers import StudentSerializer
from doceveapp.models import Student
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import json
import ast
import sys


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def StudentrecInterface(request):
    
    return render(request,'StudentInterface.html')

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def StudentEnrollmentInterface(request):
    
    return render(request,'EnrollmentCheck.html')


@api_view(['GET','POST'])
def StudentrecSubmit(request):
    global ids
    if request.method == 'POST' :
        
        student_serializer = StudentSerializer(data=request.data)
      #   cursor = connection.cursor()
        
      #   # Execute the query to fetch all the IDs
      #   cursor.execute("SELECT enrollmentid FROM doceveapp_student")
        
      #   # Fetch all the IDs
      #   ids = [row[0] for row in cursor.fetchall()]

      #   # Print the array of IDs
        
      #   print(ids)
      # #   ids_json = json.dumps(ids)
      # #   print(ids_json)
      #   data_to_pass_back = ids
      #   print(data_to_pass_back)
      #   input = sys.argv[0]
      #   output = data_to_pass_back
      #   print("xxxxxxx",output)
      #   sys.stdout.flush()

         
        if student_serializer.is_valid():
            student_serializer.save()
            return render(request,"StudentInterface.html",{"message":"Record Submitted Successfully"})
        return render(request,"StudentInterface.html",{"message":"Fail to Submit Record"})




# returned_data = StudentrecSubmit(request)

# Access the ids variable from the returned data




# @api_view(['GET','POST'])
# def StudentrecAccept(request):
#     if request.method == 'POST':
#         if(request.GET['btn']=='ACCEPT'):
#            student_serializer = StudentSerializer(data=request.data)
#            if student_serializer.is_valid():
#               student_serializer.save()
#               return render(request,"StudentInterface.html",{"message":"Record Submitted Successfully"})
#         return render(request,"StudentInterface.html",{"message":"Fail to Submit Record"})
   



@xframe_options_exempt 
@api_view(['GET','POST'])
def DisplayStudentrec(request):
  try:
    if request.method == 'GET':
      list_student=Student.objects.all()
      list_student_serializer=StudentSerializer(list_student,many=True)
      records=tuple_to_dict.ParseDict(list_student_serializer.data)
      print(records)
      return render(request,'StudentDisplay.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'StudentDisplay.html',{'data':{}})



@xframe_options_exempt 
@api_view(['GET','POST'])
def DisplayAdminStudentrec(request):
  try:
    if request.method == 'GET':
      list_student=Student.objects.all()
      list_student_serializer=StudentSerializer(list_student,many=True)
      records=tuple_to_dict.ParseDict(list_student_serializer.data)
      print(records)
      return render(request,'Adminregister.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'Adminregister.html',{'data':{}})
  

@xframe_options_exempt 
@api_view(['GET','POST'])
def DisplayAdminrec(request):
  try:
    if request.method == 'GET':
      list_student=Student.objects.all()
      list_student_serializer=StudentSerializer(list_student,many=True)
      records=tuple_to_dict.ParseDict(list_student_serializer.data)
      print(records)
      return render(request,'AcceptedStudent.html',{'data':records})
  except Exception as e:
       print("Error:",e)
       return render(request,'AcceptedStudent.html',{'data':{}})
  

# @xframe_options_exempt
# @api_view(['GET','POST'])
# def DisplayByStudentId(request):
#   try:
#     if request.method == 'GET':
#       q="Select * from doceveapp_student where enrollmentid='{0}' ".format(request.GET['enrollmentid'])
#       cursor=connection.cursor()
#       cursor.execute(q)
#       record=tuple_to_dict.ParseDictSingleRecord(cursor)
      
#     #   print("xxxx",record)
       
#       return render(request,'DisplayStudentById.html',{'data':record})
#   except Exception as e:
#        print("Error:",e)
#        return render(request,'DisplayStudentById.html',{'data':{}})
  

@xframe_options_exempt
@api_view(['GET','POST'])
def EditStudentrec(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="EDIT"):
            student=Student.objects.get(pk=request.GET['enrollmentid'])#hidden id
            student.studentname=request.GET['studentname']
            student.batchyear = request.GET['batchyear']
            student.email = request.GET['email']
            student.contactno = request.GET['contactno']
            student.status = request.GET['studentstatus']
            student.studentsem = request.GET['studentsem']
            student.currentstatus = request.GET['currentstatus']
            
            student.save()
         else:
            student=Student.objects.get(pk=request.GET['enrollmentid'])
            student.delete()

         return redirect('/api/studentrecdisplay')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/studentrecdisplay')


@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayByStudentId(request):
  try:
    if request.method == 'GET':
      q="Select * from doceveapp_student where enrollmentid='{0}' ".format(request.GET['enrollmentid'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
    #   print("xxxx",record)
       
      return render(request,'DisplayStudentById.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'DisplayStudentById.html',{'data':{}})
  

@xframe_options_exempt
@api_view(['GET','POST'])
def EditStudentrec(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="EDIT"):
            student=Student.objects.get(pk=request.GET['enrollmentid'])#hidden id
            student.studentname=request.GET['studentname']
            student.batchyear = request.GET['batchyear']
            student.email = request.GET['email']
            student.contactno = request.GET['contactno']
            student.studentstatus = request.GET['studentstatus']
            student.studentsem = request.GET['studentsem']
            student.currentstatus = request.GET['currentstatus']
            
            student.save()
         else:
            student=Student.objects.get(pk=request.GET['enrollmentid'])
            student.delete()

         return redirect('/api/studentrecdisplay')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/studentrecdisplay')



@xframe_options_exempt
@api_view(['GET','POST'])
def DeleteByStudentId(request):
  try:
    if request.method == 'GET':
      q="Select * from doceveapp_student where enrollmentid='{0}' ".format(request.GET['enrollmentid'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
    #   print("xxxx",record)
       
      return render(request,'DeleteStudentRec.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'DeleteStudentRec.html',{'data':{}})
  

@xframe_options_exempt
@api_view(['GET','POST'])
def AcceptByStudentId(request):
  try:
    if request.method == 'GET':
      q="Select * from doceveapp_student where enrollmentid='{0}' ".format(request.GET['enrollmentid'])
      cursor=connection.cursor()
      cursor.execute(q)
      record=tuple_to_dict.ParseDictSingleRecord(cursor)
    #   print("xxxx",record)
       
      return render(request,'AcceptStudentRec.html',{'data':record})
  except Exception as e:
       print("Error:",e)
       return render(request,'AcceptStudentRec.html',{'data':{}})
  

@xframe_options_exempt
@api_view(['GET','POST'])
def DeleteStudentrec(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="DELETE"):
            student=Student.objects.get(pk=request.GET['enrollmentid'])#hidden id
            student.delete()

         return redirect('/api/studentrecdisplay')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/studentrecdisplay')
   
@xframe_options_exempt
@api_view(['GET','POST'])
def AcceptStudentrec(request):
   try:
      if request.method =='GET':
         if(request.GET['btn']=="ACCEPT"):
            student=Student.objects.get(pk=request.GET['enrollmentid'])#hidden id
            student.studentname=request.GET['studentname']
            student.batchyear = request.GET['batchyear']
            student.email = request.GET['email']
            student.contactno = request.GET['contactno']
            student.studentstatus = request.GET['studentstatus']
            student.studentsem = request.GET['studentsem']
            student.currentstatus = request.GET['currentstatus']
            
            student.save()
         else:
            student=Student.objects.get(pk=request.GET['enrollmentid'])
            student.delete()

         return redirect('/api/studentrecdisplay')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/studentrecdisplay')

@xframe_options_exempt
@api_view(['GET','POST'])
def StudentEnrollmentCheck(request):
   try:
      if request.method =='GET':
          if(request.GET['btn']=="CHECK"):
             cursor = connection.cursor()
        # Execute the query to fetch all the IDs
             cursor.execute("SELECT enrollmentid FROM doceveapp_student")
        
        # Fetch all the IDs
             ids = [row[0] for row in cursor.fetchall()]

        # Print the array of IDs
        
      #   print(ids)
      #   ids_json = json.dumps(ids)
      #   print(ids_json)
             data_to_pass_back = ids
             print(data_to_pass_back)
             input = sys.argv[1]
             output = data_to_pass_back
             print("xxxxxxx",output)
             sys.stdout.flush()
            
          return render(request,'EnrollmentCheck.html')
   except Exception as e:
      print("Error:",e)
      return redirect('/api/studentrecdisplay')
