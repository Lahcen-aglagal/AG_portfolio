from django.contrib import admin
from .models import Profile , About , Contact ,Education ,Facts ,Project ,Service , Skill , ProjectImage,sociallinks , typedItem , ProfessionalExperience

# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Facts)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(ProjectImage)
admin.site.register(sociallinks)
admin.site.register(typedItem)
admin.site.register(ProfessionalExperience)