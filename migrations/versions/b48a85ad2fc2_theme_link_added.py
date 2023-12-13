"""theme link added

Revision ID: b48a85ad2fc2
Revises: 70e4c5de2af0
Create Date: 2023-12-12 20:41:45.585666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48a85ad2fc2'
down_revision = '70e4c5de2af0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('theme', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.String(length=110), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('theme', schema=None) as batch_op:
        batch_op.drop_column('link')

    # ### end Alembic commands ###