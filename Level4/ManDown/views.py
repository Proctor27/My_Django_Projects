from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'2face', 'sun':444}
    return render(request,'ManDown/index.html',context_dict)

def otherpage(request):
    return render(request, 'ManDown/other.html')

def relative(request):
    return render(request, 'ManDown/relative_url.html')

def base(request):
    return render(request, 'ManDown/base.html')