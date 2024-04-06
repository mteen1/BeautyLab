from django.db import models


from django.db import models

class HairProduct(models.Model):
    """
    Model representing a hair care product.
    """

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True)

    # Hair type options (consider adding more as needed)
    HAIR_TYPE_CHOICES = (
        ('normal', 'Normal'),
        ('dry', 'Dry'),
        ('oily', 'Oily'),
        ('curly', 'Curly'),
        ('colored', 'Colored'),
    )
    hair_type = models.CharField(max_length=20, choices=HAIR_TYPE_CHOICES)

    # Key ingredients (comma-separated)
    key_ingredients = models.CharField(max_length=255, blank=True)

    # Benefits (consider using a ManyToMany relationship later)
    benefits = models.CharField(max_length=255, blank=True)

    is_vegan = models.BooleanField(default=False)
    is_cruelty_free = models.BooleanField(default=False)

    size = models.CharField(max_length=50, blank=True)
    volume = models.CharField(max_length=50, blank=True)

    # Additional fields (optional)
    rating = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True)
    awards = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


