from decimal import Decimal

from store.models import Product


class Cart():
    """
    A base Cart class,
    provide default behaviors.
    That can be override when necessary.
    """

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id]['qty']
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to the query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())


"""
Code in this file has been inspried/reworked from other known works. Plese ensure that
the License below is included in any of your work that is directly copied from
this source file.
MIT License
Copyright (c) 2019 Packt
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
"""