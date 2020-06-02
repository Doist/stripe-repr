import stripe
import stripe.stripe_object

from stripe_repr import patch

patch()


def test_entity():
    # entity shows the id and the name.
    customer = stripe.Customer(id="cust_foo")
    customer.update({"name": "Foo"})
    assert repr(customer) == "Customer(id='cust_foo', name='Foo')"


def test_value_object():
    # value object shows the entire contents.
    obj = stripe.stripe_object.StripeObject(id=None)
    obj.update({"name": "Foo"})
    assert repr(obj) == "StripeObject(name='Foo')"


def test_value_object_datetime():
    # value object converts integers to date strings.
    obj = stripe.stripe_object.StripeObject(id=None)
    obj.update({"created": 1577836800})
    assert repr(obj) == "StripeObject(created='2020-01-01T00:00:00')"


def test_collection():
    # collection returns only its data
    customers = stripe.ListObject()
    customers.update(
        {"data": [stripe.Customer(id="cust_foo"), stripe.Customer(id="cust_bar")]}
    )
    expected_repr = (
        "ListObject(data=[Customer(id='cust_foo'), Customer(id='cust_bar')])"
    )
    assert repr(customers) == expected_repr


def test_d():
    # Formatted dict (also know as "d") removes None and [], and converts integers to
    # date strings.
    obj = stripe.stripe_object.StripeObject(id=None)
    obj.update({"name": "Foo", "created": 1577836800, "meta_info": None})
    assert obj.d() == {"name": "Foo", "created": "2020-01-01T00:00:00"}
