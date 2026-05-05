from django.apps import AppConfig
from django.contrib.auth import get_user_model


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="krimmzy",
                email="lemoakorede@gmail.com",
                password="krimmzy@101"
            )
