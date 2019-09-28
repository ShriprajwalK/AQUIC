from django.shortcuts import render
from django.http import HttpResponse as hr
from .models import Value
from django.views.decorators.csrf import csrf_exempt
import pyrebase

config = {
  "apiKey": "AIzaSyBvMbaT6pHO-G8fSP_fb4hgaUOrO0vtc_4",
  "authDomain": "qpac-f4fc5.firebaseapp.com",
  "databaseURL": "https://aqpac-f4fc5.firebaseio.com",
  "storageBucket": "qpac-f4fc5.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


# Create your views here.

def value_list(request):
    val_of_node1= Value.objects.filter(id_no=1).order_by('date_time')
    for val in val_of_node1:
        if val.check==0:
            data_of_1 = {"temperature": val.temp,
                        "humidity": val.humidity,
                        "lpg": val.lpg,
                        "propane": val.propane,
                        "carbon_monoxide": val.carbon_monoxide,
                        "carbon_dioxide": val.carbon_dioxide,
                        "ammonia": val.ammonia,
                        "methane": val.methane,
                        "alcohol": val.alcohol,
                        "smoke": val.smoke,
                        "dust": val.dust
                    }
    db.child("node1").push(data_of_1)

    return render(request, 'display/index.html', {'val1':val_of_node1})


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post(request):
    if(request.method=='POST'):
        b=request.body
        print(b)
    return hr(100)
