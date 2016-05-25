from .. import Base
from sqlalchemy import String, Integer, Column, DECIMAL
from .. import session


class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

    def export_data(self):
        return {
            'id_user': self.id_user,
            'email': self.email,
            'name': self.name
        }

    def import_data(self, data):
        if 'email' in data:
            self.email = data['email']
        if 'name' in data:
            self.name = data['name']

    @staticmethod
    def get_users():
        return [user.export_data() for user in session.query(User).all()]

    @staticmethod
    def get_user(id):
        return session.query(User).filter_by(id_user=id).one_or_none()

    @staticmethod
    def new_user(data):
        user = User()
        user.import_data(data)
        session.add(user)
        session.commit()
        return {}

class University(Base):
    __tablename__ = 'universities'
    id_university = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    id_user = Column(Integer, nullable=False)


class Semester(Base):
    __tablename__ = 'semesters'
    id_semester = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(45), nullable=False)
    id_university = Column(Integer, nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id_subject = Column(Integer, primary_key=True, index=True)
    code = Column(String(45), nullable=False)
    name = Column(String(255), nullable=False)
    id_semester = Column(Integer, nullable=False)


class Calification(Base):
    __tablename__ = 'califications'
    id_calification = Column(Integer, primary_key=True, index=True)
    note_1 = Column(DECIMAL, default=0)
    note_2 = Column(DECIMAL, default=0)
    note_3 = Column(DECIMAL, default=0)
    note_add = Column(DECIMAL, default=0)
    final_note = Column(DECIMAL, default=0)
    id_subject = Column(Integer, nullable=False)
