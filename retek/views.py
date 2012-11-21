from django.views.decorators.csrf import csrf_exempt

from spyne.server.django import DjangoApplication
from spyne.model.primitive import String, Integer, Mandatory
from spyne.model.complex import Iterable
from spyne.service import ServiceBase
from spyne.interface.wsdl import Wsdl11
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc

def save_order_to_database(user_id, food_id, amount):
    if amount >= 10:
        return False

    return True

class OrderFoodService(ServiceBase):

    @rpc(Mandatory.Integer, Mandatory.Integer, Mandatory.Integer, _returns=Mandatory.String)
    def order_food(ctx, user_id, food_id, amount):
        result = save_order_to_database(user_id, food_id, amount)
        if result:
            return 'ok'
        else:
            return "We don't have enough supplies to fulfill your order. Sorry"

order_food_service = csrf_exempt(DjangoApplication(Application([OrderFoodService],
    'webdbhazi.services.order',
    in_protocol=Soap11(),
    out_protocol=Soap11(),
    interface=Wsdl11(),
)))