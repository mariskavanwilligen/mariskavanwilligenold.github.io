Title: Inheritance
Date: 2022-01-07 11:20
Modified: 2022-01-07 15:34
Tags: Python, Classes, Inheritance, Subclasses, object-oriented
Slug: Inheritance
Authors: Mariska van Willigen
Summary: Basics of Object-oriented python programming: Inheritance explained

## Inheritance

## Overriding attributes
You can override an attribute of the parent class in the subclass:
``` js
class Product(object):
    product = "Coca Cola"

class NewProduct(Product):
    product = "Fanta"
```
Any instance of the new class will have the *Fanta* as product. Any instance of the parent/original class will have as product *Coca Cola*.

## Overriding methods
Same as with overriding methods:
``` js
class Product(object):
    def forecast_product(self, lift_factor=5)
        forecast = self.last_sales * factor
        return forecast

class NewProduct(Product):
    def forecast_product(self, lift_factor=5)
        forecast = self.last_sales * lift_factor * math.sqrt(2)
        return forecast

```
The new subclass NewProduct has a changed forecast_product function. Instances from the parent/original class will still have the old function forecat_product from the Product class.