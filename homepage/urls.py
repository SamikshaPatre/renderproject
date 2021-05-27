from .views import index,detail, banner
from django.urls import path, include

urlpatterns = [
    path('',index),
    path('<int:pk>',detail),
    path('slider',banner)
]