

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

    def add(self, product):
        """
        Adding and updating the users cart session data
        """
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
