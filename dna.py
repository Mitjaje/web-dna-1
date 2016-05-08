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
    return "neznana"

def get_face_shape(dna):
    for oblika in oblika_obraza.keys():
        if (dna.find(oblika_obraza[oblika]) != -1):
            return oblika
    return "neznana"

def get_eyes_colour(dna):
    for barva in barva_oci.keys():
        if (dna.find(barva_oci[barva]) != -1):
            return barva
    return "neznana"

def get_sex(dna):
    for sex in spol.keys():
        if (dna.find(spol[sex]) != -1):
            return sex
    return "neznana"

def get_race(dna):
    for race in rasa.keys():
        if (dna.find(rasa[race]) != -1):
            return race
    return "neznana"

def get_person(dna):
    if get_sex(dna) == "moski" and get_race(dna) == "belec" and get_hair_color(dna) ==  "korencek" and get_eyes_colour(dna) == "rjava" and get_face_shape(dna) == "okrogel":
        return "Žiga"
    elif  get_sex(dna) == "moski" and get_race(dna) == "belec" and get_hair_color(dna) ==  "crna" and get_eyes_colour(dna) == "modra" and get_face_shape(dna) == "ovalen":
        return "Matej"
    elif get_sex(dna) == "moski" and get_race(dna) == "belec" and get_hair_color(dna) ==  "rjava" and get_eyes_colour(dna) == "zelena" and get_face_shape(dna) == "kvadraten":
        return "Miha"
    else:
        return "Krivca ni med osumljenci.."

def za_referenco(): # na koncu to pobrisemo
    if (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["korencek"]) != -1 and dna.find(barva_oci["rjava"]) != -1) and dna.find(oblika_obraza["okrogel"]) != -1:
        print ("Bil je Žiga!")
    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["crna"]) != -1 and dna.find(barva_oci["modra"]) != -1 and dna.find(oblika_obraza["ovalen"]) != -1):
        print ("Bil je Matej!")
    elif (dna.find(spol["moski"]) != -1 and dna.find(rasa["belec"]) != -1 and dna.find(barva_las["rjava"]) != -1 and dna.find(barva_oci["zelena"]) != -1 and dna.find(oblika_obraza["kvadraten"]) != -1):
        print ("Bil je Miha!")
    else :
        print ("Krivca ni med osumljenci..")