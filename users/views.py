from django.shortcuts import render
from .forms import TeacherRegistrationForm, StudentRegistrationForm



def reg(request):
  return render(request, 'registration/register.html')

def student(request):
  form = StudentRegistrationForm()
  return render(request, 'registration/student_register.html', {'form': form})

def educator(request):
  form = TeacherRegistrationForm()
  return render(request, 'registration/teacher_register.html', {'form': form})
# Create your views here.
