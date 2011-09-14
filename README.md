Redis Handler for Python's logging module
======

A simple Redis handler for the python logging module, with an example of usage.

All the messages are stored on lists, with the logger's name beng the key of the list. That's usefull for logging different processes or specific parts of your app. It's simple to port to a single-key handler or to any kind of naming you want.