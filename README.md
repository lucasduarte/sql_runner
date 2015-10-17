# SQL RUNNER
####A small application to run SQL commands on databases setting the connection string dinamically

To execute it you just have to clone this repository and run a "python execute_sql.py" to run the flask server.
It will run on http://localhost:5000 by default.

To use it you just have to send a post to http://localhost:5000 with the connection_string and query on it's header.

If it succeeds it will give you a JSON return with the query results, and if it fails it returns HTTP code 500 and a JSON with the error message
