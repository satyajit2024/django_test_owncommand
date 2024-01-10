
from django.core.management.base import BaseCommand
from mqtt_app.models import Usermaster

class Command(BaseCommand):
    help = 'Your command description here'

    def handle(self, *args, **options):
        # Your script logic here
        queryset = Usermaster.objects.all()
        for item in queryset:
            self.stdout.write(self.style.SUCCESS(str(item)))
            print(item.name)