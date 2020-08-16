from django.urls import path
from classifiers import views

urlpatterns = [
    path('okved2/', views.okved2),
    path('okved2007/', views.okved2007),
    path('okpd2/', views.okpd2),
]
