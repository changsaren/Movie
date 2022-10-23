from django.urls import path
from .views import Logout, Login, signup
urlpatterns = [
    path('logout/', Logout, name='logout'),
    path('login/', Login, name='login'),
    path('signup/', signup, name='signup')
]