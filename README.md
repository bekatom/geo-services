geo-services
============

RS(შემოსავლების სამსახურის) &amp; NBG(ეროვნული ბანკის) სერვისების კლიენტი პითონზე


ვაყენებთ suds
```python
pip install suds
```

გამოყენება django-ს მაგალითზე 
```python
from django.shortcuts import HttpResponse
from geo_services.rs import RS
from ge_services.nbg import NBG
import json

def get_company_info(request):
    rs = RS(request.GET['identification']) # კომპანიის იდენტიფიკატორი
    return HttpResponse(json.dumps(rs.get_company_rs_info()),
                        content_type="application/json")
                        
                        
def get_currency_info(request):
   nbg = NBG(request.GET['curr']) # კურსის აბრევიატურა მაგ : USD , RUB
   return HttpResponse(json.dumps(nbg.get_currency_nbg()), content_type="application/json")

```


