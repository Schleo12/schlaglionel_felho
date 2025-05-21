def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor
diagrammot hoz létre a napok számáról és a csillagok számáról valamint a hőmérséklet adatairól

def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")
    print("-" * 40)

    for i in range(len(homersekletek)):
        nap = i + 1  # Napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)

diagrammot rajzol a napi átlag hőmérsékletről aminél a napok számát valamint azok hőmérsékletét veszi alapul 


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

rajzolj_diagram(napi_atlaghomersekletek)


