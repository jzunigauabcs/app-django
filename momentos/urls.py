from django.urls import path
from .views import index, save_momento

urlpatterns = [
    path('', index, name='home'),
    path('save/', save_momento, name='save_momento')
]
