bush-schedule
=============

A schedule and calendar application for the Bush School. 
To setup, first clone the respository. Then install dependencies using pip, with the command

```
pip install -r requirements.txt
```
You may need to use sudo. Next, initialize the database using the python console.

```
>>> import app
>>> import models
>>> app.db.create_all()
```

This will create the tables in the sqlite database.
The run the application, use the command
```
python app.py
```
