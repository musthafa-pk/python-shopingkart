from django.urls import include,path
from . import views

urlpatterns =  [
    path('',views.index,name='index'),
    path('productspage.html',views.productspage,),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')
]
    