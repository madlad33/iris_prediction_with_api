from django.urls import path, include
from .views import FlowerPredictView

urlpatterns = [
    path('predict/', FlowerPredictView.as_view(), name='predict')

]
