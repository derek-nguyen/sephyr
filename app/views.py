from django.shortcuts import render
import subprocess

def index(request):
	context = {}
	return render(request, 'index.html', context)