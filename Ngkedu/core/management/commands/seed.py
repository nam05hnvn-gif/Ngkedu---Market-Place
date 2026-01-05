from django.core.management.base import BaseCommand
from item.models import Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Category.objects.get_or_create(name="Furnitures")
        Category.objects.get_or_create(name="Electronics")
        Category.objects.get_or_create(name="Books")
        self.stdout.write(self.style.SUCCESS("Seed done"))