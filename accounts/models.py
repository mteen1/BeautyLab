from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """custom user model"""
    pass
class Profile(models.Model):
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    SKIN_TYPES = (
        ("NORM", "Normal"),
        ("DRY", "Dry"),
        ("OILY", "Oily"),
        ("COMB", "Combination"),
        ("SENS", "Sensitive"),
    )

    skin_type = models.CharField(
        _("نوع پوست"), choices=SKIN_TYPES, max_length=50, default="NORM"
    )
    skin_concerns = models.ManyToManyField("products.SkinConcern", verbose_name=_("skin concerns"))
    # Many-to-many field for ingredient preferences
    ing_prefer = models.ManyToManyField('products.Ingredient', blank=True, related_name='preferred_by_users')

    # Many-to-many field for ingredient sensitivities
    ing_sensitive = models.ManyToManyField('products.Ingredient', blank=True, related_name='sensitive_to_users')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

