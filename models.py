from config import session
from sqlalchemy.orm import declarative_base
#from sqlalchemy import Column,Integer,String
from sqlalchemy import Column,Integer,String,Foreignkey

#  Creating a class

Base = declarative_base()

class Backend(Base):
    _tablename_ = 'backend_class'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age= Column(Integer, nullable=False)
    email = Column(String(255), nullable= False, unique=True)

# Creating a relationship b/n tables using sql.orm
    laptops = relationship("Laptops", back_populate='student')

#Back_populate: It specifies the attribute of the related tables within the class
    
    def _str_(self):
        return f'Student\'s ID: {self.student_id}, Name: {self.first_name} {self.last_name},Age: {self.age} Email: {self.email}'

class MyLaptops(Base):
    _tablename_ = 'laptops'
    laptop_name = Column(String(50), unique=True)
    laptop_number = Column(Integer(50), primary_key=True)
    #student_id = Column(Integer)
    student_id = Column(Integer, Foreignkey(Backend.student_id), nullable=False)
    
    student = relationship("Backend",back_populate="")

# This line ensures that the tables are created in the same database that the databse is connected to
if _name_ == '_main_':
    try:
        Base.metadata.create_all(session.bind) 
        print('Tables Created')

    except Exception as e:
        print(f'An error occured: {e}')


# using Laptops creating relational tables using all methods of CRUD.