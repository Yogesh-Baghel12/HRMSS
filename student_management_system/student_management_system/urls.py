"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,admin_views,employee_views,staffs_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('ADMIN/policy',admin_views.POLICY,name='policy'),
    #login Path
    path('',views.LOGIN,name='login'),
    path('dologin',views.dologin,name='dologin'),
    path('dologout',views.doLogout,name='logout'),
    #Profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),
    #Admin pannel
    path('ADMIN/HOME',admin_views.HOME,name="home"),
    path('ADMIN/Employee/Add',admin_views.ADD_EMPLOYEE,name='add_employee'),
    path('ADMIN/Employee/View',admin_views.VIEW_EMPLOYEE,name='view_employee'),
    path('ADMIN/Employee/Edit/<str:id>',admin_views.EDIT_EMPLOYEE,name='edit_employee'),
    path('ADMIN/Employee/Update',admin_views.UPDATE_EMPLOYEE,name='update_employee'),
    path('ADMIN/Employee/active',admin_views.active_staff_and_employees,name='active_employee'),
    path('ADMIN/Employee/inactive',admin_views.inactive_staff_and_employees,name='inactive_employee'),
    path('ADMIN/Employee/all',admin_views.all_employees,name='all_employees'),
    path('ADMIN/Department/all',admin_views.ALL_DEPARTMENT,name='all_department'),
    
    path('Admin/Manager/Add',admin_views.ADD_MANAGER,name='add_manager'),
    path('Admin/Manager/view',admin_views.VIEW_MANAGER,name='view_manager'),
    path('ADMIN/Manager/Edit<str:id>',admin_views.EDIT_MANAGER,name='edit_manager'),
    path('ADMIN/Manager/Update',admin_views.UPDATE_MANAGER,name='update_manager'),
    
    path('ADMIN/Department/Add',admin_views.ADD_DEPARTMENT,name='add_department'),
    path('ADMIN/Department/View',admin_views.VIEW_DEPARTMENT,name='view_department'),
    path('ADMIN/Department/Edit/<str:id>',admin_views.EDIT_DEPARTMENT,name='edit_department'),
    path('ADMIN/Department/Update',admin_views.UPDATE_DEPARTMENT,name='update_department'),
    #path('Admin/Manager/Leave_view',admin_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('Admin/Manager/approve_leave/<str:id>',admin_views.APPROVE_LEAVE,name='approve_leave'),
    path('Admin/Manager/reject_leave/<str:id>',admin_views.REJECT_LEAVE,name='reject_leave'),
    path('Admin/Employee/approve_leave/<str:id>',admin_views.EMPLOYEE_APPROVE_LEAVE,name='employee_approve_leave'),
    path('Admin/Employee/reject_leave/<str:id>',admin_views.EMPLOYEE_REJECT_LEAVE,name='employee_reject_leave'),
    path('Admin/Manager/Leave_view',admin_views.ALL_LEAVE_VIEW,name='all_leave_view'),
    
    # Manager urls
    path('Manager/Home',staffs_views.HOME,name='manager_home'),
    path('Manager/Apply_leave',staffs_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Manager/Leave_history',staffs_views.STAFF_LEAVE_HISTORY,name="staff_leave_history"),
    path("Manager/Aplly_leave_save",staffs_views.STAFF_APPLY_LEAVE_SAVE,name="staff_apply_leave_save"),
    
    path('Manager/policy',staffs_views.POLICY,name='st_policy'),
    path('Manager/Employee/Leave_view',staffs_views.EMPLOYEE_LEAVE_VIEW,name='employee_leave_view'),

    #Employee Urls
    path('Employee/Home',employee_views.HOME,name='Employee_home'),
    path('Employee/policy',employee_views.POLICY,name='em_policy'),
    path('Employee/apply_leave',employee_views.EMPLOYEE_LEAVE,name='employee_leave'),
    path('Employee/Leave_save',employee_views.EMPLOYEE_LEAVE_SAVE,name='employee_leave_save'),
    path('Employee/Leave_history',employee_views.EMPLOYEE_LEAVE_HISTORY,name="employee_leave_history"),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
