from django.urls import path 
from . import views
from django.conf import settings 
from django.conf.urls.static import static 
from .views import HomeTemplateView , ProjectDetailView

app_name = 'Home'

urlpatterns = [
    path ("Profile" , HomeTemplateView.as_view(), name ="index"),
    path ("Profile/Details/<int:pk>/" , ProjectDetailView.as_view(), name ="project_detail"),
    path ("contact/" , views.contact , name ="contact"),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

