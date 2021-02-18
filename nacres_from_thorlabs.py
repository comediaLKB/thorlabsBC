# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:35:48 2021

@author: moro
"""

def nacres_from_thorlabs(code, name):
    # some common general cases
    # OA.01	OPTO : LENTILLES ET SYSTEMES DE LENTILLES
    # OA.02	OPTO : MIROIRS
    # OA.03	OPTO : RESEAUX (DIFFRACTION, COMPRESSION,…)
    # OA.04	OPTO : LAMES, FENETRES ET CRISTAUX OPTIQUES
    # OA.05	OPTO : FILTRES OPTIQUES, POLARISATEURS, CUBES ET PRISMES
    # OA.06	OPTO : FIBRES OPTIQUES
    # OA.07	OPTO : AUTRES COMPOSANTS OPTIQUES PASSIFS
    # OA.11	OPTO : CAMERAS UV-VISIBLE
    # OA.12	OPTO : CAMERAS INFRA-ROUGE
    # OA.14	OPTO : OPTIQUE POUR CAMERAS
    # OA.15	OPTO : DETECTEURS ET AUTRE MATERIEL D'OPTOELECTRONIQUE (HORS CAMERAS)
    # OA.21	OPTO : MICROPOSITIONNEMENT ET OPTOMECANIQUE
    # OA.22	OPTO : BANCS, TABLES OPTIQUES, ET ACCESSOIRES
    # OA.32	OPTO : LASERS A SOLIDE
    # OA.33	OPTO : LASERS A SEMI-CONDUCTEURS (DIODES LASERS)
    # OA.38	OPTO : LAMPES ET AUTRES SOURCES LUMINEUSES (LAMPES FLASH OU CONTINUE...)
    # TA.22	PETITS EQUIPEMENTS ET CONSOMMABLES POUR L'ELECTRONIQUE
    # TA.01	COMPOSANTS ELECTRONIQUES ACTIFS ET PASSIFS
    # TA.02	COMPOSANTS ELECTROMECANIQUES ET ACCESSOIRES DE CABLAGE
    # TB.11	ENERGIE : MATERIEL D'ALIMENTATION (ALIM., AMPLI., ONDULEURS,…)
	
    # some lenses
    if ((code[0:2]=='AC') or
        (code[0:2]=='LA') or
        (code[0:2]=='LB') or
        (code[0:2]=='LD') or
        (code[0:2]=='LF') or
        (code[0:2]=='AY') 
        ):
        return 'OA.01'
    # some mirror
    if ((code[0:3]=='BBE') or
        (code[0:3]=='BBD') or
        (code[0:3]=='PFD') or
        (code[0:2]=='UM') or
        (code[0:2]=='BB') or
        (code[0:3]=='BFE') 
        ):
        return 'OA.02'
    # some filters, cubes..
    if ((code[0:2]=='FL') or
        (code[0:2]=='FG') or
        (code[0:2]=='MF') or
        (code[0:2]=='FD') or
        (code[0:3]=='DML') or
        (code[0:2]=='NE') or        
        (code[0:3]=='PBS') or
        (code[0:2]=='BS') or
        (code[0:2]=='FB') 
        ):
        return 'OA.05'
    # other optical passiv optical stuff
    if ((code[0:2]=='SM')
        ):
        return 'OA.07'
    # some micropositioning and generic optomechanics
    if (("Adapter" in name) or
        ("Lens Tube" in name) or
        ("Kinematic" in name) or
        ("Post Holder" in name) or
        (code[0:2]=='CP') or
        (code[0:3]=='LCP') or
        (code[0:3]=='SPT') or
        (code[0:3]=='CXY') or
        (code[0:4]=='SM1Z') or
        (code[0:3]=='CT1') or
        (code[0:4]=='CXYZ') or
        (code[0:5]=='ST1XY') or
        (code[0:5]=='LM1XY') or
        (code[0:2]=='BE') or
        (code[0:2]=='BA') or
        (code[0:2]=='TR')
    ):
        return 'OA.21'

    else:
        print('nomeclature rule not found; take a look at nacres_from_thorlabs.py and implement the rule!')
        return ''