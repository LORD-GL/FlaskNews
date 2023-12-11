"""title_image to image name changed

Revision ID: 8ddd25c6903f
Revises: 7f907ec6625d
Create Date: 2023-12-11 16:16:48.082020

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8ddd25c6903f'
down_revision = '7f907ec6625d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=150), nullable=True))
        batch_op.alter_column('author',
               existing_type=mysql.VARCHAR(length=70),
               nullable=False)
        batch_op.drop_column('title_image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title_image', mysql.VARCHAR(length=150), nullable=True))
        batch_op.alter_column('author',
               existing_type=mysql.VARCHAR(length=70),
               nullable=True)
        batch_op.drop_column('image')

    # ### end Alembic commands ###