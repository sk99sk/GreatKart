from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
from django.http import HttpResponse
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def store(request,category_slug=None):
    categories = None
    products = None


    if category_slug!=None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('id')

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    paginator = Paginator(products,6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context={
        'products':paged_products,
        'num_products':len(products),
    }
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product = single_product).exists()
        context = {
            'single_product':single_product,
            'in_cart':in_cart,
        }
        return render(request,'store/product_detail.html',context)

    except :
        return HttpResponse("Product not found")
