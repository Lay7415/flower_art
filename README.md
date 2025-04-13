# flower_art

добавь фотку в цветы, обертка, лента
смотри я хочу чтобы в корзине я мог сразу добавить букет и указать количество
смотри также я хочу чтобы в order списке я не заходил через id, я хочу чтобы там было ссылка из фио пользователя и номер корзины
в оплате я также хочу чтобы была ссылка через имя пользователя и заказ
смотри я хочу чтобы во всех таблицах было также кнопки изменить и удалить
смотри я хочу чтобы в новом заказе, там есть поле User но это поле для флористов и в обьеденном разделе доставка там тоже есть User но это курьер, я хочу чтобы там была фильтрация по роли

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
    fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password', 'role')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    exclude = ('user_permissions', 'groups', 'is_superuser', 'last_login', 'is_staff', 'date_joined', 'active')
    list_display = ('username', 'first_name', 'last_name', 'role', 'admin_actions')
    
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
    list_display = ('name', 'price', 'display_photo', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockFlowerInline]
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = 'Photo'
    
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
    list_display = ('name', 'price', 'display_photo', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockRibbonInline]
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = 'Photo'
    
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
    list_display = ('name', 'price', 'display_photo', 'admin_actions')
    search_fields = ('name', 'description')
    inlines = [StockWrapperInline]
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = 'Photo'
    
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
    list_display = ('name', 'price', 'tag', 'display_photo', 'admin_actions')
    list_filter = ('tag',)
    search_fields = ('name', 'description', 'tag')
    inlines = [BouquetFlowerInline, BouquetRibbonInline, BouquetWrapperInline]
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />', obj.photo.url)
        return "No photo"
    display_photo.short_description = 'Photo'
    
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
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/stockwrapper/{obj.pk}/change/',
            f'/admin/core/stockwrapper/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


# Inline для добавления букетов в корзину
class BasketBouquetInline(admin.TabularInline):
    model = Basket.bouquets.through
    extra = 1


@admin.register(BasketBouquet)
class BasketBouquetAdmin(admin.ModelAdmin):
    list_display = ('bouquet', 'count', 'admin_actions')
    search_fields = ('bouquet__name',)
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/basketbouquet/{obj.pk}/change/',
            f'/admin/core/basketbouquet/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'status', 'created_at', 'admin_actions')
    list_filter = ('status', 'created_at')
    search_fields = ('user__first_name', 'user__last_name')
    inlines = [BasketBouquetInline]
    exclude = ('bouquets',)
    
    def get_user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_user_name.short_description = 'User'
    get_user_name.admin_order_field = 'user__last_name'
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/basket/{obj.pk}/change/',
            f'/admin/core/basket/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'


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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date', 'time', 'total', 'get_user_name', 'get_basket_link', 'admin_actions')
    list_filter = ('status', 'date')
    search_fields = ('id', 'basket__user__first_name', 'basket__user__last_name')
    inlines = [PaymentInline, DeliveryInline]
    
    def get_user_name(self, obj):
        if obj.basket and obj.basket.user:
            return format_html(
                '<a href="{}">{} {}</a>',
                f'/admin/core/customuser/{obj.basket.user.pk}/change/',
                obj.basket.user.first_name,
                obj.basket.user.last_name
            )
        return None
    get_user_name.short_description = 'Client'
    get_user_name.admin_order_field = 'basket__user__last_name'
    
    def get_basket_link(self, obj):
        if obj.basket:
            return format_html(
                '<a href="{}">{}</a>',
                f'/admin/core/basket/{obj.basket.pk}/change/',
                f'Basket #{obj.basket.pk}'
            )
        return None
    get_basket_link.short_description = 'Basket'
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/order/{obj.pk}/change/',
            f'/admin/core/order/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filter florists for the order form
        if db_field.name == "florist":
            kwargs["queryset"] = CustomUser.objects.filter(role='manager')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'get_order_link', 'payment_method', 'card_type', 'status', 'admin_actions')
    list_filter = ('status', 'payment_method', 'card_type')
    search_fields = ('order__id', 'order__basket__user__first_name', 'order__basket__user__last_name')
    
    def get_user_name(self, obj):
        if obj.order and obj.order.basket and obj.order.basket.user:
            return format_html(
                '<a href="{}">{} {}</a>',
                f'/admin/core/customuser/{obj.order.basket.user.pk}/change/',
                obj.order.basket.user.first_name,
                obj.order.basket.user.last_name
            )
        return None
    get_user_name.short_description = 'Client'
    
    def get_order_link(self, obj):
        if obj.order:
            return format_html(
                '<a href="{}">{}</a>',
                f'/admin/core/order/{obj.order.pk}/change/',
                f'Order #{obj.order.pk}'
            )
        return None
    get_order_link.short_description = 'Order'
    
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
    list_display = ('get_order_link', 'courier', 'delivered_date', 'delivered_time', 'address', 'admin_actions')
    list_filter = ('delivered_date',)
    search_fields = ('order__id', 'address', 'courier__first_name', 'courier__last_name')
    
    def get_order_link(self, obj):
        if obj.order:
            return format_html(
                '<a href="{}">{}</a>',
                f'/admin/core/order/{obj.order.pk}/change/',
                f'Order #{obj.order.pk}'
            )
        return None
    get_order_link.short_description = 'Order'
    
    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a>&nbsp;'
            '<a class="button" href="{}">Delete</a>',
            f'/admin/core/delivery/{obj.pk}/change/',
            f'/admin/core/delivery/{obj.pk}/delete/'
        )
    admin_actions.short_description = 'Actions'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filter couriers for the delivery form
        if db_field.name == "courier":
            kwargs["queryset"] = CustomUser.objects.filter(role='courier')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)