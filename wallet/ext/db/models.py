import datetime

from wallet.ext.db import db

class Gains(db.Model):
    __tablename__ = "gains"
    id = db.Column("id",
                    db.Integer,
                    primary_key=True)
    description = db.Column("description",
                            db.Unicode)
    amount = db.Column("amount",
                        db.Float)
    created_at = db.Column("created_at", 
                            db.DateTime)

    @staticmethod
    def add_gains(description:str, amount:float, date:datetime = datetime.datetime.utcnow()):
        """Add gains
        Args:
            description (str): descr iption of gains
            amount (float): valeus of amount
            date(datetime): date of transaction(default today)
        """
        gain = Gains( 
                description=description,
                amount=amount,
                created_at = date
                )
        db.session.add(gain)
        db.session.commit()
    
    @staticmethod
    def delete_gains(id:int):
        """Delete gains
        Args:
            id (int): id for delete gains
        """
        gain = Gains.query.filter_by(id=id).one()
        db.session.delete(gain)
        db.session.commit()
    
    def to_json(self):
        """Return dict with attributes of gain
        """
        formatted_date = self.created_at.strftime("%m/%d/%Y")
        json_gain = {
            'id': self.id,
            'description':self.description,
            'amount':self.amount,
            'created_at': formatted_date
        }
        return json_gain