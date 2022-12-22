from django.urls import path

from apps.views import HomeView, PortfolioDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('portfolio/<str:slug>', PortfolioDetailView.as_view(), name='portfolio_detail_view'),

]
