from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from ride_beta.models import Ride

rides = Blueprint('rides', __name__, template_folder='templates')

class ListView(MethodView):

    def get(self):
        ride = Ride.objects.all()
        return render_template('rides/list.html', ride=ride)


class DetailView(MethodView):

    def get(self, slug):
        ride = Ride.objects.get_or_404(slug=slug)
        return render_template('rides/detail.html', ride=ride)


# Register the urls
#rides.add_url_rule('/', view_func=TestView.as_view('test'))
rides.add_url_rule('/', view_func=ListView.as_view('list'))
rides.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))