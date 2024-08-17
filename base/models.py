from django.db import models

# Create your models here.

class Table(models.Model):
    STATUS_CHOICES = [
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
        ('available', 'Available'),
    ]

    table = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(default=3)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return str(self.table)
    
    class Meta:
        verbose_name_plural = 'Table'

class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'Category'

class Menu(models.Model):
    items = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.items
    
    class Meta:
        verbose_name_plural = 'Menu'

class Order(models.Model):
    table_no = models.ForeignKey(Table, on_delete=models.SET_NULL,null=True)
    items = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(null=True, default=1)

    def __str__(self):
        return str(self.items)
    
    class Meta:
        verbose_name_plural = 'Order'

class Waiter(models.Model):
    Gender_choice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=Gender_choice)
    address = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return str(self.first_name)
    
    class Meta:
        verbose_name_plural = 'Waiter'

class Reception(models.Model):
    Gender_choice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    ]
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=Gender_choice)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = 'Reception'
