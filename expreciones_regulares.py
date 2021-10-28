import subprocess
import optparse
import re 


def get_arguments():

    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="interface para cambiar direccion mac")
    parser.add_option("-m", "--mac", dest="new_mac",help="nueva direccion mac")
    (options,arguments)= parser.parse_args()
    if not options.interface: #si no esta bien escrito 
        parser.error("[-] por favor indicar una interfas --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] por favor indicar una direcion mac --help para mas informacion")
    return options

def change_mac(interface,new_mac):

    print("[+] cambiando la direcion mac " + interface + " este es el nuvo mac " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
 
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] no pudimos leer la direccion mac")

options=get_arguments()
current_mac=get_current_mac(options.interface)
print("current mac= "+str(current_mac))
change_mac(options.interface,options.new_mac)#para correr el porgrama

current_mac=get_current_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] si se hiso el cambio de la mac"+current_mac)
else:
    print("[-] no si se hiso el cambio de la mac"+current_mac)
