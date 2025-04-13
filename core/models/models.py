from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField("Phone", max_length=20, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('florist', 'Florist'),
        ('courier', 'Courier'),
        ('client', 'Client'),
    ]
    role = models.CharField("Role", max_length=20, choices=ROLE_CHOICES, default='client')
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class CourierLocation(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, 
                           related_name="locations", verbose_name="User")
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    def __str__(self):
        return f"Location of {self.user}"
    class Meta:
        verbose_name = "Courier Location"
        verbose_name_plural = "Courier Locations"

class UserStatus(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, 
                           related_name="status", verbose_name="User")
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
    ]
    status = models.CharField("Order Status", max_length=30, choices=STATUS_CHOICES, default='available')
    def __str__(self):
        return f"Location of {self.user}"
    class Meta:
        verbose_name = "User Status"
        verbose_name_plural = "User Statuses"


class WorkRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                           related_name="work_records", verbose_name="User")
    start_time = models.DateTimeField("Shift start date/time")
    end_time = models.DateTimeField("Shift end date/time", null=True, blank=True)
    def __str__(self):
        return f"Shift of {self.user} from {self.start_time}"
    class Meta:
        verbose_name = "Work Record"
        verbose_name_plural = "Work Records"

class Bouquet(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    description = models.TextField("Description")
    photo = models.ImageField("Photo", upload_to="bouquets/")
    tag = models.CharField("Tag", max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Bouquet"
        verbose_name_plural = "Bouquets"


class Flower(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    description = models.TextField("Description")
    photo = models.ImageField("Photo", upload_to="flowers/")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Flower"
        verbose_name_plural = "Flowers"

class BouquetFlower(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, 
                            related_name="flowers", verbose_name="Bouquet")
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, 
                             related_name="bouquets", verbose_name="Flower")
    count = models.PositiveIntegerField("Quantity")
    def __str__(self):
        return f"{self.flower} in {self.bouquet}"
    class Meta:
        verbose_name = "Bouquet Flower"
        verbose_name_plural = "Bouquet Flowers"

class Ribbon(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    description = models.TextField("Description")
    photo = models.ImageField("Photo", upload_to="ribbons/")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Ribbon"
        verbose_name_plural = "Ribbons"

class BouquetRibbon(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, 
                            related_name="ribbons", verbose_name="Bouquet")
    ribbon = models.ForeignKey(Ribbon, on_delete=models.CASCADE, 
                            related_name="bouquets", verbose_name="Ribbon")
    length = models.FloatField("Length")
    def __str__(self):
        return f"{self.ribbon} for {self.bouquet}"
    class Meta:
        verbose_name = "Bouquet Ribbon"
        verbose_name_plural = "Bouquet Ribbons"

class Wrapper(models.Model):
    name = models.CharField("Name", max_length=100)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    description = models.TextField("Description")
    photo = models.ImageField("Photo", upload_to="wrappers/")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Wrapper"
        verbose_name_plural = "Wrappers"

class BouquetWrapper(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, 
                            related_name="wrappers", verbose_name="Bouquet")
    wrapper = models.ForeignKey(Wrapper, on_delete=models.CASCADE, 
                              related_name="bouquets", verbose_name="Wrapper")
    length = models.FloatField("Length")
    def __str__(self):
        return f"{self.wrapper} for {self.bouquet}"
    class Meta:
        verbose_name = "Bouquet Wrapper"
        verbose_name_plural = "Bouquet Wrappers"


class StockFlower(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('is_used', 'Used'),
        ('reserved', 'Reserved'),
        ('damaged', 'Damaged'),
        ('expired', 'Expired'),
    ]
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, 
                             related_name="stock_items", verbose_name="Flower")
    delivery_date = models.DateField("Delivery Date")
    count = models.PositiveIntegerField("Quantity")
    number = models.CharField("Number", max_length=50)
    status = models.CharField("Stock Item Status", max_length=30, 
                           choices=STATUS_CHOICES, default='available')
    def __str__(self):
        return f"{self.flower} in stock ({self.count} pcs.)"
    class Meta:
        verbose_name = "Stock Flower"
        verbose_name_plural = "Stock Flowers"

class StockRibbon(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
    ]
    ribbon = models.ForeignKey(Ribbon, on_delete=models.CASCADE, 
                            related_name="stock_items", verbose_name="Ribbon")
    delivery_date = models.DateField("Delivery Date")
    length = models.PositiveIntegerField("Length")
    status = models.CharField("Stock Item Status", max_length=30, 
                           choices=STATUS_CHOICES, default='available')
    def __str__(self):
        return f"{self.ribbon} in stock ({self.length} m)"
    class Meta:
        verbose_name = "Stock Ribbon"
        verbose_name_plural = "Stock Ribbons"


class StockWrapper(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
    ]
    
    wrapper = models.ForeignKey(Wrapper, on_delete=models.CASCADE, 
                              related_name="stock_items", verbose_name="Wrapper")
    delivery_date = models.DateField("Delivery Date")
    length = models.PositiveIntegerField("Length")
    status = models.CharField("Stock Item Status", max_length=30, 
                           choices=STATUS_CHOICES, default='available')
    
    def __str__(self):
        return f"{self.wrapper} in stock ({self.length} m)"
    
    class Meta:
        verbose_name = "Stock Wrapper"
        verbose_name_plural = "Stock Wrappers"


class Basket(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ordered', 'Converted to Order'),
        ('canceled', 'Canceled'),
        ('reserved', 'Reserved'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                           related_name="baskets", verbose_name="User")
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)
    
    def __str__(self):
        return f"Basket of {self.user}"
    
    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"


class BasketBouquet(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, 
                            related_name="basket_items", verbose_name="Bouquet")
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, 
                            related_name="basket_of_basket_bouquets", verbose_name="Basket")
    count = models.PositiveIntegerField("Quantity")
    
    def __str__(self):
        return f"{self.bouquet} x{self.count}"
    
    class Meta:
        verbose_name = "Basket Bouquet"
        verbose_name_plural = "Basket Bouquets"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('processing', 'Processing'),
        ('accepted', 'Confirmed'),
        ('assembly', 'In Assembly'),
        ('delivery', 'Out for Delivery'),
        ('completed', 'Completed'),
        ('reserved', 'Reserved'),
        ('canceled', 'Canceled'),
    ]
    
    status = models.CharField("Order Status", max_length=30, choices=STATUS_CHOICES, default='new')
    date = models.DateField("Date")
    time = models.TimeField("Time")
    total = models.DecimalField("Total", max_digits=10, decimal_places=2)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE, 
                            related_name="basket", verbose_name="Basket")
    florist = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
    null=True, blank=True, related_name="orders",
    verbose_name="User")

    def __str__(self):
        return f"Order #{self.id} from {self.date}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('confirmed', 'Confirmed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    # Possible card types
    CARD_TYPE_CHOICES = [
        ('visa', 'VISA'),
        ('mastercard', 'MasterCard'),
        ('mir', 'MIR'),
        ('union_pay', 'Union Pay'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Card Online'),
        ('cash', 'Cash on Delivery'),
    ]
    
    card_type = models.CharField("Card Type", max_length=20, choices=CARD_TYPE_CHOICES, 
                             null=True, blank=True)
    payment_method = models.CharField("Payment Method", max_length=30, choices=PAYMENT_METHOD_CHOICES)
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, 
                            related_name="payments", verbose_name="Order")
    status = models.CharField("Payment Status", max_length=30, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Payment for Order #{self.order.id}"
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, 
                               related_name="delivery", verbose_name="Order")
    delivered_date = models.DateField("Delivery Date") 
    delivered_time = models.TimeField("Delivery Time")
    address = models.CharField("Address", max_length=255)
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    courier = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
    null=True, blank=True, related_name="deliveries",
    verbose_name="User")
    
    
    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
    
    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"
        
