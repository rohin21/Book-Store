from sqlalchemy import Column, Integer,String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from ..config.model_base import Base

class StockDBModel(Base):
    stk_id = Column(UUID(as_uuid=True), primary_key=True,unique=True, index=False, default=uuid4)
    stk_num = Column(Integer,nullable = False)
    stk_desc = Column(String,nullable = False)
