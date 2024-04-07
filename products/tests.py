from django.urls import reverse
from rest_framework.test import APITestCase

from products.models import HairProduct
from .serializers import HairProductSerializer


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        """Create sample HairProduct data for testing."""
        cls.hairproduct = HairProduct.objects.create(
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

    def test_hairproduct_list_view(self):
        """Test that the HairProduct API list view returns the correct data."""
        url = reverse('hairproduct_list')  # Replace with your actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)  # Check for successful response (200 OK)
        self.assertEqual(len(response.data), 1)  # Verify one HairProduct object returned

        # Compare serialized data with expected data
        serialized_data = HairProductSerializer(self.hairproduct).data
        self.assertDictEqual(response.data[0], serialized_data)
        self.assertContains(response, self.hairproduct)

    def test_detail_view(self):
        response = self.client.get(reverse("hairproduct_detail", kwargs={"pk": self.hairproduct.id}), format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(HairProduct.objects.count(), 1)
        self.assertContains(response, "Mousse")