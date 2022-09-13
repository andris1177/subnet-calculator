def dec_to_bin(number, binary):
    return_binary = []
    for i in range(len(number)):
        szám = number[i]
        szám = int(szám)
        return_binary.append(binary[szám])
    return return_binary


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
ahol_a_vonal_van = 0
for i in range(len(subnet_binary)):
    if subnet_binary[i] != ['11111111']:
        ahol_a_vonal_van = i+1

print(subnet_binary)
print(ip_binary)

networ_address = []
for i in range(len(subnet_binary[ahol_a_vonal_van -1])):
    for j in range(8):
        if subnet_binary[ahol_a_vonal_van -1][i][j] == "1" and subnet_binary[ahol_a_vonal_van -1][i][j] == ip_binary[ahol_a_vonal_van -1][i][j]:
            networ_address.append("1")
        else:
            networ_address.append("0")


print(networ_address)

