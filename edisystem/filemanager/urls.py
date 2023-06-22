from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'filemanager'

urlpatterns = [
    path('',views.upload_view,name='home'),
    path('upload/', views.upload_view, name='upload'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('uploadPO/', views.upload_file, name='upload_file'),
    path('uploadInvoice/', views.upload_invoice, name='upload_invoice'),
    path('submitForm/', views.dashboard_view, name='form_submit'),
    path('show_entries/', views.show_entries, name='show_entries'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
