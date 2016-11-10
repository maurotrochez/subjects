from .. import Base
from sqlalchemy import String, Integer, Column, DECIMAL, DATETIME
from .. import session
from datetime import datetime
from uuid import uuid1


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
    def mysqlget_users():
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
        return user

    @staticmethod
    def update_user(id, data):
        user = session.query(User).filter_by(id_user=id).one_or_none()
        if user is None:
            return None
        user.import_data(data)
        session.add(user)
        session.commit()
        return {}

    @staticmethod
    def get_user_by_emial(email):
        return session.query(User).filter_by(email=email).one_or_none()


class University(Base):
    __tablename__ = 'universities'
    id_university = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    id_user = Column(Integer, nullable=False)

    def export_data(self):
        return {
            'id_university': self.id_university,
            'name': self.name,
            'id_user': self.id_user
        }

    def import_data(self, data):
        if 'name' in data:
            self.name = data['name']
        if 'id_user' in data:
            self.id_user = data['id_user']

    @staticmethod
    def get_universities():
        return [university.export_data() for university in session.query(University).all()]

    @staticmethod
    def get_university(id):
        return session.query(University).filter_by(id_university=id).one_or_none()

    @staticmethod
    def new_university(data):
        university = University()
        university.import_data(data)
        session.add(university)
        session.commit()
        return {}

    @staticmethod
    def update_university(id, data):
        university = session.query(University).filter_by(id_university=id).one_or_none()
        if university is None:
            return None
        university.import_data(data)
        session.add(university)
        session.commit()
        return {}

    @staticmethod
    def get_university_by_user(id_user):
        return [university.export_data() for university in session.query(University).filter_by(id_user=id_user).all()]


class Semester(Base):
    __tablename__ = 'semesters'
    id_semester = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    code = Column(String(45), nullable=False)
    id_university = Column(Integer, nullable=False)

    def export_data(self):
        return {
            'id_semester': self.id_semester,
            'name': self.name,
            'code': self.code,
            'id_university': self.id_university
        }

    def import_data(self, data):
        if 'name' in data:
            self.name = data['name']
        if 'code' in data:
            self.code = data['code']
        if 'id_university' in data:
            self.id_university = data['id_university']

    @staticmethod
    def get_semesters():
        return [semester.export_data() for semester in session.query(Semester).all()]

    @staticmethod
    def get_semester(id):
        return session.query(Semester).filter_by(id_semester=id).one_or_none()

    @staticmethod
    def new_semester(data):
        semester = Semester()
        semester.import_data(data)
        session.add(semester)
        session.commit()
        return {}

    @staticmethod
    def update_semester(id, data):
        semester = session.query(Semester).filter_by(id_semester=id).one_or_none()
        if semester is None:
            return None
        semester.import_data(data)
        session.add(semester)
        session.commit()
        return {}

    @staticmethod
    def get_semester_by_university(id_university):
        return [university.export_data() for university in session.query(Semester).filter_by(id_university=
                                                                                             id_university).all()]


class Subject(Base):
    __tablename__ = 'subjects'
    id_subject = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(45), nullable=False)
    name = Column(String(255), nullable=False)
    teacher = Column(String(255), default=None)
    id_semester = Column(Integer, nullable=False)

    def export_data(self):
        return {
            'id_subject': self.id_subject,
            'name': self.name,
            'code': self.code,
            'teacher': self.teacher,
            'id_semester': self.id_semester
        }

    def import_data(self, data):
        if 'name' in data:
            self.name = data['name']
        if 'code' in data:
            self.code = data['code']
        if 'teacher' in data:
            self.teacher = data['teacher']
        if 'id_semester' in data:
            self.id_semester = data['id_semester']

    @staticmethod
    def get_subjects():
        return [subject.export_data() for subject in session.query(Subject).all()]

    @staticmethod
    def get_subject(id):
        return session.query(Subject).filter_by(id_subject=id).one_or_none()

    @staticmethod
    def new_subject(data):
        subject = Subject()
        subject.import_data(data)
        session.add(subject)
        session.commit()
        return {}

    @staticmethod
    def update_subject(id, data):
        subject = session.query(Subject).filter_by(id_subject=id).one_or_none()
        if subject is None:
            return None
        subject.import_data(data)
        session.add(subject)
        session.commit()
        return {}

    @staticmethod
    def get_subject_by_semester(id_semester):
        return [subject.export_data() for subject in session.query(Subject).filter_by(id_semester=id_semester).all()]


class Calification(Base):
    __tablename__ = 'califications'
    id_calification = Column(Integer, primary_key=True, index=True)
    note_1 = Column(DECIMAL(4, 2), default=0)
    note_2 = Column(DECIMAL(4, 2), default=0)
    note_3 = Column(DECIMAL(4, 2), default=0)
    note_add = Column(DECIMAL(4, 2), default=0)
    final_note = Column(DECIMAL(4, 2), default=0)
    id_subject = Column(Integer, nullable=False)

    def export_data(self):
        return {
            'note_1': float(self.note_1),
            'note_2': float(self.note_2),
            'note_3': float(self.note_3),
            'note_add': float(self.note_add),
            'final_note': float(self.final_note),
            'id_subject': self.id_subject
        }

    def import_data(self, data):
        if 'note_1' in data:
            self.note_1 = data['note_1']
        if 'note_2' in data:
            self.note_2 = data['note_2']
        if 'note_3' in data:
            self.note_3 = data['note_3']
        if 'note_add' in data:
            self.note_add = data['note_add']
        if 'final_note' in data:
            self.final_note = data['final_note']
        if 'id_subject' in data:
            self.id_subject = data['id_subject']

    @staticmethod
    def get_califications():
        return [calification.export_data() for calification in session.query(Calification).all()]

    @staticmethod
    def get_calification(id):
        return session.query(Calification).filter_by(id_calification=id).one_or_none()

    @staticmethod
    def new_calification(data):
        calification = Calification()
        calification.import_data(data)
        session.add(calification)
        session.commit()
        return {}

    @staticmethod
    def update_calification(id, data):
        calification = session.query(Calification).filter_by(id_calification=id).one_or_none()
        if calification is None:
            return None
        calification.import_data(data)
        session.add(calification)
        session.commit()
        return {}

    @staticmethod
    def get_calification_by_subject(id_subject):
        return session.query(Calification).filter_by(id_subject=id_subject).one_or_none()


class Registers(Base):
    __tablename__ = 'registers'
    id = Column(String, primary_key=True, index=True)
    temperature = Column(DECIMAL(4, 2), default=0)
    humidity = Column(DECIMAL(4, 2), default=0)
    date = Column(DATETIME, default=datetime.now())

    def export_data(self):
        return {
            "temperature": float(self.temperature),
            "humidity": float(self.humidity),
            "date": self.date
        }

    def import_data(self, data):
        self.id = str(uuid1())
        self.temperature = data.get('temperature')
        self.humidity = data.get('humidity', 0)
        self.date = datetime.now()

    @staticmethod
    def get_last_temperature():
        temp = session.query(Registers).order_by(-Registers.date).first()
        if temp is not None:
            return temp.temperature
        return 0

    @staticmethod
    def save_register(data):
        try:
            register = Registers()
            register.import_data(data)
            session.add(register)
            session.commit()
        except Exception as e:
            print e
            raise e


