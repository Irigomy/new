from django.shortcuts import render

# Create your views here.


def post_list(request):
        return render(request, 'webs/index.html', {})
def katalog(request):
        return render(request, 'webs/katalog.html', {})
def kontak(request):
            return render(request, 'webs/kontak.html', {})
def pembayaran(request):
        return render(request, 'webs/pembayaran.html',{})
def showrooms(request):
        return render(request, 'webs/showrooms.html', {})
def product1(request):
        return render(request, 'webs/product1.html' ,{})
def product2(request):
        return render(request, 'webs/product2.html' ,{})
def product3(request):
        return render(request, 'webs/product3.html' ,{})
def product4(request):
        return render(request, 'webs/product4.html' ,{})
def product5(request):
        return render(request, 'webs/product5.html' ,{})
def product6(request):
        return render(request, 'webs/product6.html' ,{})
def product7(request):
        return render(request, 'webs/product7.html' ,{})
def product8(request):
        return render(request, 'webs/product8.html' ,{})
def product9(request):
        return render(request, 'webs/product9.html' ,{})
def product10(request):
        return render(request, 'webs/product10.html' ,{})
def product11(request):
        return render(request, 'webs/product11.html' ,{})
def about(request):
            return render(request, 'webs/about.html' ,{})

