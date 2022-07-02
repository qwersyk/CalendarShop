"""CalendarShop URL Configuration

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
from OnlineStoreOfCalendars import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:lg>/Home/',views.Home,name="home"),
    path('<str:lg>/<int:id>/',views.Install,name="install"),
    path('<str:lg>/Release/',views.Release,name="release"),
    path('<str:lg>/Event/',views.Event,name="event"),
    path('<str:lg>/Other/',views.Other,name="other"),
    path('<str:lg>/Sport/',views.Sport,name="sport"),
    path('<str:lg>/Holidays/',views.Holidays,name="holidays"),
    path('<str:lg>/Create/',views.Create,name="create"),
    path('<str:lg>/Post/',views.Post,name="post"),
    path('GetName',views.GetName,name="GetName"),
    path('<str:lg>/edit/<int:id>/',views.Edit,name="edit"),
    path('<str:lg>/search=/<str:sear>/',views.Search,name="search")
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
