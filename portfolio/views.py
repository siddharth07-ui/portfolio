from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, './index.html')

def about(request):
    return render(request, './skills.html')

def experience(request):
    return render(request, './exp.html')

def education(request):
    return render(request, './educt.html')