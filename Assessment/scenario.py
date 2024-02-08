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
    pass   # name, description, and price.

class Address(models.Model):
    """Each Customer can have multiple Addresses."""
    pass    # street, city, state, and zip code.

class Customer(models.Model):
    """Each Customer can have multiple Address instances."""
    pass    # name, email.

class Profile(models.Model):
    """Each user can have only one Profile."""
    pass    # date_of_birth, photo.

class Order(models.Model):
    """Each Order can contain multiple Products."""
    pass   # total_price.

class OrderProduct(models.Model):
    """This model will be used to track the quantity of each Product in an Order.
    Override the save method to calculate the total price of an Order in the Order model."""
    pass    # quantity.


# <-------------------Signals------------------->
# Create a receiver that creates a Profile instance for each new Customer.

