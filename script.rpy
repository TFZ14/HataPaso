#Character
define mc1=Character("[nama1]", who_bold=True)
define mc2=Character("[nama2]", who_bold=True)
define klien=Character("Mary", who_bold=True)
define uefi1=Character("IO Tech 1023345", who_bold=True)
define uefi2=Character("IO Tech 1023123", who_bold=True)
define uefi3=Character("IO Tech 1455690", who_bold=True)
define chiefcpu=Character("IO Tech 1126480", who_bold=True)

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
    mc1 "... dan petugas IO itu pergi begitu saja."
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Ada apa [nama1]?"
    italic "Suara [nama2] berdengung di kepalamu karena jalur komunikasi langsung dari otak ke otak."
    mc1 "Ga. Gapapa."

    play music "music/Disital_Delta.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")

    italic "Lobi UEFI terlihat memang terlihat sibuk, banyak Petugas IO berlalu-lalang untuk mempersiapkan laptop."

    italic "Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan."

    show iotech1
    with dissolve

    play sound "audio/sound/キーボードで入力する音.mp3"
    uefi1 "Euh..."

    italic "Teknisi yang berada dibalik counter terlihat sedikit cemas, apa mungkin ada kendala?"

    jump act1_quiz3
    return
#act1_quiz3

label act1_cpu:
    play music "music/pandora.mp3"
    $ renpy.music.set_volume(0.4, channel="music")

    scene cutscene2
    with fade

    show screen locinfo("Ruang Kendali : CPU")
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
    italic "Ruang CPU dipenuhi oleh pekerja yang berbaris rapih menghadap ke arah yang sama. Mereka diam seribu bahasa, mengantisipasi perintah yang entah kapan munculnya, tidak seperti petugas IO di Lobi UEFI yang sibuk berlalu-lalang."
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
    show iotechchiefcpu
    with dissolve
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
    mc1 "Tunggu. Kalau begitu... tempat terakhir data berada sebelum eksekusi dimulai adalah RAM, kan?"
    uefi1 "Benar. Tapi jika berkas bootloader memang tidak sempat tersalin, Tuan harus mencarinya langsung dari sumber utama..."

    jump act1_quiz5
    return
#act1_quiz5

label act2_ram_minigame:
    $ setup_files()
    call screen manage_files
    return

label act2_ramdone:
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

    menu:
        mc1 "Hmm..."

        "Antar ke Partisi SSD untuk mengambil bootloader":
            mc1 "Anu, bisa antar saya ke Partisi SSD yang menyimpan bootloader?"
            uefi2 "Baik, Tuan [nama1]"
            italic "[nama1] segera meninggalkan Ruang Arsip RAM dan menuju ke arah Partisi SSD diantar oleh [uefi2]."
            jump act2_connecting

        "Aku coba cek dulu robekan kertasnya":
            jump act2_ram_hint

    return

label act2_ram_hint:
    mc1 "Permisi, robekan kertasnya boleh saya lihat?"
    italic "[uefi2] memberikan serpihan kertas pada [nama1] yang segera menjajarkannya di lantai."
    mc1 "Coba aku satukan dulu serpihannya."
    $ setup_puzzle()
    call screen reassemble_puzzle

    return

label act2_connecting:
    play music "music/pandora.mp3" fadein 2
    $ renpy.music.set_volume(0.4, channel="music")
    scene lorong
    show screen locinfo("Connecting Bridge")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    show iotech3
    uefi3 "!"
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    uefi3 "Tolong kembali! Disini ada Teknisi IO yang terkena virus!"
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

    jump act2_connecting_minigame
    
    return

label act2_connecting_minigame:
    play sound "audio/sound/システム決定音_11.mp3"
    show screen mission_splash("Battle Start!")
    $ renpy.pause(2.5)
    hide screen mission_splash

    play music "audio/music/Certain_Curse.mp3" fadein 1
    $ renpy.music.set_volume(0.4, channel="music")

    jump act2_connecting_moveset

    return

label act2_connectingdone:
    scene lorong
    with fade

    hide screen healthpoint
    hide screen enemyhp

    show iotechvirus
    with vpunch

    mc1 "Hhh... siapa sangka ada virus di sini. Mundur, biar aku pindai untuk berjaga-jaga."
    italic "[nama1] maju dan mengeluarkan debugging tool : scan. Digunakan untuk memindai virus untuk mengetahui apakah ada sesuatu yang dibawa atau dihilangkan, juga untuk melihat daya gangguan yang dimiliki virus."
    with hpunch
    stop music
    play sound "audio/sound/ミステリー音.mp3"
    mc1 "Wah?"
    hide iotechvirus
    with dissolve
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

    uefi1 "Bootloader sudah diantarkan ke Lantai OS, memulai booting."
    mc1 "[nama2], bagaimana di luar sana, apa laptop bekerja dengan baik?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Sudah bekerja dengan baik, tapi layarnya masih hitam. Mari kita tunggu sebentar lagi."

    $ renpy.pause(3.0, hard=True)

    mc1 "Euh... [nama2]?"
    play sound "audio/sound/LAPUTA_alert.mp3"
    mc2 "Haha, memang belum bisa ternyata..."

    jump act2_quiz1

    return
#act2_quiz1

label act3_gpu:
    #scene gpu

    play sound "audio/sound/ローファー.mp3"
    show screen locinfo("GPU : Studio Visual")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    italic "Lampu-lampu dalam Studio Visual mulai menyala tanda booting sudah sukses. Di sana, para teknisi segera menyiapkan hal yang diperlukan, seperti menyusun piksel, efek, elemen visual, dan lainnya."
    mc1 "Hmm?"
    uefi3 "Ah, halo Tuan."
    uefi3 "Sedang mengecek Studio Visual, ya."
    stop music fadeout 2
    play sound "audio/sound/ミステリー音.mp3"
    mc1 "..."
    uefi3 "Kalau begitu, saya permisi dulu."
    italic "[uefi3] berjalan santai melewati [nama1]."
    mc1 "..."
    uefi2 "Permisi Tuan, saya kembali."
    mc1 "Hei, apa kamu kenal dengan teknisi barusan? Kalian papasan di pintu keluar, kan?"
    uefi2 "?"
    uefi2 "Tidak ada yang aneh dari teknisi tadi."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    italic "[nama1] menepuk dahi dirinya sendiri, merasa bodoh."
    mc1 "{i}Tentu saja. Mereka kan hanya visualisasi dari NOVA, bukan entitas nyata.{/i}"
    mc1 "[nama2], aku merasa ada yang mengganjal. Ada salah satu 'teknisi' yang terlihat aneh, seperti dia hanya mondar-mandir tanpa pekerjaan."
    mc1 "Kulihat ada beberapa, mungkin tidak banyak, namun ada. Sesuatu yang janggal terjadi pada Teknisi IO untuk bersantai atau mondar-mandir, bukan? Mereka juga bukan manusia, untuk apa melakukan itu semua?"
    play sound "audio/sound/ミステリー音.mp3"
    mc2 "Eeh? Masuk akal."

    stop music fadeout 2.0

    jump act3_quiz1

    return
#act3_quiz1
#act3_quiz2

label act3_eeprom:
    #scene eeprom
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

    play sound "audio/sound/ローファー.mp3"
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
    $ renpy.pause(1.0)
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

    jump act3_mebromi
    #jump vidcutscene
    return

#label vidcutscene:
    $ renpy.movie_cutscene("oa4_launch.webm")
    jump act1_whatsnova

    return

label act3_mebromi:
    play sound "audio/sound/ミステリー音.mp3"
    with hpunch
    mc1 "kamu?!"
    play sound "audio/sound/え？どうしたの？.mp3"
    with hpunch
    uefi3 "Eh? Iya, Tuan??"
    mc1 "{i}Pertamakali kita bertemu ketika aku baru masuk ke komponen yang pertamakali berjalan dibanding komponen lainnya. Komponen yang bekerja sebelum OS dimulai, yaitu{/i}"
    
    return


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