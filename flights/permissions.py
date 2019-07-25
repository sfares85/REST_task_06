from rest_framework.permissions import BasePermission
from datetime import date

class IsOwner(BasePermission):
	message = " you are not authorized to access this page."

	def has_object_permission(self,request,view,obj):
		if request.user == obj.user or request.user.is_staff:
			return True
		else:
			return False

class PastDate(BasePermission):
	message = "this booking is past modifcation period."

	def has_object_permission(self,request,view,obj):
		if  (obj.date - date.today()).days < 3:
			return False
		else:
			return True