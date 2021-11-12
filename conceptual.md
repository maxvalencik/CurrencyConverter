### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

_**Javascript is a script language and is interpreted at run time, Python is similar even though it uses an interpreter to be able to run. Python is used for a lot of application including data manipulation and backend services. JS is the language of the web for DOM manipulation and logic, used a lot for frontend.**_

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.

_**dictionary\_name.get('key') will return none is not existing key. Can return a default value specified in the get function if needed (dictionary\_name.get ("key", "default")).**_

_**key in dictionary\_name will return false if key does not exist.**_

- What is a unit test?

_**Test of an individual unit or function.**_

- What is an integration test?

_**A test that verifies that all the units/functions work well together.**_

- What is the role of web application framework, like Flask?

_**Support the development of web applications.**_
 
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
_**It depends if we want the associated route to be dynamic (query param) or static (param).**_

- How do you collect data from a URL placeholder parameter using Flask?

_**@app.route('/example/\<parameter>')**_

_**def function(parameter):**_

- How do you collect data from the query string using Flask?

_**request.args.get('argument\_name')**_ (for get requests)

_**request.form.get('argument\_name')**_ (for post requests)


- How do you collect data from the body of the request using Flask?

_**data = request.json or request.form if not JSon formatted.**_

- What is a cookie and what kinds of things are they commonly used for?



_**Cookies are small pieces of data used to remember a user using a browser. It is created by the server when the connection is established with the user. The data stored in a cookie is unique to the user and browser. A cookie can be used to store data such as:**_

 * _**shopping cart**_
 * _**username**_
 * _**password**_
 * _**web surfing habits...**_
 

- What is the session object in Flask?

_**A session object in flask is used to store data about the client using the front end of the app. It is a type of dictionary that stores data in key/value pairs**_

- What does Flask's `jsonify()` do?

_**Format data into JSon format.**_
