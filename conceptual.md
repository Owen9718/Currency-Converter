### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

The importance of indentation, and Python is a backend language.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  Using get() or setdefault()

- What is a unit test?

Testing a small specific piece of code.

- What is an integration test?

Testing multiple pieces/functions of code.

- What is the role of web application framework, like Flask?

To help making a web application easier and more user firendly for the coder.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

You would use /foods/pretzel for a predetermined route that may change from a input. You use query params more for a search.

- How do you collect data from a URL placeholder parameter using Flask?

request.args

- How do you collect data from the query string using Flask?

request.args.get()

- How do you collect data from the body of the request using Flask?

request.form

- What is a cookie and what kinds of things are they commonly used for?

Cookies are stored data specific to a user

- What is the session object in Flask?

The session object is how data is stored to a specific user during a session

- What does Flask's `jsonify()` do?

Turn python in to JSON
