from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Intro(request):
    name="Job"
    company = "LTIMindtree"
    Gender = "Male"
    my_dict= {'Name':name,"Company":company,"Gender":Gender}
    return render(request,'intro.html',my_dict)
    #return HttpResponse(<p> Hello world! <p>)

