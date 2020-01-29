"""sih URL Configuration
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
from django.views.generic import TemplateView
from . import views


app_name = 'accident'

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html')),
    path('', views.accident_list),
    path('<int:pk>', views.accident_detail, name='accident_detail'),
    path('tracking', views.track, name='track'),
    path('tracking/acknowledge/<int:pk>', views.acknowledge, name='acknowledge'),
    path('log/list', views.accidents_log_list, name='log_list'),
    path('log/detail/<int:pk>', views.accidents_log_detail, name='log_detail'),
]
