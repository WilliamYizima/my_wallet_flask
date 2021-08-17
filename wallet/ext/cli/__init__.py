import click
import datetime

from wallet.ext.db import db
from wallet.ext.db.models import Gains

def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando iniciliza o db"""
        db.create_all()

        click.echo("criei a tabela conforme solicitado")

    @app.cli.command()
    def list_db():
        """Neste comando estou mostrando os registros"""
        gains = Gains.query.all()
        if(len(gains) == 0):
            click.echo(f"lista de registros vazia")
        else:
            gain_attributes = [gain.to_json() for gain in gains]
            click.echo(f"lista de registros: {gain_attributes}")
        

    @app.cli.command()
    @click.option("--description", "-de")
    @click.option("--amount", "-am")
    
    def add_gains(description: str, amount: float):
        """adicionando um ganho"""
        date = datetime.datetime.utcnow()
        gains = Gains.add_gains(
                    description=description, 
                    amount=amount)

        click.echo(f"Foi a descrição:{description} e o amount:{amount}")
