from telnetlib import EL
from django.shortcuts import redirect, render

from Tax_viewer.settings import RESOURCES
from .forms import CalcForm, SelectForm, ForeignServiceForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import pandas as pd





# Create your views here.

#VIEW FOR SELECTING THE SERVICE TYPE
def calcapi(request):
    if(request.method == 'POST'):

       
        select_form = SelectForm(request.POST)

        if select_form.is_valid():
            item_selection = select_form.cleaned_data.get('item_selection')
            supplier_selection = select_form.cleaned_data.get('supplier_selection')
            
            #LOCAL SELECTION
            if supplier_selection == 'Local':
                
                response = redirect(local)
                return response
  
            #FOREIGN  SELECTION
            else:
                #GO TO FOREIGN SERVICE CALCULATION
                if item_selection == 'Service':
                    response = redirect(foreignservice)
                    return response
                else:
                    return render(request, 'foreign_goods.html')

    else:      
        select_form = SelectForm()
        
        context = {
                    'calc_form' : select_form,
                    
        }
        #return render(request, 'selection_view.html', context)
        return render(request, 'selection_view.html', context)


#VIEW FOR THE LOCAL SERVICES AND GOODS
def local(request):
    if(request.method == 'POST'):

        #FORM FOR CAPTURING THE DATA
        calc_form = CalcForm(request.POST)

        if calc_form.is_valid():
            cost_value = calc_form.cleaned_data.get('cost_value')
            wht_included = calc_form.cleaned_data.get('wht_included')
            vatable_selection = calc_form.cleaned_data.get('vatable_selection')
            vatreg_selection = calc_form.cleaned_data.get('vatreg_selection')

            #print(supplier_country)
            #print(wht_included)
            #print(vatable_selection)
            #print(vatreg_selection)
            
            cost_float = float(cost_value)


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


        print(cost_float) 
        cost_val = str(round(cost_float,2))
        context = {
                'calc_form' : calc_form,
                'cost_val' : cost_val,
        }
                            
        print(cost_float)        
        return render(request, 'data_view.html', context)


    else:        
        calc_form = CalcForm()
        
        cost_val = 0
        context = {
                    'calc_form' : calc_form,
                    'cost_val' : cost_val,
                    
        }

        return render(request, 'data_view.html', context)


#VIEW FOR THE SERVICES
def foreignservice(request):
    if(request.method == 'POST'):

        #FORM FOR CAPTURING THE DATA
        calc_form = ForeignServiceForm(request.POST)

        if calc_form.is_valid():
            cost_value = calc_form.cleaned_data.get('cost_value')
            supplier_country = calc_form.cleaned_data.get('supplier_country')
            wht_included = calc_form.cleaned_data.get('wht_included')
            
            
            cost_float = float(cost_value)
        
            #CASE FOR WHT TAX INCLUDED
            if wht_included == 'Yes':
                cost_float = cost_float

            #WHEN WITHHOLDING TAX IS NOT INCLUDED AND HAS TO BE CALCULATED BY COUNTRY
            else:
                #THESE ARE FOR COUNTRIES WHERE WHT IS 10 PERCENT
                if supplier_country == 'Other':

                    cost_float = cost_float/0.85
                #FOR COUNTRIES WHERE WITHHOLDINH TAX IS 15 PERCENT
                else:
                    cost_float = cost_float/0.9

                #READING THE DIFFERENT COUNTRY WITHHOLDING TAX DATA

                '''
                resource_path = os.path.join(RESOURCES, 'WHT_rates.xlsx')
                wht_df = pd.read_excel(resource_path)
                
                country_list = list(wht_df['All Countries'])
                percentage_list = list(wht_df['Percentage'])
                
                country_index = country_list.index(supplier_country)
                target_percentage = percentage_list[country_index]
        
                cost_float = cost_float/(1 - target_percentage)
                '''

                print(cost_float)
  
            #VAT CALCULATION
            cost_float = cost_float*1.18
              
            #return render(request, 'goods_foreign.html')

            print()

        print(cost_float) 
        cost_val = str(round(cost_float,2))
        context = {
                'calc_form' : calc_form,
                'cost_val' : cost_val,
        }
                            
        print(cost_float)        
        return render(request, 'data_view.html', context)


    else:        
        calc_form = ForeignServiceForm()
        
        cost_val = 0
        context = {
                    'calc_form' : calc_form,
                    'cost_val' : cost_val,
                    
        }

        return render(request, 'data_view.html', context)






'''
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

            
            print(item_selection)
            print(supplier_selection)
            print(wht_included)
            print(vatable_selection)
            print(vatreg_selection)
            
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


                #WHEN THE SUPPLIER OF THE GOOD IS A FOREIGN
                else:
                    return render(request, 'goods_foreign.html')

                    print()





            #CASE FOR WHEN IT IS A SERVICE.
            else:

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

                #CASE FOR WHEN THE SERVICE IS FOREIGN
                else:

                    if wht_included == 'Yes':
                        cost_float = cost_float

                    #HERE WE LOOK AT THE COUNTRIES WITH THE DIFFERENT WHT VALUES
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









                    return render(request, 'service_foreign.html')

                    
                

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

'''