from django.urls import path

from mycoin.views import MyCoinsView

urlpatterns = [
    path('coins/', MyCoinsView.as_view(), name="my-coins-view")
]