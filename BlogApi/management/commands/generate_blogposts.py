from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from BlogApi.models import Author, BlogPost
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generate and add sample blog posts to the database'

    def handle(self, *args, **options):
        users = []
        for _ in range(200):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )
            users.append(user)
        authors = [Author.objects.create(user=user, bio=fake.text()) for user in users]

    
        for _ in range(200):
            title = fake.sentence()
            content = fake.paragraphs(nb=3)
            author = random.choice(authors)

            BlogPost.objects.create(
                title=title,
                content='\n'.join(content),
                author=author,
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated and added blog posts.'))
