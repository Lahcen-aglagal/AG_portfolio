from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpRequest ,JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User 
from .models import *
# Create your views here.

def index(request): 
    return render(request , 'index.html')


class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['title'] = "Portfolio LAHCEN AGLAGAL"
        context['user'] = User.objects.first()
        context['profile'] = Profile.objects.first()
        context['about'] = About.objects.first()
        context['contact'] = Contact.objects.first()
        context['education'] = Education.objects.all()
        context['facts'] = Facts.objects.first()
        context['project'] = Project.objects.all()
        context['service'] = Service.objects.all()
        context['skill'] = Skill.objects.all()
        context['projectimage'] = ProjectImage.objects.all()
        context['sociallinks'] = sociallinks.objects.first()
        return context
    