from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Home_lest(request):
    context={}
    studentform=StudentForm()
    student=Student.objects.all().order_by('-id')
    if request.GET.get('search'):
        search = request.GET.get('search')
        student = Student.objects.filter(
            Q(ism__icontains = search) |
            Q(id__icontains = search) |
            Q(yoshi__icontains = search) |
            Q(familya__icontains = search) |
            Q(manzil__icontains = search) 
            
        )
    paginator=Paginator(student, 5)
    page_number=request.GET.get('page', 1)
    try:
        student=paginator.page(page_number)
    except EmptyPage:
        student=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        student=paginator.page(1) 
    if request.method == 'POST':
        if 'save' in request.POST:
            pk=request.POST.get('save')
            if not pk:
                studentform=StudentForm(request.POST)
                if studentform.is_valid():
                   f = studentform.save(commit=False)
                   f.save()
                   messages.info(request, ' Saqlash yahshi bojarildi !!!')
            else:
                stu= get_object_or_404(Student, id = pk)
                studentform=StudentForm(request.POST, instance=stu)           
                if studentform.is_valid():
                   f = studentform.save(commit=False)
                   f.save()
                   messages.info(request, ' o\'zgartirish yahshi bojarildi !!!')
            return redirect('home')
        elif 'delete' in request.POST:
            pk=request.POST.get('delete')
            student=Student.objects.get(id=pk)
            student.delete()
            messages.info(request, ' yahshi o\'chirildi !!!')
            return redirect('home')
        
        elif 'edit' in request.POST:
            pk=request.POST.get('edit')
            print("bu id", pk)
            stu= get_object_or_404(Student, id = pk)
            studentform=StudentForm(instance=stu)
        
    context['studentform']=studentform
    context['student']=student
    return render(request, 'index.html',context)