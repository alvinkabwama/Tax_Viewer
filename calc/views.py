from telnetlib import EL
from django.shortcuts import render
from .forms import CalcForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import pandas as pd



# Create your views here.
def calcapi(request):
    if(request.method == 'POST'):

       
        calc_form = CalcForm(request.POST)

        if calc_form.is_valid():
            cost_value = calc_form.cleaned_data.get('cost_value')
            item_selection = calc_form.cleaned_data.get('item_selection')
            supplier_selection = calc_form.cleaned_data.get('supplier_selection')
            wht_included = calc_form.cleaned_data.get('wht_included')
            vatable_selection = calc_form.cleaned_data.get('vatable_selection')
            vatreg_selection = calc_form.cleaned_data.get('vatreg_selection')

            '''
            print(item_selection)
            print(supplier_selection)
            print(wht_included)
            print(vatable_selection)
            print(vatreg_selection)
            '''

            
            cost_float = float(cost_value)

            #CASE FOR WHEN IT IS A GOOD 
            if item_selection == 'Good':

                #CASE FOR LOCAL SUPPLIER
                if supplier_selection == "Local":
 
                    #CASE FOR WHT TAX INCLUDED
                    if wht_included == 'Yes':
                        cost_float = cost_float
                    else:
                        cost_float = cost_float/0.94
                        print(cost_float)

                    
                    #CHECKING IF THE GOOD IS VATABLE SUPPLY
                    if vatable_selection == 'Yes':

                        #CHECK IF SUPLLIER IS ON LIST OF VAT REGISTERED SUPPLIERS
                        if  vatreg_selection == 'Yes':
                             cost_float = cost_float*1.18

                        else:
                            cost_float = cost_float

                    else:
                        cost_float = cost_float


            #CASE FOR WHEN IT IS A SERVICE.
            else:

                print()



        print(cost_float) 
        

        cost_val = str(cost_float)
        context = {
                'calc_form' : calc_form,
                'cost_val' : cost_val,
        }
                            
        print(cost_float)        
        return render(request, 'dataview.html', context)


    else:        
        calc_form = CalcForm()
        
        cost_val = 0
        context = {
                    'calc_form' : calc_form,
                    'cost_val' : cost_val,
                    
        }

        return render(request, 'dataview.html', context)

