from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home_view, name='home'),
    path('<slug:slug>/', views.single_view, name='single'),
    # path('single/', views.single_post, name='single'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
