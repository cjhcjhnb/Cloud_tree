



from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def count(request):
    total_text =request.GET['text']
    return render(request,'count.html',{'total_text':total_text})