
from django.urls import path
from .views import *
from .import views #function base views

app_name='Relationsapp'


urlpatterns = [
    #'''=============== Student Urls ================'''
    path('',StudentList.as_view(),name='list'),
    path('regis/',StudentReg.as_view(),name='registration'),
    path('delete/<int:pk>/',StudentDelete.as_view(),name='delete'),
    path('update/<int:pk>/',StudentUpdate.as_view(),name='update'),
    path('results/',SearchResultsView.as_view(),name='results'),

    #'''=============== Lecturer Urls ================'''
    path('letlist/',LecturerList.as_view(),name='letlist'),
    path('letregis/',LecturerReg.as_view(),name='letregis'),
    path('letresult/',LecturerResultView.as_view(),name='letresult'),

    #'''=============== Department Urls ================'''
    path('depreg/',DepartReg.as_view(),name='depreg'),
    path('deptList/',DeptList.as_view(),name='deptList'),
    path('depresult/',views.deptSearchView,name='depresult')
]
