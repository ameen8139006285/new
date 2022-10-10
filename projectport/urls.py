from django.contrib import admin
from django.urls import path
from hmdport import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('contact', views.viewcontact,name='contact'),
    path('gallery', views.gallery,name='gallery'),
    path('gallery-single', views.gallerysingle,name='gallerysingle'),
    path('gallery2', views.gallery2,name='gallery2'),
    path('gallery3', views.gallery3,name='gallery3'),
    path('gallery4', views.gallery4,name='gallery4'),
    path('gallery5', views.gallery5,name='gallery5'),
    path('gallery6', views.gallery6,name='gallery6'),
    path('gallery7', views.gallery7,name='gallery7'),
    path('services', views.services,name='services'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
