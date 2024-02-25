"""

To render html web pages

"""
from django.shortcuts import render


def index(request):
  """
  Take in a request (Dj)
  """
  return render(request, 'index.html')