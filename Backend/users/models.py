from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
<<<<<<< HEAD

=======
>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payments(models.Model):

<<<<<<< HEAD
    PAYMENT_CHOICES = [
        ('VISA', 'Visa'),
        ('MASTERCARD', 'MasterCard'),
        ('AMEX', 'American Express'),
=======
    CARD_CHOICES = [
        ('VISA', 'Visa'),
        ('MASTERCARD', 'MasterCard'),
        ('AMEX', 'American Express')
>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066
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
        choices=PAYMENT_CHOICES
    )

<<<<<<< HEAD
    cardNumber = models.CharField(max_length=16)
=======
    cardNumber = models.CharField(
        max_length=16
    )
>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066

    expirationDate = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-2])\/([0-9]{2})$',
                message='Formato inválido. Use MM/YY'
            )
        ]
    )

<<<<<<< HEAD
    cvv = models.CharField(max_length=4)

    def clean(self):
        if self.cardType == 'VISA':
            if len(self.cardNumber) != 16:
                raise ValidationError("Visa requiere exactamente 16 dígitos.")
            if len(self.cvv) != 3:
                raise ValidationError("Visa usa CVV de 3 dígitos.")

        elif self.cardType == 'MASTERCARD':
=======
    cvv = models.CharField(
        max_length=4
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):

        # VISA
        if self.cardType == 'VISA':

            if len(self.cardNumber) != 16:
                raise ValidationError(
                    "Visa requiere exactamente 16 digitos."
                )

            if len(self.cvv) != 3:
                raise ValidationError(
                    "Visa usa CVV de 3 digitos."
                )

        # Mastercard
        elif self.cardType == 'MASTERCARD':

>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066
            if len(self.cardNumber) != 16:
                raise ValidationError("MasterCard requiere 16 dígitos.")
            if len(self.cvv) != 3:
<<<<<<< HEAD
                raise ValidationError("MasterCard usa CVV de 3 dígitos.")

=======
                raise ValidationError(
                    "MasterCard usa CVV de 3 dígitos."
                )

        # American Express
>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066
        elif self.cardType == 'AMEX':
            if len(self.cardNumber) != 15:
                raise ValidationError("AMEX requiere 15 dígitos.")
            if len(self.cvv) != 4:
<<<<<<< HEAD
                raise ValidationError("AMEX usa CVV de 4 dígitos.")

    def __str__(self):
        return f"{self.user} - {self.cardType}"
    
# DIreccion 
class Country(models.Model):
    code = models.CharField(max_length=3, unique=True) # Ej: "MEX", "COL", "USA"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('country', 'name') # Evita estados duplicados en el mismo país

    def __str__(self):
        return f"{self.name}, {self.country.code}"

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.postal_code})"

class Address(models.Model):
    ADDRESS_TYPES = [
        ('SHIPPING', 'Envío'),
        ('BILLING', 'Facturación'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPES, default='SHIPPING')
    full_name = models.CharField(max_length=150)
    street_address = models.CharField(max_length=255) # Calle, número, apartamento
    
    # Reemplazamos los CharField por relaciones ForeignKey
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='addresses')
    
    phone_number = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.street_address}, {self.city}"
=======
                raise ValidationError(
                    "AMEX usa CVV de 4 dígitos."
                )

    def __str__(self):
        return f"{self.user} - {self.cardType}"
>>>>>>> 3327129c414db7d8b91a2b616abe2c88f427b066
