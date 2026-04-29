from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Text
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)


