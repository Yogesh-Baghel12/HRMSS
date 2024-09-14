from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from student_management_app.models import Departement,CustomUser,Employee,Staff,StaffLeave,EmployeeLeave
from django.contrib import messages
from datetime import datetime

@login_required(login_url='/')
def HOME(request):
    employee_count=Employee.objects.all().count()
    staff_count=Staff.objects.all().count()
    department_count=Departement.objects.all().count()
    active_count = Employee.objects.filter(status=Employee.STATUS_ACTIVE).count()
    inactive_count = Employee.objects.filter(status=Employee.STATUS_INACTIVE).count()
    
    Staff_active_count=Staff.objects.filter(status=Staff.STATUS_ACTIVE).count()
    Staff_inactive_count=Staff.objects.filter(status=Staff.STATUS_INACTIVE).count()

    male_count = Employee.objects.filter(gender='Male').count()
    staff_male=Staff.objects.filter(gender='Male').count()
    staff_female=Staff.objects.filter(gender='Female').count()
    female_count=Employee.objects.filter(gender='Female').count()
    
    total_male= male_count + staff_male
    total_female=female_count + staff_female
    print(total_male,total_female)
    
    active_employees_staff = active_count + Staff_active_count
    inactive_employees_staff=inactive_count + Staff_inactive_count
    total_employee_count=employee_count + staff_count
    context={
        'total_employee_count':total_employee_count,
        'department_count':department_count,
        'active_employees_staff':active_employees_staff,
        'inactive_employees_staff':inactive_employees_staff,
        'total_male':total_male,
        'total_female':total_female
    }
    return render(request,'Admin/home.html',context)
@login_required(login_url='/')
def POLICY(request):
    return render(request,'Admin/policy.html')

#EMployee views

@login_required(login_url='/')
def ADD_EMPLOYEE(request):
    department=Departement.objects.all()
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        department_id=request.POST.get('department_id')
        dob=request.POST.get('dob')
        Joining_date=request.POST.get('Joining_date')
        tenth_marks=request.POST.get('tenth_marks')
        twelfth_marks=request.POST.get('twelfth_marks')
        Graduation_marks=request.POST.get('Graduation_marks')
        contact_number=request.POST.get('contact_number')
        adharcard=request.POST.get('adharcard')
        pancard=request.POST.get('pancard')
        address=request.POST.get('address')
        half_day=request.POST.get('half_day')
        full_day=request.POST.get('full_day')
        father_name=request.POST.get('father_name')
        #father_occupation=request.POST.get('father_occupation')
        father_mobile=request.POST.get('father_mobile')
        mother_name=request.POST.get('mother_name')
       # mother_occupation=request.POST.get('mother_occupation')
        role=request.POST.get('role')
        username=request.POST.get('username')
        personal_email=request.POST.get('personal_email')
        off_email=request.POST.get('off_email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        
        print(first_name,last_name,gender,department_id,dob,Joining_date,tenth_marks,twelfth_marks,Graduation_marks,adharcard,pancard,address,father_name,father_mobile,mother_name,mother_occupation,role,username,password,off_email,status)
        if CustomUser.objects.filter(email=off_email).exists():
            messages.warning(request,"email is already taken")
            return redirect("add_employee")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"username is already taken")
            return redirect("add_employee")
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=off_email,
                user_type= 3
                
            )
            user.set_password(password)
            user.save()
            department=Departement.objects.get(id=department_id)
            
            #models field=view post field
            
            employee=Employee(
                admin=user,
                contact_number=contact_number,
                DOB=dob,
                DOJ=Joining_date,
                tenth_percentage=tenth_marks,
                twelfth_percentage=twelfth_marks,
                graduation_percentage=Graduation_marks,
                gender=gender,
                address=address,
                father_name=father_name,
                mother_name=mother_name,
               # father_occupation=father_occupation,
               # mother_occupation=mother_occupation,
                father_mobile=father_mobile,
                role=role,
                full_day_leaves_remaining=full_day,
                half_day_leaves_remaining=half_day,
                personal_email=personal_email,
                departement_id=department,
                pancard=pancard,
                adharcard=adharcard,
                status=status,
            )
            
            employee.save()
            messages.success(request,user.first_name+ " " + user.last_name+ "are  succssfully Added")
            return redirect('add_employee')
            
        
   


    context={
        'department':department
    }
    #print(department)
    return render(request,'Admin/add_employee.html',context)
@login_required(login_url='/')
def VIEW_EMPLOYEE(request):
    employee=Employee.objects.all()
    context={
        'employee':employee,
    }
    return render(request,'Admin/view_employee.html',context)

@login_required(login_url='/')
def EDIT_EMPLOYEE(request,id):
    employee=Employee.objects.filter(id=id)
    department=Departement.objects.all()
    context={
        'employee':employee,
        'department':department,
    }
    return render(request,'Admin/edit_employee.html',context)

@login_required(login_url='/')
def UPDATE_EMPLOYEE(request):
    if request.method == "POST":
        employee_id=request.POST.get('employee_id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        department_id=request.POST.get('department_id')
        dob=request.POST.get('dob')
        Joining_date=request.POST.get('Joining_date')
        tenth_marks=request.POST.get('tenth_marks')
        twelfth_marks=request.POST.get('twelfth_marks')
        Graduation_marks=request.POST.get('Graduation_marks')
        contact_number=request.POST.get('contact_number')
        adharcard=request.POST.get('adharcard')
        pancard=request.POST.get('pancard')
        address=request.POST.get('address')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_mobile=request.POST.get('father_mobile')
        mother_name=request.POST.get('mother_name')
        mother_occupation=request.POST.get('mother_occupation')
        role=request.POST.get('role')
        half_day=request.POST.get('half_day')
        full_day=request.POST.get('full_day')
        username=request.POST.get('username')
        personal_email=request.POST.get('personal_email')
        off_email=request.POST.get('off_email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        
        user=CustomUser.objects.get(id=employee_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=off_email
        if password != None and password!="":
            user.set_password(password)
        user.save()
        
        employee=Employee.objects.get(admin=employee_id)
        employee.gender=gender
        employee.dob=dob
        employee.Joining_date=Joining_date
        employee.tenth_marks=tenth_marks
        employee.twelfth_percentage=twelfth_marks
        employee.Graduation_marks=Graduation_marks
        employee.contact_number=contact_number
        employee.adharcard=adharcard
        employee.pancard=pancard
        employee.address=address
        employee.father_name=father_name
        employee.father_occupation=father_occupation
        employee.mother_name=mother_name
        employee.mother_occupation=mother_occupation
        employee.father_mobile=father_mobile
        employee.role=role
        employee.status=status
        employee.full_day_leaves_remaining=full_day
        employee.half_day_leaves_remaining=half_day
        employee.personal_email=personal_email
        
        department=Departement.objects.get(id=department_id)
        employee.departement_id=department
        
        employee.save()
        messages.success(request,'Record are succesfully updated')
        return redirect('view_employee')
    return render(request,'Admin/edit_employee.html')

#end Of Employee view

#Department Views
@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    if request.method == "POST":
        department_name=request.POST.get('department_name')
        department=Departement(
            departement_name=department_name  
        )
        department.save()
        messages.success(request,"Department Succesfully Added")
        print(department_name)
        return redirect('add_deaprtment')
    return render(request,'Admin/add_department.html')

@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department=Departement.objects.all()
    context={
        'department':department,
    }
    return render(request,'Admin/view_department.html',context)

@login_required(login_url='/')
def EDIT_DEPARTMENT(request,id):
    department=Departement.objects.filter(id=id)
    context={
        'department':department,
    }
    return render(request,'Admin/edit_department.html',context)
@login_required(login_url='/')
def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        department_names=request.POST.get('department_name')
        department_id=request.POST.get('department_id')
        
        
        department=Departement.objects.get(id=department_id)
        department.departement_name=department_names
        
        department.save()
        messages.success(request,"Department Successfully Updated")
        
        return redirect('view_department')
    return render(request,'Admin/edit_department.html')

#End of Department views

#start of Manager Views
@login_required(login_url='/')
def ADD_MANAGER(request):
    department=Departement.objects.all()
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        department_id=request.POST.get('department_id')
        dob=request.POST.get('dob')
        Joining_date=request.POST.get('Joining_date')
        tenth_marks=request.POST.get('tenth_marks')
        twelfth_marks=request.POST.get('twelfth_marks')
        Graduation_marks=request.POST.get('Graduation_marks')
        contact_number=request.POST.get('contact_number')
        adharcard=request.POST.get('adharcard')
        pancard=request.POST.get('pancard')
        address=request.POST.get('address')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_mobile=request.POST.get('father_mobile')
        mother_name=request.POST.get('mother_name')
        mother_occupation=request.POST.get('mother_occupation')
        role=request.POST.get('role')
        username=request.POST.get('username')
        personal_email=request.POST.get('personal_email')
        off_email=request.POST.get('off_email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        
        print(first_name,last_name,gender,department_id,dob,Joining_date,tenth_marks,twelfth_marks,Graduation_marks,adharcard,pancard,address,father_name,father_mobile,father_occupation,mother_name,mother_occupation,role,username,password,off_email,status)
        if CustomUser.objects.filter(email=off_email).exists():
            messages.warning(request,"email is already taken")
            return redirect("add_manager")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"username is already taken")
            return redirect("add_manager")
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=off_email,
                user_type= 2
                
            )
            user.set_password(password)
            user.save()
            department=Departement.objects.get(id=department_id)
            
            #models field=view post field
            
            staff = Staff (
                admin=user,
                contact_number=contact_number,
                DOB=dob,
                DOJ=Joining_date,
                tenth_percentage=tenth_marks,
                twelfth_percentage=twelfth_marks,
                graduation_percentage=Graduation_marks,
                gender=gender,
                address=address,
                father_name=father_name,
                mother_name=mother_name,
                father_occupation=father_occupation,
                mother_occupation=mother_occupation,
                father_mobile=father_mobile,
                role=role,
                personal_email=personal_email,
                departement_id=department,
                pancard=pancard,
                adharcard=adharcard,
                status=status,
            )
            
            
            staff.save()
            messages.success(request,user.first_name+ " " + user.last_name+ "are  succssfully Added")
            return redirect('add_manager')
            
        
   


    context={
        'department':department
    }
    #print(department)
    return render(request,'Admin/add_manager.html',context)

@login_required(login_url='/')
def VIEW_MANAGER(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
    }
    
    return render(request,'Admin/view_manager.html',context)
@login_required(login_url='/')
def EDIT_MANAGER(request,id):
    staff =Staff.objects.filter(id=id)
    department=Departement.objects.all()
    context={
        'staff':staff,
        'department':department,
    }

    return render(request,'Admin/edit_manager.html',context)

@login_required(login_url='/')
def UPDATE_MANAGER(request):
    if request.method == "POST":
        staff_id=request.POST.get('staff_id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        department_id=request.POST.get('department_id')
        dob=request.POST.get('dob')
        Joining_date=request.POST.get('Joining_date')
        tenth_marks=request.POST.get('tenth_marks')
        twelfth_marks=request.POST.get('twelfth_marks')
        Graduation_marks=request.POST.get('Graduation_marks')
        contact_number=request.POST.get('contact_number')
        adharcard=request.POST.get('adharcard')
        pancard=request.POST.get('pancard')
        address=request.POST.get('address')
        father_name=request.POST.get('father_name')
        father_occupation=request.POST.get('father_occupation')
        father_mobile=request.POST.get('father_mobile')
        mother_name=request.POST.get('mother_name')
        mother_occupation=request.POST.get('mother_occupation')
        role=request.POST.get('role')
        username=request.POST.get('username')
        personal_email=request.POST.get('personal_email')
        off_email=request.POST.get('off_email')
        password=request.POST.get('password')
        status=request.POST.get('status')
        
        user=CustomUser.objects.get(id=staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=off_email
        if password != None and password!="":
            user.set_password(password)
        user.save()
        
        staff=Staff.objects.get(admin=staff_id)
        staff.gender=gender
        staff.dob=dob
        staff.Joining_date=Joining_date
        staff.tenth_marks=tenth_marks
        staff.twelfth_percentage=twelfth_marks
        staff.Graduation_marks=Graduation_marks
        staff.contact_number=contact_number
        staff.adharcard=adharcard
        staff.pancard=pancard
        staff.address=address
        staff.father_name=father_name
        staff.father_occupation=father_occupation
        staff.mother_name=mother_name
        staff.mother_occupation=mother_occupation
        staff.father_mobile=father_mobile
        staff.role=role
        staff.status=status
        staff.personal_email=personal_email
        
        department=Departement.objects.get(id=department_id)
        staff.departement_id=department
        
        staff.save()
        messages.success(request,'Record are succesfully updated')
        return redirect('view_manager')
    return render(request,'Admin/edit_manager.html')

@login_required(login_url='/')
def all_employees(request):
    employees = list(Employee.objects.all())
    staffs = list(Staff.objects.all())
    all_employees = employees + staffs  # Combine the two lists
    context = {
        'all_employees': all_employees,
    }
    return render(request, 'Admin/all_employee.html', context)

@login_required(login_url='/')
def ALL_DEPARTMENT(request):
    department=Departement.objects.all()
    context={
        'department':department,
    }
    return render(request,'Admin/all_department.html',context)

@login_required(login_url='/')
def active_staff_and_employees(request):

    active_staff = Staff.objects.filter(status=Staff.STATUS_ACTIVE)
    active_employees = Employee.objects.filter(status=Employee.STATUS_ACTIVE)
    
    active_people = list(active_staff) + list(active_employees)
    
    context = {
        'active_people': active_people,
    }
    
    return render(request, 'Admin/active_employees.html', context)

@login_required(login_url='/')
def inactive_staff_and_employees(request):

    inactive_staff = Staff.objects.filter(status=Staff.STATUS_INACTIVE)
    inactive_employees = Employee.objects.filter(status=Employee.STATUS_INACTIVE)
    
    active_people = list(inactive_staff) + list(inactive_employees)
    
    context = {
        'active_people': active_people,
    }
    
    return render(request, 'Admin/inactive_employees.html', context)


   
#Leave Manager approval/Disapproval


@login_required(login_url='/')
def APPROVE_LEAVE(request,id):
    leave=StaffLeave.objects.get(id=id)
    leave.status=1
    leave.save()
    return redirect('all_leave_view')

@login_required(login_url='/')
def REJECT_LEAVE(request,id):
    leave=StaffLeave.objects.get(id=id)
    leave.status=2
    leave.save()
    return redirect("all_leave_view")


#Leave Employee approval/Disapproval


@login_required(login_url='/')
def EMPLOYEE_APPROVE_LEAVE(request,id):
    leave=EmployeeLeave.objects.get(id=id)
    leave.status=1
    leave.save()

    return redirect('all_leave_view')

@login_required(login_url='/')
def EMPLOYEE_REJECT_LEAVE(request,id):
    leave=EmployeeLeave.objects.get(id=id)
    leave.status=2
    leave.save()
    return redirect("all_leave_view")


@login_required(login_url='/')
def ALL_LEAVE_VIEW(request):
    staff_leave = StaffLeave.objects.all()
    employee_leave = EmployeeLeave.objects.all()

    # Combine staff_leave and employee_leave into one list
    all_leaves = list(staff_leave) + list(employee_leave)

    context = {
        'all_leaves': all_leaves,
    }
    return render(request, 'Admin/all_leave.html', context)
