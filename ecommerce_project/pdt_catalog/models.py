import random
import os
from django.urls import reverse
from django.dispatch import receiver
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from .utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 9999999)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'


class Seller(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def get_by_id(self, id):
        # self.get_queryset() doing the same thing as Product.objects
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        lookups = Q(name__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().filter(lookups).distinct()


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=0, max_digits=10, blank=False)
    image = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'pdt_catalog:product', kwargs={
                'slug': self.slug,
                'pk': self.id
            })
        # return reverse('pdt_catalog:product', kwargs={'pk': self.id})


# NOTE: Clean up


@receiver(pre_save, sender=Product)
def model_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# look into picking class name with instance.__class__.__name__
# pre_save.connect(product_pre_save_receiver, sender=Product)
