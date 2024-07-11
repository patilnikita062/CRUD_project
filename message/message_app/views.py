from django.shortcuts import render,HttpResponse,redirect
# from message_app.models import Msg
from .models import Msg

def create(request):
    if request.method=='POST': 
        # print('method mode:',request.method)
        # print('print from frontend data into backend:',n)
        
        n= request.POST['uname']
        mail=request.POST['uemail']
        num=request.POST['mobile']
        message=request.POST['msg']
        # obj_name = model_name.objects.create(col1=val1,col2=val2,....)
        m=Msg.objects.create(name=n,email=mail,mobile=num,msg=message)
        m.save()
        # return HttpResponse('Insert data into database table')
        return redirect('/') 

    else: #default method GET run first and then after submiting button POST activate
        print('method mode:',request.method)
        return render(request,'create.html')
    
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    # return HttpResponse('<h1>data Fetched from database</h>')

def delete(request,rid):
    print('Id to be deleted:',rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/')

    # return HttpResponse('Id to be deleted:'+rid)

def edit(request,rid):
    if request.method=='POST':
        n= request.POST['uname']
        mail=request.POST['uemail']
        num=request.POST['mobile']
        message=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=num,msg=message)
        return redirect('/') 
    else:
        #display form with old values
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)

