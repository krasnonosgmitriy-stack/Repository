from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///app.db', echo=True)

Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    def __repr__(self):
        return '<Students %r>' % self.name

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('students.id'))

    def __repr__(self):
        return '<Posts %r>' % self.title


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_student = Students(
    name='Student_1',
    email='email_student_1@gmail.com'
)

session.add(new_student)
session.commit()

session.add_all([
    Students(name='Student_2', email='email_student_2@gmail.com'),
    Students(name='Student_3', email='email_student_3@gmail.com'),
])
session.commit()

#students = session.query(Students).all()
#for student in students:
#    print(student.name)
#
#student_1 = session.query(Students).filter(Students.id == 1).first()
#print("-" * 100)
#student_1 = "email_student_4@gmail.com"
#session.commit()
#
#student_2 = session.query(Students).filter(Students.name == "Student_2").first()
#session.delete(student_2)
#session.commit()