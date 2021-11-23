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
    # NB.32 HUILE A IMMERSION POUR MICROSCOPIE
	
    # some lenses and objectives
    if ((code[0:2]=='AC') or
        (code[0:2]=='LA') or
        (code[0:2]=='LB') or
        (code[0:2]=='LD') or
        (code[0:2]=='LF') or
        (code[0:3]=='N20') or
        (code[0:3]=='N10') or
        (code[0:3]=='N60') or
        (code[0:2]=='AY') 
        ):
        return 'OA.01'
    # some mirror
    if ((code[0:3]=='BBE') or
        (code[0:3]=='BBD') or
        (code[0:3]=='PFD') or
        (code[0:2]=='UM') or
        (code[0:2]=='BB') or
        (code[0:3]=='BFE') or
        (code[0:3]=='DMS') 
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

    # fibers
    if ((code[0:2]=='FP') or
        (code[0:3]=='M28') 
        ):
        return 'OA.06'
    # other optical passiv optical stuff
    if ((code[0:2]=='SM')
        ):
        return 'OA.07'

    # DETECTEURS ET AUTRE MATERIEL D'OPTOELECTRONIQUE (HORS CAMERAS)
    if ((code[0:4]=='S425')
        ):
        return 'OA.15'

    # some micropositioning and generic optomechanics
    if (("Adapter" in name) or
        ("Lens Tube" in name) or
        ("Kinematic" in name) or
        ("Post Holder" in name) or
        (code[0:2]=='CP') or
        (code[0:2]=='CF') or
        (code[0:2]=='SM') or
        (code[0:3]=='LCP') or
        (code[0:3]=='SPT') or
        (code[0:3]=='CXY') or
        (code[0:4]=='SM1Z') or
        (code[0:3]=='CT1') or
        (code[0:2]=='CL') or
        (code[0:4]=='CXYZ') or
        (code[0:5]=='ST1XY') or
        (code[0:5]=='LM1XY') or
        (code[0:3]=='XYT') or
        (code[0:2]=='BE') or
        (code[0:2]=='BA') or
        (code[0:2]=='TR') or
        (code[0:2]=='LC') or
        (code[0:2]=='LB') or
        (code[0:2]=='LF') or
        (code[0:2]=='RS') or
        (code[0:2]=='C6') or
        (code[0:2]=='B3') or
        (code[0:2]=='B5') or
        (code[0:2]=='B6') or
        (code[0:2]=='RB') or
        (code[0:2]=='PF') or
        (code[0:2]=='BE') or
        (code[0:3]=='H45') or
        (code[0:3]=='R1D') or
        (code[0:2]=='K6') or
        (code[0:2]=='ND') or
        (code[0:2]=='ER') or
        (code[0:2]=='GV') or
        (code[0:4]=='P350') or
        (code[0:3]=='SLH') 
    ):
        return 'OA.21'

    # BANCS, TABLES OPTIQUES, ET ACCESSOIRES
    if ((code[0:3]=='B90') or
        (code[0:3]=='SB1') or
        (code[0:2]=='S9') or
        (code[0:3]=='TPS') or
        (code[0:3]=='BK5') or
        (code[0:3]=='S14')
        ):
        return 'OA.38'

    # LED
    if ((code[0:2]=='MW') or
        (code[0:2]=='M8') 
        ):
        return 'OA.38'

    # some drivers and power supplies
    if ((code[0:2]=='GP') or
        (code[0:2]=='GC') or
        (code[0:2]=='GC') or
        (code[0:3]=='KST') or
        (code[0:3]=='KCH') or
        (code[0:3]=='ZFS') or
        (code[0:3]=='LED')
        ):
        return 'TB.11'

    # HUILE A IMMERSION POUR MICROSCOPIE
    if ((code[0:4]=='MOIL')
        ):
        return 'NB.32'

    else:
        print('nomeclature rule not found; take a look at nacres_from_thorlabs.py and implement the rule!')
        return ''