from django.shortcuts import render
from .models import copperProduct

from .forms import FeedbackForm

# Create your views here.

def index(r):
    prd_list=copperProduct.objects.all()
    md={'prd_list':prd_list}

    return render(r,'copper/index.html',context=md)


def feedback(r):
    form = FeedbackForm()
    return render(r,'copper/feedback.html',{'form':form})

