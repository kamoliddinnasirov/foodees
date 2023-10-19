from django.urls import path
from main.views  import Home, Menu

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('Menu/', Menu.as_view(), name='menu'),

]