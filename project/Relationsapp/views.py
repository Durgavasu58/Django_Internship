from django.shortcuts import render, redirect
from .forms import StudentForm, LecturerForm, DepartForm
from django.views.generic.edit import FormView,UpdateView,DeleteView
from django.views.generic import ListView
from .models import Departmentbranch,Studentdata,Lecturer
from django.urls import reverse_lazy
from django.db.models import Q

""" ====================== Students Views ========================= """

class StudentReg(FormView):
    form_class =  StudentForm
    template_name= 'studentlists/studentreg.html'
    success_url = reverse_lazy('Relationsapp:list')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class StudentList(ListView):
    model = Studentdata
    context_object_name='stulist'
    template_name='studentlists/studentlist.html'

class StudentUpdate(UpdateView):
    model=Studentdata
    fields ='__all__'
    template_name='studentlists/studentupdate.html'
    success_url=reverse_lazy('Relationsapp:list')

class StudentDelete(DeleteView):
    model=Studentdata
    template_name='studentlists/studentdel.html'
    success_url=reverse_lazy('Relationsapp:list')

class SearchResultsView(ListView):
    model= Studentdata
    context_object_name = 'stulist'
    template_name='studentlists/searchresults.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Studentdata.objects.filter(
			Q(name__icontains=query)|Q(city__icontains=query)|Q(marks__icontains=query)
        )

""" ====================== Lecturer Views ========================= """
class LecturerReg(FormView):
    form_class = LecturerForm
    template_name='lecturer/lecturerReg.html'
    succes_url=reverse_lazy('Relationsapp:letlist')
    def form_valid(self, form):
        form.save()
        return redirect('/letlist/') 
        #super().form_valid(form)

class LecturerList(ListView):
    model = Lecturer
    context_object_name='lectlist'
    template_name='lecturer/lecturerList.html'

class LecturerResultView(ListView):
    model= Lecturer
    context_object_name = 'lectlist'
    template_name='lecturer/letresults.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Lecturer.objects.filter(
			Q(Lecturer_name__icontains = query)
        )
            


""" ====================== Department Views ========================= """

class DepartReg(FormView):
    form_class = DepartForm
    template_name= 'Department/depReg.html'
    success_url = reverse_lazy('Relationsapp:deptList')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeptList(ListView):
    model = Departmentbranch
    context_object_name='deplist'
    template_name='Department/deplist.html'

def deptSearchView(request):
    n = request.GET.get('dep_branch')
    deptlist = Departmentbranch.objects.filter(branch__contains=n).first()
    profs = deptlist.lecturer_set.all()
    studs = deptlist.studentdata_set.all()

    print(f"{deptlist},\n{profs},\n{studs}")

    template_name='Department/depresults.html'
    context = {'deptlist':deptlist,'dep_branch':n,'profs_list':profs,'studlist':studs}
    return render(request,template_name,context)

