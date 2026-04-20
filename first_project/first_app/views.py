from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Users,Details,Descriptions
from first_app.forms import MyNewForm
# Create your views here.

def index(request):
    evangeline = {"World":"Don't go to sleep, don't rest your head"}
    return render(request,'first_app/Crazy.html',context=evangeline)

 

def profiles(request):
    #Query the model
    lady = Users.objects.order_by('usernames')
     
    #create a dictionary to display the queried model.
    Dolly = {'jolene':lady}
    return render(request,'first_app/Users.html',context=Dolly)

def Dets(request):
    #Query the model
    lady = Details.objects.order_by('users')
   # form = forms.MyNewForm()
    #create a dictionary to display the queried model.
    Dolly = {'jolene':lady}#'pacify':form}
    
    return render(request,'first_app/Details.html',context=Dolly)
def Desc(request):
    #Query the model
    lady = Descriptions.objects.order_by('date')
     
    #create a dictionary to display the queried model.
    Dolly = {'jolene':lady}
    return render(request,'first_app/Descriptions.html',context=Dolly)
 
def NewformMethod(request):
    form = MyNewForm()
    
    # 1. Use 'request.method', not 'render.Method'
    if request.method == 'POST':
        form = MyNewForm(request.POST)

        if form.is_valid():
            # 2. Use 'True' (capitalized) for Python booleans
            form.save(commit=True)
            # 3. Call your index view or redirect
            return index(request)
        else:
            print("Form is invalid!")
            
    return render(request, "first_app/form.html", {'pacify': form})
