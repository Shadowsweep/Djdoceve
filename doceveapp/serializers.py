from rest_framework import serializers 
from doceveapp.models import Teachers
from doceveapp.models import CollegeEvent
from doceveapp.models import EventRegistration
from doceveapp.models import Document
from doceveapp.models import Student
from doceveapp.models import AssignmentSubmissionStudent
from doceveapp.models import AssignmentSubmissionTeacher
from doceveapp.models import Administrator


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields =  ('id','teacherid','teachername','designation','email','contactno','password')

class CollegeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeEvent
        fields = ('id','eventname','startdate','enddate','starttime','endtime','eventlocation','description','facultycoordinatorid','studentcoordinatorid1','studentcoordinatorid2')


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ('eid','enrollmentid','regdate','regtime','remarks')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('docid','teacherid','coursename','doctype','docname','uploadby','uploadtime','uploaddate','url','remarks')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('enrollmentid','studentname','batchyear','email','contactno','studentstatus','studentsem','password','currentstatus')

class AssignmentSubmissionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmissionStudent
        fields =('assignmentid','enrollmentid','url','uploaddate','uploadtime','remarks')

class AssignmentSubmissionTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmissionTeacher
        fields =('assignmentid','coursename','teacherid','uploaddate','startdate','enddate','url')

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','adminname','mobileno','emailid','password')

