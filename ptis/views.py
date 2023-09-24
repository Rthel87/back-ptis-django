from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from .models import WorkingDay

# Create your views here.
class ListWorkingDays(APIView):
    """
    View to list all working days on de sistem
    Don't work
    """
    permission_classes = [permissions.AllowAny]

    def get(self, format=None):
        workingdays = WorkingDay.objects.filter(borrado=False)
        return Response(workingdays)


@api_view(['GET'])
def index(request):
    # Work
    workingdays = WorkingDay.objects.filter(borrado=False)
    return Response(workingdays)
