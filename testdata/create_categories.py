#!/usr/bin/env python3

from accounts.models import Category

categories = [
    'fruit',
    'vegetables',
    'meat'
]

for cat in categories:
    _cat = Category(category_name=cat)
    _cat.save()
