from django.urls import path

from .views import HomeView, CategoryView, FurnitureDetailView, CompanyInfoView, TableTopInfoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('furniture/<int:pk>/', FurnitureDetailView.as_view(), name='furniture_detail'),
    path('company-info/', CompanyInfoView.as_view(), name='company_info'),
    path('table_top_info/', TableTopInfoView.as_view(), name='table_top_info')
]
