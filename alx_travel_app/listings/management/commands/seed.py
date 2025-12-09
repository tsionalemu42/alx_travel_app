from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Apartment", "description": "A nice place in the city center", "price_per_night": 50.00, "location": "Addis Ababa"},
            {"title": "Luxury Villa", "description": "Spacious villa with swimming pool", "price_per_night": 200.00, "location": "Bahir Dar"},
            {"title": "Budget Room", "description": "Affordable room near university", "price_per_night": 20.00, "location": "Hawassa"},
        ]

        for data in sample_data:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings ✅"))
