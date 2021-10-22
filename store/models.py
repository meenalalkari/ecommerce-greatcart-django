from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='photos/products')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    stock = models.IntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

class Product_Variation_Manager(models.Manager):
    def colours(self):
        return super(Product_Variation_Manager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(Product_Variation_Manager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
('color','color'),
('size','size'),
)

class Product_Variation(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    variation_category = models.CharField(max_length=100, choices = variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = Product_Variation_Manager()

    def __str__(self):
        return self.variation_value
