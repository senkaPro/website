from django.shortcuts import render
from .models import Story


def home(request):
    return render(request,'stories/base.html')

def stories_view(request):
    template = 'stories/story_list.html'
    qs = Story.objects.all()
    return render(request,template,{'stories':qs})
