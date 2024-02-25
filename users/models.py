from django.db import models

class Student(models.Model):
    app_label = 'users'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Teacher(models.Model):
    app_label = 'users'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)















# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django import forms
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class CustomUser(AbstractBaseUser, PermissionsMixin):

    # id = models.AutoField(primary_key=True)
    # email = models.EmailField(unique=True)
    # username = models.CharField(max_length=150, blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)
    
    # # Пользовательский метод
    # def send_confirmation_email(self):
    #     pass
    
    # # Переопределение метода save()
    # def save(self, *args, **kwargs):
    #     # Ваша логика сохранения
    #     super().save(*args, **kwargs)
    
    # # Дополнительное свойство
    # @property
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}" if self.first_name or self.last_name else self.email


# from django.shortcuts import render, redirect
# from .forms import StudentSignUpForm, TeacherSignUpForm

# def student_register(request):
#     if request.method == 'POST':
#         form = StudentSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
#     else:
#         form = StudentSignUpForm()
#     return render(request, 'registration/student_register.html', {'form': form})

# def teacher_register(request):
#     if request.method == 'POST':
#         form = TeacherSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
#     else:
#         form = TeacherSignUpForm()
#     return render(request, 'registration/teacher_register.html', {'form': form})