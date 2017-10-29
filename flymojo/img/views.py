from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from django.http import JsonResponse
from models import Kyc
from django.forms import modelform_factory


@csrf_exempt
# Create your views here.
def get_pan_details(request):
    kyc = Kyc.objects.get()
    print kyc
    response = {'responseCode':'responseCode'}
    return JsonResponse(response)


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
        'pan_no': kyc.pan_no, 'image': '/media/%s' % kyc.image.url
    }})
