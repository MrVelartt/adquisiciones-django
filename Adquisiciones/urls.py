from django.urls import path
from .views import AcquisitionListCreateAPIView, AcquisitionDetailAPIView

urlpatterns = [
    path('acquisitions/', AcquisitionListCreateAPIView.as_view(), name='acquisition-list-create'),
    path('acquisitions/<int:pk>/', AcquisitionDetailAPIView.as_view(), name='acquisition-detail'),
]