from django.shortcuts import render,redirect,get_object_or_404
from . models import Student
from . forms import StudentForm
from django.views.generic import ListView
from django.http import Http404
from django.contrib import messages
from . filters import NameFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

'''Student list view contain every detail of easy student '''

class StudentView(LoginRequiredMixin,ListView):
    model=Student
    paginate_by = 2
    login_url = '/accounts/login/'
    redirect_field_name = 'accounts:login'
    
    #overwrite contexgt method because to insert filter method into it
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["filter"]=NameFilter(self.request.GET,queryset=self.get_queryset())
        return context


#method for student registration to fill the form
@login_required
def student_registration(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        messages.info(request,"new student added successfully")
        return redirect("student:home")
    else:
        form=StudentForm()
        context={"form":form}
        messages.info(request,"welcome to add new data")
        return render(request,"student/registration-form.html",context)

#this method use for update student record
@login_required
def edit(request,slug):
    edit_student=get_object_or_404(Student,slug=slug)
    form=StudentForm(instance=edit_student)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=edit_student)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.save()
            print("form.save")
            messages.success(request,"updated successfully")
            return redirect("student:home")
        else:
            messages.warning(request,"there is something wrong in your input")
            return redirect("student:home")
    else:
        form=StudentForm(instance=edit_student)
        context={"form":form}
        messages.info(request,"this is original data")
        return render(request,"student/registration-form.html",context)

#this method use for deleting the record of student but this method is only by teacher
@login_required
def delete(request,slug):
    item=get_object_or_404(Student,slug=slug)
    item.delete()
    messages.success(request,"successfully delete the data..")
    return redirect("student:home")





