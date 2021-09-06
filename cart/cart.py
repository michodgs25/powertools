


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