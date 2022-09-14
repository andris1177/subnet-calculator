def dec_to_bin(number, binary):
    return_binary = []
    for i in range(len(number)):
        szám = number[i]
        szám = int(szám)
        return_binary.append(binary[szám])
    return return_binary


#változók
ahol_a_vonal_van = 0
networ_address = []
network_address_változatott = ""
first_ip_address = ""


#1-től 255-ig számok binárisan beolvasása és számmá alakítása
f = open("binary.txt", "r", encoding = "utf-8")
binaryk = []
for adat in f:
    binaryk.append(adat.strip().split())


# adatok bekérése
ip_cím = input("Add meg az ip címet\n->")
hálózati_cím = input("Add meg a hálózati maszkot\n->")

#listává alakítás és pontok levétele
hálózati_cím = hálózati_cím.split(".")
ip_cím = ip_cím.split(".")

#a subnet és ip binaryssá alakítása
subnet_binary =  dec_to_bin(hálózati_cím, binaryk)
ip_binary = dec_to_bin(ip_cím, binaryk)

#megnézni mettől oszthatók ki a címek
for i in range(len(subnet_binary)):
    if subnet_binary[i] != ['11111111']:
        ahol_a_vonal_van = i
        break

print(subnet_binary)
print(ip_binary)

#a vonalba beleső ip cím szegmens

for i in range(len(subnet_binary[ahol_a_vonal_van])):
    for j in range(8):
        if subnet_binary[ahol_a_vonal_van][i][j] == "1" and subnet_binary[ahol_a_vonal_van][i][j] == ip_binary[ahol_a_vonal_van][i][j]:
            networ_address.append("1")
        else:
            networ_address.append("0")

#a csatlakozatatható eszközök száma
kettő_négyzeten = 0
for i in range(len(subnet_binary)):
    for j in range(len(subnet_binary[i][0])):
        if subnet_binary[i][0][j] == "0":
            kettő_négyzeten += 1

networ_address_egyben = (f"{networ_address[0]}{networ_address[1]}{networ_address[2]}{networ_address[3]}{networ_address[4]}{networ_address[5]}{networ_address[6]}{networ_address[7]}")

for i in range(len(binaryk)):
    if binaryk[i] == [networ_address_egyben]:
        networ_address_egyben = i


if ahol_a_vonal_van == 3:
    network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address_egyben}")
    first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address+1}")

if ahol_a_vonal_van == 2:
    network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address_egyben}.0")
    first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address}.1")

if ahol_a_vonal_van == 1:
    network_address_változatott = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address_egyben}.0.0")
    first_ip_address = (f"{ip_cím[:ahol_a_vonal_van]}.{networ_address_egyben}.0.1")
    

network_address_változatott = network_address_változatott.replace("[", "").replace("]", "").replace("'", "").replace(",", ".").replace(" ", "")
first_ip_address = first_ip_address.replace("[", "").replace("]", "").replace("'", "").replace(",", ".").replace(" ", "")



print(f"Network address: {network_address_változatott}")
print(f"First ip address: {first_ip_address}")

#print(f"kettő {kettő_négyzeten}.en = ")