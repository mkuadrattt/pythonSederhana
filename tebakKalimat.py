kataKunci = "Aku Sayang Kamu"
jawabanUser = ""
bantuan = False

while jawabanUser != kataKunci and (bantuan is False):
    print("Jawaban Salah")
    jawabanUser = input("Masukan Kata Kunci : ")
else:
    bantuan = True
    print("Tulus dari lubuk hatiku")
