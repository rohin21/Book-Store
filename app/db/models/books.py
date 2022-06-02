from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from ..config.model_base import Base

class BookDBModel(Base):
    book_id = Column(UUID(as_uuid=True), primary_key=True,unique=True, index=False, default=uuid4)
    book_name = Column(String,nullable = False)
    book_author = Column(String,nullable = False)
    book_type = Column(String,nullable=True)
    book_desc = Column(String,nullable=True)
    book_price = Column(Integer,nullable=False)