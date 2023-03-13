from .database import Base, SessionLocal, engine

# create tables in the database
Base.metadata.create_all(bind=engine)

# define a function to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
