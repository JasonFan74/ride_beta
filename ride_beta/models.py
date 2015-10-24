from ride_beta import db
from sqlalchemy.dialects.postgresql import JSON

class Ride(db.Model):
    __tablename__="rides"
    ride_id = db.Column(db.Integer, primary_key=True)
    #created_at = db.Column(db.)
    depart_time = db.Column(db.DateTime(timezome=False)) #always UTC

    def __init__(self, depart_time):
        self.depart_time = depart_time
        
    def __repr__(self):
        return '<id{}>'.format(self.id)

class SignUp(db.Model):
    __tablename__ = "signups"
    signup_id = db.Column(db.Integer, primary_key=True)
    ride_id = db.Column(db.Integer, ForeignKey("rides.ride_id"))
    member_id = db.Column(db.Integer, ForeignKey("members.member_id"))

    def __init__(self, ride, member):
        self.ride_id = ride.id
        self.member_id = member.id

    def __repr__(self):
        return '<id{}>'.format(self.id)



class Member(db.Model):
    __tablename__ = "members"
    member_id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id{}>'.format(self.id)


"""
class Driver(db.Model):
    id = db.Column(Integer, primary_key=True)


class Car(db.Model):
    id = db.Column(Integer, primary_key=True)
"""