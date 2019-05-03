
#%%
import pandas as pd


#%%
out = pd.read_excel('./Korunove_dluhopisy_20181231_anonym.xlsx', sheet_name='Table 1', header=None)

#%%
out['rok'] = None
out['rok'] = out[out[1] == 'ČR'][0]
out.rok.fillna(method='ffill', inplace=True)
#%%
out = out[out[1] != 'ČR']
out = out[out[0] != 'A1']
out = out[out[0] != 'FÚ, který případ řeší']

#%%
out.columns = [
'FÚ, který případ řeší',
'Místně příslušný FÚ',
'Místně příslušné ÚzP',
'DIČ',
'Název DS',
'Ready made',
'Analytické prověření',
'Vybrání DS k prověření na dani z příjmů právnických osob',
'Emise dluhopisů',
'Výše nákladových úroků dle ÚZ',
'Úroková sazba v %',
'Suma emise',
'Počet kupujících',
'Rok splatnosti',
'Místní šetření',
'Vydání výzvy k DoDAP',
'Podání DoDAP',
'Změna základu daně celkem DoDAP',
'Změna daňové ztráty celkem DoDAP',
'Změna daně celkem DoDAP',
'Zahájení POP',
'Ukončení POP',
'Zahájení DK',
'Ukončení DK',
'Kontrolní zjištění z dluhopisů',
'Titul kontrolního zjištění',
'Změna základu daně celkem',
'Změna daňové ztráty celkem',
'Změna daně celkem',
'Kontrola následujících zdaňovacích období',
'Další prověřované zdaňovací období',
'Odvolání',
'Výsledek odvolacího řízení',
'Zneužití práva',
'Podání trestního oznámení',
'"Mimořádný opr. prostředek/dozorčí prostředek"',
'Soudní řízení',
'Související úkony/řízení',
'Poznámky',
'rok'
]

#%%
def to_int(val):
    try:
        return int(val.replace(' ', ''))
    except:
        return val


#%%
out['Změna daně celkem DoDAP'] = out['Změna daně celkem DoDAP'].apply(lambda x: to_int(x))


#%%
sranec = 'Podání DoDAP'
out[out[sranec] == 'ANO'].groupby('rok')[sranec].value_counts()

#%%
out['Kontrolní zjištění z dluhopisů'].value_counts().to_clipboard()

#%%
out['Změna základu daně celkem DoDAP'].value_counts().to_clipboard()

#%%
out.groupby('rok')['Vybrání DS k prověření na dani z příjmů právnických osob'].value_counts().to_clipboard()