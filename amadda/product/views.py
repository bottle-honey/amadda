from django.shortcuts import render,redirect
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from .serializer import ProductSerializer
from .forms import ProductForm
# Create your views here.
# api_view(['GET'])
class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

# product 등록
def Product_post(request):
    if request.method == "POST":
    #폼에서 데이터를 받아와 변수화시키기
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'product_list.html', {
                'form' : form,
            })
        # img = request.FILES["product_imgloc"]
    else:
        form = ProductForm()
    return render(request, 'product_list.html')
    #     # 정보를 파일에 저장하기
    #     img_upload = Product(
    #         product_imgloc = img
    #     )
    #     img_upload.save()
 
    # 변수_테이블의모든정보 = models.테이블.objects.all()
 
    # return render(request, "앱이름2/결과.html", context = {
    #     "키_테이블의모든정보": 변수_테이블의모든정보
    # })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products' : products})
def product_add(request):
    return render(request, 'product_add.html')