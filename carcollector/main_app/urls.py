from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_service/', views.add_service, name='add_service'),
    path('cars/<int:car_id>/assoc_passenger/<int:passenger_id>/', views.assoc_passenger, name='assoc_passenger'),
    path('passengers/', views.PassengerList.as_view(), name='passengers_index'),
    path('passengers/<int:pk>/', views.PassengerDetail.as_view(), name='passengers_detail'),
    path('passengers/create/', views.PassengerCreate.as_view(), name='passengers_create'),
    path('passengers/<int:pk>/update/', views.PassengerUpdate.as_view(), name='passengers_update'),
    path('passengers/<int:pk>/delete/', views.PassengerDelete.as_view(), name='passengers_delete'),
]