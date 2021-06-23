"""alinascloset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import include
from django.urls import path
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from alinasclosetapi.views import login_user, register_user
from alinasclosetapi.views.piece import PieceView
from alinasclosetapi.views.user import UserView
from alinasclosetapi.views.userpiece import UserPieceView
from alinasclosetapi.views.look import LookView
from alinasclosetapi.views.list import ListView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pieces', PieceView, 'piece')
router.register(r'users', UserView, 'user')
router.register(r'userpieces', UserPieceView, 'userpiece')
router.register(r'looks', LookView, 'look')
router.register(r'lists',ListView, 'list')


urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user)
]   + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)