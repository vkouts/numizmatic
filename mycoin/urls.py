from django.urls import path

from mycoin.views import MyCoinsView, AboutView, MyCoinDetailView

urlpatterns = [
    path('detail/<int:pk>/', MyCoinDetailView.as_view(), name="my-coin-detail"),
    path('coins/', MyCoinsView.as_view(), name="my-coins-view"),
    path('about/', AboutView.as_view(), name="about-view"),
]