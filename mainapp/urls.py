from django.urls import path
from .views import (
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
    DestinationListCreateView,
    DestinationRetrieveUpdateDestroyView
)

urlpatterns = [
    path('api/accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('api/accounts/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-retrieve-update-destroy'),
    path('api/accounts/<int:account_id>/destinations/', DestinationListCreateView.as_view(), name='destination-list-create'),
    path('api/accounts/<int:account_id>/destinations/<int:pk>/', DestinationRetrieveUpdateDestroyView.as_view(), name='destination-retrieve-update-destroy'),
]
