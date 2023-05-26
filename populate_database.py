import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cineflix.settings')

import django
django.setup()

from faker import Faker
from api.models import Post, Toy

fake = Faker()

# for _ in range(10):
#     Post.objects.create(
#         title = fake.text(max_nb_chars=50),
#         content = fake.text()
#     )


for _ in range(10):
    Toy.objects.create(
        name=fake.word(),
        category=fake.random_element(elements=Toy.CATEGORY_CHOICES)[0],
        color=fake.color_name(),
        makes_sound=fake.boolean()
    )
    