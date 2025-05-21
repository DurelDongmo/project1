age = 30
taille= 174
print('bonjour jai',age, 'je fais', taille, "cm",'et je fais mes debuts sur python')
a= 3 
b= -5
c= a+b
if c>0: 
    print("c est postif") 
elif c==0:
     print("c est  nul")
else:
     print("c est negatif") 
age= int(input("quel est ton age?")) 
if age>= 18:
     print('majeur')
else:
     print('mineur')
T=int(input("Total amount of daily purchases"))
if T> 1500:
     print("over")
elif T== 1500:
     print("averae acceptable")
else:
     print("normal")
N=int(input("entre la note des eleves(entre 0 et 20):"))
if 0<=N<=9:
     print("ECHEC")
elif 10<=N<=11:
     print("PASSALE")
elif 12<=N<=13:
     print("ASSEZ BIEN")
elif 14<=N<=15:
     print("BIEN")
elif 16<=N<=17:
     print("TRES BIEN")
elif 18<=N<=20:
     print("EXCELLENT")
else:
     print("INVALIDE")
Annee =int(input('veuillez entrer une annee(en chiffre) pour verication:'))
if (Annee % 4 == 0 and Annee % 100!= 0 ) or (Annee % 400 == 0 ):
     print("ANNEE BISEXTILLE")
else:
     print("NON BISEXTILLE")
Age = int(input("How old are you(an integer)?:"))
Statut= int(input("what is your current statut(student or no-student)?:"))
if 12 < Age:
     print("FREE")
elif 12 <= Age <= 17:
     print("7$")
elif Age > 18 and statut == student:
     print("8$")
elif 18 <= age <= 64 and statut == no-student:
     print("12$")
elif Age >= 65:
     print("6$")
else:
     print("invalide")