from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from datetime import timedelta,datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from student_management_app.models import StaffLeave,Staff,Employee,EmployeeLeave


@login_required(login_url='/')
def HOME(request):
    employee = Employee.objects.get(admin=request.user)
    
    current_month = datetime.now().month
    if current_month == 1:  # If it's January, update the leave balance
        # Add new leave allowances for the year
        new_full_day_leave_allowance = 12
        new_half_day_leave_allowance = 12
        
        # Update remaining leaves by adding the new allowance
        employee.full_day_leaves_remaining += new_full_day_leave_allowance
        employee.half_day_leaves_remaining += new_half_day_leave_allowance
        
        # Update total allowed leaves for display purposes
        #employee.full_day_leaves_remaining = employee.full_day_leaves_remaining
        #employee.full_day_leaves_remaining = employee.half_day_leaves_remaining
        
        # Save the updated leave allowances
        employee.save()
  
   # approved_full_day_leaves = EmployeeLeave.objects.filter(
    #    employee_id=employee, leave_type='full day', status=1  # status=1 means approved
    #).count()
    
    #approved_half_day_leaves = EmployeeLeave.objects.filter(
    #    employee_id=employee, leave_type='half day', status=1  # status=1 means approved
    #).count()
    
    #remaining_full_day_leaves = employee.full_day_leaves_remaining - approved_full_day_leaves
    #remaining_half_day_leaves = employee.half_day_leaves_remaining - approved_half_day_leaves
    approved_leaves = EmployeeLeave.objects.filter(
        employee_id=employee, status=1  # status=1 means approved
    )
    total_approved_full_day_leaves = 0
    total_approved_half_day_leaves = 0
    
    # Loop through approved leaves and calculate the difference between from_date and to_date
    for leave in approved_leaves:
        leave_days = (leave.to_date - leave.from_date).days + 1  # Include the to_date
        
        # Check if the leave is full day or half day and subtract accordingly
        if leave.leave_type == 'full day':
            total_approved_full_day_leaves += leave_days
        elif leave.leave_type == 'half day':
            total_approved_half_day_leaves += leave_days
    remaining_full_day_leaves = employee.full_day_leaves_remaining - total_approved_full_day_leaves
    remaining_half_day_leaves = employee.half_day_leaves_remaining - total_approved_half_day_leaves
    
    context = {
        'Total_full_day_leave': employee.full_day_leaves_remaining,
        'total_half_day_leave': employee.half_day_leaves_remaining,
        'remiaing_full_day_leave':remaining_full_day_leaves,
        'remaining_half_day_leave':remaining_half_day_leaves
    }
    
    
    return render(request,"employee/employee_dashboard.html",context)

@login_required(login_url='/')
def POLICY(request):
    return render(request,'Admin/policy.html')



@login_required(login_url='/')
def EMPLOYEE_LEAVE(request):
    return render(request,"employee/apply_leave.html")

@login_required(login_url='/')
def EMPLOYEE_LEAVE_SAVE(request):
    if request.method == 'POST':
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        leave_type=request.POST.get('leave_type')
        reason=request.POST.get("reason")
        employee=Employee.objects.get(admin=request.user.id)
        employee_leave=EmployeeLeave(
            employee_id=employee,
            from_date=from_date,
            to_date=to_date,
            messages=reason,
            leave_type=leave_type
        )
        employee_leave.save()
        messages.success(request,'Leave Successfully Sent')
    return redirect('employee_leave')

@login_required(login_url='/')      
def STAFF_LEAVE_HISTORY(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
        staff_leave_history=StaffLeave.objects.filter(staff_id=staff_id)
    context={
            'staff_leave_history':staff_leave_history
        }
    return render(request,"Staffs/leave_history.html",context)

@login_required(login_url='/')      
def EMPLOYEE_LEAVE_HISTORY(request):
    employee=Employee.objects.filter(admin=request.user.id)
    for i in employee:
        employee_id=i.id
        employee_leave_history=EmployeeLeave.objects.filter(employee_id=employee_id)
        context={
            'employee_leave_history':employee_leave_history
        }
    return render(request,"employee/leave_history.html",context)
