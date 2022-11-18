from django.views.generic.base import TemplateView

class ShoppingCartPageView(TemplateView):
    template_name = 'orders/purchase.html'
