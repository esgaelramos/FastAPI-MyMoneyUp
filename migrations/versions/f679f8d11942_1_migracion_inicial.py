"""1_migracion_inicial

Revision ID: f679f8d11942
Revises: 
Create Date: 2024-01-12 17:40:43.098934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f679f8d11942"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "endpoints",
        sa.Column("endpoint_name", sa.String(length=255), nullable=True),
        sa.Column("endpoint_url", sa.String(length=512), nullable=False),
        sa.Column("endpoint_request", sa.String(length=10), nullable=False),
        sa.Column("endpoint_parameters", sa.JSON(), nullable=True),
        sa.Column("endpoint_description", sa.String(length=512), nullable=True),
        sa.Column("endpoint_status", sa.Boolean(), nullable=False),
        sa.Column("endpoint_authenticated", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_endpoints_endpoint_description"), "endpoints", ["endpoint_description"], unique=False)
    op.create_index(op.f("ix_endpoints_endpoint_name"), "endpoints", ["endpoint_name"], unique=True)
    op.create_index(op.f("ix_endpoints_endpoint_url"), "endpoints", ["endpoint_url"], unique=True)
    op.create_index(op.f("ix_endpoints_id"), "endpoints", ["id"], unique=False)
    op.create_table(
        "groups",
        sa.Column("group_name", sa.String(length=75), nullable=False),
        sa.Column("group_description", sa.String(length=255), nullable=True),
        sa.Column("group_status", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_groups_group_description"), "groups", ["group_description"], unique=False)
    op.create_index(op.f("ix_groups_group_name"), "groups", ["group_name"], unique=True)
    op.create_index(op.f("ix_groups_id"), "groups", ["id"], unique=False)
    op.create_table(
        "roles",
        sa.Column("role_name", sa.String(length=75), nullable=False),
        sa.Column("role_description", sa.String(length=255), nullable=True),
        sa.Column("role_status", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_roles_id"), "roles", ["id"], unique=False)
    op.create_index(op.f("ix_roles_role_description"), "roles", ["role_description"], unique=False)
    op.create_index(op.f("ix_roles_role_name"), "roles", ["role_name"], unique=True)
    op.create_table(
        "users",
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=512), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_table(
        "endpoints_groups",
        sa.Column("endpoint_id", sa.Integer(), nullable=True),
        sa.Column("group_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["endpoint_id"],
            ["endpoints.id"],
        ),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
        ),
    )
    op.create_table(
        "endpoints_roles",
        sa.Column("endpoint_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["endpoint_id"],
            ["endpoints.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
        ),
    )
    op.create_table(
        "groups_roles",
        sa.Column("group_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
        ),
    )
    op.create_table(
        "historical_movements",
        sa.Column("url_request", sa.String(length=255), nullable=True),
        sa.Column("type_request", sa.String(length=10), nullable=True),
        sa.Column("system", sa.String(length=255), nullable=True),
        sa.Column("user_ip", sa.String(length=255), nullable=True),
        sa.Column("user_browser", sa.String(), nullable=True),
        sa.Column("query", sa.String(), nullable=True),
        sa.Column("details", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_historical_movements_id"), "historical_movements", ["id"], unique=False)
    op.create_table(
        "profiles",
        sa.Column("first_name", sa.String(length=250), nullable=False),
        sa.Column("last_name", sa.String(length=250), nullable=False),
        sa.Column("document", sa.String(length=50), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index(op.f("ix_profiles_document"), "profiles", ["document"], unique=True)
    op.create_index(op.f("ix_profiles_id"), "profiles", ["id"], unique=False)
    op.create_table(
        "users_groups",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("group_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
    )
    op.create_table(
        "users_roles",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_roles")
    op.drop_table("users_groups")
    op.drop_index(op.f("ix_profiles_id"), table_name="profiles")
    op.drop_index(op.f("ix_profiles_document"), table_name="profiles")
    op.drop_table("profiles")
    op.drop_index(op.f("ix_historical_movements_id"), table_name="historical_movements")
    op.drop_table("historical_movements")
    op.drop_table("groups_roles")
    op.drop_table("endpoints_roles")
    op.drop_table("endpoints_groups")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_roles_role_name"), table_name="roles")
    op.drop_index(op.f("ix_roles_role_description"), table_name="roles")
    op.drop_index(op.f("ix_roles_id"), table_name="roles")
    op.drop_table("roles")
    op.drop_index(op.f("ix_groups_id"), table_name="groups")
    op.drop_index(op.f("ix_groups_group_name"), table_name="groups")
    op.drop_index(op.f("ix_groups_group_description"), table_name="groups")
    op.drop_table("groups")
    op.drop_index(op.f("ix_endpoints_id"), table_name="endpoints")
    op.drop_index(op.f("ix_endpoints_endpoint_url"), table_name="endpoints")
    op.drop_index(op.f("ix_endpoints_endpoint_name"), table_name="endpoints")
    op.drop_index(op.f("ix_endpoints_endpoint_description"), table_name="endpoints")
    op.drop_table("endpoints")
    # ### end Alembic commands ###
