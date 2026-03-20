from django.urls import path
from crime.views import get_crimes, add_crime

urlpatterns = [
    path('crimes/', get_crimes),
    path('add-crime/', add_crime),
]