from django.db import models

# Create your models here.

# class product_category(models.Model):
# 	product_category_name = models.CharField(max_length=200, unique=True)
# 	product_type = models.CharField(max_length=200, unique=True)

# 	def __str__(self):
# 		return str(self.product_category_name)

# class product_detail(models.Model):
#     product_category = models.ForeignKey(product_category,on_delete=models.PROTECT)
#     product_name = models.CharField(max_length=200, unique=True)
#     price = models.FloatField()
#     quantity = models.IntegerField()
#     description = models.TextField()
#     brand = models.TextField()
#     model = models.TextField()
#     released_on = models.DateField()
#     dimensions = models.TextField()
#     features = models.TextField()
#     image_large = models.ImageField(upload_to = 'themes/images/products/large/')

#     def __str__(self):
#         return (self.product_name)