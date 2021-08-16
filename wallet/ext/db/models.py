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
                            db.DateTime, 
                            default=datetime.datetime.utcnow)

    @staticmethod
    def add_gains(description:str, amount:float):
        """Add gains
        Args:
            description (str): descr iption of gains
            amount (float): valeus of amount
        """
        gain = Gains( 
                description=description,
                amount=amount
                )
        db.session.add(gain)
        db.session.commit()
    
    def to_json(self):
        """Return dict with attributes of gain
        """
        formatted_date = self.created_at.strftime("%m/%d/%Y")
        json_gain = {
            'description':self.description,
            'amount':self.amount,
            'created_at': formatted_date
        }
        return json_gain