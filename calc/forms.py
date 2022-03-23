from django import forms

class SelectForm(forms.Form):
    
    item_option = (
        ('', ''),
        ('Good', 'Good'),
        ('Service', 'Service')   
    ) 
    item_selection = forms.CharField(widget=forms.Select(choices=item_option), label = 'Item Selection')

    supplier_option = (
        ('', ''),
        ('Local', 'Local'),
        ('Foreign', 'Foreign')   
    ) 
    supplier_selection = forms.CharField(widget=forms.Select(choices=supplier_option), label = 'Supplier Location')

    

class CalcForm(forms.Form):
    cost_value = forms.CharField()
 
    wht_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    wht_included = forms.CharField(widget=forms.Select(choices=wht_option), label = 'Is WHT included in amount')

    vatable_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    vatable_selection = forms.CharField(widget=forms.Select(choices=vatable_option),label = 'VATable Selection')

    vatreg_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    vatreg_selection = forms.CharField(widget=forms.Select(choices=vatreg_option), label = 'VATreg Selection')




class ForeignServiceForm(forms.Form):
    cost_value = forms.CharField()
 

    supplier_country_option = (
        ('', ''),
        ('Denmark', 'Denmark'),
        ('India', 'India') ,
        ('Italy', 'Italy'),
        ('Mauritius', 'Mauritius'),  
        ('Netherlands', 'Netherlands'),
        ('Norway', 'Norway') ,
        ('South Africa', 'South Africa'),
        ('Other', 'Other'),   
    ) 
    supplier_country = forms.CharField(widget=forms.Select(choices=supplier_country_option), label = 'Supplier Country')

    wht_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    wht_included = forms.CharField(widget=forms.Select(choices=wht_option), label = 'Is WHT included in amount')

   
    



'''
class CalcForm(forms.Form):
    cost_value = forms.CharField()

    item_option = (
        ('', ''),
        ('Good', 'Good'),
        ('Service', 'Service')   
    ) 
    item_selection = forms.CharField(widget=forms.Select(choices=item_option), label = 'Item Selection')

    
    supplier_option = (
        ('', ''),
        ('Local', 'Local'),
        ('Foreign', 'Foreign')   
    ) 
    supplier_selection = forms.CharField(widget=forms.Select(choices=supplier_option), label = 'Supplier Selection')

    wht_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    wht_included = forms.CharField(widget=forms.Select(choices=wht_option), label = 'WHT Selection')

    vatable_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    vatable_selection = forms.CharField(widget=forms.Select(choices=vatable_option),label = 'VATable Selection')

    vatreg_option = (
        ('', ''),
        ('Yes', 'Yes'),
        ('No', 'No')   
    ) 
    vatreg_selection = forms.CharField(widget=forms.Select(choices=vatreg_option), label = 'VATreg Selection')
'''
   
    
    
