from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    class Payments(models.Model):
    
     CARD_CHOICES = [
        ('VISA', 'Visa'), 
        ('MASTERCARD', 'MasterCard')
        ('AMEX', 'American Express')
     ]
    
    user = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message='Solo se permiten letras y espacios.' 
            )
        ]
    )
    
    cardType = models.CharField(
        max_length=20,
        choices=CARD_CHOICES
    )
    
    cardNumber = models.IntegerField(
        max_length=16
    )
    
    expirationDate = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-2])\/([0-9]{2})$',
                message='Formato inválido. Use MM/YY'
            )
        ]
    )
    
    cvv = models.CharField(
        max_length=4
    )
    
    def clean(self):
        
        #VISA
        if self.cardType == 'VISA':
            
            if len(self.cardNumber) != 16:
                raise ValidationError(
                    "Visa requiere exactamente 16 digitos."
                )
                
            if len(self.cvv) != 3:
                raise ValidationError(
                    "Visa usa CVV de 3 digitos."
            )
            
        #Mastercard
        elif self.cardType == 'MASTERCARD':
            
            if len(self.cardNumber) != 16:
                raise ValidationError(
                    "MasterCard requiere 16 dígitos."
                )

            if len(self.cvv) != 3:
                raise ValidationError(
                    "MasterCard usa CVV de 3 dígitos."
                )
                
        #American Express
        elif self.cardType == 'AMEX':

            if len(self.cardNumber) != 15:
                raise ValidationError(
                    "AMEX requiere 15 dígitos."
                )

            if len(self.cvv) != 4:
                raise ValidationError(
                    "AMEX usa CVV de 4 dígitos."
                )


    def __str__(self):
        return f"{self.user} - {self.cardType}"