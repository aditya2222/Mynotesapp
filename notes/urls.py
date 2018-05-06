from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.NotesListView.as_view(),name='home'),
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name='notes'),
    path('thanks',views.ThanksView.as_view(),name='thanks'),
    path('signup/',views.SignUpCreateView.as_view(),name='signup'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)