from django.shortcuts import render
from Third_app import forms

# Create your views here.
def battle(request):
    form = forms.Form_Cupid()
    #check if the method is post
    if request.method == 'POST':
        form = forms.Form_Cupid(request.POST)
        #check if the form is valid
        if form.is_valid():
            #do something
            print("validation success!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,"Third_app/Form.html",{'pacify':form})
def index(request):
    return render(request,"Third_app/index.html")