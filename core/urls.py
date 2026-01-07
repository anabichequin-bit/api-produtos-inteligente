from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet,
    ItemMaisCaroView,
    ItemMaisBaratoView,
    SomaPrecosView,
    MediaPrecosView,
    ContagemItensView,
    ItensAcimaPrecoView,
)

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('items/mais_caro/', ItemMaisCaroView.as_view()),
    path('items/mais_barato/', ItemMaisBaratoView.as_view()),
    path('items/soma_precos/', SomaPrecosView.as_view()),
    path('items/media_precos/', MediaPrecosView.as_view()),
    path('items/contagem_itens/', ContagemItensView.as_view()),
    path('items_acima_preco/', ItensAcimaPrecoView.as_view()),
]

urlpatterns += router.urls
