from django.shortcuts import render
from django.http import HttpResponse,Http404
# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
from .models import Ngo,NgoDetails

# Create your views here.
def index(request):
    all_ngos=Ngo.objects.all()
    return render(request,'ngo/index.html', {'all_ngos':all_ngos})

def detail(request,ngo_id):
    try:
        ngo=Ngo.objects.get(pk=ngo_id)
    except Ngo.DoesNotExist:
        raise Http404()
    return render(request,'ngo/detail.html', {'ngo':ngo})

def signup(request):
    return render(request,'ngo/signup.html')

def login(request):
    return render(request,'ngo/login.html')

# class NgoCreate(CreateView):
#     model=Ngo
#     fields=['ngo_name','ngo_logo','ngo_loc','relief_type']

#     def form_valid(self,form):
#         form.instance.created_by=self.request.user
#         return super().form_valid(form)