label act2_2_ssd:
    scene lorong
    with fade
    
    play sound "audio/sound/ローファー.mp3"
    show screen locinfo("Connecting Bridge")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    italic "[nama1] dan [uefi2] berjalan menuju SSD melewati Connecting Bridge."
    show iotech3
    with dissolve
    italic "Disana, mereka berpapasan dengan beberapa teknisi."
    uefi3 "Akan ke SSD: Gudang Data, ya, Tuan?"
    italic "Sapa teknisi tadi dengan ramah."
    hide iotech3
    show mcnovaidle
    mc1 "Benar. Semangat kerja, ya."
    italic "[nama1] hanya menyapanya singkat dan melanjutkan perjalanan ke SSD: Ruang Data."

    scene ramroom
    with fade
    show iotech4
    italic "Sesaat [nama1] akan masuk ke SSD: Gudang Data, ia hampir menabrak teknisi yang sedang bertugas."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    uefi4 "Ah! Maaf Tuan."
    hide iotech4
    play sound "audio/sound/打撃・ビンタ音.mp3"
    show mcnovaidle2
    with hpunch
    mc1 "Tidak, apa-apa. Maaf tidak hati-hati."
    hide mcnovaidle2
    italic "Setelahnya, teknisi itu melangkahkan kaki keluar."
    italic "[nama1] berjalan ke arah rak-rak untuk memindai apakah bootloader ada di sini atau tidak."
    stop music
    play sound "audio/sound/ネガティブズーン.mp3"
    mc1 "Tidak ada..."
    show mcnovaring
    with dissolve
    italic "[nama1] mencoba menghubungi [nama2]."
    mc1 "Hei, bisa kamu pindai dari sana apakah ada bootloader?"
    mc1 "Aku akan coba pindai dari sisi sini."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Ok."
    mc1 "Ah, satu lagi. Berikan perintah global agar semua teknisi berkumpul di Lobi UEFI."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Ok. Anggap udah selesai."

    jump act2_2_uefigather
    return

label act2_2_uefigather:
    play music "audio/music/Another_World.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    scene lobiuefi
    with fade

    show iotech1:
        xalign 0.01
        yalign 1.0
    show iotech3:
        xalign 0.35
        yalign 1.0
    show iotech4:
        xalign 0.65
        yalign 1.0
    show iotechchiefcpu:
        xalign 0.98
        yalign 1.0

    italic "[nama1] berdiri di depan kumpulan teknisi untuk memindai mereka satu persatu."
    italic "Namun, tidak ada tanda-tanda bootloader ditemukan."
    hide iotech1
    hide iotech3
    hide iotech4
    hide iotechchiefcpu
    with dissolve
    italic "Bahkan [nama2] sebagai Navigator pun tidak menemukan tanda-tanda bootloader di mana pun."
    stop music
    play sound "audio/sound/古いロボットの音.mp3"
    scene lobiuefidark
    with hpunch
    italic "Saat [nama1] sedang berpikir, tiba-tiba guncangan terjadi, seluruh pencahayaan meredup."
    play sound "audio/sound/ミステリー音.mp3"
    with vpunch
    mc1 "Hah!"
    italic "[nama1] buru-buru memencet modul di dada kirinya, menampilkan layar hologram. Ia memilih menu untuk Log Out sebelum kesadarannya terperangkap di laptop Bu Mary"
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    mc1 "Aku tidak bisa log out??"
    italic "Astaga..."
    italic "Astaga, astaga..."

    jump losebattle

    return