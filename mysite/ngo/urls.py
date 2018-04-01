from django.urls import path, include
from . import views
#from ngo.views import NgoCreate

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:ngo_id>/' ,views.detail ,name='detail'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
   # path('add/',NgoCreate.as_view(),name="ngo-add"),
]