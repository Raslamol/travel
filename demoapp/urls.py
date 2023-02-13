from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/', views.substration, name='substration'),
    # path('mul/', views.multiplication, name='multiplication'),
    # path('div/', views.division, name='division'),


    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks'),

]
