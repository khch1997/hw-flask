from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect

# Fake database for now
top_cities = []

@myapp_obj.route("/", methods=["GET", "POST"])
def index():
  form = TopCities()
  if form.validate_on_submit():
    city = form.city_name.data
    if city in top_cities:
      flash("The city is already added")
      return redirect("/")
    top_cities.append(city)
    flash(f"You added {city} sucessfully")

  return render_template("home.html", title="Top Cities", form=form, top_cities=top_cities)