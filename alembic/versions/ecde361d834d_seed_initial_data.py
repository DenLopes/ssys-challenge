"""seed_initial_data

Revision ID: ecde361d834d
Revises: c0a0c225f3e9
Create Date: 2024-11-10 01:22:26.301306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column
from infrastructure.database.seeds.users_seed import get_users_data
from infrastructure.database.seeds.employees_seed import get_employees_data


# revision identifiers, used by Alembic.
revision: str = 'ecde361d834d'
down_revision: Union[str, None] = 'c0a0c225f3e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    users = table('users',
        column('id', sa.Integer),
        column('username', sa.String),
        column('email', sa.String),
        column('password', sa.String),
        column('full_name', sa.String),
        column('is_active', sa.Boolean),
        column('is_superuser', sa.Boolean)
    )
    
    employees = table('employees',
        column('id', sa.Integer),
        column('name', sa.String),
        column('email', sa.String),
        column('department', sa.String),
        column('salary', sa.Numeric),
        column('birth_date', sa.Date)
    )

    op.bulk_insert(users, get_users_data())
    op.bulk_insert(employees, get_employees_data())

def downgrade() -> None:
    op.execute("DELETE FROM users WHERE username IN ('admin', 'user')")
    op.execute("DELETE FROM employees WHERE email IN ('skywalker@ssys.com.br', 'kenobi@ssys.com.br', 'organa@ssys.com.br')")
