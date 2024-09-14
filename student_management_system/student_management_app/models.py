from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,'Admin'),(2,'Staff'),(3,'Employee'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    
"""class Admin(models.Model):
    
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=False)
    name=models.CharField(max_length=150)
    email=models.EmailField()
    password=models.CharField(max_length=150)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
"""


class Departement(models.Model):
    departement_name=models.CharField(max_length=150)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    def __str__(self):
        return self.departement_name
    


"""class Role(models.Model):
    id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=150)
    departement_id=models.ForeignKey(Departement,on_delete=models.CASCADE)
    staffs_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
"""
    
class Employee(models.Model):
    STATUS_ACTIVE='active'
    STATUS_INACTIVE="inactive"
    STATUS_CHOICES=[
        (STATUS_ACTIVE,'Active'),
        (STATUS_INACTIVE,'Inactive'),
    ]
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=False)
    contact_number=models.CharField(max_length=15)
    DOB=models.DateField()
    DOJ=models.DateField()
   
    tenth_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 10th grade")
    twelfth_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 12th grade")
    graduation_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 12th grade")
    gender=models.CharField(max_length=20)
    address=models.TextField(max_length=150)
    full_day_leaves_remaining = models.IntegerField(default=12)
    half_day_leaves_remaining = models.IntegerField(default=12)
    #staffs_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    #father_occupation=models.CharField(max_length=150)
    #mother_occupation=models.CharField(max_length=150)
    father_mobile=models.IntegerField()
    role=models.CharField(max_length=150)
    official_mail=models.EmailField()
    personal_email=models.EmailField()
    departement_id=models.ForeignKey(Departement,on_delete=models.DO_NOTHING)
    pancard=models.CharField(max_length=12)
    adharcard=models.CharField(max_length=15)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_ACTIVE)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

  
    def __str__(self):
        return f"{self.admin.get_full_name()} - {self.role} ({self.departement_id})"
    
class Staff(models.Model):
    STATUS_ACTIVE='active'
    STATUS_INACTIVE="inactive"
    STATUS_CHOICES=[
        (STATUS_ACTIVE,'Active'),
        (STATUS_INACTIVE,'Inactive'),
    ]
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=False)
    contact_number=models.CharField(max_length=15)
    DOB=models.DateField()
    DOJ=models.DateField()
   
   
    tenth_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 10th grade")
    twelfth_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 12th grade")
    graduation_percentage = models.DecimalField(max_digits=3, decimal_places=1, help_text="Percentage obtained in 12th grade")
    gender=models.CharField(max_length=20)
    full_day_leaves_remaining = models.IntegerField(default=12)
    half_day_leaves_remaining = models.IntegerField(default=12)
    address=models.TextField(max_length=150)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
   # father_occupation=models.CharField(max_length=150)
   # mother_occupation=models.CharField(max_length=150)
    father_mobile=models.IntegerField()
    role=models.CharField(max_length=150)
    official_mail=models.EmailField()
    personal_email=models.EmailField()
    departement_id=models.ForeignKey(Departement,on_delete=models.DO_NOTHING)
    pancard=models.CharField(max_length=12)
    adharcard=models.CharField(max_length=15)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_ACTIVE)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

 
    
    def __str__(self):
        return f"{self.admin.get_full_name()} - {self.role} ({self.departement_id})"
    
"""   
class LeaveReportEmployee(models.Model):
    id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=50)
    leave_messages=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
""" 
class StaffLeave(models.Model):
    FULL_DAY = 'full day'
    HALF_DAY = 'half day'
    
    LEAVE_TYPE_CHOICES = [
        (FULL_DAY, 'Full Day'),
        (HALF_DAY, 'Half Day'),
    ]
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField()
    messages=models.TextField()
    
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES, default=FULL_DAY)
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    def __str__(self):
        return f"{self.staff_id}"
    
class EmployeeLeave(models.Model):
    FULL_DAY = 'full day'
    HALF_DAY = 'half day'
    
    LEAVE_TYPE_CHOICES = [
        (FULL_DAY, 'Full Day'),
        (HALF_DAY, 'Half Day'),
    ]
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField()
    messages=models.TextField()
    
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES, default=FULL_DAY)
    status=models.IntegerField(default=0)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
    def __str__(self):
        return f"{self.employee_id}"

"""  
class FeedbackEmployee(models.Model):
    id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255)
    feddback_reply=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class FeedbackStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255)
    feddback_reply=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class NotificationEmployee(models.Model):
    id=models.AutoField(primary_key=True)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class NotificationStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    """