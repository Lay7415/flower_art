from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    """User model of the system"""
    # Possible user roles
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('courier', 'Courier'),
        ('client', 'Client'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    phone = models.CharField("Phone", max_length=20)
    email = models.EmailField("Email")
    date_registered = models.DateField("Registration Date", auto_now_add=True)
    role = models.CharField("Role", max_length=20, choices=ROLE_CHOICES, default='client')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class CourierLocation(models.Model):
    """Courier location"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                           related_name="locations", verbose_name="User")
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    
    def __str__(self):
        return f"Location of {self.user}"
    
    class Meta:
        verbose_name = "Courier Location"
        verbose_name_plural = "Courier Locations"


class UserStatus(models.Model):
    """User status"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
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
    """Work record"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                           related_name="work_records", verbose_name="User")
    start_time = models.DateTimeField("Shift start date/time")
    end_time = models.DateTimeField("Shift end date/time", null=True, blank=True)
    
    def __str__(self):
        return f"Shift of {self.user} from {self.start_time}"
    
    class Meta:
        verbose_name = "Work Record"
        verbose_name_plural = "Work Records"


class Bouquet(models.Model):
    """Bouquet"""
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
    """Flower"""
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
    """Flower in bouquet"""
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
    """Ribbon"""
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
    """Bouquet ribbon"""
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
    """Wrapper"""
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
    """Bouquet wrapper"""
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
    """Stock flower"""
    # Possible stock item statuses
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
    """Stock ribbon"""
    # Possible stock item statuses
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
    """Stock wrapper"""
    # Possible stock item statuses
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


class BasketBouquet(models.Model):
    """Basket bouquet"""
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, 
                            related_name="basket_items", verbose_name="Bouquet")
    count = models.PositiveIntegerField("Quantity")
    
    def __str__(self):
        return f"{self.bouquet} x{self.count}"
    
    class Meta:
        verbose_name = "Basket Bouquet"
        verbose_name_plural = "Basket Bouquets"


class Basket(models.Model):
    """Basket"""
    # Possible basket statuses
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('ordered', 'Converted to Order'),
        ('canceled', 'Canceled'),
        ('reserved', 'Reserved'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                           related_name="baskets", verbose_name="User")
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES, default='active')
    bouquets = models.ManyToManyField(BasketBouquet, related_name="baskets", verbose_name="Bouquets")
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)
    
    def __str__(self):
        return f"Basket of {self.user}"
    
    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"


class Order(models.Model):
    """Order"""
    # Possible order statuses
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
    
    def __str__(self):
        return f"Order #{self.id} from {self.date}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Payment(models.Model):
    """Payment"""
    # Possible payment statuses
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
    
    # Possible payment methods
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
    """Delivery"""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, 
                               related_name="delivery", verbose_name="Order")
    delivered_date = models.TimeField("Delivery Date")
    delivered_time = models.TimeField("Delivery Time")
    address = models.CharField("Address", max_length=255)
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    
    
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, 
                              null=True, blank=True, related_name="deliveries", 
                              verbose_name="User")
    
    def __str__(self):
        return f"Delivery for Order #{self.order.id}"
    
    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"