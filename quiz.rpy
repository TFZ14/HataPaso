#timer
default retrace = None

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
init:
    $ timer_range=0
    $ timer_jump=0
    $ time=0
    $ mayoi=0 #level tersesat (interogasi)
    #untuk penilaian pemain di akhir
    $ score=0
    $ act1=0
    $ act2=0
    $ act3=0

screen countdown:
    timer 0.01 repeat True action If(time>0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.04 xmaximum 900 at alpha_dissolve

label zoneout:
    with vpunch
    play sound "sound/打撃・ビンタ音.mp3"
    mc2 "Woy, bangun!"
    with vpunch
    play sound "sound/打撃・ビンタ音.mp3"
    mc2 "Malah ngelamun!"
    play sound "audio/sound/どうしたの？？.mp3"
    mc1 "Maaf, maaf, tadi kamu ngomong apa?"
    $ thinking_value-=5

    jump expression retrace
    return

#semua rute
label act1_quiz1:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act1_quiz1'
    $ time=20
    $ timer_range=20.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show friendidle2

    menu:
        
        mc2 "hmm... pertama-tama, kita cek apanya dulu, ya?"

        "Ganti RAM":
            hide screen countdown
            stop sound
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Oi, oi, yang bener aja..."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz1 #Kembali ke menu pilihan

        "Cek kabel monitor":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Aah, benar juga, walau bisa menyala, kalau kabel monitor longgar atau rusak, layar tetap mati."
            $ score+=5
            $ act1+=5

        "Reset UEFI":
            hide screen countdown
            stop sound
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... langsung banget nih?"
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
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

    $ retrace='act1_quiz2'
    $ time=20
    $ timer_range=20.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show screen thinkingpoint
    scene toko

    show friendidle2

    menu:
        mc2 "Benar, mungkin bisa kita urut dari awal seperti POST {i}(Power-On Self Test) yang dilakukan oleh...{/i}"

        "UEFI":
            hide screen countdown
            stop sound
            hide friendidle2
            show friendidle
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Oooh! Oke, akan ku kirim ke Lobi UEFI, ya!"
            $ score+=5
            $ act1+=5

        "CPU":
            hide screen countdown
            stop sound
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan

        "ALU":
            hide screen countdown
            stop sound
            hide friendidle2
            show friendconfuse
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan
    
    mc1 "Ok, aku siapkan NOVA-nya."
    hide screen thinkingpoint
    with dissolve

    stop music fadeout 3

    jump act1_whatsnova
    #jump opening
    return

label act1_quiz3:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act1_quiz3'
    $ time=20
    $ timer_range=20.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show screen thinkingpoint
    with dissolve
    
    menu :
        mc1 "Biasanya, jika POST di UEFI memiliki kendala, itu karena..."

        "Komputer kehabisan baterai CMOS":
            hide screen countdown
            stop sound
            with vpunch
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            mc2 "... kayaknya bukan, deh. Baterai CMOS berpengaruh pada penyimpanan pengaturan, bukan langsung ke POST."
            italic "Suara [nama2] berdengung di kepalamu."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value <= 0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz3

        "Perangkat keras gagal terdeteksi oleh sistem":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "Jika {i}Hardware{/i} (perangkat keras) gagal dideteksi oleh sistem saat POST, maka akan gagal booting."
            italic "Suara [nama2] berdengung di kepalamu."
            $ score+=5
            $ act1+=5

        "Driver belum diinstal":
            hide screen countdown
            stop sound
            with vpunch
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            mc2 "... hmm, driver penting setelah OS jalan, tapi POST bekerja sebelum sistem operasi aktif."
            italic "Suara [nama2] berdengung di kepalamu."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz3

    hide screen thinkingpoint
    with dissolve
    stop music fadeout 2.0
    play music "music/Disital_Delta.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

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

    jump act1_alrzone
    return

label act1_quiz4:
    $ retrace='act1_quiz4'
    $ time=20
    $ timer_range=20.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop
    
    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Ternyata, mereka tidak terjadwal dan terkoordinasi dengan baik dikarenakan..."

        "Ruang RAM tidak cukup besar":
            hide screen countdown
            stop sound
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... kayaknya bukan, deh... RAM memang penting, tapi ini soal koordinasi kerja."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<= 0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz4

        "Karena GPU tidak terhubung":
            hide screen countdown
            stop sound
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "... hmm, GPU memang penting, tapi ini bukan tugas utamanya..."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz4

        "Clock Generatornya rusak":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Tanpa Clock Generator yang aktif, tidak ada yang mengatur kapan para pekerja CPU harus bergerak..."
            mc1 "Seperti orkestra tanpa konduktor."
            $ score+=5
            $ act1+=5

    a "Clock Generator menentukan kecepatan kerja komponen dalam satuan MHz atau GHz. Clock Generator mengirim sinyal denyut {i}(clock pulse){/i} agar data diproses secara teratur dan terkoordinasi."

    hide screen thinkingpoint
    with dissolve

    play sound "audio/sound/ミステリー音.mp3"
    mc1 "...dan Clock Generatornya rusak"
    italic "[nama1] mengurut kening pusing."
    italic "[nama1] berjalan mendekat Teknisi yang terlihat sebagai pemimpin kelompok tersebut. Teknisi itu menoleh ke arah [nama1] ketika Zona ALR yang mengenai tubuhnya."
    scene cpuroom
    with fade
    show iotechchiefcpu
    with dissolve
    show kekkai
    with dissolve

    chiefcpu "Tuan [nama1], ada apa ya?"
    mc1 "Ada masalah di Clock Generatornya makanya kalian tidak bisa bekerja. Coba aku cek dulu, dimana panel kontrolnya?"
    chiefcpu "Sebelah sini..."
    italic "[chiefcpu] mengantar [nama1] ke arah panel kontrol."

    jump act1_cpu_minigame
    return

label act1_quiz5:
    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act1_quiz5'
    $ time=20
    $ timer_range=20.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Sumber utama bootloader..."

        "SSD: Gudang Data":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "lebih spesifiknya, bootloader disimpan di partisi khusus ESP dalam SSD atau hard drive"
            $ score+=5
            $ act1+=5

        "RAM: Ruang Transit Data":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            uefi1 "Anu... tadi sudah bicara hal yang sama. Bootloader memang diload di RAM, tapi tempat awalnya bukan dari sana."
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz5

        "GPU: Studio Visual":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Hei! GPU berfungsi untuk rendering grafis, bukan tempat penyimpanan bootloader!"
            $ thinking_value-=5
            $ score-=5
            $ act1-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act1_quiz5

    a "ESP atau EFI (Extensible Firmware Interface) System Partition adalah partisi khusus pada hard drive atau SSD yang berisi file bootloader dan konfigurasi lainnya. Jika ESP hilang atau rusak, maka sistem tidak bisa booting meskipun OS masih utuh."

    hide screen thinkingpoint
    with dissolve

    jump bootloader_branch
    return

#rute ending 1
label act2_1_quiz1:
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act2_1_quiz1'
    $ time=15
    $ timer_range=15.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show screen thinkingpoint
    with dissolve

    mc1 "Hanya layar yang tidak berfungsi, mungkin kita harus mengecek komponen yang berhubungan dengan pemrosesan grafik yaitu..."

    menu:
        "Cek kabel monitor":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Bukan kabel... kan, tadi sudah kita cek diawal."
            $ thinking_value-=5
            $ score-=5
            $ act2-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act2_1_quiz1
            
        "GPU: Studio Visual":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Mungkin aku harus cek GPU: Studio Visual."
            $ score+=5
            $ act2+=5

        "Driver Grafis - Teknisi Penerjemah Grafis":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            uefi1 "Yang benar saja, kita bahkan belum bisa masuk ke sistem operasi, jadi, driver belum bisa bekerja."
            $ thinking_value-=5
            $ score-=5
            $ act2-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act2_1_quiz1

    a "GPU atau Graphic Processing Unit adalah komponen komputer yang berfungsi untuk memproses dan menampilkan grafis, gambar, dan video. Jika GPU tidak bisa bekerja, maka laptop tidak bisa menampilkan informasi."

    hide screen thinkingpoint

    mc1 "Minta akses masuk GPU: Studio Visual, [nama2]."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sedang diminta."
    $ renpy.pause(2.5, hard=True)
    play sound "audio/sound/システム決定音_9.mp3"
    mc2 "Ok, sudah bisa."
    play sound "audio/sound/急ぐ足音.mp3"
    show iotech1
    with moveinright
    uefi1 "Sebentar, Tuan, teknisi lain akan mengantar anda."
    stop sound
    mc1 "Ah, sampaikan padanya untuk menyusul aku di GPU: Studio Visual."
    uefi1 "Baik."
    hide iotech1
    with dissolve
    scene lorong
    with fade
    play sound "audio/sound/ローファー.mp3"
    italic "[nama1] berjalan menuju GPU: Studio Visual melewati lorong."

    jump act3_1_gpu

    return

label act3_1_quiz1:
    #scene gpu
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act3_1_quiz1'
    $ time=10
    $ timer_range=10.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    show screen thinkingpoint
    with dissolve

    mc2 "Jika ada sebagian teknisi UEFI kehilangan arah tentang apa yang harus mereka kerjakan, kira-kira masalahnya ada di..."

    menu:   
        mc2 "Jika ada sebagian teknisi UEFI kehilangan arah tentang apa yang harus mereka kerjakan, kira-kira masalahnya ada di..."

        "Firmware - pedoman kerja":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "Karena Firmware bagaikan protokol resmi. Jika ada masalah pada Firmware, bisa jadi teknisi-teknisi ada yang tidak memiliki pedoman untuk bekerja."
            mc2 "Benar."
            $ score+=5
            $ act3+=5

        "Kerusakan fisik EEPROM - Kerusakan Kantor":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Kerusakan fisik EEPROM sangat jarang dan biasanya tidak akan menimbulkan kebingungan teknisi, namun kegagalan pembacaan firmware yang mengakibatkan seluruh teknisi samasekali tidak mendapat perintah."
            mc2 "Jadi, kalau memang benar fisik EEPROM rusak, seharusnya, sejak awal POST tidak bisa dilakukan."
            $ thinking_value-=5
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz1

        "RAM: Ruang Transit Data berantakan - urutan perintah tidak beraturan":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Tadi kan sudah kamu bereskan sendiri??"
            mc2 "Lagi pula, RAM akan mulai terisi saat proses boot, tapi teknisi UEFI tidak tergantung pada berkas di RAM."
            $ thinking_value-=5
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz1
    
    jump act3_1_quiz2
    
    return

label act3_1_quiz2:
    play music "audio/music/モノクロライブラリー.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    $ retrace='act3_1_quiz2'
    $ time=10
    $ timer_range=10.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    mc1 "Dan Firmware disimpan di..."
    
    menu:
        mc1 "Dan Firmware disimpan di..."

        "CPU Cache":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "CPU Cache adalah memori kecil untuk mempercepat proses CPU, bukan tempat menyimpan firmware."
            $ thinking_value-=5
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz2

        "GPU: Studio Visual":
            hide screen countdown
            stop sound
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Euh... kamu sakit???"
            play music "audio/music/さがしもの.mp3"
            $ renpy.music.set_volume(0.4, channel="music")
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Berapakali kubilang, GPU itu komponen untuk memproses data grafis dan visual!"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Bahkan kamu belum beranjak dari GPU, bisa-bisanya!"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc1 "Ampuuun! Ampuuun!!"
            italic "[nama1] diomeli habis-habisan oleh [nama2]."
            $ thinking_value-=15
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz2
        
        "Chip EEPROM - Ruang Archive Protokol Firmware":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc2 "firmware biasanya disimpan di EEPROM — chip memori kecil yang menyimpan kode permanen yang bisa di-update."
            $ score+=5
            $ act3+=5

    jump act3_1_eeprom

    return

#2 question
label act3_1_quiz3:
    play music "audio/music/Chain_Datura.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    screen ramroom

    $ mayoi=0

    show screen thinkingpoint
    with dissolve

    show mcnovafight
    with hpunch
    mc1 "Kamu ada urusan apa ke EEPROM?"
    hide mcnovafight
    show iotech3
    uefi3 "Saya akan melakukan pengecekan rutin saat protokol awal yaitu checksum."

    $ time=10
    $ timer_range=10.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    menu:
        uefi3 "Saya hanya melakukan verifikasi rutin yaitu checksum."

        "Percaya":
            hide screen countdown
            stop sound
            hide iotech3
            show mcnovaidle2
            mc1 "..."
            a "checksum adalah urutan angka dan huruf yang digunakan untuk memeriksa kesalahan data."
            a "Saat data dikirim atau disimpan, sistem menghitung nilai checksum, yang biasanya berupa hash atau angka tertentu, dan mengecek ulang nanti apakah nilai tersebut masih cocok."
            a "Kalau tidak cocok, berarti datanya kemungkinan rusak atau dimodifikasi."
            a "Checksum bisa dilakukan di berbagai tahap sistem komputer seperti saat POST untuk mengecek apakah UEFI rusak atau komponen seperti RAM, GPU, dan storage masih berfungsi dengan baik."
            a "Contoh lainnya ialah saat bootloader akan dimuat, checksum digunakan untuk mengecek apakah bootloader ini sudah di modifikasi atau tidak."
            mc1 "Oke, tapi sebelum mengecek, biarkan aku menanyaimu sampai aku puas."
            hide mcnovaidle2
            show iotech3
            uefi3 "Baik, Tuan."
            $ score+=5
            $ act3+=5

        "Tidak percaya":
            hide screen countdown
            stop sound
            hide iotech3
            play sound "audio/sound/ミステリー音.mp3"
            show mcnovaidle2
            mc1 "... mencurigakan."
            hide mcnovaidle2
            show iotech3
            uefi3 "Dimananya Tuan?"
            hide iotech3
            show mcnovaidle2
            mc1 "Kamu cuma alasan melakukan checksum agar bisa masuk EEPROM, kan?"
            hide mcnovaidle2
            show iotech3
            play sound "audio/sound/どうしたの？？.mp3"
            uefi3 "Maaf, saya tidak mengerti maksud Tuan."
            uefi3 "Atau begini, Tuan paham, kan, apa itu checksum?"
            hide iotech3
            play sound "audio/sound/打撃・ビンタ音.mp3"
            with vpunch
            show mcnovafight
            mc1 "Tentu saja!"

            $ time=10
            $ timer_range=10.5
            $ timer_jump='zoneout'
            show screen countdown
            play sound "audio/sound/LAPUTA_counter.mp3" loop
            
            menu:
                mc1 "Checksum itu..."
                
                "Checksum adalah file cadangan yang menyimpan salinan lengkap dari sistem operasi.":
                    hide screen countdown
                    stop sound
                    stop music
                    play sound "audio/sound/LAPUTA_alert.mp3"
                    mc2 "Sudah lah, [nama1], jangan permalukan dirimu lagi."
                    hide mcnovafight
                    show mcnovaring
                    with hpunch
                    mc1 "Eh??"
                    play sound "audio/sound/LAPUTA_alert.mp3"
                    mc2 "Yang kamu jawab itu definisi dari backup..."
                    $ thinking_value-=15
                    hide mcnovaring
                    show iotech3
                    uefi3 "..."
                    uefi3 "Sepertinya Tuan memang kurang paham... kalau begitu, permisi saya izin melanjutkan kerjaan."
                    hide iotech3
                    show mcnovaidle2
                    play sound "audio/sound/ネガティブズーン.mp3"
                    mc1 "Tch."
                    hide mcnovaidle2
                    show mcnovafight
                    with hpunch
                    mc1 "Biarkan aku tanya satu lagi!"
                    $ mayoi+=5

                "Checksum adalah nilai numerik yang dihasilkan dari data untuk memverifikasi integritas.":
                    hide screen countdown
                    stop sound
                    hide mcnovafight
                    show iotech3
                    uefi3 "..."
                    hide iotech3
                    show mcnovafight
                    mc1 "Checksum digunakan untuk mendeteksi kesalahan pada data."
                    mc1 "Saat data dikirim atau disimpan, sistem menghitung nilai checksum, yang biasanya berupa hash atau angka tertentu, dan mengecek ulang nanti apakah nilai tersebut masih cocok."
                    mc1 "Kalau tidak cocok, berarti datanya kemungkinan rusak atau dimodifikasi."
                    hide mcnovafight
                    stop music
                    show iotech2
                    with dissolve
                    uefi2 "..."
                    hide iotech2
                    show iotech3
                    with dissolve
                    uefi3 "..."
                    mc2 "..."
                    uefi3 "... Tuan hanya mengulangi perkataan saya sebelumnya. Sudah saya katakan, saya hanya ingin melakukan verifikasi rutin, Kenapa tadi Tuan tidak percaya saya?"
                    hide iotech3
                    play sound "audio/sound/ミステリー音.mp3"
                    show mcnovaidle2
                    with flash
                    mc1 "Ah-"
                    $ thinking_value-=15
                    italic "[nama1] bisa mendengar [nama2] mengerang malu, lelah dengan kelakuan [nama1] yang tidak masuk akal."
                    hide mcnovaidle2
                    show mcnovaidle
                    mc1 "Ahaha..."
                    hide mcnovaidle
                    show iotech3
                    uefi3 "kalau begitu, permisi saya izin melanjutkan kerjaan."
                    hide iotech3
                    show mcnovafight
                    with hpunch
                    mc1 "Biarkan aku tanya satu lagi!"
                    $ mayoi+=5
                    
                "Checksum adalah alat fisik di motherboard yang mempercepat koneksi internet.":
                    hide screen countdown
                    stop sound
                    stop music
                    play sound "audio/sound/LAPUTA_alert.mp3"
                    mc2 "Sudah lah, [nama1], jangan permalukan dirimu lagi."
                    hide mcnovafight
                    show mcnovaring
                    with hpunch
                    mc1 "Eh??"
                    mc1 "A- aku salah, kah?"
                    play sound "audio/sound/打撃・ビンタ音.mp3"
                    with vpunch
                    mc2 "BANGET!!"
                    play sound "audio/sound/LAPUTA_alert.mp3"
                    mc2 "Checksum bukan perangkat keras, melainkan bagian dari proses perangkat lunak. Lagipula, mempercepat internet juga tidak ada hubungannya dengan checksum—yang tugasnya hanya memastikan data tidak korup atau rusak."
                    $ thinking_value-=15
                    hide mcnovaring
                    show iotech3
                    uefi3 "..."
                    uefi3 "Sepertinya Tuan memang kurang paham... kalau begitu, permisi saya izin melanjutkan kerjaan."
                    hide iotech3
                    show mcnovaidle2
                    play sound "audio/sound/ネガティブズーン.mp3"
                    mc1 "Tch."
                    hide mcnovaidle2
                    show mcnovafight
                    with hpunch
                    mc1 "Biarkan aku tanya satu lagi!"
                    $ mayoi+=5
            $ mayoi+=5

    jump act3_1_quiz4
    return

label act3_1_quiz4:
    play music "audio/music/Chain_Datura.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    scene ramroom

    show mcnovafight
    mc1 "Kita sempat papasan di GPU: Studio Visual..."
    mc1 "Apa yang kamu lakukan di sana?"
    hide mcnovafight
    show iotech3
    uefi3 "Saya hanya lewat saja, Tuan."
    hide iotech3
    show mcnovafight
    mc1 "Lewat?"
    hide mcnovafight
    show iotech3
    uefi3 "Saya tidak ada tugas di sana. Saya sungguhan hanya mampir."

    $ time=10
    $ timer_range=10.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    menu:
        "Percaya":
            hide screen countdown
            stop sound
            hide iotech3
            show mcnovaidle2
            mc1 "Yah... kalau dipikir-pikir, memang tidak ada keganjilan apapun. sih, di GPU: Studio Visual."
            hide mcnovaidle2
            show iotech3
            uefi3 "Sudah? Saya izin melanjutkan kerjaan, Tuan."
            hide iotech3
            play sound "audio/sound/ミステリー音.mp3"
            show mcnovafight
            with flash
            mc1 "Uit!! Satu pertanyaan lagi!"
            hide mcnovafight
            show iotech3
            italic "Walau wajah [uefi3] datar, [nama1] merasa [uefi3] sedikit jengkel."
            uefi3 "Baik, beneran terakhir, ya. Kalau bisa dipercepat."
            $ mayoi+=5
            
        "Tidak Percaya":
            hide screen countdown
            stop sound
            hide iotech3
            play sound "audio/sound/打撃・ビンタ音.mp3"
            show mcnovafight
            with hpunch
            mc1 "Kalau memang tidak ada tugas di sana, kenapa datang ke GPU: Studio Visual?"
            play sound "audio/sound/LAPUTA_alert.mp3"
            with hpunch
            mc2 "Ah! Benar juga."
            mc1 "Tiap Teknisi memiliki tugasnya masing-masing, sesuai protokol."
            mc1 "Dan Teknisi bukan lah makhluk yang bisa memikirkan hal lain selain tugasnya sendiri."
            mc1 "Yang bisa melakukan hal itu hanya lah manusia..."
            play sound "audio/sound/ネガティブズーン.mp3"
            mc1 "Dan malware yang memang tidak memiliki kewajiban untuk mengikuti protokol!"
            hide mcnovafight
            play sound "audio/sound/打撃・ビンタ音.mp3"
            show iotech3
            with vpunch
            uefi3 "Ah-"
            $ score+=5
            $ act3+=5
            $ thinking_value+=10

    jump act3_1_quiz5
    return

#2 Pertanyaan
label act3_1_quiz5:
    play music "audio/music/Chain_Datura.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    screen ramroom

    show mcnovafight
    italic "Semua mulai terlihat jelas."
    mc1 "Jangan-jangan, pertemuan pertama kita bukan suatu kebetulan..."

    $ time=5
    $ timer_range=5.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    menu:
        mc1 "Pertama kali kita bertemu adalah saat aku baru memasuki sistem yang pertama kali aktif ketika komputer dinyalakan, yaitu..."

        "SSD: Gudang Data - ESP: Partisi Khusus":
            hide screen countdown
            stop sound
            play sound "audio/sound/ミステリー音.mp3"
            show mcnovafight
            with flash
            mc1 "Kita bertemu di ESP!"
            hide mcnovafight
            show iotech2
            stop music
            play music "audio/music/さがしもの.mp3"
            $ renpy.music.set_volume(0.4, channel="music")
            uefi2 "Maksud Tuan, kita bertemu dia sebelum Tuan menuju ESP?"
            play sound "audio/sound/ミステリー音.mp3"
            hide iotech2
            show mcnovaidle2
            with hpunch
            mc1 "Eh?"
            play sound "sound/打撃・ビンタ音.mp3"
            with vpunch
            mc2 "Woy!"
            play sound "audio/sound/LAPUTA_alert.mp3"
            mc2 "ESP adalah partisi di hard disk atau SSD yang menyimpan bootloader. Ada program lain yang dijalankan sebelum bootloader di load."
            play sound "sound/打撃・ビンタ音.mp3"
            mc2 "Lagian mana ada aku kirim kamu ke ESP, pertamakali aku kirim kamu bukan ke ESP!"
            $ thinking_value-=20
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz5

        "Driver - Teknisi Penerjemah":
            hide screen countdown
            stop sound
            play sound "audio/sound/ミステリー音.mp3"
            show mcnovafight
            with flash
            mc1 "Kita ketemuan sama teknisi penerjemah, kan!"
            a "Driver itu seperti penerjemah antara hardware dan sistem operasi. Mereka dibutuhkan untuk membuat hardware berfungsi, tapi mereka dimuat setelah firmware awal berjalan dan biasanya setelah sistem operasi mulai dimuat. Jadi, mereka bukan komponen yang pertama kali berjalan sendiri saat komputer dihidupkan."
            hide mcnovafight
            show iotech3
            uefi3 "..."
            stop music
            play sound "sound/打撃・ビンタ音.mp3"
            hide iotech3
            show mcnovaring
            with vpunch
            mc2 "Kamu gaada cerita ketemuan sama Driver?"
            hide mcnovaring
            play sound "sound/打撃・ビンタ音.mp3"
            show iotech2
            with vpunch
            uefi2 "Seingat saya, Tuan tidak bertemu Teknisi Penerjemah manapun."
            play sound "audio/sound/LAPUTA_alert.mp3"
            mc2 "Hhhh... skizo."
            hide iotech2
            $ thinking_value-=20
            $ score-=5
            $ act3-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                mc2 "[nama1]!"
                jump game_over
            else:
                jump act3_1_quiz5

        "Chip EEPROM - Lobi UEFI":
            hide screen countdown
            stop sound
            play sound "sound/システムSE_決定音1.mp3"
            mc1 "{i}Yep! Firmware utama, seperti UEFI atau BIOS, tersimpan di dalam chip memori khusus di motherboard, yang seringkali adalah EEPROM... atau jenis Flash memory serupa. Ketika komputer dinyalakan, CPU akan langsung menjalankan instruksi dari chip ini terlebih dahulu.{/i}"
            $ score+=5
            $ act3+=5

    scene ramroom
    with dissolve
    show mcnovaidle2
    mc1 "Kamu waktu itu ada di Lobi UEFI, kan? Kamu ngapain di sana?"
    hide mcnovaidle2
    show iotech3
    uefi3 "Saya... saya buru-buru ke CPU untuk bekerja. Tapi sebelum masuk, saya melihat clock generatornya rusak."
    uefi3 "Saya laporkan ini ke [uefi1], Teknisi yang ada dibalik counter di Lobi UEFI."
    uefi3 "Setelahnya, saya dapat pekerjaan baru, jadi saya segera menuju tempat yang diinstruksikan oleh protokol kerja."

    $ time=5
    $ timer_range=5.5
    $ timer_jump='zoneout'
    show screen countdown
    play sound "audio/sound/LAPUTA_counter.mp3" loop

    menu:
        "Percaya":
            hide screen countdown
            stop sound
            hide iotech3
            show mcnovaidle2
            mc1 "..."
            mc1 "Masuk akal..."
            italic "Tapi, kok, aku rasa ada yang mengganjal, ya..."
            italic "Apa..."
            $ mayoi+=10
            jump ending_1

        "Tidak percaya":
            hide screen countdown
            stop sound
            hide iotech3
            play sound "audio/sound/ミステリー音.mp3"
            show mcnovaidle2
            mc1 "CPU hanya bisa bekerja jika mendapat sinyal dari clock generator. Tanpa clock, CPU tidak bisa mengeksekusi apa pun, termasuk program POST."
            mc1 "Jadi, jika clock rusak, semua proses akan terhenti."
            play sound "audio/sound/打撃・ビンタ音.mp3"
            with vpunch
            mc1 "Dan semua Teknisi terhenti!"
            play sound "audio/sound/システムSE_決定音1.mp3"
            hide mcnovaidle2
            show iotech3
            with hpunch
            show correct
            uefi3 "Ah!"
            hide correct
            $ score+=5
            $ act3+=5
            $ thinking_value+=10

    jump ending_1
    return
