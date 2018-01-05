from django.urls import path

from mycoin.views import MyCoinsView, AboutView

urlpatterns = [
    path('coins/', MyCoinsView.as_view(), name="my-coins-view"),
    path('about/', AboutView.as_view(), name="about-view"),
]