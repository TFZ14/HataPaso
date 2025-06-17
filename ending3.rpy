init:
    $ ending=0
label act1_3_esp:
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
    italic "Disana, mereka berpapasan dengan Teknisi yang familiar."
    uefi3 "Akan ke SSD: Gudang Data, ya, Tuan?"
    italic "Sapa teknisi tadi dengan ramah."
    hide iotech3
    show mcnovaidle
    mc1 "Benar. Semangat kerja, ya."
    italic "[nama1] hanya menyapanya singkat dan melanjutkan perjalanan ke SSD: Ruang Data."

    stop music
    scene ramroom
    with fade
    show iotech4
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    uefi4 "!!"
    hide iotech4

    play music "audio/music/Scary_Shaper.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    play sound "audio/sound/打撃・ビンタ音.mp3"
    show mcnovafight
    with vpunch
    mc1 "Apa yang kamu lakukan!!"
    italic "[nama1] melihat [uefi4] seperti merusak salah satu brankas. Disekitar brankas banyak kabel-kabel yang langsung terhubung pada kepalanya."
    hide mcnovafight
    play sound "audio/sound/打撃・ビンタ音.mp3"
    show iotechvirus
    with hpunch
    italic "[uefi4] melepas paksa kabel-kabel itu dan mulai menyerang [nama1] bagai orang gila."
    hide iotechvirus
    play sound "audio/sound/打撃・ビンタ音.mp3"
    show mcnovafight
    with hpunch
    mc1 "AWAS!"
    italic "[nama1] refleks mendorong [uefi2] mundur dan menahan serangan dari [uefi3]."

    play sound "audio/sound/打撃・ビンタ音.mp3"
    scene lorong
    with hpunch

    italic "Serangan [uefi3] mementalkan [nama1] sampai ke lorong connecting bridge."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "[nama1]!"
    show mcnovafight
    with dissolve
    italic "[nama1] berdiri dan menyiapkan kuda-kuda."

    stop music fadeout 1.0
    play sound "audio/sound/システム決定音_11.mp3"
    show screen mission_splash("Battle Start!")
    $ renpy.pause(2.5)
    hide screen mission_splash

    play music "audio/music/Certain_Curse.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    $ ending=3

    jump act2_1_connecting_moveset
    return

label closing_3:
    play music "audio/music/Ravioli.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    scene black
    with fade

    show screen mission_splash("Kamu menyelesaikan misi dengan baik. Tinggal tunggu klien untuk mengambil laptop.")
    with dissolve
    $ renpy.pause(8.0)
    show screen mission_splash("Keesokan harinya, Bu Mary datang untuk mengambil laptop miliknya. Bu Mary berterimakasih dan pamit pulang dengan senyuman.")
    with dissolve
    $ renpy.pause(8.0)
    show screen mission_splash("Namun, beberapa hari kemudian, Bu Mary kembali lagi ke SchnellFix Service Center dengan wajah muram.")
    with dissolve
    $ renpy.pause(8.0)
    hide screen mission_splash
    with dissolve

    scene toko
    with dissolve
    show side mcidle
    mc1 "Wah, bukannya ini Bu Mary? Silakan, silakan, apa ada yang bisa kami bantu?"
    hide side mcidle
    show mary2
    with dissolve
    klien "Anu... memang laptop saya kemarin sudah benar, namun kenapa, ya, kinerjanya sedikit lebih lambat dari yang saya ingat?"
    stop music
    play sound "audio/sound/ミステリー音.mp3"
    show mary2:
        xalign 0.2
        yalign 1.0
    with moveinleft
    show friendconfuse:
        xalign 0.8
        yalign 1.0
    with moveinright
    mc2 "Wah, kok, bisa, Bu?"
    klien "Saya juga kurang tau. Waktu saya tanya-tanya teman, katanya ada masalah memori. Tapi, memori mana saya juga kurang paham."
    hide friendconfuse
    show friendidle2:
        xalign 0.8
        yalign 1.0
    play music "audio/music/Ravioli.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    mc2 "Baik, Bu. Akan kami periksa lagi. Dan juga, di toko kami ada garansi 30 hari, jadi, Bu Mary tidak usah bayar lagi, ya."
    klien "Baik, terimakasih, ya."
    hide mary2
    show friendidle2:
        xalign 0.5
        yalign 1.0
    with moveinleft
    mc2 "Mungkin ada yang terlewat saat kemarin mengecek. Coba kali ini aku yang nge-Dive, kamu jadi Navigator dulu."
    mc1 "Oh, oke."
    hide friendidle
    
    italic "Saat di cek ulang, ternyata hanya masalah minor, tidak ada malware yang mengganggu."
    italic "Kini laptop Bu Mary benar-benar sembuh."

    jump selesai

    return