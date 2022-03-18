from django import forms

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

   
    
    
