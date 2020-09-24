# Having these separate Python files is good because you can use the same model to query or load data outside of an app.

#### Declarative
#### https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/index.html
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///notebook/hawaii.db"
# SQLALCHEMY_DATABASE_URL = Allows for other databases.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# Using SQLAlcehmy’s declarative_base() allows you to write just one model
# per table that app uses. We use “declarative_base” to create a class
# using our engine that we then create the subclass from like
# measurement and station.
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models

    Base.metadata.create_all(bind=engine)


# #### Automap
# #### https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html
# If you already have an existing database and want to use it with Flask-SQLAlchemy,
# reflect and automap might be what you need. Think reflection as read only. automap
# as class maker.

# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

# Base = automap_base()

# # engine, suppose it has two tables 'measurement' and 'station' set up
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# # reflect the tables
# Base.prepare(engine, reflect=True)

# # mapped classes are now created with names by default
# # matching that of the table name.
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# session = Session(engine)
