from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from ..config.model_base import Base

class RolesDBModel(Base):
    role_id = Column(UUID(as_uuid=True), primary_key=True,unique=True, index=False, default=uuid4)
    role_name = Column(String,nullable = False)
    role_desc = Column(String,nullable = False)
