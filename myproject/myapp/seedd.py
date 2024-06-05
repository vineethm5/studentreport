import random
from .models import *
from faker import Faker

faker=Faker()




def whatever(n=10)->None:
    try:
        for _ in range(0,n):
            deparq=Department.objects.all()
            departrand=random.randint(0,len(deparq)-1)
            department=deparq[departrand]
            studeStudentId=f'STU-0{random.randint(100,500)}'
            studentname=faker.name()
            studentage=random.randint(18,26)
            studentemail=faker.email()
            studentaddress=faker.address()
            print(studeStudentId)

            stuent_id_o=StudendId.objects.create(student_id=studeStudentId)

            student_de=student.objects.create(
                studendid=stuent_id_o,
                department=department,
                studentname=studentname,
                studentage=studentage,
                studentemail=studentemail,
                studentaddress=studentaddress

            )

    except Exception as e:
        print(e)



def createma()->None:
    try:
        students=student.objects.all()
        for student in students:
            subjectss=subject.objects.all()
            for subject in subjectss:
                subjj=subjectmarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0,100))
    except Exception as e:
     print(e)        
