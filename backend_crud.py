from config import session
from models import Backend

class Backend_Crud:
    def _init_(self):
        self.session = session
    
    def insert_student(self, first_name, last_name, email, age):
        new_student = Backend(first_name=first_name, last_name=last_name, age=age, email=email) 
        self.session.add(new_student)  
        self.session.commit()
        return f'New student with these details {new_student} was added'
    
    def get_all_students(self):
        return session.query(Backend).all()
    
    def get_student_by_first(self, first_name):
        return self.session.query(Backend).filter_by(first_name=first_name).first()
    
    def get_student_id(self, student_id):
        return self.session.query(Backend).filter_by(student_id=student_id).first()
    
# student1 = Backend_Crud('Nana','Afua','nanaafuaantwiwaa@gmail.com',19) 
# backend_crud = Backend_Crud()
# student_1 = backend_crud.insert_student('Habiba','Adams','hab@gmail.com',22)
# print(student_1)

# all_students = backend_crud.get_all_students()
# for student in all_students:
#     print(student)

backend_crud = Backend_Crud()
student_id = backend_crud.get_student_id(1)
print(student_id)

# Upadating based on ID, they are set to None because we don't what the user's criteria
# None means with the value the function should run.
def update_student(self, student_id, first_name=None,last_name=None,age=None,email=None):
    selected_student = self.session.query(Backend).filter_by(student_id)
    if selected_student:
        if first_name:
            selected_student.first_name = first_name
        if last_name:
            selected_student.last_name = last_name
        if age:
            selected_student.age = age
        if email:
            selected_student.email = email
        self.session.commit()
    return selected_student



# Deleting a particular record
def delete_student(self, student_id):
    selected_student = self.session.query(Backend).filter_by(student_id=student_id).filter_by
    if selected_student:
        self.session.delete(selected_student)
    self.session.commit()
    return f"Student with ID{student_id} has been deleted "

backend_crud = Backend_Crud(session)
selected_student = Backend_Crud.delete_student(5)
print(selected_student)
