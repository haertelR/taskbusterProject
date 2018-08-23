from django.shortcuts import render

def home(request):
  return render(request, "taskbuster/index.html", {} )

def home_files(request, filename):
  return render(request, filename, {}, context_type='text/plain')
