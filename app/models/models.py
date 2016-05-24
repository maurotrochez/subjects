from .. import Base
from sqlalchemy import String, Integer, Column

class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)