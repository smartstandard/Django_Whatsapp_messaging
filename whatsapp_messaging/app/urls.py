
from django.contrib import admin
from django.urls import path
from .views import send_whatsapp_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-whatsapp/', send_whatsapp_message, name='send_whatsapp'),
]