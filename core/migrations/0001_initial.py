# Generated by Django 5.2 on 2025-04-13 08:51

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='bouquets/', verbose_name='Photo')),
                ('tag', models.CharField(max_length=100, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Bouquet',
                'verbose_name_plural': 'Bouquets',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='flowers/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Flower',
                'verbose_name_plural': 'Flowers',
            },
        ),
        migrations.CreateModel(
            name='Ribbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='ribbons/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Ribbon',
                'verbose_name_plural': 'Ribbons',
            },
        ),
        migrations.CreateModel(
            name='Wrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='wrappers/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Wrapper',
                'verbose_name_plural': 'Wrappers',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Phone')),
                ('role', models.CharField(choices=[('admin', 'Administrator'), ('florist', 'Florist'), ('courier', 'Courier'), ('client', 'Client')], default='client', max_length=20, verbose_name='Role')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('ordered', 'Converted to Order'), ('canceled', 'Canceled'), ('reserved', 'Reserved')], default='active', max_length=30, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='BasketBouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_of_basket_bouquets', to='core.basket', verbose_name='Basket')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='core.bouquet', verbose_name='Bouquet')),
            ],
            options={
                'verbose_name': 'Basket Bouquet',
                'verbose_name_plural': 'Basket Bouquets',
            },
        ),
        migrations.CreateModel(
            name='CourierLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Courier Location',
                'verbose_name_plural': 'Courier Locations',
            },
        ),
        migrations.CreateModel(
            name='BouquetFlower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flowers', to='core.bouquet', verbose_name='Bouquet')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bouquets', to='core.flower', verbose_name='Flower')),
            ],
            options={
                'verbose_name': 'Bouquet Flower',
                'verbose_name_plural': 'Bouquet Flowers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('accepted', 'Confirmed'), ('assembly', 'In Assembly'), ('delivery', 'Out for Delivery'), ('completed', 'Completed'), ('reserved', 'Reserved'), ('canceled', 'Canceled')], default='new', max_length=30, verbose_name='Order Status')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='core.basket', verbose_name='Basket')),
                ('florist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered_date', models.DateField(verbose_name='Delivery Date')),
                ('delivered_time', models.TimeField(verbose_name='Delivery Time')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deliveries', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='core.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(blank=True, choices=[('visa', 'VISA'), ('mastercard', 'MasterCard'), ('mir', 'MIR'), ('union_pay', 'Union Pay')], max_length=20, null=True, verbose_name='Card Type')),
                ('payment_method', models.CharField(choices=[('card', 'Card Online'), ('cash', 'Cash on Delivery')], max_length=30, verbose_name='Payment Method')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('confirmed', 'Confirmed'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=30, verbose_name='Payment Status')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='core.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='BouquetRibbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(verbose_name='Length')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ribbons', to='core.bouquet', verbose_name='Bouquet')),
                ('ribbon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bouquets', to='core.ribbon', verbose_name='Ribbon')),
            ],
            options={
                'verbose_name': 'Bouquet Ribbon',
                'verbose_name_plural': 'Bouquet Ribbons',
            },
        ),
        migrations.CreateModel(
            name='StockFlower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Delivery Date')),
                ('count', models.PositiveIntegerField(verbose_name='Quantity')),
                ('number', models.CharField(max_length=50, verbose_name='Number')),
                ('status', models.CharField(choices=[('available', 'Available'), ('is_used', 'Used'), ('reserved', 'Reserved'), ('damaged', 'Damaged'), ('expired', 'Expired')], default='available', max_length=30, verbose_name='Stock Item Status')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_items', to='core.flower', verbose_name='Flower')),
            ],
            options={
                'verbose_name': 'Stock Flower',
                'verbose_name_plural': 'Stock Flowers',
            },
        ),
        migrations.CreateModel(
            name='StockRibbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Delivery Date')),
                ('length', models.PositiveIntegerField(verbose_name='Length')),
                ('status', models.CharField(choices=[('available', 'Available'), ('out_of_stock', 'Out of Stock')], default='available', max_length=30, verbose_name='Stock Item Status')),
                ('ribbon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_items', to='core.ribbon', verbose_name='Ribbon')),
            ],
            options={
                'verbose_name': 'Stock Ribbon',
                'verbose_name_plural': 'Stock Ribbons',
            },
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Available'), ('busy', 'Busy')], default='available', max_length=30, verbose_name='Order Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Status',
                'verbose_name_plural': 'User Statuses',
            },
        ),
        migrations.CreateModel(
            name='WorkRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Shift start date/time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Shift end date/time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_records', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Work Record',
                'verbose_name_plural': 'Work Records',
            },
        ),
        migrations.CreateModel(
            name='StockWrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(verbose_name='Delivery Date')),
                ('length', models.PositiveIntegerField(verbose_name='Length')),
                ('status', models.CharField(choices=[('available', 'Available'), ('out_of_stock', 'Out of Stock')], default='available', max_length=30, verbose_name='Stock Item Status')),
                ('wrapper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_items', to='core.wrapper', verbose_name='Wrapper')),
            ],
            options={
                'verbose_name': 'Stock Wrapper',
                'verbose_name_plural': 'Stock Wrappers',
            },
        ),
        migrations.CreateModel(
            name='BouquetWrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(verbose_name='Length')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wrappers', to='core.bouquet', verbose_name='Bouquet')),
                ('wrapper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bouquets', to='core.wrapper', verbose_name='Wrapper')),
            ],
            options={
                'verbose_name': 'Bouquet Wrapper',
                'verbose_name_plural': 'Bouquet Wrappers',
            },
        ),
    ]
