label losebattle:
    "kalah lawan anomali"
    return

label game_over:
    scene toko
    "gagal"
    return

label selesai:
    scene toko
    if score<=0:
        "Oi, oi, yang bener aje."
    elif score<=5:
        "waduh, belajar lagi"
    else :
        "Loh?"
    "selesai"
    return