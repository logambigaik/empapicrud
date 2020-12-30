# it provides #Loclhost:port/api
from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)


##Loclhost:port/api
# GET , POST , PUT, DELETE
# list -loclhost:port/api/employee
# retrieve -loclhost:port/api/employee/5