from django.test import TestCase
from .models import HairProduct


class HairProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create sample HairProduct data for testing."""
        HairProduct.objects.create(
            name="Voluminous Mousse",
            brand="Acme Hair Co.",
            description="This lightweight mousse adds volume and body to your hair without stiffness.",
            price=100000,
            image="https://example.com/voluminous_mousse.jpg",
            hair_type="normal,fine",
            key_ingredients="Panthenol, Hydrolyzed Wheat Protein",
            benefits="Adds volume, Boosts body",
            is_vegan=True,
            is_cruelty_free=True,
            size="8oz",
        )

    def test_hairproduct_content(self):
        """Test that a HairProduct object has the expected attributes."""
        hair_product = HairProduct.objects.get(name="Voluminous Mousse")
        self.assertEqual(hair_product.name, "Voluminous Mousse")
        self.assertEqual(hair_product.brand, "Acme Hair Co.")
        # Add assertions for other relevant fields as needed
        self.assertEqual(hair_product.price, 100000)
        self.assertEqual(hair_product.hair_type, "normal,fine")
        self.assertEqual(hair_product.is_vegan, True)

    def test_hairproduct_listview(self):
        """Test that the hair product list view displays the correct content."""
        # Simulate a GET request to the hair product list view (replace with your actual URL pattern)
        response = self.client.get("/hair-products/")
        self.assertEqual(
            response.status_code, 200
        )  # Check for successful response (200 OK)
        self.assertContains(
            response, "Voluminous Mousse"
        )  # Check if product name is present in response
        # Add assertions to check for other expected content in the response (e.g., descriptions, prices)
