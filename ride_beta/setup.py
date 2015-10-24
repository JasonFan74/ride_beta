from models import *
import datetime


def addTestEntries():
	ride = Ride(
				departure= datetime.datetime.now
				destination="Metro"
				driver="Jason"
				comment="try hard"
				capacity=4
				slug="jason-1")
	ride.save()
