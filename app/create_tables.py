from app.database import Base, engine
from app.models import user
from app.models import note

def create_tables():
    Base.metadata.create_all(engine)