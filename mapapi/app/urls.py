from django.urls import path
from app.views import GetAddressDetails


urlpatterns = [
    path('api/getAddressDetails/',GetAddressDetails.as_view()),
]