import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mqtt.settings")
django.setup()


from mqtt_app.models import Usermaster

queryset = Usermaster.objects.all()
for item in queryset:
    print(item.name)