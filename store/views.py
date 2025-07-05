from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product, Order, OrderItem
from django.db.models import Q

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'category', 'description', 'stock',]
    template_name = 'store/product_form.html'
    permission_required = 'store.add_product'
    success_url = '/'

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)
    item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if created:
        item.quantity = 1
    else:
        item.quantity += 1
    item.save()
    return redirect('cart')

@login_required
def cart_view(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'store/cart.html', {'order': order})

@login_required
def confirm_order(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if order:
        order.is_paid = True
        order.save()
    return render(request, 'store/order_confirmation.html')


class ProductSearchView(ListView):
    model = Product
    template_name = 'store/product_search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(Q(name__icontains=query))
        return Product.objects.none()
