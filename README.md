# OpenAPI with Flask for Surf's Up

> This code base serves as starting point for writing your next Flask application delivering observed weather patterns from Hawaii. BUT I REALLY JUST WANTED TO FOCUS ON FLASK AND APIs!

## New Flask Project

Its not just Flask but an ecosystem to properly create a RESTful API service... SO FILE app_refactored.py is that using:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight WSGI web application framework in Python. It is designed to make getting started very quickly and very easily.
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/) is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) is a thin integration layer for Flask and marshmallow that adds additional features to marshmallow.
- [SQLAlchemy](https://www.sqlalchemy.org/library.html) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask.
- [Tailwind](https://tailwindcss.com/) is a utility-first CSS framework for rapidly building custom user interfaces.

- Using well organized directories with comments
  - /notebooks # Holding climate_analysis.ipynb & SurfsUp_Challenge.ipynb
  - /resources # Folder of graphs created from the exploratory climate analysis
  - /templates # Jinja2 HTML template files with Tailwind
  - .editorconfig # .editorconfig to power some workflows in VS Code.
  - .gitignore # .gitignore
  - app_refactored # The flask app using the libraries above
  - app.py # The Module's Flask app but running through connextion
  - database.py # Following some basic best practice of breaking the functions into modules.
  - hawaii.db # Raw weather data
  - models.py # I went against the grain and practiced the declarative version of SQLAlchemy
  - openapi.yaml # This file is the actual file that connextion to power a proper OpenAPI spec and UI

## Usage

```powershell
PS ~/surfs-up/> $env:FLASK_APP = 'app'
PS ~/surfs-up/> $env:FLASK_ENV = 'development'
PS ~/surfs-up/> python app.py
```

## Endpoints

/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/temp/2017-06-01/2017-06-30

## Data Powering the Web app

Using Python and SQLAlchemy in jupyter notebook to do basic climate analysis and data exploration of our hawaii.db database.

The module and module Challenge were basically Exploratory Climate Analysis:

- Script a query to retrieve the last 12 months of precipitation data.
- Select only the date and prcp values.
- Load the query results into a Pandas DataFrame and set the index to the date column.
- Sort the DataFrame values by date.
- Plot the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.

... included in the climate_analysis.ipynb & SurfsUp_Challenge.ipynb files. The code from the notebooks were used in app.py to power the endpoints in Flask, including the calc_temps function that accepts a start date and end date in the format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Finish the last three endpoints in pure openapi format.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
