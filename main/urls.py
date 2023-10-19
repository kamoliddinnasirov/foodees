from django.urls import path
from main.views  import HomeView, AboutView


app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),

]