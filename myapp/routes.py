from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import City

@myapp_obj.route("/", methods=["GET", "POST"])
def index():
  form = TopCities()
  if form.validate_on_submit():
    city_name = form.city_name.data
    city_rank = form.city_rank.data
    is_visited = form.is_visited.data
    
    existed_city = City.query.filter_by(name=city_name).first()
    if existed_city:
      flash("The city name is already added")
      return redirect("/")
    
    city = City(name=city_name, rank=city_rank, is_visited=is_visited)
    db.session.add(city)
    db.session.commit()
    flash(f"You added {city_name} sucessfully")
    return redirect("/")

  return render_template(
    "home.html", 
    title="Top Cities", 
    form=form, 
    top_cities=City.query.order_by(City.rank).all()
  )