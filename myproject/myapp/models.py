from django.db import models

# Create your models here.
class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=["department"]


class StudendId(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE)
    studendid=models.OneToOneField(StudendId,related_name='studenttidd',on_delete=models.CASCADE)
    studentname=models.CharField(max_length=100)
    studentage=models.CharField(max_length=100)
    studentemail=models.EmailField(max_length=100)
    studentaddress=models.TextField(max_length=100)

    def __str__(self)->str:
        return self.studentname
    
    class Meta:
        ordering=['studentname']
        verbose_name="student"

        
class subject(models.Model):
    subject_name=models.CharField(max_length=100)

class subjectmarks(models.Model):
    student=models.ForeignKey(student, related_name='student', on_delete=models.CASCADE)
    subject=models.ForeignKey(subject,related_name='subject',on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self)->str:
        return  f'{self.student.studentname}  {self.subject.subject_name}'
    
    class Meta:
        unique_together =['student','subject']