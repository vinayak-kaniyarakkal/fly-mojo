from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from django.http import JsonResponse
from models import Kyc
import random
@csrf_exempt
# Create your views here.
def get_pan_details(request):

	kyc = Kyc.objects.filter(verified = False, check_count__lt = 4)
	random_num = random.randint(0, kyc.count() - 1)
	kyc = kyc[random_num]
	image = '/media/%s'%kyc.image.url
	return JsonResponse({'response_code':'success','name':kyc.name,'pan_no':kyc.pan_no,'dob':kyc.dob,'image':image,'id':kyc.id})