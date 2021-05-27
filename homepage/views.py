from django.shortcuts import render
from .models import page,Slider_Images
# Create your views here.
def index(request):
    mod=page.objects.all()
    tom = Slider_Images.objects.all()
    context={
        'mod':mod,
        'tom':tom
    }
    return render(request,'index.html',context=context)

def detail(request,pk):
    mod=page.objects.get(pk=pk)
    context={
        'mod':mod

    }
    return render(request,'detail.html',context=context)

def banner(request):
    tom=Slider_Images.objects.all()

    context={
        'tom':tom
    }

    return render(request,'new.html',context=context)