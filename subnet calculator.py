def bekér():
    ip_cím_subnet = input("Add meg az íp címet (192.168.1.12/24)\n->")
    hossz = len(ip_cím_subnet)
    subnet_szám = ip_cím_subnet[hossz -2:]
    ip_cím = ip_cím_subnet[:hossz -3]
    ip_cím = ip_cím.split(".")
    return subnet_szám, ip_cím

def net_mask_convert(subnet_szám):
    f = open("txt/subnet.txt", "r", encoding="utf-8")
    subnet_list = []
    for adat in f:
        subnet_list.append(adat.replace("\n", "").strip().split())
    subnet_address = ""
    f.close()
    for i in range(len(subnet_list)):
        if subnet_list[i][0] == subnet_szám:
            subnet_address = subnet_list[i][1]
    subnet_address = subnet_address.split(".")
    return subnet_address
            

def binary_converter(szám):
    f = open("txt/binary.txt", "r", encoding="utf-8")
    binary_list = []
    for adat in f:
        binary_list.append(adat.replace("\n", "").strip().split())
    f.close()
    binary = []
    for i in range(len(szám)):
        érték = szám[i]
        érték = int(érték)
        binary.append(binary_list[érték])
    return binary

def vonal_keres(subnet_binary):
    for i in range(len(subnet_binary)):
        if subnet_binary[i] != ['11111111']:
            ahol_a_vonal_van = i
            break
    return ahol_a_vonal_van

def eszköz_db(subnet_binary):
    kettő_négyzeten = 0
    for i in range(len(subnet_binary)):
        for j in range(len(subnet_binary[i][0])):
            if subnet_binary[i][0][j] == "0":
                kettő_négyzeten += 1
    alap = 2
    eredmény = alap ** kettő_négyzeten
    return eredmény -2

def és_kapcsolat(subnet_binary, ahol_a_vonal_van, ip_binary):
    f = open("txt/binary.txt", "r", encoding="utf-8")
    binary_list = []
    for adat in f:
        binary_list.append(adat.replace("\n", "").strip().split())
    f.close()
    network_address = []
    for i in range(len(subnet_binary[ahol_a_vonal_van])):
        for j in range(8):
            if subnet_binary[ahol_a_vonal_van][i][j] == "1" and subnet_binary[ahol_a_vonal_van][i][j] == ip_binary[ahol_a_vonal_van][i][j]:
                network_address.append("1")
            else:
                network_address.append("0")
    network_address = (f"{network_address[0]}{network_address[1]}{network_address[2]}{network_address[3]}{network_address[4]}{network_address[5]}{network_address[6]}{network_address[7]}")
    for i in range(len(binary_list)):
        if binary_list[i] == [network_address]:
            networ_address_dec = i
    return networ_address_dec

def last_host(ahol_a_vonal_van, ip_cím_binary, subnet_binary):
    számon_belüli_vonal = 0
    for i in range(len(subnet_binary[ahol_a_vonal_van][0])):
        if subnet_binary[ahol_a_vonal_van][0][i] == "0":
            számon_belüli_vonal = i
    szám_eleje = ip_cím_binary[ahol_a_vonal_van][0][:számon_belüli_vonal]
    szám_vége = ip_cím_binary[ahol_a_vonal_van][0][számon_belüli_vonal:]
            
def kiír(ip_cím_dec, subnet_address, subnet_binary, ip_cím_binary, eszköz_db_szám, ahol_a_vonal_van, network_address_dec, ip_cím):
    if ahol_a_vonal_van == 3:
        network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec}")
        first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec+1}")

    if ahol_a_vonal_van == 2:
        network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec}.0")
        first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec}.1")

    if ahol_a_vonal_van == 1:
        network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec}.0.0")
        first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{network_address_dec}.0.1")
        

    network_address_változatott = network_address_változatott.replace("[", "").replace("]", "").replace("'", "").replace(",", ".").replace(" ", "")
    first_ip_address = first_ip_address.replace("[", "").replace("]", "").replace("'", "").replace(",", ".").replace(" ", "")


    print(f"\nip cím: {ip_cím_dec}")
    print(f"subnet: {subnet_address}")
    print("----------------------")
    print(f"ip cím bináris: {ip_cím_binary}")
    print(f"subnet bináris: {subnet_binary}")
    print("----------------------")
    print(f"A hálózatra csatlakoztatható eszközök száma: {eszköz_db_szám}")
    print(f"Network address: {network_address_változatott}")
    print(f"First ip address: {first_ip_address}")


def main():
    subnet_szám, ip_cím_dec = bekér()
    subnet_address = net_mask_convert(subnet_szám)
    ip_cím_binary = binary_converter(ip_cím_dec)
    subnet_binary = binary_converter(subnet_address)
    ahol_a_vonal_van = vonal_keres(subnet_binary)
    eszköz_db_szám = eszköz_db(subnet_binary)
    network_address_dec = és_kapcsolat(subnet_binary, ahol_a_vonal_van, ip_cím_binary)
    last_host(ahol_a_vonal_van, ip_cím_binary, subnet_binary)
    kiír(ip_cím_dec, subnet_address, subnet_binary, ip_cím_binary, eszköz_db_szám, ahol_a_vonal_van, network_address_dec, ip_cím_dec)
    

    

main()
