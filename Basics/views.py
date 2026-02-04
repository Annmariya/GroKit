from django.shortcuts import render

def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        result=num1+num2
        return render(request,"Basics/Sum.html",{'sum':result})
    else:
        return render(request,"Basics/Sum.html")


def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        btn= request.POST.get("btn_submit")
        if btn =="+":
            result=num1+num2
        elif btn =="-":
            result=num1-num2
        elif btn =="*":
            result=num1*num2
        elif btn =="/":
            result=num1/num2
        return render(request,"Basics/Calculator.html",{'result':result})
    else:
        return render(request,"Basics/Calculator.html")
    
def Largest(request):
    if request.method =="POST":
        num1=int(request.POST.get("txt_n1"))
        num2=int(request.POST.get("txt_n2"))
        largest= max(num1,num2)
        smallest= min(num1,num2)
        return render(request,"Basics/Largest.html",{'largest':largest,'smallest':smallest})
    else:
         return render(request,"Basics/Largest.html")