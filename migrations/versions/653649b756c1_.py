"""empty message

Revision ID: 653649b756c1
Revises: 25d1e2c5f1b9
Create Date: 2024-09-27 14:17:02.345069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653649b756c1'
down_revision = '25d1e2c5f1b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_answer_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_answer_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
