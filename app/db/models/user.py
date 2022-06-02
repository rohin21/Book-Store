from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from ..config.model_base import Base

class UserDBModel(Base):
    user_id = Column(UUID(as_uuid=True), primary_key=True,unique=True, index=False, default=uuid4)
    user_name = Column(String,nullable = False)
    user_mobile = Column(String,nullable = False)
    user_email = Column(String,nullable=True)
    user_address = Column(String,nullable=True)