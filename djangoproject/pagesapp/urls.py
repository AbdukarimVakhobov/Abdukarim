from django.urls import path
from .views import HomapageView, AboutpageView


urlpatterns = [
    path('', HomapageView.as_view(), name='home'),
    path('about', AboutpageView.as_view(), name='about')
]