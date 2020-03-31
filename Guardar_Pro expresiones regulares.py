import re

def Comprobar(Dato):
     if re.match('^([A-Z]{1})([0-9]{3})([a-z]{3})([-!$%^&*()_+|~=`{}\[\]:";<>?,.\/]{3})$',Dato):
         print("El Dato Si Cumple Con La Condiccion")
     else:
        print("El Dato No Cumple Con La Condiccion");
   

Dato = input("INGRESE EL CODIGO QUE DESEE COMPROBAR : ");  
Comprobar(Dato);