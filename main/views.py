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
            result = f"The sum is: {sum}"
        except:
            error = "Something went wrong"

    return render(request, 'add.html', {'result': result, 'error': error}) 