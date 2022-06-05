"""prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import indexPLview, indexENview, resultsPLview, resultsENview, surveyPLview, surveyENview, thanksPLview, thanksENview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pl/', indexPLview),
    path('en/', indexENview),
    path('pl/survey/', surveyPLview),
    path('en/survey/', surveyENview),
    path('pl/thanks/', thanksPLview),
    path('en/thanks/', thanksENview),
    path('pl/results/', resultsPLview),
    path('en/results/', resultsENview),
]
