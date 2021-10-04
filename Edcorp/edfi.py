import time
import sys
# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def display_style(T):
    for i in T + '':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1. /100)
        
def banner():
    print (G+'''Product of Edson corperations (EDCORP).'''+O+"|")
    print (O+'''_______________________________________|''')
    
    
    display_style(O+'''
   ################################################
   ##            ___   _                         ##
   ##            |_ `__| __ __ __ ___            ##
   ##            |__[__|[__[__]| '|__].          ##
   ##                            _|              ##
   ################################################                            
     ''')   
    
    print (G +'''  .;'                     `;,    ''')
    print (G +''' .;'  ,;'             `;,  `;,   ''')
    print (G +'''.;'  ,;'  ,;'     `;,  `;, `;,  ''')
    print (G +'''::   ::   :  ''' + GR+'''( )'''+G +'''   :    ::  :: ''')  
    print (G +''':.  ':.  ':. ''' + GR + '''/_\\'''+ G+'''  ,:'  ,:  .:''')
    print (G +''':.  ':.    '''+ GR +''' /___\\'''+ G + "    ,:'  ,")
    print (G + "  ':.      " + GR + "/_____\\" + G + "      ,:'")
    print (G + "          " + GR + "/       \\" + G + "        ")
 
banner()  
