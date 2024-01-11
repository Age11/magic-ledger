import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

from .extensions import api

__version__ = (0, 0, 1, "dev")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    api.init_app(app)

    # some deploy systems set the database url in the environment
    db_url = os.environ.get("DATABASE_URL")

    if db_url is None:
        # default to a sqlite database in the instance folder
        db_url = "sqlite:///db.sqlite"

    app.config.from_mapping(
        # default secret that should be overridden in environ or config
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # initialize Flask-SQLAlchemy and the init-db command
    db.init_app(app)
    app.cli.add_command(init_db_command)

    # apply the blueprints to the app
    from magic_ledger import projects

    api.add_namespace(projects.ns)

    from magic_ledger import third_parties

    api.add_namespace(third_parties.ns)

    from magic_ledger import inventory

    api.add_namespace(inventory.ns)

    from magic_ledger import invoices

    api.add_namespace(invoices.ns)

    from magic_ledger import transactions

    api.add_namespace(transactions.ns)

    from magic_ledger import account_plan

    api.add_namespace(account_plan.ns)

    from magic_ledger import assets

    app.register_blueprint(assets.bp)

    from magic_ledger import financial_holdings

    app.register_blueprint(financial_holdings.bp)

    from magic_ledger import liquidity

    app.register_blueprint(liquidity.bp)

    from magic_ledger import account_balance

    app.register_blueprint(account_balance.bp)

    from magic_ledger import exchange

    app.register_blueprint(exchange.bp)

    from magic_ledger import inflow

    app.register_blueprint(inflow.bp)

    return app


def init_db():
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


# add a python function that inserts all the entries in the accounts.sql file into the database
def insert_account_plan():
    with open(
        r"C:\Users\ageor\PycharmProjects\magic-ledger\magic_ledger\accounts.sql",
        mode="r",
    ) as sql_file:
        for line in sql_file:
            db.session.execute(text(line))
            db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
    insert_account_plan()
    click.echo("provisionsed account plan.")
