from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Invoice,PurchaseOrder
from datetime import datetime
from .forms import MyForm
from itertools import chain

# Create your views here.

def uploadPO(request):
    return render(request,'filemanager/home.html')

def upload_view(request):
    return render(request, 'filemanager/upload.html')

def dashboard_view(request):
    items = PurchaseOrder.objects.all()
    form = MyForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            selected_value = form.cleaned_data['dropdown_field']
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            # Process the selected value as needed
            # ...
            type = "850"
            view_type = "Invoices"
            items = []
            show = True

            

            if selected_value=='850':
                items = PurchaseOrder.objects.all()
                if start_date and end_date:
                    # Convert date strings to datetime objects
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')

                    # Filter entries based on the date range
                    items = PurchaseOrder.objects.filter(date__range=(start_date, end_date))

                type = "Total Purchase Orders : " + str(len(items))
            elif selected_value=='810':
                items = Invoice.objects.all()
                view_type = "Purchase orders"
                if start_date and end_date:
                    # Convert date strings to datetime objects
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')

                    # Filter entries based on the date range
                    items = PurchaseOrder.objects.filter(date__range=(start_date, end_date))

                type = "Total Invoices : " + str(len(items))
            elif selected_value=='All':
                item0 = PurchaseOrder.objects.all()
                item1 = Invoice.objects.all()
                items = list(chain(item0, item1))
                show = False
                if start_date and end_date:
                    # Convert date strings to datetime objects
                    start_date = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date = datetime.strptime(end_date, '%Y-%m-%d')

                    # Filter entries based on the date range
                    items = PurchaseOrder.objects.filter(date__range=(start_date, end_date))

                type = "Total EDI files : " + str(len(items))

            if start_date and end_date:
                print(start_date,end_date)
            else:
                print('None')


            return render(request, 'filemanager/dashboard.html', {'show':show,'items': items, 'form': form,'type':type,'view_type':view_type})

    return render(request, 'filemanager/dashboard.html', {'items': items, 'form': form})


def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        
        # Perform file operations
        if myfile:
            # Access file properties
            sender = ''
            receiver = ''
            pNo = 0
            date = ''

            line_no = 0

            isa_date = None

            for line in myfile:
                line_text = line.decode('utf-8').strip() 
                arr = line_text.split('*')
                print(arr)
                if line_no==0:
                    sender = arr[6]
                    receiver = arr[8]
                    date = arr[9]
                    isa_date = datetime.strptime(date, "%y%m%d").date()
                elif line_no==3:
                    pNo = int(arr[5][0:len(arr[5])-1])
                line_no+=1
            
            order = PurchaseOrder(sender,receiver,pNo,isa_date)

            print(order)

            order.save()
            
            # Return a response or redirect as needed
            return HttpResponse('Success')
    
    return HttpResponse('Failure')

def upload_invoice(request):
    if request.method == 'POST':
        print(request.FILES)  # Print request.FILES dictionary
        
        myfile = request.FILES.get('myfile-invoice')
        
        if myfile:
            # Access file properties
            sender = ''
            receiver = ''
            pNo = 0
            date = ''

            line_no = 0

            isa_date = None

            for line in myfile:
                line_text = line.decode('utf-8').strip() 
                arr = line_text.split('*')
                print(arr)
                if line_no==0:
                    sender = arr[6]
                    receiver = arr[8]
                    date = arr[9]
                    isa_date = datetime.strptime(date, "%y%m%d").date()
                elif line_no==3:
                    pNo = int(arr[5][0:len(arr[5])-1])
                line_no+=1
            
            order = Invoice(sender,receiver,pNo,isa_date)

            print(order)

            order.save()
            
            return HttpResponse('Success Invoice')
    
    return HttpResponse('Failure Invoice')


def show_entries(request):

    if request.method=='POST':
        purchase_order_no = request.POST.get('purchase_order_id')
        type = request.POST.get('type')
        items = None
        if type=='850':
            items = Invoice.objects.filter(purchaseOrderNumber=purchase_order_no)
        elif type=='810':
            items = PurchaseOrder.objects.filter(purchaseOrderNumber=purchase_order_no)
        
        print(items)
        return render(request, 'filemanager/show_entries.html',{'items':items})
    
    return HttpResponse('Failed')
