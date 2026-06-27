from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Crea usuarios iniciales (1 admin + 2 clientes) de forma idempotente"

    USERS = [
        {
            "username": "admin",
            "email": "admin@ecommerce.com",
            "password": "admin123",
            "is_staff": True,
            "is_superuser": True,
            "telefono": "555-0001",
        },
        {
            "username": "cliente1",
            "email": "cliente1@email.com",
            "password": "cliente123",
            "is_staff": False,
            "is_superuser": False,
            "telefono": "555-1001",
        },
        {
            "username": "cliente2",
            "email": "cliente2@email.com",
            "password": "cliente123",
            "is_staff": False,
            "is_superuser": False,
            "telefono": "555-1002",
        },
    ]

    def handle(self, *args, **options):
        for user_data in self.USERS:
            username = user_data["username"]
            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.WARNING(f"Usuario '{username}' ya existe, saltando...")
                )
                continue

            password = user_data.pop("password")
            user = User(**user_data)
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Usuario '{username}' creado exitosamente")
            )
