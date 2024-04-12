from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """details about the skincare products"""

    name = models.CharField(_("نام محصول"), max_length=50)
    description = models.TextField(_("توضیحات"), blank=True)
    ingredients = models.CharField(_("مواد تشکیل دهنده"), max_length=50)
    SKIN_TYPES = (
        ("normal", "نرمال"),
        ("dry", "خشک"),
        ("oily", "چرب"),
        ("combination", "ترکیبی"),
        ("sensitive", "حساس"),
        ("all", "همه پوست ها"),
    )
    skin_type = models.CharField(
        _("برای پوست ها"), choices=SKIN_TYPES, max_length=50, default="all"
    )
    # slug = AutoSlugField from django extentions

    slug = models.SlugField(_("آدرس url"))
    draft = models.BooleanField(_("پیش نویس"), default=False)

    def __str__(self):
        return f"{self.name} - {self.pk}"


class Ingredient(models.Model):
    """different ingredients"""

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class SkinConcern(models.Model):
    """skin concern objects"""
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name





class Rating:
    pass


class Interaction:
    pass


class Recommendation:
    pass
