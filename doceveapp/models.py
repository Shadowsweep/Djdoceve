from django.db import models

# Create your models here.
class Teachers(models.Model):
    teacherid =  models.CharField(max_length=70,blank=False,default='',primary_key=True)
    teachername = models.CharField(max_length=70,blank=False,default='')
    designation = models.CharField(max_length=150,blank=False,default='')
    email = models.CharField(max_length=150,blank=False,default='')
    contactno = models.CharField(max_length=150,blank=False,default='')
    password = models.CharField(max_length=150, blank=False,default='')

class CollegeEvent(models.Model):
    eventname = models.CharField(max_length=150,blank=False,default='')
    startdate = models.CharField(max_length=70,blank=False,default='')
    enddate = models.CharField(max_length=70,blank=False,default='')
    starttime = models.CharField(max_length=70,blank=False,default='')
    endtime = models.CharField(max_length=70,blank=False,default='')
    eventlocation = models.CharField(max_length=150,blank=False,default='')
    description = models.CharField(max_length=150,blank=False,default='')
    facultycoordinatorid = models.CharField(max_length=70,blank=False,default='')
    studentcoordinatorid1 = models.CharField(max_length=70,blank=False,default='')
    studentcoordinatorid2 = models.CharField(max_length=70,blank=False,default='')

class EventRegistration(models.Model):
    eid = models.AutoField(primary_key=True)
    enrollmentid = models.CharField(max_length=70,blank=False,default='')
    regdate = models.CharField(max_length=70,blank=False,default='')
    regtime = models.CharField(max_length=70,blank=False,default='')
    remarks = models.CharField(max_length=150,blank=False,default='')

class Document(models.Model):
    docid  = models.AutoField(primary_key=True,editable=False)
    teacherid =  models.CharField(max_length=70,blank=False,default='')
    coursename =  models.CharField(max_length=70,blank=False,default='')
    doctype =  models.CharField(max_length=70,blank=False,default='')
    docname =  models.CharField(max_length=150,blank=False,default='')
    uploadby =  models.CharField(max_length=150,blank=False,default='')
    uploadtime =  models.CharField(max_length=70,blank=False,default='')
    uploaddate =  models.CharField(max_length=70,blank=False,default='')
    url =  models.CharField(max_length=150,blank=False,default='')
    remarks = models.CharField(max_length=150,blank=False,default='')
    
class Student(models.Model):
    # enrollmentid = models.AutoField(primary_key=True,editable=False)
    enrollmentid = models.CharField(max_length=70,blank=False,default='',primary_key=True)
    studentname = models.CharField(max_length=150,blank=False,default='')
    batchyear = models.CharField(max_length=70,blank=False,default='')
    email = models.CharField(max_length=150,blank=False,default='')
    contactno = models.CharField(max_length=70,blank=False,default='')
    studentstatus = models.CharField(max_length=70,blank=False,default='')
    studentsem = models.CharField(max_length=70,blank=False,default='')
    password = models.CharField(max_length=150, blank=False,default='')
    currentstatus = models.CharField(max_length=70,blank=False,default='')


class AssignmentSubmissionStudent(models.Model):
    assignementid = models.AutoField(primary_key=True,editable=False)
    enrollmentid = models.CharField(max_length=70,blank=False,default='')
    url = models.CharField(max_length=150,blank=False,default='')
    uploaddate = models.CharField(max_length=70,blank=False,default='')
    uploadtime = models.CharField(max_length=70,blank=False,default='')
    remarks = models.CharField(max_length=150,blank=False,default='')

class AssignmentSubmissionTeacher(models.Model):
    assignementid = models.AutoField(primary_key=True,editable=False)
    coursename = models.CharField(max_length=70,blank=False,default='')
    teacherid = models.CharField(max_length=70,blank=False,default='')
    uploaddate = models.CharField(max_length=70,blank=False,default='')
    startdate = models.CharField(max_length=70,blank=False,default='')
    enddate = models.CharField(max_length=70,blank=False,default='')
    url = models.CharField(max_length=150,blank=False,default='')
    
class Administrator(models.Model):

    adminname = models.CharField(max_length=70, blank=False,default='')
    mobileno = models.CharField(max_length=150, blank=False,default='')
    emailid = models.CharField(max_length=150, blank=False,default='')
    password = models.CharField(max_length=150, blank=False,default='')


