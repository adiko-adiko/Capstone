# Capstone

By running the Flask app the database is created Then if we run the pandas file, it loads the csv into the database Those changes are then visible into the app. While presenting I noticed that for the flask app while submitting the form, the app breaks. It's due to the presence of the "id" input in the new_order=Order(...) which once remove fixes that issue.
