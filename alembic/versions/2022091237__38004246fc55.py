"""empty message

Revision ID: 38004246fc55
Revises: 953a56d69386
Create Date: 2022-09-12 14:37:48.036348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "38004246fc55"
down_revision = "953a56d69386"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("result", sa.Column("kid_id", sa.Integer(), nullable=False))
    op.add_column("result", sa.Column("text", sa.String(length=150), nullable=False))
    op.add_column("result", sa.Column("analysis", sa.JSON(), nullable=False))
    op.create_foreign_key(None, "result", "kid", ["kid_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "result", type_="foreignkey")
    op.drop_column("result", "analysis")
    op.drop_column("result", "text")
    op.drop_column("result", "kid_id")
    # ### end Alembic commands ###