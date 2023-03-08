from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        'variable1':"This is SAIRAM",
         'variable2':" HELLO "
        }
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")


def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")


def Services(request):
    return render(request,'services.html')
    #return HttpResponse("this is Repair page")


def contact(request):
    return render(request,'contact.html' )
    #return HttpResponse("this is about page")

def Repair(request):
    return render(request,'repair.html' )
    #return HttpResponse("this is about page")    