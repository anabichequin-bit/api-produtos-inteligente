from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Avg
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemMaisCaroView(APIView):
    def get(self, request):
        item = Item.objects.order_by('-preco').first()
        if not item:
            return Response({"message": "Nenhum item encontrado"}, status=404)
        return Response({"id": item.id, "nome": item.nome, "preco": item.preco})

class ItemMaisBaratoView(APIView):
    def get(self, request):
        item = Item.objects.order_by('preco').first()
        if not item:
            return Response({"message": "Nenhum item encontrado"}, status=404)
        return Response({"id": item.id, "nome": item.nome, "preco": item.preco})

class SomaPrecosView(APIView):
    def get(self, request):
        total = Item.objects.aggregate(total=Sum('preco'))['total'] or 0
        return Response({"total_precos": total})

class MediaPrecosView(APIView):
    def get(self, request):
        media = Item.objects.aggregate(media=Avg('preco'))['media'] or 0
        return Response({"media_precos": media})

class ContagemItensView(APIView):
    def get(self, request):
        return Response({"total_itens": Item.objects.count()})

class ItensAcimaPrecoView(APIView):
    def get(self, request):
        min_preco = request.query_params.get('min_preco')
        if min_preco is None:
            return Response({"message": "Informe o parâmetro min_preco"}, status=400)
        try:
            min_preco = float(min_preco)
        except ValueError:
            return Response({"message": "min_preco deve ser numérico"}, status=400)

        itens = Item.objects.filter(preco__gt=min_preco)
        data = ItemSerializer(itens, many=True).data
        return Response(data)
