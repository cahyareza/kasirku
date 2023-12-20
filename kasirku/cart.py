from django.conf import settings
from decimal import Decimal
from .models import Barang

class Cart():
    '''
    Akan membuat session dengan keys cart dan salah satu valuenya product_id
    "cart" ={
    "product_id": {
        'price': $9.99,
        'quantity': 1,
        'id': nike,
        'stok': 114
        }
    }

    Kemudian pada session ini bisa menambahkan di session cart menggunakan prinsip2 dictionary data type
    '''

    def __init__(self, request):
        self.session = request.session
        # initialize session cart
        cart = self.session.get(settings.CART_SESSION_ID)

        # jika tidak bukan cart
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart


    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.harga), 'quantity': 0, 'stok': str(product.quantity)}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            # edit logic from += to =
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Barang.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            print(item)
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            item['total_diskon'] = item['product'].diskon * (item['price'] / 100)
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_subtotal_price(self):
        return sum(item['price']* item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return int(sum(Decimal(item['price']* item['quantity']) - int(Decimal(item['price']* item['quantity'] * Decimal((item["product"].diskon/100)))) for item in self.cart.values()))

    def get_total_diskon(self):
        return int(sum(item['price']* item['quantity'] * Decimal((item["product"].diskon/100)) for item in self.cart.values()))

    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True






