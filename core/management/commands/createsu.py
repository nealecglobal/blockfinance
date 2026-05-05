from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username="krimmzyadmin").exists():
            User.objects.create_superuser(
                username="krimmzyadmin",
                email="lemoakorede1@gmail.com",
                password="krimmzy@101"
            )
            print("Superuser created")
        else:
            print("Superuser already exists")