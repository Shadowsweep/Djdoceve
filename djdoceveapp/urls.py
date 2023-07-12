"""djdoceveapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from doceveapp import admin_view
from doceveapp import teacher_view
from doceveapp import eventreg_view
from doceveapp import student_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/loginpage/$',admin_view.LoginPage),
    re_path(r'^api/categoryinterface/',admin_view.CategoryInterface),

    ############## adding admin register #############
    re_path(r'^api/adminlogin',admin_view.AdminLogin),
    re_path(r'^api/adminregistersubmit',admin_view.AdminSubmit),
    re_path(r'^api/checkadminlogin',admin_view.CheckAdminLogin),
    re_path(r'^api/acceptedstudentdisplay',student_view.DisplayAdminrec),
    re_path(r'^api/openform',admin_view.Openform),
    re_path(r'^api/enrollmenttester',admin_view.StudentEnrollmentCheck),

    ############# teacher details #########
    re_path(r'^api/addteacherrecinterface/$',teacher_view.TeacherrecInterface),
    re_path(r'^api/addteacherrecsubmit',teacher_view.TeacherrecSubmit),

     ############# student details #########
    re_path(r'^api/addstudentrecinterface/$',student_view.StudentrecInterface),
    re_path(r'^api/addstudentrecsubmit',student_view.StudentrecSubmit),
    # re_path(r'^api/studentrecdisplay',student_view.DisplayStudentrec),
    re_path(r'^api/studentrecdisplay',student_view.DisplayAdminStudentrec),
    re_path(r'^api/display_student_by_id',student_view.DisplayByStudentId),
    re_path(r'^api/studentrecedit',student_view.EditStudentrec),
    re_path(r'^api/studentrecdelete',student_view.DeleteStudentrec),
    re_path(r'^api/delete_student_by_id',student_view.DeleteByStudentId),
    re_path(r'^api/accept_student_by_id',student_view.AcceptByStudentId),
    re_path(r'^api/studentrecaccept',student_view.AcceptStudentrec),

    re_path(r'^api/addstudentrecinterface/$',student_view.StudentrecInterface),
    re_path(r'^api/addstudentenrollmentinterface/$',student_view.StudentEnrollmentInterface),
    re_path(r'^api/studentenrollmentcheck',student_view.StudentEnrollmentCheck),
    # re_path(r'^api/studentrecaccept',student_view.AcceptStudentrec),

    


    ############# Event Registration ######
    re_path(r'^api/addeventregistrationinterface/$',eventreg_view.EventRegistrationInterface),
    re_path(r'^api/addeventregistrationsubmit',eventreg_view.EventRegistrationSubmit),



]
