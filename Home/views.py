from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpRequest ,JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User 
from .models import *
from .models import Profile,typedItem,About,ProfessionalExperience,Education,Facts,Project,ProjectImage,Service,Skill,sociallinks,Contact,Category
# Create your views here.
from datetime import date
from django.shortcuts import render, get_object_or_404

def M_Profile(request): 
    user = User.objects.first()
    profile = Profile.objects.first()
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'Base/footer.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    ImgProj = ProjectImage.objects.filter(project=project)
    context  = {
        'project': project ,
        'projectimages': ImgProj
        }
    return render(request, 'includes/portfolio-details.html', context)

class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    # override get context date method
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['title'] = "Portfolio LAHCEN AGLAGAL"

        context['user'] = User.objects.first()
        context['profile'] = Profile.objects.first()
        context['typedItem'] = typedItem.objects.all()

        context['about'] = About.objects.first()
        context['contact'] = Contact.objects.first()
        context['education'] = Education.objects.all()
        context['facts'] = Facts.objects.first()
        context['service'] = Service.objects.all()
        context['skill'] = Skill.objects.all()
        
        context['sociallinks'] = sociallinks.objects.all()
        context['myposition'] = typedItem.objects.all()[3]
        context['ProfessionalExperience'] = ProfessionalExperience.objects.all()


        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.all()
        # context['projectimage'] = ProjectImage.objects.first(proje=context['project'])

        skills = Skill.objects.filter(user=context['user'])
        num_skills = len(skills)
        middle_index = num_skills // 2
        skills_column1 = skills[:middle_index]
        skills_column2 = skills[middle_index:]  
        
        context['skills_column1'] = skills_column1
        context['skills_column2'] = skills_column2
        today = date.today()
        birth_date = context['profile'].birth_date
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        context['age'] = age
        return context
    