"""
Design models for a simple e-commerce system with the following requirements:

Each Product has a name, description, and price.

Each Customer has a name, email, and can have multiple Address instances. 
They also have a Profile model with a date_of_birth and photo fields.

There is a receiver that creates a Profile instance for each new Customer.

Each Address has a street, city, state, and zip code.

A Customer can have multiple Order instances. Each Order can contain multiple Product instances. 

The quantity of each Product in an Order should be tracked.

When an Order is placed, the total price should be calculated and saved.

Discuss how you would design the models for this system. What fields would each model have? How would you use OneToOne, ManyToMany, and ForeignKey relationships? 

How would you override the save method to calculate the total price of an Order in the Order model?


"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    """Each Product has a name, description, and price."""
    # name, description, and price.
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    price=models.FloatField()


class Customer(models.Model):
    """Each Customer can have multiple Address instances."""
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    pass    # name, email.

class Address(models.Model):
    #street, city, state, and zip code
    customer=models.ForeignKey(Customer)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip_code=models.IntegerField()
    """Each Customer can have multiple Addresses."""
    pass    # street, city, state, and zip code.

class Profile(models.Model):
    date_of_birth=models.DateField()
    photo=models.ImageField()
    """Each user can have only one Profile."""
    pass    # date_of_birth, photo.

class Order(models.Model):
    total_price=models.DecimalField()
    """Each Order can contain multiple Products."""
    pass   # total_price.

class OrderProduct(models.Model):
    product=models.ForeignKey(Order)
    quantitiy=models.IntegerField()


    """This model will be used to track the quantity of each Product in an Order.
    Override the save method to calculate the total price of an Order in the Order model."""
    pass    # quantity.


# <-------------------Signals------------------->
# Create a receiver that creates a Profile instance for each new Customer.
