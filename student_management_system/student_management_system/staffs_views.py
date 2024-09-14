from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from student_management_app.models import StaffLeave,Staff,Employee,EmployeeLeave
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    manager = Staff.objects.get(admin=request.user)

    employees = Employee.objects.filter(departement_id=manager.departement_id, admin__user_type=3)
    
    context = {
        'employees': employees,
        'full_day_leaves_remaining': manager.full_day_leaves_remaining,
        'half_day_leaves_remaining': manager.half_day_leaves_remaining,
    }
    return render(request, 'Staffs/manager_dashboard.html', context)
    

@login_required(login_url='/')
def POLICY(request):
    return render(request,'Admin/policy.html')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    return render(request,"Staffs/apply_leave.html")
        
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
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        names=request.POST.get('names')
        off_email=request.POST.get('off_email')
        from_date=request.POST.get("from_date")
        to_date=request.POST.get("to_date")
        reason=request.POST.get("reason")
        leave_type=request.POST.get('leave_type')
        staff=Staff.objects.get(admin=request.user.id)
        leave=StaffLeave(
            staff_id=staff,
            from_date=from_date,
            to_date=to_date,
            messages=reason,
            leave_type=leave_type,
        )

            
        leave.save()
        messages.success(request,"Leave Successfully Sent")
    return redirect("staff_apply_leave")



@login_required(login_url='/')
def EMPLOYEE_LEAVE_VIEW(request):
    manager = Staff.objects.get(admin=request.user)

    employee_leave=EmployeeLeave.objects.filter(employee_id__departement_id=manager.departement_id)


    
    context = {
        'employee_leave': employee_leave,
    }
    
    return render(request,'Staffs/all_leave.html',context)