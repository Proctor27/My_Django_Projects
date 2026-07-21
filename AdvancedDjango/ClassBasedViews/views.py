from django.shortcuts import render
#from django.http import HttpResponse
#import View from django for class Based View
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy  # Changed from django.core.urlresolvers
# Create your views here.
"""def index(request):
    return render(request,"cbv/index.html")"""


class IndexView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['signs'] = 'BARBIE GIRL'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'cbv/school_list.html'
    #it gets return as a context dictionary as school_list. but it can be
    #changed using context_object_name

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv/school_details.html'
    #detailview returns just the model in lowercase, as opposed to listview that returns it as
    #school_list


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    template_name = 'cbv/school_form.html'

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    template_name = 'cbv/school_form.html'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('ClassBasedViews:list')
    template_name = 'cbv/school_confirm.html'