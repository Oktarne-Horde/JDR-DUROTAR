# @title
# générateur_orc.py
import random
import math

# ---------------------------
# ARMES (liste complète d'après ta table)
# Format simple : "Nom": {"expr": "...", "maniement": "Une main"/"Deux mains"/"munition", "rarete":"", "taille": "XXS/XS/S/M/L/XL/XXL"}
# NE PAS MODIFIER LA LISTE SANS ME LE DIRE.
ARMES = {
    "Dague de Gobelin en acier":        {"expr":"1d6",                     "maniement":"Une main",   "rarete":"Commune", "taille":"XXS"},
    "Épée de Gobelins à une main":     {"expr":"1d10+1d4",               "maniement":"Une main",   "rarete":"Commune", "taille":"XS"},
    "Dague en bronze":                 {"expr":"1d20",                   "maniement":"Une main",   "rarete":"Commune", "taille":"S"},
    "Dague en fer":                    {"expr":"1d12+1d8",               "maniement":"Une main",   "rarete":"Commune", "taille":"S"},
    "Dague courte amélioré":           {"expr":"1d20",                   "maniement":"Une main",   "rarete":"Commune", "taille":"S"},
    "Dague renforcée":                 {"expr":"1d20",                   "maniement":"Une main",   "rarete":"Commune", "taille":"S"},
    "Machette basique":                {"expr":"1d20+1d12",             "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Épée courte en bronze":           {"expr":"1d20+1d12",             "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Hache courte de combat":          {"expr":"2d20+1d8",              "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Faucille de guerre":              {"expr":"2d20+1d8",              "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Épée bâtarde":                    {"expr":"2d20+2d8",              "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Épée courte":                     {"expr":"2d20+1d12",             "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Machette de combat":              {"expr":"3d20",                  "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Hache à une main":                {"expr":"2d20+1d12",             "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Sabre de combat":                 {"expr":"2d20x2",                "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Hache de combat":                 {"expr":"2d20+2d12",             "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Épée longue standard":            {"expr":"2d20x2+1d12",          "maniement":"Deux mains", "rarete":"Rare",    "taille":"L"},
    "Épée à double tranchant":         {"expr":"2d20x2+1d12+1d8",      "maniement":"Deux mains", "rarete":"Rare",    "taille":"L"},
    "Glaive lourd":                    {"expr":"2d20x2+1d20+1d12",     "maniement":"Deux mains", "rarete":"Rare",    "taille":"L"},
    "Garde épée à deux main":          {"expr":"(2d20+1d12)x2",        "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Hache de combat (2 mains)":       {"expr":"2d20+2d12x2",          "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Épée de duelliste":               {"expr":"2d20x3",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Épée à large lame":               {"expr":"4d20+1d12",            "maniement":"Deux mains", "rarete":"Commune", "taille":"XL"},
    "Épée de champion":                {"expr":"2d20x3+1d12+10",      "maniement":"Deux mains", "rarete":"Épique",  "taille":"XL"},
    "Épée de guerre":                  {"expr":"2d20x3",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Épée à deux mains robuste":       {"expr":"3d20x2",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Claymore orc":                    {"expr":"2d20x3+1d20",          "maniement":"Deux mains", "rarete":"Épique",  "taille":"XL"},
    "Hache de guerre":                 {"expr":"3d20x2+1d12",          "maniement":"Deux mains", "rarete":"Épique",  "taille":"XL"},
    "Épée étoile d'acier":             {"expr":"6d20",                 "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Épée de duel":                    {"expr":"3d20x2",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Épée longue":                     {"expr":"3d20x2",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Hache à double tranchant":        {"expr":"2d20x2+1d20",          "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    "Grande hallebarde":               {"expr":"3d20x2",               "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    # Armes Huran (présentes aussi dans la table générale — conservées ici)
    "Tranche-épines":                   {"expr":"3d20x2",               "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Marteflanc":                       {"expr":"2d20+1d10+2",         "maniement":"Une main",   "rarete":"Rare",    "taille":"M"},
    "Fendoir Sauvage":                  {"expr":"2d20x3",               "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Lance Gemmes":                     {"expr":"2d20+1d12",            "maniement":"Deux mains", "rarete":"Rare",    "taille":"L"},
    "Couperet Tranchecrins":            {"expr":"1d20+1d4",             "maniement":"Une main",   "rarete":"Rare",    "taille":"S"},
    "Hachette de Huran":                {"expr":"2d20+1d12",            "maniement":"Une main",   "rarete":"Rare",    "taille":"M"},
    "Fléau Tranchecrins":               {"expr":"2d20+4",               "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    # Contondantes / masses
    "Masse en fer":                     {"expr":"2d20+1d6",            "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Masse en bronze":                  {"expr":"1d20+1d10+1d6",       "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Masse d'armes":                    {"expr":"2d20+1d10",           "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Masse d'arme (var)":               {"expr":"1d20+1d8+1d6",        "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Fléau d'arme léger":               {"expr":"3d20+1d12+8",         "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Masse d'arme à deux mains":        {"expr":"2d20x2+2d12",         "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Masse lourde":                     {"expr":"4d20+1d12",           "maniement":"Deux mains", "rarete":"Rare",    "taille":"L"},
    "totem de guerre":                  {"expr":"3d20x2+1d20",         "maniement":"Deux mains", "rarete":"Épique",  "taille":"XXL"},
    # Hast
    "Lance simple":                     {"expr":"2d20+1d12+1d8",      "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Lance de guerre":                  {"expr":"3d20+1d12+4",        "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Trident de guerre":                {"expr":"3d20x2+1d12",        "maniement":"Deux mains", "rarete":"Rare",    "taille":"XL"},
    # Distance
    "Fusil a plomb de gobelin":         {"expr":"3d20",               "maniement":"Deux mains", "rarete":"Épique",  "taille":"XS"},
    "Hache de jet":                     {"expr":"1d20+1d12+1d8",      "maniement":"Une main",   "rarete":"Commune", "taille":"M"},
    "Arc court":                        {"expr":"3d20",               "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Arc rudimentaire":                 {"expr":"2d20+1d12+1d8",      "maniement":"Deux mains", "rarete":"Commune", "taille":"L"},
    "Arc long":                         {"expr":"3d20x2",             "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    "Hache de jet à deux main":         {"expr":"3d20x2",             "maniement":"Deux mains", "rarete":"Épique",  "taille":"L"},
    # Munitions
    "Flèches en bois":                  {"expr":"1d4",                "maniement":"munition",   "rarete":"Commune", "taille":"-"},
    "Flèches en bronze":                {"expr":"1d6",                "maniement":"munition",   "rarete":"Commune", "taille":"-"},
    "Flèches en fer":                   {"expr":"1d8",                "maniement":"munition",   "rarete":"Rare",    "taille":"-"},
    "Flèches taillées":                 {"expr":"1d8",                "maniement":"munition",   "rarete":"Rare",    "taille":"-"},
}

# ---------------------------
# ARMURES ORC (toutes les pièces non-Trophée) - format comme pour Huran
# Chaque slot contient une liste d'objets (plusieurs sets possibles pour le même emplacement)
# J'ai intégré toutes les pièces orc de ton PDF (Trophées exclus).
# ---------------------------

armures_orc = {
    "Tête": [
        {"nom":"Casque en tete de daim","set":"Armure du chasseur de daim","armure":"1d12","degats":None,"rarete":"Commune","taille":"L","slots":["12/12"]},
        {"nom":"Casque en cuir léger","set":"Armure du chasseur en cuir","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["12/12"]},
        {"nom":"Tete de Crocilisque","set":"Armure du Crocilisque","armure":"2d12+3","degats":None,"rarete":"Épique","taille":"L","slots":["12/12"]},
        {"nom":"Casque en métal forgé","set":"Armure de métal classic","armure":"2d12","degats":None,"rarete":"Rare","taille":"L","slots":["12/12"]},
        {"nom":"Casque en cuir renforcé","set":"Armure de cuir fin","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["12/12"]},
        {"nom":"Casque en cuir usé","set":"Armure de cuir classic","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["12/12"]}
    ],
    "Épaules": [
        {"nom":"Epaule de fourure","set":"Armure du chasseur de daim","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaule en cuir léger","set":"Armure du chasseur en cuir","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaulière du chien de guerre","set":"Armure du chien de guerre","armure":"1d12+1d4","degats":None,"rarete":"Rare","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaulière en écaille de Crocilisque","set":"Armure du Crocilisque","armure":"1d12+1d8+4","degats":None,"rarete":"Rare","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaule en bois de fer renforcé","set":"Armure de la garde de tranchcolline","armure":"1d12+4","degats":None,"rarete":"Rare","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaulière en bois renforcé de fer","set":"Armure du pêcheur scintillant","armure":"1d12+1d4","degats":None,"rarete":"Rare","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaulière cérémoniel en bois","set":"Armure du loup chamanique","armure":"1d12","degats":None,"rarete":"Commune","taille":"L","slots":["7;8/12"]},
        {"nom":"Epaulière bois renforcé de fer","set":"Armure du Grunt","armure":"1d12+1d10+2","degats":None,"rarete":"Rare","taille":"L","slots":["7;8/12"]},
        {"nom":"Épaulière de fer","set":"Armure de métal classic","armure":"1d20+1d6+2","degats":None,"rarete":"Épique","taille":"L","slots":["7;8/12"]}
    ],
    "Torse": [
        {"nom":"Plastron en cuir de daim","set":"Armure du chasseur de daim","armure":"1d12","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Plastron en cuir léger","set":"Armure du chasseur en cuir","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Ceinturons de cuir de Crocilisque","set":"Armure du Crocilisque","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Plastron en Bronze","set":"Armure de la garde de tranchcolline","armure":"2d12+1d4+4","degats":None,"rarete":"Épique","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Ceinture en fer forgé","set":"Armure du pêcheur scintillant","armure":"2d12+4","degats":None,"rarete":"Épique","taille":"L","slots":["3;4/12"]},
        {"nom":"Plastron de bronze","set":"Armure de métal classic","armure":"1d20+1d12+1d8+3","degats":None,"rarete":"Épique","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Lanière de cuir renforcé","set":"Armure du Grunt","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Plastron en cuir cousue main","set":"Armure de cuir classic","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]},
        {"nom":"Harnais endommagé en cuir","set":"Armure en cuir artisanal","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["9;10;11/12"]}
    ],
    "Avant-bras": [
        {"nom":"Gantelet en cuir renforcé","set":"Armure du chasseur en cuir","armure":"1d12","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]},
        {"nom":"Brassard décoré renforcés","set":"Armure du chien de guerre","armure":"1d8+1","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]},
        {"nom":"Gantelet de Crocilisque","set":"Armure du Crocilisque","armure":"1d10+1d6","degats":None,"rarete":"Rare","taille":"L","slots":["5;6/12"]},
        {"nom":"Gantelet de cuir renforcé","set":"Armure de la garde de tranchcolline","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]},
        {"nom":"Mini bouclier renforcé de fer","set":"Armure du pêcheur scintillant","armure":"1d20","degats":None,"rarete":"Rare","taille":"L","slots":["5;6/12"]},
        {"nom":"Gantelet en fourure renforcé de cuir","set":"Armure du Grunt","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]},
        {"nom":"Gantelet de fer","set":"Armure de métal classic","armure":"2d12+1","degats":None,"rarete":"Épique","taille":"L","slots":["5;6/12"]},
        {"nom":"Gantelet en cuir","set":"Armure de cuir classic","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]},
        {"nom":"Brassard de cuir usé","set":"Armure en cuir artisanal","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["5;6/12"]}
    ],
    "Jambes": [
        {"nom":"Jambière de cuir","set":"Armure du chasseur en cuir","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["3;4/12"]},
        {"nom":"Pantalon renforcé d'anneaux","set":"Armure du chien de guerre","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["3;4/12"]},
        {"nom":"Jupe de Crocilisque renforcée","set":"Armure du Crocilisque","armure":"1d12+1d6","degats":None,"rarete":"Rare","taille":"L","slots":["3;4/12"]},
        {"nom":"Jambiere en cuir clouté","set":"Armure de la garde de tranchcolline","armure":"1d12+1d4","degats":None,"rarete":"Rare","taille":"L","slots":["3;4/12"]},
        {"nom":"Ceinture en fer forgé","set":"Armure du pêcheur scintillant","armure":"2d12+4","degats":None,"rarete":"Épique","taille":"L","slots":["3;4/12"]},
        {"nom":"Jupe en lin","set":"Armure du Grunt","armure":"1d6","degats":None,"rarete":"Commune","taille":"L","slots":["3;4/12"]},
        {"nom":"Jambières de plaque","set":"Armure de métal classic","armure":"1d20+1d12+3","degats":None,"rarete":"Épique","taille":"L","slots":["3;4/12"]},
        {"nom":"Pantalon en cuir robuste","set":"Armure en cuir artisanal","armure":"1d10+1d4","degats":None,"rarete":"Commune","taille":"L","slots":["3;4/12"]}
    ],
    "Bottes": [
        {"nom":"Botte en cuir de daim","set":"Armure du chasseur de daim","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Botte en cuir laminé","set":"Armure du chasseur en cuir","armure":"1d6","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Protèges tibias décorés renforcés","set":"Armure du chien de guerre","armure":"1d10","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Bottes de Crocilisque en cuir renforcé","set":"Armure du Crocilisque","armure":"1d10+1d4","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"botte en bois de fer reforcée","set":"Armure de la garde de tranchcolline","armure":"1d10+2","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Bottes en lanière de cuir","set":"Armure du pêcheur scintillant","armure":"1d6","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Botte en cuir tressé","set":"Armure de cuir fin","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Botte de fourure","set":"Armure du Grunt","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]},
        {"nom":"Botte en fer","set":"Armure de métal classic","armure":"1d12+1d8","degats":None,"rarete":"Épique","taille":"L","slots":["1;2/12"]},
        {"nom":"Botte en cuir brulé","set":"Armure en cuir artisanal","armure":"1d8","degats":None,"rarete":"Commune","taille":"L","slots":["1;2/12"]}
    ],
    # Boucliers (emplacement "Bras faible" — géré comme bouclier mais some are listed as Avant-bras in sets; we include both)
    "Boucliers": [
        {"nom":"Bouclier en bois renforcé","set":"Boucliers","armure":"1d20","degats":None,"rarete":"Rare","taille":"M;L","slots":["5;7/12"]},
        {"nom":"Bouclier en tôle cabossé","set":"Boucliers","armure":"1d12","degats":None,"rarete":"Commune","taille":"M;L","slots":["5;7/12"]},
        {"nom":"Bouclier renforcé de fer","set":"Boucliers","armure":"2d12+4","degats":None,"rarete":"Rare","taille":"M;L","slots":["5;7/12"]},
        # mini bouclier present in set (stays in Avant-bras entries above)
        {"nom":"Mini bouclier renforcé de fer","set":"Armure du pêcheur scintillant","armure":"1d20","degats":None,"rarete":"Rare","taille":"L","slots":["5;6/12"]}
    ]
}

# ---------------------------
# UTILITAIRES GLOBAUX
# ---------------------------

def tirer_rarete_armure():
    """Commune 50% / Rare 33% / Epique 17%"""
    r = random.random()
    if r < 0.50:
        return "Commune"
    elif r < 0.83:
        return "Rare"
    else:
        return "Épique"

def weapon_fits_orc(info):
    """Orc can use:
       - one-hand: sizes S, M
       - two-hand: sizes L, XL
       - XS/XXS only for huran, not for orc.
       Returns True if usable by orc.
    """
    t = info.get("taille","")
    maniement = info.get("maniement","")
    if maniement == "Une main":
        return t in ("S","M")
    if maniement == "Deux mains":
        return t in ("L","XL")
    return False

# Build pools for orc-usable weapons
WEAPONS_S = [ (n,i) for n,i in ARMES.items() if i.get("taille")=="S" and weapon_fits_orc(i) ]
WEAPONS_M = [ (n,i) for n,i in ARMES.items() if i.get("taille")=="M" and weapon_fits_orc(i) ]
WEAPONS_L = [ (n,i) for n,i in ARMES.items() if i.get("taille")=="L" and weapon_fits_orc(i) ]
WEAPONS_XL = [ (n,i) for n,i in ARMES.items() if i.get("taille")=="XL" and weapon_fits_orc(i) ]

# Flatten all L-sized armures (for selection)
ALL_ARMURES = []
for slot, pieces in armures_orc.items():
    for p in pieces:
        # skip Trophée entries — we already excluded them when building the dict
        ALL_ARMURES.append({
            "Nom": p["nom"],
            "Armure": p["armure"],
            "Degats": p.get("degats"),
            "Emplacement": slot,         # Note: some pieces are in Boucliers but may have slots like 5;6/12
            "Rareté": p["rarete"],
            "Taille": p["taille"],
            "Set": p["set"],
            "slots_str": p.get("slots",[])
        })

# ---------------------------
# GÉNÉRATION D'UN ORC
# ---------------------------

def generer_orc():
    # Sexe et PV
    sexe = random.choice(["Mâle","Femelle"])
    pv = random.randint(130,150)

    # Facultés : bornes définies, total fixé à 76
    bornes = {
        "COR (Corps)": (9,14),
        "AGI (Agilité)": (5,14),
        "INT (Intelligence)": (5,14),
        "REL (Relation)": (5,14),
        "PER (Perception)": (5,14),
        "VIS (Visée)": (5,14),
        "COMBAT": (7,14)
    }

    min_total = sum(v[0] for v in bornes.values())
    max_total = sum(v[1] for v in bornes.values())
    cible = 76
    if not (min_total <= cible <= max_total):
        raise ValueError(f"Impossible d'atteindre la somme {cible} avec les bornes fournies.")

    # Start at minimums
    facultes = {k: v[0] for k,v in bornes.items()}
    points_restants = cible - min_total
    keys = list(bornes.keys())
    while points_restants > 0:
        k = random.choice(keys)
        if facultes[k] < bornes[k][1]:
            facultes[k] += 1
            points_restants -= 1

    # PV, Esprit, Bdeg
    esprit = 10 + random.randint(0,10)
    bdeg = 5 + (facultes["COR (Corps)"] // 3)

    # Esquive : average between AGI and COMBAT floored, then mapped to racial table, min 10
    avg = (facultes["AGI (Agilité)"] + facultes["COMBAT"]) // 2

    # racial table for ORC as provided:
    # avg 5-9 -> 11, 10 -> 12, 11-12 ->13, 13 ->14, 14 ->15, >=15 ->16
    if avg <= 9:
        esquive_calc = 11
    elif avg == 10:
        esquive_calc = 12
    elif avg in (11,12):
        esquive_calc = 13
    elif avg == 13:
        esquive_calc = 14
    elif avg == 14:
        esquive_calc = 15
    else:
        esquive_calc = 16
    esquive = max(10, esquive_calc)

    # Compétences (exemple same list)
    liste_competences = [
        "arme de trait","arme de jet","arme à feu","instinct","survie",
        "arme blanche","arme contondante","mains nues","athlétisme",
        "constitution physique","force brute"
    ]
    nb_comp = random.randint(1,8)
    competences = {}
    pool_comp = liste_competences[:]
    for _ in range(nb_comp):
        c = random.choice(pool_comp)
        pool_comp.remove(c)
        competences[c] = random.randint(1,4)

    # Nombre d'armes selon règle (tirage 1-12)
    tir_arme = random.randint(1,12)
    nb_armes = 3 if tir_arme == 1 else (2 if tir_arme <=5 else 1)

    # Construire pool d'armes utilisables par l'orc
    pool = []
    if nb_armes == 3:
        pool = WEAPONS_S + WEAPONS_M + WEAPONS_L + WEAPONS_XL
    else:
        pool = WEAPONS_M + WEAPONS_L + WEAPONS_XL

    armes_choisies = []
    # Sélection : éviter deux armes deux-mains (L/XL) en double
    while len(armes_choisies) < nb_armes:
        if not pool:
            break
        candidate = random.choice(pool)
        taille_cand = candidate[1].get("taille")
        if taille_cand in ("L","XL") and any(a[1].get("taille") in ("L","XL") for a in armes_choisies):
            # Already have a two-handed, try to pick one-handed
            onehand = [c for c in pool if c[1].get("taille") not in ("L","XL")]
            if onehand:
                candidate = random.choice(onehand)
            else:
                # if no one-handed left, allow duplicate two-hand only if no other option
                pass
        armes_choisies.append(candidate)

    # Format armes
    armes_final = []
    for n,i in armes_choisies:
        armes_final.append({
            "Nom": n,
            "Expr": i["expr"],
            "Maniement": i["maniement"],
            "Taille": i["taille"],
            "Rareté": i["rarete"]
        })

    # Bouclier (15% chance)
    bouclier = None
    if random.random() < 0.15:
        handed = random.choices(["Droitier","Gaucher","Ambidextre"], weights=[70,20,10], k=1)[0]
        if handed in ("Droitier","Ambidextre"):
            emplacement_codes = "5;7"
            emplacement_note = "Main gauche (5;7)"
        else:
            emplacement_codes = "6;8"
            emplacement_note = "Main droite (6;8)"
        # pick random bouclier from armures_orc["Boucliers"]
        boucl = random.choice(armures_orc["Boucliers"])
        bouclier = {
            "Nom": boucl["nom"],
            "Armure": boucl["armure"],
            "Degats": boucl.get("degats"),
            "Rareté": boucl["rarete"],
            "Set": boucl["set"],
            "Emplacement_note": emplacement_note,
            "Emplacement_codes": emplacement_codes
        }

    # Armures : tirage présence par slot
    slots_threshold = {
        "Tête": 5,
        "Épaules": 4,
        "Torse": 6,
        "Avant-bras": 9,
        "Jambes": 8,
        "Bottes": 10
    }

    armures_result = {}
    for slot, seuil in slots_threshold.items():
        roll = random.randint(1,12)
        if roll <= seuil:
            rarity = tirer_rarete_armure()
            # candidates across ALL_ARMURES filtered by emplacement slot and rarity
            candidates = [a for a in ALL_ARMURES if a["Emplacement"].lower() == slot.lower() and a["Rareté"] == rarity]
            # fallback: any with same emplacement (ignore rarity)
            if not candidates:
                candidates = [a for a in ALL_ARMURES if a["Emplacement"].lower() == slot.lower()]
            if candidates:
                chosen = random.choice(candidates)
                armures_result[slot] = {
                    "present": True,
                    "rarete": rarity,
                    "set": chosen["Set"],
                    "piece": chosen["Nom"],
                    "armure": chosen["Armure"],
                    "degats": chosen.get("Degats"),
                    "slots_str": chosen.get("slots_str","")
                }
            else:
                armures_result[slot] = {"present": False}
        else:
            armures_result[slot] = {"present": False}

    # Gestion des pièces doubles (Épaules, Avant-bras, Bottes)
    def maybe_generate_pair(slot_name):
        left_key = f"{slot_name} gauche"
        right_key = f"{slot_name} droite"
        base = armures_result.get(slot_name, {"present":False})
        if not base["present"]:
            return {left_key: {"present":False}, right_key: {"present":False}}
        left = base.copy()
        # 30% chance that right side is generated independently (different)
        if random.random() < 0.30:
            rarity = tirer_rarete_armure()
            candidates = [a for a in ALL_ARMURES if a["Emplacement"].lower() == slot_name.lower() and a["Rareté"] == rarity]
            if not candidates:
                candidates = [a for a in ALL_ARMURES if a["Emplacement"].lower() == slot_name.lower()]
            if candidates:
                chosen = random.choice(candidates)
                right = {
                    "present": True,
                    "rarete": rarity,
                    "set": chosen["Set"],
                    "piece": chosen["Nom"],
                    "armure": chosen["Armure"],
                    "degats": chosen.get("Degats"),
                    "slots_str": chosen.get("slots_str","")
                }
            else:
                right = {"present": False}
        else:
            right = left.copy()
        return {left_key:left, right_key:right}

    pairs = {}
    for p in ["Épaules","Avant-bras","Bottes"]:
        pairs.update(maybe_generate_pair(p))

    # Compose final armure dict for display
    final_armure = {}
    for s in ["Tête","Torse","Jambes"]:
        if armures_result[s]["present"]:
            final_armure[s] = {
                "piece": armures_result[s]["piece"],
                "set": armures_result[s]["set"],
                "rarete": armures_result[s]["rarete"],
                "armure": armures_result[s]["armure"],
                "degats": armures_result[s]["degats"],
                "slots_str": armures_result[s].get("slots_str","")
            }
        else:
            final_armure[s] = {"present": False}

    final_armure["Épaule gauche"] = pairs["Épaules gauche"]
    final_armure["Épaule droite"] = pairs["Épaules droite"]
    final_armure["Avant-bras gauche"] = pairs["Avant-bras gauche"]
    final_armure["Avant-bras droite"] = pairs["Avant-bras droite"]
    final_armure["Bottes gauche"] = pairs["Bottes gauche"]
    final_armure["Bottes droite"] = pairs["Bottes droite"]

    if bouclier:
        final_armure["Bouclier"] = {
            "Nom": bouclier["Nom"],
            "Armure": bouclier["Armure"],
            "Degats": bouclier["Degats"],
            "Rareté": bouclier["Rareté"],
            "Set": bouclier["Set"],
            "Emplacement_note": bouclier["Emplacement_note"],
            "Emplacement_codes": bouclier["Emplacement_codes"]
        }

    # Construire fiche textuelle (format lisible, une ligne par compétence / pièce, encadré pour armures)
    fiche_lines = []
    fiche_lines.append("════════════════════════════════════════════════")
    fiche_lines.append("                  FICHE D'ORC                  ")
    fiche_lines.append("════════════════════════════════════════════════")
    fiche_lines.append(f"Sexe : {sexe}")
    fiche_lines.append(f"PV : {pv}")
    fiche_lines.append(f"Esprit : {esprit}")
    fiche_lines.append(f"Esquive : {esquive}")
    fiche_lines.append(f"Bdeg : {bdeg}")
    fiche_lines.append("")
    fiche_lines.append("Facultés :")
    for k,v in facultes.items():
        fiche_lines.append(f"  - {k} : {v}")
    fiche_lines.append("")
    fiche_lines.append("Compétences :")
    if competences:
        for comp,dm in competences.items():
            fiche_lines.append(f"  - {comp} (DM {dm})")
    else:
        fiche_lines.append("  Aucune")
    fiche_lines.append("")
    fiche_lines.append("Armes :")
    if armes_final:
        for idx,w in enumerate(armes_final,1):
            fiche_lines.append(f"  - Arme {idx} : {w['Nom']} — {w['Expr']} — Taille {w['Taille']} — {w['Maniement']} — {w['Rareté']}")
    else:
        fiche_lines.append("  Aucune")
    fiche_lines.append("")
    fiche_lines.append("Armures :")
    display_order = ["Tête","Épaule gauche","Épaule droite","Torse","Avant-bras gauche","Avant-bras droite","Jambes","Bottes gauche","Bottes droite","Bouclier"]
    for slot in display_order:
        info = final_armure.get(slot)
        if not info:
            fiche_lines.append(f"  - {slot} : Aucune")
            continue
        if slot == "Bouclier" and info:
            b = info
            fiche_lines.append("  ┌────────────────────────────────────────┐")
            fiche_lines.append(f"  │ {b['Nom']}")
            fiche_lines.append("  ├────────────────────────────────────────┤")
            fiche_lines.append(f"  │ Protection : {b['Armure']}")
            fiche_lines.append(f"  │ Set : {b['Set']} | Rareté : {b['Rareté']}")
            fiche_lines.append(f"  │ Emplacement : {b['Emplacement_note']} (codes {b['Emplacement_codes']})")
            fiche_lines.append("  └────────────────────────────────────────┘")
            continue
        if info.get("present", True) is False:
            fiche_lines.append(f"  - {slot} : Aucune")
        else:
            fiche_lines.append("  ┌────────────────────────────────────────┐")
            fiche_lines.append(f"  │ {info['piece']}")
            fiche_lines.append("  ├────────────────────────────────────────┤")
            fiche_lines.append(f"  │ Protection : {info['armure']}")
            if info.get("degats"):
                fiche_lines.append(f"  │ Dégâts infligeables : {info['degats']}")
            fiche_lines.append(f"  │ Set : {info['set']} | Rareté : {info['rarete']}")
            fiche_lines.append(f"  │ Emplacement : {slot} | Valeur emplacement : {info.get('slots_str','')}")
            fiche_lines.append("  └────────────────────────────────────────┘")

    fiche_lines.append("════════════════════════════════════════════════")
    return "\n".join(fiche_lines)

# ---------------------------
# EXECUTION (script autonome)
# ---------------------------
if __name__ == "__main__":
    print(generer_orc())
