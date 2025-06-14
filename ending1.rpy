label act1_1_ram:
    scene lobiuefi

    mc1 "Aku mau cek RAM dulu. Kalau memang bootloadernya belum tersalin, akan ku cek SSD."
    uefi1 "Baik, Tuan. hati-hati di jalan."
    uefi2 "Akan saya antar, Tuan."

    stop music fadeout 2
    play sound "audio/sound/ローファー.mp3"

    scene ramroom-chaos
    with fade
    
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
    $ renpy.pause(1.0, hard=True)
    mc1 "......"
    $ renpy.pause(1.0, hard=True)
    mc1 ".........!"
    $ renpy.pause(1.0, hard=True)
    mc1 "Hhhh! Oke, saatnya beres-beres dulu..."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "... semangat."
    play sound "sound/打撃・ビンタ音.mp3"
    with hpunch
    mc1 "Ssh!"
    mc1 "Yang nggak bantuin beres-beres diem aja!"
    uefi2 "Akan saya bantu, Tuan."

    jump act2_1_ram_minigame

    return

label act2_1_ram_minigame:
    $ setup_files()
    call screen manage_files
    return

label act2_1_ramdone:
    stop music fadeout 2
    play music "music/Disital_Delta.mp3" fadein 2
    
    mc1 "Sudah ku pindai, memang bootloader belum tersalin."
    mc1 "[nama2], apa jalur ke SSD bisa di akses?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Bisa, namun ada sesuatu yang sedikit aneh. Beberapa kali peta di lorong menuju SSD glitch."
    mc1 "Glitch? Oke, terimakasih infonya. Kalau begitu, aku minta akses debugging tool."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Hm? Apa ada firasat?"
    mc1 "Untuk jaga-jaga."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Oke."
    a "{b}Debugging Tool{/b} digunakan untuk mendeteksi, menganalisis, dan memperbaiki kesalahan (bug) dalam program atau sistem, seperti menampilkan error, melacak alur program, memeriksa nilai variabel saat program, berjalan, dan lainnya."
    a "NOVA memberikan bentuk Debugging Tool sebagai senjata (weapon) yang digunakan Diver untuk mengatasi bug dalam sistem. Bentuknya menyerupai kursor raksasa, digunakan bagai pisau bilah pendek."
    play sound "audio/sound/システム決定音_9.mp3"
    mc2 "Akses sudah di approve, ya. Jangan sembarangan dipakai."
    mc1 "Oke, terima kasih."
    uefi2 "Anu, kertas-kertas yang tercabik ini dikemanakan, Tuan?"
    mc1 "Benar juga, tadi ada visual robekan kertas yang berhamburan."
    mc1 "Sebentar, ya..."
    italic "Lebih baik tanya [nama2] dulu..."
    mc1 "[nama2], waktu aku membereskan Ruang Arsip RAM, ada visualisasi berkas yang tampak seperti kertas robek. coba pindai dari sebelah sana sebagai Navigator, apa ada sesuatu yang kurang atau ada keanehan?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Hmm? Aneh."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "NOVA seharusnya hanya menyajikan simulasi visual untuk memudahkan pemahaman sehingga semua benda di-generate dalam kondisi ideal, bukan tampilan yang menunjukkan kerusakan fisik seperti kertas robek."
    mc1 "Kan? Ada yang janggal."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Ah!"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sudah selesai ku pindai, tidak ada yang aneh. Langsung pergi juga tak apa."

    jump hint_branch

    return

label hint_branch:
    menu:
        mc1 "Hmm..."

        "Antar ke Partisi SSD untuk mengambil bootloader":
            mc1 "Anu, bisa antar saya ke Partisi SSD yang menyimpan bootloader?"
            uefi2 "Baik, Tuan [nama1]"
            italic "[nama1] segera meninggalkan Ruang Arsip RAM dan menuju ke arah Partisi SSD diantar oleh [uefi2]."
            jump act2_2_ssd

        "Aku coba cek dulu robekan kertasnya":
            jump act2_1_ram_hint

label act2_1_ram_hint:
    mc1 "Permisi, robekan kertasnya boleh saya lihat?"
    italic "[uefi2] memberikan serpihan kertas pada [nama1] yang segera menjajarkannya di lantai."
    mc1 "Coba aku satukan dulu serpihannya."
    $ setup_puzzle()
    call screen reassemble_puzzle

    return

label act2_1_connecting:
    play music "music/pandora.mp3" fadein 2
    $ renpy.music.set_volume(0.4, channel="music")
    scene lorong
    show screen locinfo("Connecting Bridge")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    show iotechvirus
    with hpunch
    uefi3 "!"
    play sound "audio/sound/打撃・ビンタ音.mp3"
    hide iotechvirus
    show iotech3
    with hpunch
    uefi3 "Tolong kembali! Disini ada Teknisi IO yang terkena virus!"
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    mc1 "Eh?"
    hide iotech3
    with dissolve
    show iotech2
    with dissolve
    uefi2 "Kami tidak deteksi apa-apa sebelumnya. Saya laporkan pada front."
    play sound "audio/sound/LAPUTA_alert.mp3"
    italic "[uefi2] melaporkan situasi melewati radio komunikasi."
    uefi2 "Permisi, saya harus ambil alat-alat pencegahan dari front."
    play sound "audio/sound/急ぐ足音.mp3"
    hide iotech2
    with dissolve
    show iotechvirus
    with dissolve
    italic "Teknisi yang berada di hadapan [nama1] terlihat tidak terkendali. Penutup matanya sudah lepas, menampakkan mata merah menyala."

    show iotechvirus:
        xalign 0.2
        yalign 1.0
    with moveinleft
    show mcnovafight:
        xalign 0.8
        yalign 1.0
    with moveinright

    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    mc1 "Minggir, akan kuselesaikan."
    
    stop music fadeout 2.0

    jump act2_1_connecting_minigame
    
    return

label act2_1_connecting_minigame:
    play sound "audio/sound/システム決定音_11.mp3"
    show screen mission_splash("Battle Start!")
    $ renpy.pause(2.5)
    hide screen mission_splash

    play music "audio/music/Certain_Curse.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    jump act2_1_connecting_moveset

    return

label act2_1_connectingdone:
    scene lorong
    with fade

    hide screen healthpoint
    hide screen enemyhp

    show iotechvirus
    with vpunch

    mc1 "Hhh... siapa sangka ada virus di sini. Menyerahlah!"
    italic "Teknisi yang terkena virus masih terdiam namun tubuhnya tidak bergerak. Untuk berjaga-jaga, [nama1] menyuruh [uefi2] untuk menahan Teknisi tersebut."
    hide iotechvirus
    with dissolve
    show iotechviruskeep
    with dissolve
    italic "[uefi2] mengeluarkan alat seperti Lampu LED Emergency Portable dan mengarahkannya pada Teknisi yang terkena virus."
    italic "Seketika bayangan tipis berbentuk balok mengurung Teknisi tersebut."
    italic "[nama1] maju dan mengeluarkan debugging tool : scan. Digunakan untuk memindai virus untuk mengetahui apakah ada sesuatu yang dibawa atau dihilangkan, juga untuk melihat daya gangguan yang dimiliki virus."
    stop music
    hide iotechvirus
    with dissolve
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    mc1 "Wah?"
    italic "[nama1] menemukan berkas dengan tanda bootloader."

    play music "audio/music/Disital_Delta.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    mc1 "Bootloader sudah berhasil di recovery."
    uefi2 "Baik"
    play sound "audio/sound/LAPUTA_alert.mp3"
    italic "[uefi2] mematikan transmisi."
    uefi2 "Baik, Tuan [nama1], silakan berikan bootloader-nya, saya akan mengantarkannya langsung ke lantai OS."
    mc1 "Oke, akan kutunggu di Lobi UEFI."

    play sound "audio/sound/ローファー.mp3"

    scene lobiuefi
    with fade
    show screen locinfo("Lobi Inisiasi : UEFI")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    play sound "audio/sound/キーボードで入力する音.mp3"
    uefi1 "Bootloader sudah diantarkan ke Lantai OS, memulai booting."
    mc1 "[nama2], bagaimana di luar sana, apa laptop bekerja dengan baik?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sudah bekerja dengan baik, tapi layarnya masih hitam. Mari kita tunggu sebentar lagi."

    $ renpy.pause(3.0, hard=True)

    mc1 "Euh... [nama2]?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Haha, memang belum bisa ternyata..."

    jump act2_1_quiz1

    return
#act2_1_quiz1

label act3_1_gpu:
    play sound "audio/sound/ローファー.mp3"

    scene gpuroom
    with fade

    show screen locinfo("GPU : Studio Visual")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    italic "Lampu-lampu dalam Studio Visual mulai menyala tanda booting sudah sukses. Di sana, para teknisi segera menyiapkan hal yang diperlukan, seperti menyusun piksel, efek, elemen visual, dan lainnya."
    play sound "audio/sound/ローファー.mp3"
    mc1 "Hmm?"
    uefi3 "Ah, halo Tuan."
    italic "Suara yang familiar memanggilmu."
    uefi3 "Sedang mengecek Studio Visual, ya."
    stop music fadeout 2
    play sound "audio/sound/ミステリー音.mp3"
    show iotech3
    with flash
    mc1 "..."
    italic "[nama1] tak mengatakan apapun, namun tatapannya menyiratkan kebingungan."
    uefi3 "Kalau begitu, saya permisi dulu."
    play sound "audio/sound/ローファー.mp3"
    hide iotech3
    with dissolve
    italic "[uefi3] berjalan santai melewati [nama1]."
    mc1 "..."
    show iotech2
    with dissolve
    uefi2 "Permisi Tuan, saya kembali."
    mc1 "Hei, apa kamu kenal dengan teknisi barusan? Kalian papasan di pintu keluar, kan?"
    uefi2 "?"
    uefi2 "Tidak ada yang aneh dari teknisi tadi."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    italic "[nama1] menepuk dahi dirinya sendiri, merasa bodoh."
    mc1 "{i}Tentu saja. Mereka kan hanya visualisasi dari NOVA, bukan entitas nyata.{/i}"
    mc1 "[nama2], aku merasa ada yang mengganjal. Ada salah satu 'teknisi' yang terlihat aneh, seperti dia hanya mondar-mandir tanpa pekerjaan."
    mc1 "Kulihat ada beberapa... mungkin tidak banyak, tapi tetap ada. Sesuatu terasa janggal. Teknisi IO tidak seharusnya bersantai atau mondar-mandir tanpa tujuan, bukan? Mereka bukan manusia... lalu, untuk apa melakukan semua itu?"
    play sound "audio/sound/ミステリー音.mp3"
    mc2 "Eeh? Masuk akal."

    stop music fadeout 2.0

    jump act3_1_quiz1

    return
#act3_1_quiz1
#act3_1_quiz2

label act3_1_eeprom:
    play music "audio/music/Another_World.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    italic "[nama1] terdiam sedikit lebih lama untuk berpikir."
    mc1 "Kamu,"
    show iotech2
    with dissolve
    uefi2 "Ya?"
    mc1 "Coba antar aku ke Ruang Archive Protokol Firmware : EEPROM."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Apa ada ide?"
    play sound "audio/sound/システム決定音_9.mp3"
    italic "Suara 'approve' terdengar walau [nama1] belum meminta akses menuju EEPROM."
    mc1 "Aku mau cek sesuatu."
    hide iotech2
    with dissolve

    play sound "audio/sound/ローファー.mp3"
    scene ramroom
    with fade
    show screen locinfo("Ruang Archive Protokol Firmware : EEPROM")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    italic "[nama1] membukan laci satu dan lainnya, mencari sesuatu."
    play sound "audio/sound/ミステリー音.mp3"
    mc1 "Ah! Akhirnya ketemu."
    italic "[nama1] mengeluarkan debugging toolnya lagi untuk memindai dokumen itu."
    mc1 "Bisa aku minta list private key dari vendor AMI untuk laptop model ini?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sekarang? Request ini bakal memakan waktu yang sedikit lama, loh. Aku harus menghubungi pihak vendor dulu soalnya."
    mc1 "Tak apa."
    play sound "audio/sound/ローファー.mp3"
    italic "[nama1] berjalan pelan ke pinggir ruangan, duduk di lantai untuk istirahat."
    $ renpy.pause(3.0)
    italic "Tiga jam berlalu, [nama2] menghidupkan kembali alat komunikasi."
    $ renpy.pause(1.0)
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Hei, [nama1], jangan tidur dulu. Sudah ku kirim private key-nya, ya."
    italic "[nama1] menyentuh kotak penyimpanan digital yang ada di dada kirinya, layar hologram muncul, menampilkan binary file yang berisi deretan huruf. Itu adalah bentuk encoded dalam format Base64."
    mc1 "Wow, kamu bisa dapatkan ini dalam waktu tiga jam? Ternyata kerjasama NOVA dengan vendor-vendor nggak main-main."
    a "{b}Private Key{/b} adalah kode rahasia dalam kriptografi yang digunakan oleh vendor untuk membuat tanda tangan digital (signature) yang membuktikan bahwa firmware tersebut asli dan belum dimodifikasi."
    a "Private key tidak boleh bocor. Jika bocor, siapa pun bisa membuat firmware palsu dengan signature yang seolah-olah valid."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Yah, ada harga, ada kualitas. Lagipula, tidak semua orang bisa memiliki NOVA."
    mc1 "... kau benar. Berapa perjanjian yang harus kita tanda tangani... apalagi menunggu waktu verifikasi yang lumayan lama juga."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Yap, itu penting agar tidak ada celah kejahatan."
    italic "[nama1] melakukan crosscheck antara signature dengan private key milik vendor."
    stop music fadeout 1.0
    play sound "audio/sound/ネガティブズーン.mp3"
    mc1 "Ketakutanku terbukti. Signature pada firmware ini rusak."
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    mc2 "Rusak??"
    a "{b}Signature{/b} merujuk pada tanda tangan digital yang digunakan untuk memverifikasi bahwa firmware berasal dari sumber resmi dan belum mengalami perubahan sejak dibuat."
    a "Signature dalam firmware tergantung pada vendor pembuatnya. Jika tanda tangan digital ini berbeda, bahkan sedikit saja, maka firmware tersebut bisa dianggap tidak asli, rusak, termodifikasi, atau terinfeksi malware."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "OK, jadi kali ini karena apa rusaknya? Apa jangan-jangan virus?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Maksudku, tadi kita sempat bertemu teknisi yang terjangkit virus."
    mc1 "Bisa jadi."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    mc1 "Pause seluruh pekerjaan dan coba crosscheck seluruh teknisi dan perintah yang mereka terima."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Oke, pekerjaan sudah di pause. Untuk mengecek perintah tiap teknisi, kamu bisa pindai menyeluruh."

    jump act3_1_mebromi
    #jump vidcutscene
    return

#label vidcutscene:
    $ renpy.movie_cutscene("oa4_launch.webm")
    jump act1_whatsnova

    return

label act3_1_mebromi:
    scene ramroom
    
    play sound "audio/sound/ミステリー音.mp3"
    show mcnovaring
    with hpunch
    mc1 "kamu?!"
    hide mcnovaring
    play sound "audio/sound/え？どうしたの？.mp3"
    show iotech3
    with hpunch
    uefi3 "Eh? Iya, Tuan??"
    
    jump act3_1_quiz3
    return