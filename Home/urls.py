from django.urls import path , include
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from .views import HomeTemplateView , project_detail

app_name = 'Home'

urlpatterns = [
    path ("Profile" , HomeTemplateView.as_view(), name ="index"),
    path('Profile/project/details/<int:pk>/', project_detail , name='project_detail'),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

