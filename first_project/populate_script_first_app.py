import os
# Configure settings for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## --- Import your models ---
import random
from first_app.models import Users, Details, Descriptions # Import all used models
from faker import Faker

# Initialize Faker
fakegen = Faker() 

def populate(N=5):
    for _ in range(N):
        # 1. Create or get the User
        # Using .user_name() for the 'usernames' field
        fake_user_name = fakegen.unique.user_name()
        user_obj = Users.objects.get_or_create(usernames=fake_user_name)[0]

        # 2. Add Details
        # Links to the user_obj created above
        Details.objects.get_or_create(
            users=user_obj,
            ipv4=fakegen.unique.ipv4(),
            catchphrase=fakegen.unique.catch_phrase()
        )

        # 3. Add Descriptions
        Descriptions.objects.get_or_create(
            users=user_obj,
            word=fakegen.word(),
            sentences=fakegen.sentence(),
            paragraphs=fakegen.paragraph(),
            text=fakegen.text(),
            date=fakegen.date()
        )

if __name__ == '__main__':
    print("Starting population script...")
    populate(50) # Change 50 to however many users you want
    print("Population complete!")