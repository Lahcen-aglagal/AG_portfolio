from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
import  os 
import re

class Profile(models.Model):
    user = models.OneToOneField (User , on_delete = models.CASCADE ,default=0)
    image = models.ImageField('Image' , upload_to= 'image/' , default= 'image/default_profile.png')
    STAT_CHOICES = (
        ('married', 'Married'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    )

    DEGREE_CHOICES = (
        ('Licence' , 'Licence'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    )

    phone = models.CharField('Phone', max_length=100,null=True )
    address = models.CharField('Address', max_length=100,null = True )
    status = models.CharField('Status', max_length=20, choices=STAT_CHOICES, default='single',null=True)
    birth_date = models.DateField('Birth date', auto_now_add=False,null=True)
    city = models.CharField('City', max_length=100,null=True)
    degree = models.CharField('Degree',max_length=20,choices=DEGREE_CHOICES,null=True)


    def __str__(self):
        return str(self.user)

class About(models.Model):
    user = models.OneToOneField (User , on_delete = models.CASCADE ,default=0 )
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=1000, blank=True, null=True)
    resume = models.FileField('Resume', upload_to='media/', blank=True, null=True)
    def __str__(self):
        return str(self.title)
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=100, verbose_name='Skill Name', null=True)
    proficiency_choices = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    )
    proficiency = models.CharField(max_length=20, choices=proficiency_choices, default='beginner', null=True)
    percent = models.PositiveIntegerField(verbose_name='Proficiency Percentage', default=0, help_text='Enter a value between 0 and 100', null=True)

    def __str__(self):
        return self.title


    def __str__(self):
        return str(self.title)
    
class ProfessionalExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    title = models.CharField('Job Title', max_length=100 ,null=True)
    company = models.CharField('Company', max_length=100 ,null=True)
    location = models.CharField('Location', max_length=100 ,null=True)
    start_date = models.DateField('Start Date' , null = True)
    end_date = models.DateField('End Date', null=True, blank=True)
    description = models.TextField('Description', max_length=1000 ,null=True)

    def __str__(self):
        return self.title
    
class Education(models.Model):
    DEGREE_CHOICES = (
        ('baccalaureate' , 'baccalaureate'),
        ('Bac+2' , 'Bac+2'),
        ('Bac+3/Licence' , 'Bac+3/Licence'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    degree = models.CharField('Degree', max_length=100 ,null=True , choices=DEGREE_CHOICES)
    institution = models.CharField('Institution', max_length=100 ,null=True)
    location = models.CharField('Location', max_length=100 ,null=True)
    start_date = models.DateField('Start Date' ,null=True)
    end_date = models.DateField('End Date', null=True, blank=True)
    description = models.TextField('Description', max_length=1000 ,null=True)

    def __str__(self):
        return self.degree
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField('Project Title', max_length=100, null=True)
    description = models.TextField('Description', max_length=1000, null=True)
    technologies = models.CharField('Technologies Used', max_length=200, null=True)
    github_url = models.URLField('GitHub URL', blank=True, null=True)
    demo_url = models.URLField('Demo URL', blank=True, null=True)

    def __str__(self):
        return self.title

def sanitize_filename(filename):
    return re.sub(r'[\/:*?"<>|]', '', filename)

def image_upload_path(instance, filename):
    title = instance.project.title
    sanitized_title = sanitize_filename(title)
    directory_path = os.path.join(sanitized_title, filename)
    return directory_path

class ProjectImage(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='images')  # Add related_name here
    image = models.ImageField('Image', upload_to=image_upload_path)

    def __str__(self):
        return self.project.title + ' Image'

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,default=0)
    title = models.CharField('Service Title', max_length=100, null=True)
    description = models.TextField('Description', max_length=1000, null=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2,null=True)
    
    def __str__(self):
        return self.title

class Facts(models.Model):
    description = models.TextField('Description', max_length=1000, blank=True, null=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default=0)
    email = models.EmailField('Email', max_length=100)
    phone = models.CharField('Phone', max_length=20, blank=True, null=True)
    address = models.CharField('Address', max_length=200, blank=True, null=True)
    message = models.TextField('Message', max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.user.username + "'s Contact Info"
    
@receiver(post_save , sender = User)
def create_user_profile(sender , instance  , created , **kwargs):
    if created :
        Profile.objects.create(
            user = instance 
        )
        About.objects.create(
            user = instance
        )
        Skill.objects.create(
            user = instance
        )
        ProfessionalExperience.objects.create(
            user = instance
        )
        Education.objects.create(
            user = instance
        )
        Project.objects.create(
            user = instance
        )
        Service.objects.create(
            user = instance
        )
        Facts.objects.create(
            user = instance
        )