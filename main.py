from classhelper import HE
from classhelper import Hasil
from classhelper import EH
from classhelper import H


def main():
    print("Program Penghitung Naive Bayes untuk UTS AI")
    fakta = input("Masukkan Fakta: ")
    countFakta = input("Berapa jumlah hipotesa yang ada? ")
    hipo = []

    for i in range(0, int(countFakta)):
        hipo.append(input("Masukkan hipotesa ke-" + str(i + 1) + ": "))

    print("Apakah data berikut benar?")
    print("Fakta: " + fakta)
    print("Hipotesa")
    cnt = 1
    for i in hipo:
        print(str(cnt) + ") " + i)
        cnt += 1

    continues = input("Jawaban anda? y/Y/n/N: ")
    if continues == "y" or continues == "Y":
        hitung(hipo, fakta)
    elif continues == "n" or continues == "N":
        main()


def hitung(hipo, fakta):
    print("============")
    eh = []
    h = []
    for i in hipo:
        ehh = input("Probalitas %s terhadap hipotesa: %s p(%s|%s): " % (fakta, i, fakta, i))
        eh.append(EH(i, fakta, float(ehh)))
        hh = input("Probalitas %s tanpa memandang fakta %s p(%s):" % (i, fakta, i))
        h.append(H(i, float(hh)))
    # Menghitung probalitas
    print("=====Probalitas semua hipotesa=====\n")
    count = 0
    hasils = []
    for i in hipo:
        print("p(%s|%s) = p(%s|%s) * p(%s) / " % (i, fakta, fakta, i, i), end='')
        for x in hipo:
            print("p(%s|%s) * p(%s) + " % (fakta, x, x), end='')

        print("\n===Dibawah adalah perhitungannya====")

        print("p(%s|%s) = (%f) * (%f) / " % (i, fakta, eh[count].value, h[count].value), end='')
        bawah = 0.0
        for x in range(0, len(hipo)):
            print("(%f) * (%f) + " % (eh[x].value, h[x].value), end='')
            bawah += eh[x].value * h[x].value

        atas = eh[count].value * h[count].value
        hasilakhir = atas / bawah
        print("\nHasil = %f/%f = %f " % (atas, bawah, hasilakhir))
        print("==========END=========\n")
        hasils.append(Hasil(i, hasilakhir))
        count += 1

    print("Urutan dari yang paling besar probalitas nya adalah:")
    hasils.sort(key=lambda x: x.value, reverse=True)
    for i in range(0, len(hasils)):
        print("%d) %s ,hasil = %f" % (i+1, hasils[i].nameH, hasils[i].value))


if __name__ == "__main__":
    main()
