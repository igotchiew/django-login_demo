#!/usr/bin/env python3

from accounts.models import CustomUser

# CustomUser.objects.create_superuser(
#     username='admin2',
#     email='admin2@admin.com',
#     password='pass12345678'
# )

CustomUser.objects.create_superuser(
    username='grgie',
    email='admin2@admin.com',
    password='pass12345678'
)

CustomUser.objects.create_superuser(
    username='drbson',
    email='admin2@admin.com',
    password='pass12345678'
)

CustomUser.objects.create_superuser(
    username='dasgoob',
    email='admin2@admin.com',
    password='pass12345678'
)
