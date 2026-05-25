from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings

# ==========================================
# 1. MÓDULO DE PRODUCTOS Y CATEGORÍAS
# ==========================================

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==========================================
# 2. MÓDULO DE UBICACIÓN GEOGRÁFICA (3FN)
# ==========================================

class Country(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Ej: "MEX", "COL", "CRI"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('country', 'name')  # Evita duplicar el mismo estado en un país

    def __str__(self):
        return f"{self.name}, {self.country.code}"


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.postal_code})"


# ==========================================
# 3. MÓDULO DE DIRECCIONES DE USUARIO
# ==========================================

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
    street_address = models.CharField(max_length=255)  # Calle, Avenida, # Casa, Apto
    
    # Vinculamos a la Ciudad en vez de guardar texto plano para mantener 3FN
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='addresses')
    
    phone_number = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Si esta dirección se marca como predeterminada, desmarcamos las demás del usuario
        if self.is_default:
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.street_address}, {self.city}"


# ==========================================
# 4. MÓDULO DE MÉTODOS DE PAGO
# ==========================================

class Payments(models.Model):
    CARD_CHOICES = [
        ('VISA', 'Visa'),
        ('MASTERCARD', 'MasterCard'),
        ('AMEX', 'American Express')
    ]

    # Corregido: Ahora vincula directamente al modelo de usuario del sistema
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    cardType = models.CharField(max_length=20, choices=CARD_CHOICES)
    cardNumber = models.CharField(max_length=16)
    expirationDate = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^(0[1-9]|1[0-2])\/([0-9]{2})$',
                message='Formato inválido. Use MM/YY'
            )
        ]
    )
    cvv = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validación de longitud según franquicia bancaria
        if self.cardType == 'VISA':
            if len(self.cardNumber) != 16:
                raise ValidationError("Visa requiere exactamente 16 digitos.")
            if len(self.cvv) != 3:
                raise ValidationError("Visa usa CVV de 3 digitos.")

        elif self.cardType == 'MASTERCARD':
            if len(self.cardNumber) != 16:
                raise ValidationError("MasterCard requiere 16 dígitos.")
            if len(self.cvv) != 3:
                raise ValidationError("MasterCard usa CVV de 3 dígitos.")

        elif self.cardType == 'AMEX':
            if len(self.cardNumber) != 15:
                raise ValidationError("AMEX requiere 15 dígitos.")
            if len(self.cvv) != 4:
                raise ValidationError("AMEX usa CVV de 4 dígitos.")

    def __str__(self):
        return f"{self.user.username} - {self.cardType}"
