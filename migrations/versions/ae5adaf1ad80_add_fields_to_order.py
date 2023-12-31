"""Add fields to Order

Revision ID: ae5adaf1ad80
Revises: 45fde85f9e25
Create Date: 2023-12-27 20:13:32.808554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae5adaf1ad80'
down_revision = '45fde85f9e25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_subtotal_amount', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('platform_order_id', sa.Integer(), nullable=False))
        batch_op.drop_column('order_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.INTEGER(), nullable=False))
        batch_op.drop_column('platform_order_id')
        batch_op.drop_column('order_subtotal_amount')

    # ### end Alembic commands ###
