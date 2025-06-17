#Character
define mc1=Character("[nama1]", who_bold=True)
define mc2=Character("[nama2]", who_bold=True, who_color="#30e5f9")
define klien=Character("Mary", who_bold=True, who_color="#dc8c8d")
define uefi1=Character("IO Tech 1023345", who_bold=True, who_color="#bd75b7")
define uefi2=Character("IO Tech 1023123", who_bold=True, who_color="#969ecf")
define uefi3=Character("IO Tech 1455690", who_bold=True, who_color="#cf8f2c")
define mebromi=Character("Mebromi", who_bold=True, who_color="#cf8f2c")
define chiefcpu=Character("IO Tech 1126480", who_bold=True, who_color="#4aacb2")

#Text
define a=Character(
    None,
    window_background=None,
    what_outlines=[( 1, "#06405b", 0, 0)],
    what_italic=True,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define italic=Character(
    None,
    what_italic=True)

screen locinfo(text):
    frame:
        background None
        xalign 0.5
        yalign 0.1
        text "[text]" size 40 bold True

screen mission_splash(text):
    frame:
        background None
        xalign 0.5
        yalign 0.5
        text "[text]" size 40 bold True

#mechanics
init python:
    health_value=100
    thinking_value=100
    enemyhp_value=100
    score=10 #untuk penilaian pemain di akhir

    def update_thinking(val):
        global thinking_value
        thinking_value = max(0, min(thinking_value+val, 100))

screen healthpoint():
    frame:
        xalign 0.98
        ypos 100
        ysize 650
        hbox:
            spacing 10
            vbar value AnimatedValue(health_value, 100, 0.5)

screen enemyhp():
    frame:
        xalign 0.02
        ypos 100
        ysize 650
        hbox:
            spacing 10
            vbar value AnimatedValue(enemyhp_value, 100, 0.5)

screen thinkingpoint():
    frame:
        xalign 0.94
        ypos 100
        ysize 650
        hbox:
            spacing 10
            vbar value AnimatedValue(thinking_value, 100, 0.5)

screen score():
    frame:
        xalign 0.99 ypos 30
        text "Skor : [score]":
            size 30

#misc
define flash = Fade(0.2, 0.0, 0.8, color='#fff')

label start:
    show screen score
    scene toko
    play music "music/Ravioli.mp3" fadein 2
    $ renpy.music.set_volume(0.4, 0.6, channel="music")
 

    show screen locinfo("SchnellFix Service Center")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    #Opening
    klien "Iya, sudah saya bawa ke service center sebelumnya, awalnya bisa dinyalakan, namun, tidak berapa lama, kembali mati lagi, jadi saya coba ke toko ini."

    show mary2
    with dissolve

    "Ooh, begitu. Masalahnya apa, Bu Mary?"

    klien "Layarnya mati walau lampu di tombol powernya sudah nyala, bahkan mesinnya pun sudah terdengar."

    show mary2:
        xalign 0.8
        yalign 1.0
    with moveinright

    show friendidle:
        xalign 0.2
        yalign 1.0
    with dissolve

    a "Kamu mendengarkan keluhan-keluhan Bu Mary panjang lebar sambil mengira-ngira akar dari kendala tersebut, sementara rekanmu disamping mencatat detail-detail dari keluhan Bu Mary, jaga-jaga jika kamu terlewat atau melupakan beberapa detail."

    klien "Baik, berarti saya ambil paling cepat berapa hari, ya? Anu, dengan pak siapa?"

    scene cutscene1
    with dissolve

    #input nama
    $ nama1 = renpy.input("{i}Namamu?{size=-5}  tekan enter untuk skip{/size}{/i}", length=20)
    $ nama1 = nama1.strip()
    if not nama1:
        $ nama1 = "Noa"
    mc1 "saya [nama1] dan dia..."

    $ nama2 = renpy.input("{i}Nama rekanmu?{size=-5}  tekan enter untuk skip{/size}{/i}", length=20)
    $ nama2 = nama2.strip()
    if not nama2:
        $ nama2 = "Franz"
    mc2 "[nama2]."

    klien "Baik Pak [nama1], Pak [nama2], kalian, kan, punya NOVA, seharusnya bisa selesai cepat, kan?"
    italic "[nama2] menutup note digitalnya dengan seringai tipis."
    mc1 "Tentu saja. Bu Mary."
    italic "Ucap [nama1] penuh percaya diri."

    stop music fadeout 2

    window hide

    show screen mission_splash("Misi SchnellFix Service Center menggunakan teknologi NOVA DIMULAI!")
    play sound "sound/システム決定音_11.mp3"
    $ renpy.pause(2.5)
    hide screen mission_splash

    scene toko
    with fade

    play music "music/モノクロライブラリー.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    show screen thinkingpoint
    show friendidle

    italic "Aku dan [nama2] membongkar dan mengecek hardware laptop Bu Mary, namun semuanya terlihat baik-baik saja, hanya butuh sedikit bersih-bersih saja."

    hide friendidle
    show friendidle2
    mc2 "Hhh... kalau sudah begini, saatnya lihat dari dalam."

    italic "Mary pamit undur diri, keluar melalui pintu kaca. Kebetulan ini masih sangat pagi dan belum ada klien lain, [nama2] mengusulkan untuk segera mengecek laptop Mary."

    hide friendidle2
    show friendidle

    mc1 "Sesuai kata Bu Mary, memang terlihat nyala laptopnya, tetapi layarnya tetap hitam."

    hide friendidle

    jump act1_quiz1
    return
#act1_quiz1
#act1_quiz2

#label opening:
    $ renpy.movie_cutscene("oa4_launch.webm")
    jump act1_whatsnova

    return

label act1_whatsnova:
    scene lorong
    with fade
    play music "music/Tactics.Shimtone.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    
    a "{b}NOVA{/b} atau Neural Operation Virtual Access adalah teknologi terbaru yang akhir-akhir viral, khususnya dikalangan penggiat informatika. Untuk mendapatkan device ini dibutuhkan 6 bulan antri."

    a "Pengguna NOVA minimal ada dua orang, yang masuk ke dalam dunia virtual, disebut sebagai {b}“Diver”{/b}, dan yang menjaga dari dunia nyata, disebut sebagai {b}“Navigator”{/b}. Orang yang menggunakan NOVA akan memasuki zona waktu khusus yang bisa diatur oleh navigator."

    a "NOVA berisi empat komponen. Komponen pertama dan kedua adalah {b}NeuroDriver{/b}, alat seperti bando yang bisa menghubungkan sinyal otak dengan sistem NOVA untuk ditransfer ke dalam NeuroLink USB dan EchoLink Hub dengan metode penyamaan frekuensi otak."

    a "NeuroDriver digunakan diver untuk mentransfer kesadarannya ke dalam komputer melalui NeuroLink USB, sementara bagi navigator, alat ini berfungsi untuk menavigasi dan memantau informasi menyeluruh tentang kondisi komputer secara langsung saat proses terjadi."

    a "Komponen ketiga, {b}NeuroLink USB{/b}, yang berguna untuk memungkinkan pemilik USB tersebut berinteraksi langsung ke dalam komputer. NeuroLink USB menangkap frekuensi otak yang sudah dikonversi oleh NeuroDriver lalu menyalurkannya ke sistem NOVA."

    a "Kesadaran atau sinyal tersebut menjelma menjadi avatar virtual dan bisa menjelajahi sistem komputer dengan leluasa. Pemilik bisa menggerakkan avatar untuk menemukan, memperbaiki, atau mengecek error pada komputer secara interaktif agar pemilik bisa lebih paham dengan keadaan komputer."

    a "Komponen keempat, {b}EchoLink Hub{/b} yang digunakan asisten dari pemakai NeuroLink USB, digunakan untuk komunikasi dan navigasi dari dunia luar."

    play sound "sound/システム決定音_9.mp3"
    italic "[nama1] menancapkan NeuroLink USB ke laptop klien lalu memakai NeuroDriver di kepala."
    
    mc1 "Aku serahkan padamu, ya, Tuan Navigator."

    mc2 "Santai, Diver. lagian siapa yang ngajarin kamu, heh?"

    mc1 "Iya, iya."

    italic "[nama2] memakai EchoLink Hub yang terlihat penuh dikepalanya.[nama2] bersiap di set up mejanya untuk memulai menavigasi Diver. [nama1] menyamankan diri di atas kursi malas, memejamkan mata bersiap untuk Diving."

    stop music fadeout 2

    jump act1_post
    return

label act1_post:
    scene lobiuefi
    with fade

    show screen locinfo("Lobi Inisiasi : UEFI")
    with dissolve

    mc1 "Kembali lagi ke sini..."
    window hide
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    play sound "audio/sound/急ぐ足音.mp3"
    $ renpy.pause(1.0, hard=True)
    play sound "sound/打撃・ビンタ音.mp3"
    show iotech3
    with hpunch

    mc1 "Aduh!"
    play sound "sound/打撃・ビンタ音.mp3"
    uefi3 "Uhh!"
    with hpunch
    uefi3 "Mohon maaf!"
    hide iotech3

    play sound "sound/どうしたの？？.mp3"
    mc1 "... dan Teknisi IO itu pergi begitu saja."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Ada apa [nama1]?"
    italic "Suara [nama2] berdengung di kepalamu karena jalur komunikasi langsung dari otak ke otak."
    mc1 "Ga. Gapapa."

    play music "music/Disital_Delta.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    italic "Lobi UEFI terlihat memang terlihat sibuk, banyak Teknisi IO berlalu-lalang untuk mempersiapkan laptop."

    italic "Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan."

    show iotech1
    with dissolve

    play sound "audio/sound/キーボードで入力する音.mp3"
    uefi1 "Euh..."

    italic "Teknisi yang berada dibalik counter terlihat sedikit cemas, apa mungkin ada kendala?"

    jump act1_quiz3
    return
#act1_quiz3

label act1_alrzone:
    scene lorong
    with fade
    play sound "audio/sound/ローファー.mp3"
    italic "Menuju Ruang CPU dengan Connecting Bridge."
    italic "Ditengah perjalanan, lampu dan cahaya kebiruan dari kabel-kabel yang menjalar hidup-mati dengan aneh."
    italic "Bahkan Teknisi IO yang mengantarnya terdiam di tempat."

    show mcnovaidle2
    with dissolve
    mc1 "Ada yang nggak beres."
    hide mcnovaidle2

    italic "[nama1] menekan tombol dari modul yang ada di dada kirinya. Layar hologram muncul, menampilkan beberapa menu."
    italic "[nama1] mengaktifkan Zona Pemulihan Logika Buatan dan mendekati [uefi2]- Teknisi yang tadi sedang mengantarnya."
    show kekkai
    with dissolve
    a "Zona ALR, atau Artificial Logic Recovery Zone, adalah salah satu fitur milik NOVA khusus untuk Diver."
    a "Zona ini menciptakan ruang terbatas yang independen dari kondisi sistem utama perangkat, memungkinkan unit dasar seperti Teknisi tetap aktif meski lingkungan aslinya lumpuh."
    a "Kekurangan atau kesalahan yang membuat Teknisi tidak bisa berfungsi akan ditambal oleh sistem milik NOVA sehingga teknisi bisa tetap berfungsi, selama Teknisi itu berada dalam jangkauan Zona ALR."
    mc1 "Kamu, jangan jauh-jauh dariku."
    mc1 "{i}Tidak ada gunanya menjelaskan tentang Zona ALR pada Teknisi. Mereka hanya visualisasi sistem saja.{/i}"
    uefi2 "Baik."
    italic "Sesuai dugaan [nama1], Teknisi tersebut berlaku selayaknya tidak ada yang salah."
    play sound "audio/sound/ローファー.mp3"
    italic "Mereka melanjutkan perjalanan menuju CPU: Ruang Kendali."

    jump act1_cpu
    return

label act1_cpu:
    play music "music/pandora.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    scene cutscene2-alr
    with fade

    show screen locinfo("CPU: Ruang Kendali")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    play sound "sound/え？どうしたの？.mp3"
    mc1 "...!!"
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    mc1 "apa-apaan!"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "kenapa [nama1]? Ada apa?"
    italic "Ruang CPU dipenuhi oleh pekerja yang berbaris rapih menghadap ke arah yang sama. Mereka diam seribu bahasa, mengantisipasi perintah yang entah kapan munculnya, tidak seperti Teknisi IO di Lobi UEFI yang sibuk berlalu-lalang."
    mc1 "Aah! Pantas saja Lobi UEFI tidak dapat kabar dari CPU..."

    jump act1_quiz4
    return
#act1_quiz4

label act1_cpu_minigame:
    $ setup_cable_game()
    call screen connect_the_cables
    return

label act1_cpudone:
    hide cable_game_success

    mc1 "Untung hanya masalah sedikit, tidak sampai perlu ganti komponennya di dunia nyata."
    mc1 "[nama2], catat untuk Bu Mary, kalau pakai laptop, pastikan sumber listriknya stabil. Tegangan yang nggak stabil bisa bikin clock generator error."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Siap!"
    italic "[nama1] mematikan Zona ALR melalui layar hologram yang dipancarkan modul di dada kirinya."
    hide kekkai
    with dissolve
    show iotechchiefcpu
    with dissolve
    play sound "audio/sound/ローファー.mp3"
    italic "[chiefcpu] menghampiri [nama1]."
    stop sound
    chiefcpu "Terima kasih. Karena detak jam untuk jadwal kami sudah diperbaiki, kami akan memulai bekerja."

    play sound "audio/sound/ローファー.mp3"
    hide iotechchiefcpu
    with dissolve

    italic "[chiefcpu] hilang begitu saja, membaur dengan teknisi lain, bekerja dengan giat."

    show iotech2
    with dissolve

    uefi2 "Baik, mari saya antar kembali ke Lobi."

    play sound "audio/sound/ローファー.mp3"
    scene lobiuefi
    with fade
    
    show screen locinfo("Lobi Inisiasi : UEFI")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    show iotech1
    with dissolve

    mc1 "Silakan coba booting lagi"
    uefi1 "Baik."
    play sound "audio/sound/キーボードで入力する音.mp3"
    italic "[uefi1] mulai menjalankan perintah booting. Namun layar holografik di lobi menunjukkan peringatan merah. [uefi1] mulai terlihat gugup lagi."
    stop music fadeout 1.0
    play sound "audio/sound/ミステリー音.mp3"
    uefi1 "I- instruksi booting tidak bisa dilanjutkan."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with vpunch
    mc1 "Eh? Kenapa lagi?"
    uefi1 "CPU melaporkan bahwa instruksi tidak bisa dilanjutkan karena berkas bootloader todak ada di memori."
    play sound "audio/sound/ミステリー音.mp3"
    mc1 "Memori...? Maksudmu RAM?"
    uefi1 "Benar. RAM: Ruang Transit Data seharusnya menjadi tempat sementara bagi bootloader sebelum dijalankan."
    mc1 "Jadi kemungkinan... data bootloader belum pernah sampai ke sana?"
    uefi1 "Itu yang saya khawatirkan. Jika memang tidak sempat tersalin, Tuan harus mencarinya langsung dari sumber aslinya."

    jump act1_quiz5
    return
#act1_quiz5

label bootloader_branch:
    scene lobiuefi

    menu:
        mc1 "Sebaiknya..."

        "langsung cek ESP di SSD: Gudang Data":
            jump act1_3_esp
        
        "cek RAM: Ruang Transit Data terlebih dahulu":
            jump act1_1_ram
    
    return