# Flask with Poetry

> This code base serves as starting point for writing your next Flask application through Poetry.

I come from the JS/TS world and we have a great cli tool NPM & Yarn to start projects. Well, I wanted the same for Python. What this looks like in action is something that resembles JavaScript's yarn tool. There is the pyproject.toml similar to package.json and a poetry.lock like yarn.lock. There is also configuration of the tool itself kept in poetry.toml (again, like .yarnrc.yml).

## New Project

Use the package manager [Poetry](https://python-poetry.org/docs/#installation) to install Flask with Poetry.

Its not just Flask but an ecosystem to properly create a RESTful API service...

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight WSGI web application framework in Python. It is designed to make getting started very quickly and very easily.
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/) is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) is a thin integration layer for Flask and marshmallow that adds additional features to marshmallow.
- [SQLAlchemy](https://www.sqlalchemy.org/library.html) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask.
- [Tailwind](https://tailwindcss.com/) is a utility-first CSS framework for rapidly building custom user interfaces.

```powershell
PS ~/> poetry new --name app --src poetry-flask
PS ~/> Set-Location -Path poetry-flask
PS ~/poetry-flask/> poetry config --local virtualenvs.in-project true
PS ~/poetry-flask/> poetry install
```

- Well organized directories with lots of comments
  - poetry-flask
    - .venv
    - src
      _ app
        _ commands # Commands made available to manage.py
        _ models   # Database Models (and their Forms)
        _ static   # Static asset files that will be mapped to the "/static/" URL
        _ templates# Jinja2 HTML template files with Tailwind
        _ views    # View functions
    - tests



## Usage

```powershell
PS ~/poetry-flask/> poetry add flask flask-marshmallow flask-sqlalchemy marshmallow-sqlalchemy
PS ~/poetry-flask/> poetry add -D black flake8

PS ~/poetry-flask/src/app/> $env:FLASK_APP = 'app'
PS ~/poetry-flask/src/app/> $env:FLASK_ENV = 'development'
PS ~/poetry-flask/src/app/> poetry run flask run
```

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Actually follow my own folder structure.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
