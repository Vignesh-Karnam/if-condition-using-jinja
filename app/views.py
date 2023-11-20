from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10}
    return render(request,'condition.html',d)

def condition2(request):
    k={'a':10,'b':20}
    return render(request,'condition2.html',k)