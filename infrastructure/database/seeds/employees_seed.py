from datetime import datetime
from decimal import Decimal

def get_employees_data():
    return [
        {
            'name': 'Anakin Skywalker',
            'email': 'skywalker@ssys.com.br',
            'department': 'Architecture',
            'salary': Decimal('4000.00'),
            'birth_date': datetime(1983, 1, 1).date()
        },
        {
            'name': 'Obi-Wan Kenobi',
            'email': 'kenobi@ssys.com.br',
            'department': 'Back-End',
            'salary': Decimal('3000.00'),
            'birth_date': datetime(1977, 1, 1).date()
        },
        {
            'name': 'Leia Organa',
            'email': 'organa@ssys.com.br',
            'department': 'DevOps',
            'salary': Decimal('5000.00'),
            'birth_date': datetime(1980, 1, 1).date()
        }
    ]