from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard route
    path('map/', views.map_view, name='map_view'),  # Map route
    path('smart-bins/', views.smart_bins, name='smart_bins'),  # Smart bins route
    path('smart-bins/update/<int:bin_id>/', views.update_bin_fill_level, name='update_bin_fill_level'),  # Update fill level route
    path('tracking/', views.tracking, name='tracking'),  # Tracking route
    path('dumping-area/', views.dumping_area, name='dumping_area'),  # Dumping area route
    path('company-portal/', views.company_portal, name='company_portal'),  # Company portal route
    path('company-portal/signup/', views.company_signup, name='company_signup'),  # Company signup route
]