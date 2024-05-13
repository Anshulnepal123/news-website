from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('breaking',views.breaking, name='breaking'),
    path('breaking/<int:pk>', views.breaking_detail,name='breaking_detail'),
    path('politics', views.politics, name='politics'),
    path('politics/<int:pk>',views.politics_detail,name='politics_detail'),
    path('technology', views.technology, name='technology'),
    path('technology/<int:pk>', views.technology_detail, name='technology_detail'),
    path('sports', views.sports, name='sports'), 
    path('sports/<int:pk>', views.sports_detail, name='sports_detail'), 
    # Other URL patterns
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add this line to serve media files only in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
