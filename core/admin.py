from django.contrib import admin
from django.utils.html import format_html
from core.models.models import (
    CustomUser, CourierLocation, UserStatus, WorkRecord,
    Bouquet, Flower, BouquetFlower, Ribbon, BouquetRibbon,
    Wrapper, BouquetWrapper, StockFlower, StockRibbon,
    StockWrapper, BasketBouquet, Basket, Order, Payment, Delivery
)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'phone', 'email','password', 'role')  # порядок полей
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    exclude = ('user_permissions', 'groups', 'is_superuser', 'last_login', 'is_staff', 'date_joined', 'active')
    list_display = ('username', 'first_name', 'last_name', 'role', 'admin_actions')
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/customuser/{obj.pk}/change/',
            f'/admin/core/customuser/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'

@admin.register(CourierLocation)
class CourierLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'longitude', 'latitude', 'admin_actions')
    search_fields = ('user__first_name', 'user__last_name')
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/courierlocation/{obj.pk}/change/',
            f'/admin/core/courierlocation/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'admin_actions')
    list_filter = ('status',)
    search_fields = ('user__first_name', 'user__last_name')
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/userstatus/{obj.pk}/change/',
            f'/admin/core/userstatus/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(WorkRecord)
class WorkRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time', 'admin_actions')
    list_filter = ('start_time', 'end_time')
    search_fields = ('user__first_name', 'user__last_name')
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/workrecord/{obj.pk}/change/',
            f'/admin/core/workrecord/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


# Inline для добавления элементов склада при создании цветка
class StockFlowerInline(admin.TabularInline):
    model = StockFlower
    extra = 1


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockFlowerInline]
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/flower/{obj.pk}/change/',
            f'/admin/core/flower/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


# Inline для добавления элементов склада при создании ленты
class StockRibbonInline(admin.TabularInline):
    model = StockRibbon
    extra = 1


@admin.register(Ribbon)
class RibbonAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockRibbonInline]
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/ribbon/{obj.pk}/change/',
            f'/admin/core/ribbon/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


# Inline для добавления элементов склада при создании обертки
class StockWrapperInline(admin.TabularInline):
    model = StockWrapper
    extra = 1


@admin.register(Wrapper)
class WrapperAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockWrapperInline]
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/wrapper/{obj.pk}/change/',
            f'/admin/core/wrapper/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


# Inlines для добавления цветков, лент и оберток при создании букета
class BouquetFlowerInline(admin.TabularInline):
    model = BouquetFlower
    extra = 1


class BouquetRibbonInline(admin.TabularInline):
    model = BouquetRibbon
    extra = 1


class BouquetWrapperInline(admin.TabularInline):
    model = BouquetWrapper
    extra = 1


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'tag', 'admin_actions')
    list_filter = ('tag',)
    search_fields = ('name', 'description', 'tag')
    inlines = [BouquetFlowerInline, BouquetRibbonInline, BouquetWrapperInline]
    list_per_page = 15  # Pagination - 15 bouquets per page
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/bouquet/{obj.pk}/change/',
            f'/admin/core/bouquet/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(BouquetFlower)
class BouquetFlowerAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'flower', 'count', 'admin_actions')
    list_filter = ('bouquet', 'flower')
    search_fields = ('bouquet__name', 'flower__name')
    list_per_page = 25  # Pagination - 25 bouquet flowers per page
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/bouquetflower/{obj.pk}/change/',
            f'/admin/core/bouquetflower/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(BouquetRibbon)
class BouquetRibbonAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'ribbon', 'length', 'admin_actions')
    list_filter = ('bouquet', 'ribbon')
    search_fields = ('bouquet__name', 'ribbon__name')
    list_per_page = 25  # Pagination - 25 bouquet ribbons per page
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/bouquetribbon/{obj.pk}/change/',
            f'/admin/core/bouquetribbon/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(BouquetWrapper)
class BouquetWrapperAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'wrapper', 'length', 'admin_actions')
    list_filter = ('bouquet', 'wrapper')
    search_fields = ('bouquet__name', 'wrapper__name')
    list_per_page = 25  # Pagination - 25 bouquet wrappers per page
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/bouquetwrapper/{obj.pk}/change/',
            f'/admin/core/bouquetwrapper/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(StockFlower)
class StockFlowerAdmin(admin.ModelAdmin):
    list_display = ('flower', 'delivery_date', 'count', 'number', 'status', 'admin_actions')
    list_filter = ('status', 'delivery_date')
    search_fields = ('flower__name', 'number')
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/stockflower/{obj.pk}/change/',
            f'/admin/core/stockflower/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(StockRibbon)
class StockRibbonAdmin(admin.ModelAdmin):
    list_display = ('ribbon', 'delivery_date', 'length', 'status', 'admin_actions')
    list_filter = ('status', 'delivery_date')
    search_fields = ('ribbon__name',)
    list_per_page = 20 
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/stockribbon/{obj.pk}/change/',
            f'/admin/core/stockribbon/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(StockWrapper)
class StockWrapperAdmin(admin.ModelAdmin):
    list_display = ('wrapper', 'delivery_date', 'length', 'status', 'admin_actions')
    list_filter = ('status', 'delivery_date')
    search_fields = ('wrapper__name',)
    list_per_page = 20 
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/stockwrapper/{obj.pk}/change/',
            f'/admin/core/stockwrapper/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(BasketBouquet)
class BasketBouquetAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'count', 'admin_actions')
    search_fields = ('bouquet__name',)
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/basketbouquet/{obj.pk}/change/',
            f'/admin/core/basketbouquet/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'

class BasketBouquetInline(admin.TabularInline):
    model = BasketBouquet
    extra = 1

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'admin_actions')
    list_filter = ('status', 'created_at')
    search_fields = ('user__first_name', 'user__last_name')
    inlines = [BasketBouquetInline]
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/basket/{obj.pk}/change/',
            f'/admin/core/basket/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = CustomUser.objects.filter(role='client')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Inline для добавления оплаты при создании заказа
class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 1
    max_num = 1


# Inline для добавления доставки при создании заказа
class DeliveryInline(admin.StackedInline):
    model = Delivery
    extra = 1
    max_num = 1
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "courier":
            kwargs["queryset"] = CustomUser.objects.filter(role='courier')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date', 'time', 'calculated_total', 'get_user', 'admin_actions')
    list_filter = ('status', 'date')
    search_fields = ('id', 'basket__user__first_name', 'basket__user__last_name')
    inlines = [PaymentInline, DeliveryInline]
    list_per_page = 15  # Pagination - 15 orders per page

    def get_user(self, obj):
        return obj.basket.user if obj.basket else None
    get_user.short_description = 'User'
    get_user.admin_order_field = 'basket__user'

    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/order/{obj.pk}/change/',
            f'/admin/core/order/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "florist":
            kwargs["queryset"] = CustomUser.objects.filter(role='florist')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def calculated_total(self, obj):
        items = BasketBouquet.objects.filter(basket=obj.basket)
        total = sum(item.bouquet.price * item.count for item in items)
        return f"{total:.2f} сом"
    calculated_total.short_description = "Calculated Total"

    def save_model(self, request, obj, form, change):
        if obj.basket:
            items = BasketBouquet.objects.filter(basket=obj.basket)
            obj.total = sum(item.bouquet.price * item.count for item in items)
        super().save_model(request, obj, form, change)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'card_type', 'status', 'admin_actions')
    list_filter = ('status', 'payment_method', 'card_type')
    search_fields = ('order__id',)
    list_per_page = 20
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/payment/{obj.pk}/change/',
            f'/admin/core/payment/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'courier', 'delivered_date', 'delivered_time', 'address', 'admin_actions')
    list_filter = ('delivered_date',)
    search_fields = ('order__id', 'address', 'courier__first_name', 'courier__last_name')
    list_per_page = 20
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/delivery/{obj.pk}/change/',
            f'/admin/core/delivery/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "courier":
            kwargs["queryset"] = CustomUser.objects.filter(role='courier')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)