import stripe
import stripe.stripe_object

from stripe_repr import patch

patch()


def test_entity():
    customer = stripe.Customer(id="cust_foo")
    customer.update({"name": "Foo"})
    assert repr(customer) == "Customer(id='cust_foo', name='Foo')"


def test_value_object():
    obj = stripe.stripe_object.StripeObject(id=None)
    obj.update({"name": "Foo"})
    assert repr(obj) == "StripeObject(name='Foo')"


def test_value_object_datetime():
    obj = stripe.stripe_object.StripeObject(id=None)
    obj.update({"created": 1577836800})
    assert repr(obj) == "StripeObject(created='2020-01-01T00:00:00')"


def test_collection():
    obj = stripe.Invoice(id=None)
    obj.update({"data": [stripe.InvoiceItem(id="foo_1")]})
    assert repr(obj) == "Invoice(data=[InvoiceItem(id='foo_1')])"
