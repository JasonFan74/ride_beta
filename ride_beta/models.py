import datetime
from flask import url_for
from ride_beta import db

class Ride(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    departure = db.DateTimeField(required=True)
    destination = db.StringField(max_length=255, required=True)
    driver = db.StringField(max_length=255, required=True)
    comment = db.StringField(required=True)
    capacity = db.IntField(required=True)
    slug = db.StringField(max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }