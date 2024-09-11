from django.shortcuts import render

# Create your views here.
def add_numbers(request):
    result = None
    error = None

    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')

        try:
            sum = float(num1) + float(num2)
            # sum = num1+num2
            result = f"The sum is: {sum}"
        except Exception as e:
            error = f"Something went wrong in boot {e}"

    return render(request, 'add.html', {'result': result, 'error': error}) 

def simple_interest(request):
    result = None
    error = None

    if request.method == "POST":
        p=request.POST.get('p')
        n=request.POST.get('n')
        r=request.POST.get('r')

        try:
            simple=(float(p) * float(n) * float(r))/100
            result = f"The sum is:{simple}"
        except:
            error = "Something went wrong"
    return render(request,'pnr.html',{'result':result,'error':error})

def product(request):
    result = None
    error = None

    if request.method == "POST":
        p=request.POST.get('p')
        n=request.POST.get('n')
        r=request.POST.get('r')

        try:
            simple=(float(p) * float(n) * float(r))
            result = f"The product is:{simple}"
        except:
            error = "Something went wrong"
    return render(request,'mul.html',{'result':result,'error':error})