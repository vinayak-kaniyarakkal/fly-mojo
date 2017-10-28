from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from django.http import JsonResponse
from models import Kyc
@csrf_exempt
# Create your views here.
def get_pan_details(request):
	kyc = Kyc.objects.get()
	print kyc
	response = {'responseCode':'responseCode'}
	return JsonResponse(response)