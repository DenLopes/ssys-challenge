from datetime import datetime
from utils.security import get_password_hash

def get_users_data():
    return [
        {
            'username': 'admin',
            'email': 'admin@example.com',
            'password': get_password_hash('admin'),
            'full_name': 'Admin User',
            'is_superuser': True,
            'is_active': True,
        },
    ]
