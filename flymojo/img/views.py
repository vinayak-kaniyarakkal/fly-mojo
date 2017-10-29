from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from django.http import JsonResponse
from models import Kyc
from models import Moderator
import random
from django.forms import modelform_factory
import json


@csrf_exempt
def get_pan_details(request):
	kyc = Kyc.objects.filter(verified = False, check_count__lt = 4)
	random_num = random.randint(0, kyc.count() - 1)
	kyc = kyc[random_num]
	image = '/media/%s'%kyc.image.url
	return JsonResponse({'response_code':'success','name':kyc.name,'pan_no':kyc.pan_no,'dob':kyc.dob,'image':image,'id':kyc.id})


def get_leaderboard(request):
 	leaders = [{'name' : str(each), 'points' : each.get_points(), 'rank' : rank+1 }
 				for (rank, each) in enumerate(sorted(Moderator.objects.all(), key=lambda m: -m.get_points())[:10])]
	return JsonResponse({'success': True, 'leaders': leaders})


@csrf_exempt
def image_upload(request):
    img = request.FILES.get('image')
    if not img:
        return JsonResponse({'success': False,
                             'detail': 'Image not provided'})
    merchant = request.user.merchant_set.get()
    form_class = modelform_factory(Kyc, fields=[
        'merchant', 'confidence_level', 'verified', 'image'])
    info = {'merchant': merchant.id, 'confidence_level': 0, 'verified' :False}
    form = form_class(info, request.FILES)
    kyc = form.save()
    
    return JsonResponse({'success': True, 'info': {
        'name': kyc.name, 'dob': kyc.dob,
        'pan_no': kyc.pan_no, 'image': kyc.image.url
    }})
