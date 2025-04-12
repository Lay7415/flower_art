from django.contrib import admin
from core.models.models import (
    User, CourierLocation, UserStatus, WorkRecord,
    Bouquet, Flower, BouquetFlower, Ribbon, BouquetRibbon,
    Wrapper, BouquetWrapper, StockFlower, StockRibbon,
    StockWrapper, BasketBouquet, Basket, Order, Payment, Delivery
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'role', 'date_registered')
    list_filter = ('role', 'date_registered')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


@admin.register(CourierLocation)
class CourierLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'longitude', 'latitude')
    search_fields = ('user__first_name', 'user__last_name')


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
    list_filter = ('status',)
    search_fields = ('user__first_name', 'user__last_name')


@admin.register(WorkRecord)
class WorkRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('user__first_name', 'user__last_name')


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'tag')
    list_filter = ('tag',)
    search_fields = ('name', 'description', 'tag')


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(BouquetFlower)
class BouquetFlowerAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'flower', 'count')
    list_filter = ('bouquet', 'flower')
    search_fields = ('bouquet__name', 'flower__name')


@admin.register(Ribbon)
class RibbonAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(BouquetRibbon)
class BouquetRibbonAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'ribbon', 'length')
    list_filter = ('bouquet', 'ribbon')
    search_fields = ('bouquet__name', 'ribbon__name')


@admin.register(Wrapper)
class WrapperAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


@admin.register(BouquetWrapper)
class BouquetWrapperAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'wrapper', 'length')
    list_filter = ('bouquet', 'wrapper')
    search_fields = ('bouquet__name', 'wrapper__name')


@admin.register(StockFlower)
class StockFlowerAdmin(admin.ModelAdmin):
    list_display = ('flower', 'delivery_date', 'count', 'number', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('flower__name', 'number')


@admin.register(StockRibbon)
class StockRibbonAdmin(admin.ModelAdmin):
    list_display = ('ribbon', 'delivery_date', 'length', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('ribbon__name',)


@admin.register(StockWrapper)
class StockWrapperAdmin(admin.ModelAdmin):
    list_display = ('wrapper', 'delivery_date', 'length', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('wrapper__name',)


@admin.register(BasketBouquet)
class BasketBouquetAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'count')
    search_fields = ('bouquet__name',)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__first_name', 'user__last_name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date', 'time', 'total')
    list_filter = ('status', 'date')
    search_fields = ('id', 'basket__user__first_name', 'basket__user__last_name')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'card_type', 'status')
    list_filter = ('status', 'payment_method', 'card_type')
    search_fields = ('order__id',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'courier', 'delivered_date', 'delivered_time', 'address')
    list_filter = ('delivered_date',)
    search_fields = ('order__id', 'address', 'courier__first_name', 'courier__last_name')