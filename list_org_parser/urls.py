from django.urls import path
from list_org_parser import views

urlpatterns = [
    path('parse_urls/', views.parse_urls),
    path('parse_orgs/', views.parse_orgs),
]