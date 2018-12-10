print("hello world")
gedung = "BPK"
tinggi = 8
print(tinggi)
#tinggi = True
print(tinggi)

is_alive = 'gak jelas'

#list
hari = ['minggu', 'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']
print(hari)
print(hari[0])
print(hari[len(hari)-1])

#dictionary
antonim = {}
antonim['tinggi'] = 'pendek'
antonim['gelap'] = 'terang'
antonim['jauh'] = 'dekat'
print("antonim dari jauh adalah {}".format(antonim['jauh']))

#control flow
if is_alive == True:
    print("hore... hidup...")
elif is_alive == False:
    print("mati")
else:
    print("gak jelas")


#loop
#untuk perulangan yang pasti
for i in range(0,3):
    print(i)

i = 0
while is_alive:
    print(i, 'hidup')
    i = i + 1
    if i == 10:
        is_alive = False

#for loop untuk list
for h in hari:
    print(h)

for h in range(len(hari)):
    print(h[h])
#push