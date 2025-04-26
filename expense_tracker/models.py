from django.db import models

# Create your models here.
class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'รายรับ'),
        ('expense', 'รายจ่าย'),
    ]
    
    name = models.CharField("ชื่อรายการ ", max_length=200)
    amount = models.DecimalField("จำนวนเงิน ", max_digits=10, decimal_places=2)
    category = models.CharField("หมวดหมู่ ", max_length=10, choices=CATEGORY_CHOICES,blank=False, null=False)
    date = models.DateField("วันที่ ")
    description = models.TextField("รายละเอียด ", blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.category} - {self.amount} บาท"
