#!/usr/bin/env python
# -*- coding: utf-8 -*-

barva_las = {
    "crna":"CCAGCAATCGC",
    "rjava":"GCCAGTGCCG",
    "korencek":"TTAGCTATCGC"
}
oblika_obraza = {
    "kvadraten":"GCCACGG",
    "okrogel":"ACCACAA",
    "ovalen":"AGGCCTCA"
}
barva_oci = {
    "modra":"TTGTGGTGGC",
    "zelena":"GGGAGGTGGC",
    "rjava":"AAGTAGTGAC"
}
spol = {
    "moski":"TGCAGGAACTTC",
    "zenska":"TGAAGGACCTTC"
}
rasa = {
    "belec":"AAAACCTCA",
    "crnec":"CGACTACAG",
    "azijec":"CGCGGGCCG"
}

def get_hair_color(dna):
    for barva in barva_las.keys():
        if (dna.find(barva_las[barva]) != -1):
            return barva
    return "Neznana"

# Dodaj funkcije za posamezne lastnosti

def get_person(hair_color, sex):
    # logika
    return "Neznan"

def za_referenco(): # na koncu to pobrisemo
    if (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["korencek"]) != -1 and dna.find(barva_oci["rjava"]) != -1) and dna.find(oblika_obraza["okrogel"]) != -1:
        print ("Bil je Žiga!")
    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["crna"]) != -1 and dna.find(barva_oci["modra"]) != -1 and dna.find(oblika_obraza["ovalen"]) != -1):
        print ("Bil je Matej!")
    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["rjava"]) != -1 and dna.find(barva_oci["zelena"]) != -1 and dna.find(oblika_obraza["kvadraten"]) != -1):
        print ("Bil je Miha!")
    else :
        print ("Krivca ni med osumljenci..")