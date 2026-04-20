from django.shortcuts import render
from django.http import HttpResponse
from Barbie.models import Femi,Webpage,AccessRecord
# Create your views here.

def lady(request):
    #Query the model
    lady = AccessRecord.objects.order_by('date')
    heading = Webpage.objects.order_by('topic')
    #create a dictionary to display the queried model.
    Dolly = {'jolene':lady,"sometimes":heading}
    return render(request,'Barbie/index.html',context=Dolly)
 