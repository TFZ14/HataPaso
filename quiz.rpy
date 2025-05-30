label act1_quiz1:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    show friendidle2

    menu:
        
        mc2 "hmm... pertama-tama, kita cek apanya dulu, ya?"

        "Ganti RAM":
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Oi, oi, yang bener aja..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz1 #Kembali ke menu pilihan

        "Cek kabel monitor":
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Aah, benar juga, walau bisa menyala, kalau kabel monitor longgar atau rusak, layar tetap mati."
            $ score+=5

        "Reset UEFI":
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... langsung banget nih?"
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz1

    hide friendidle2
    show friendidle

    italic "Aku dan [nama2] membongkar dan mengecek hardware laptop Bu Mary, namun semuanya terlihat baik-baik saja, hanya butuh sedikit bersih-bersih saja."

    hide friendidle
    show friendidle2
    mc2 "Hhh... kalau sudah begini, saatnya lihat dari dalam."

    jump act1_quiz2

    return

label act1_quiz2:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    show screen thinkingpoint
    scene toko

    show friendidle2

    menu:
        mc2 "Benar, mungkin bisa kita urut dari awal seperti POST {i}(Power-On Self Test) yang dilakukan oleh...{/i}"

        "UEFI":
            hide friendidle2
            show friendidle
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Oooh! Oke, akan ku kirim ke Lobi UEFI, ya!"
            $ score+=5

        "CPU":
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan

        "ALU":
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan
    
    mc1 "Ok, aku siapkan NOVA-nya."
    hide screen thinkingpoint
    with dissolve

    stop music fadeout 3

    jump act1_whatsnova
    return

label act1_quiz3:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    show screen thinkingpoint
    with dissolve
    
    menu :
        mc1 "Biasanya, jika POST di UEFI memiliki kendala, itu karena..."

        "Komputer kehabisan baterai CMOS":
            with vpunch
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            mc2 "... kayaknya bukan, deh. Baterai CMOS berpengaruh pada penyimpanan pengaturan, bukan langsung ke POST."
            italic "Suara [nama2] berdengung di kepalamu."
            $ thinking_value-=5
            $ score-=5
            if thinking_value <= 0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz3

        "Perangkat keras gagal terdeteksi oleh sistem":
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Jika {i}Hardware{/i} (perangkat keras) gagal dideteksi oleh sistem saat POST, maka akan gagal booting."
            italic "Suara [nama2] berdengung di kepalamu."
            $ score+=5

        "Driver belum diinstal":
            with vpunch
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            mc2 "... hmm, driver penting setelah OS jalan, tapi POST bekerja sebelum sistem operasi aktif."
            italic "Suara [nama2] berdengung di kepalamu."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz3

    hide screen thinkingpoint
    with dissolve
    stop music fadeout 2.0
    play music "music/Disital_Delta.mp3" fadein 1

    mc1 "Bagaimana? Apa ada kendala?"
    play sound "audio/sound/キーボードで入力する音.mp3"
    uefi1 "Ah Tuan [nama1], kami belum dapat laporan status dari CPU..."
    mc1 "Hmm? Baik akan ku cek."
    mc1 "[nama2], bisa aku akses CPU?"
    mc2 "..."
    $ renpy.pause(2.0, hard=True)
    play sound "audio/sound/システム決定音_9.mp3"
    mc2 "Oke, bisa."

    show iotech1:
        xalign 0.2
        yalign 1.0
    with moveinleft
    show iotech2:
        xalign 0.8
        yalign 1.0
    with moveinright

    uefi2 "Mari saya antar."

    scene lorong
    with fade
    play sound "audio/sound/ローファー.mp3"
    italic "Menuju Ruang CPU dengan Connecting Bridge."

    jump act1_cpu
    return

label act1_quiz4:
    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Ternyata, mereka tidak terjadwal dan terkoordinasi dengan baik dikarenakan..."

        "RAM tidak cukup besar":
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh... RAM memang penting, tapi ini soal koordinasi kerja."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<= 0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz4

        "Karena GPU tidak terhubung":
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... hmm, GPU memang penting, tapi ini bukan tugas utamanya..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz4

        "Clock Generatornya rusak":
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Tanpa Clock Generator yang aktif, tidak ada yang mengatur kapan para pekerja CPU harus bergerak..."
            mc1 "Seperti orkestra tanpa konduktor."
            $ score+=5

    italic "Clock Generator menentukan kecepatan kerja komponen dalam satuan MHz atau GHz. Clock Generator mengirim sinyal denyut {i}(clock pulse){/i} agar data diproses secara teratur dan terkoordinasi."

    hide screen thinkingpoint
    with dissolve

    play sound "audio/sound/ミステリー音.mp3"
    mc1 "...dan Clock Generatornya rusak"
    italic "[nama1] mengurut kening pusing."

    show iotechchiefcpu
    with dissolve

    chiefcpu "Tuan [nama1], sepertinya ada yang salah dengan Clock Generator-nya."
    mc1 "Ya, aku bisa lihat. Coba aku cek dulu, dimana panel kontrolnya?"
    chiefcpu "Sebelah sini..."

    jump act1_cpu_minigame
    return

label act1_quiz5:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")
    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Sumber utama bootloader..."

        "SSD":
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "lebih spesifiknya, bootloader disimpan di partisi khusus ESP dalam SSD atau hard drive"
            $ thinking_value+=5

        "RAM":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            uefi1 "Anu... tadi sudah bicara hal yang sama. Bootloader memang diload di RAM, tapi tempat awalnya bukan dari sana."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz5
        "GPU":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Hei! GPU berfungsi untuk rendering grafis, bukan tempat penyimpanan bootloader!"
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act1_quiz5

    italic "ESP atau Extensible Firmware Interface System Partition adalah partisi khusus pada hard drive yang berisi file bootloader dan konfigurasi lainnya. Jika ESP hilang atau rusak, maka sistem tidak bisa booting meskipun OS masih utuh."

    hide screen thinkingpoint
    with dissolve

    mc1 "Aku mau cek RAM dulu. Kalau memang bootloadernya belum tersalin, akan ku cek SSD."
    uefi1 "Baik, Tuan. hati-hati di jalan."
    uefi2 "Akan saya antar, Tuan."

    stop music fadeout 2
    play sound "audio/sound/ローファー.mp3"
    show screen locinfo("Ruang Arsip : RAM")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    with hpunch
    play sound "sound/え？どうしたの？.mp3"
    mc1 "Astaga, kenapa lagi?!"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Tenang, tenang..."
    italic "Arsip-arsip berhamburan di lantai, beberapa kertas terlihat kusut, bahkan ada yang tercabik-cabik. Namun rak penyimpanan arsip masih terlihat bagus."
    play music "music/さがしもの.mp3"
    mc1 "..."
    mc1 "......"
    mc1 ".........!"
    mc1 "Hhhh! Oke, saatnya beres-beres dulu..."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "... semangat."
    play sound "sound/打撃・ビンタ音.mp3"
    with hpunch
    mc1 "Ssh!"
    mc1 "Yang nggak bantuin beres-beres diem aja!"
    uefi2 "Akan saya bantu, Tuan."

    jump act2_ram_minigame
    return

label act2_quiz1:
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    show screen thinkingpoint
    with dissolve

    mc1 "Jika semua sudah berjalan dengan baik namun hanya layar yang tidak berfungsi, mungkin kita harus mengecek..."

    menu:
        "Cek kabel monitor":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Bukan kabel... kan, tadi sudah kita cek diawal."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act2_quiz1
            
        "GPU":
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Mungkin aku harus cek GPU: Studio Visual."
            $ thinking_value+=5

        "Driver Grafis":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            uefi1 "Yang benar saja, kita bahkan belum bisa masuk ke sistem operasi, jadi, driver belum bisa bekerja."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act2_quiz1

    italic "GPU atau Graphic Processing Unit adalah komponen komputer yang berfungsi untuk memproses dan menampilkan grafis, gambar, dan video. Jika GPU tidak bisa bekerja, maka laptop tidak bisa menampilkan informasi."

    hide screen thinkingpoint

    mc1 "Minta akses masuk GPU: Studio Visual, [nama2]."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sedang diminta."
    $ renpy.pause(2.5, hard=True)
    play sound "audio/sound/システム決定音_9.mp3"
    mc2 "Ok, sudah bisa."
    uefi1 "Sebentar, Tuan, teknisi lain akan mengantar anda."
    mc1 "Ah, sampaikan padanya untuk menyusul aku di GPU."
    uefi1 "Baik."
    italic "[nama1] berjalan menuju GPU melewati lorong."

    jump act3_gpu

    return

label act3_quiz1:
    #scene gpu
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    show screen thinkingpoint
    with dissolve

    mc2 "Jika ada teknisi UEFI kehilangan arah tentang apa yang harus mereka kerjakan, kira-kira masalahnya ada di..."

    menu:   
        "Firmware":
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Karena Firmware bagaikan protokol resmi. Jika ada masalah pada Firmware, bisa jadi teknisi-teknisi ada yang tidak memiliki pedoman untuk bekerja."
            mc2 "Benar."
            $ thinking_value+=5

        "Kerusakan fisik EEPROM":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Kerusakan fisik EEPROM sangat jarang dan biasanya tidak akan menimbulkan kebingungan teknisi, namun kegagalan pembacaan firmware."
            mc2 "Jadi, kalau memang benar fisik EEPROM rusak, seharusnya, sejak awal POST tidak bisa dilakukan."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act3_quiz1

        "RAM berantakan.":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Tadi kan sudah kamu bereskan sendiri??"
            mc2 "Lagi pula, RAM akan mulai terisi saat proses boot, tapi teknisi UEFI tidak tergantung pada berkas di RAM."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act3_quiz1
    
    jump act3_quiz2
    
    return

label act3_quiz2:
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    mc1 "Dan Firmware disimpan di..."
    
    menu:
        "CPU Cache":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "CPU Cache adalah memori kecil dan cepat untuk mempercepat proses CPU, bukan tempat menyimpan firmware."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act3_quiz2

        "GPU":
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Euh... kamu sakit???"
            play music "audio/music/さがしもの.mp3"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Berapakali kubilang, GPU itu komponen untuk memproses data grafis dan visual!"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Bahkan kamu belum beranjak dari GPU, bisa-bisanya!"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc1 "Ampuuun! Ampuuun!!"
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]..."
                jump game_over
            else:
                jump act3_quiz2
        
        "EEPROM":
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "firmware biasanya disimpan di EEPROM — chip memori kecil yang menyimpan kode permanen yang bisa di-update."
            $ thinking_value+=5

    jump act3_eeprom

    return
