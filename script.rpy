#Character
define mc1=Character("[nama1]", who_bold=True)
define mc2=Character("[nama2]", who_bold=True)
define klien=Character("Mary", who_bold=True)
define uefi1=Character("uefi 1023345", who_bold=True)
define uefi2=Character("uefi 1023123", who_bold=True)
define chiefcpu=Character("CPU 1126480", who_bold=True)

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
    what_italic=True,
)

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
    score=10 #untuk penilaian pemain di akhir

screen healthpoint():
    frame:
        xalign 0.98
        ypos 100
        ysize 650
        hbox:
            spacing 10
            vbar value AnimatedValue(health_value, 100, 0.5)

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

    show screen locinfo("SchnellFix Service Center")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    #Opening
    klien "Iya, sudah saya bawa ke service center sebelumnya, awalnya bisa dinyalakan, namun, tidak berapa lama, kembali mati lagi, jadi saya coba ke toko ini."

    show mary2

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

    window hide
    #show launch
    show screen mission_splash("Misi SchnellFix Service Center menggunakan teknologi NOVA DIMULAI!")
    $ renpy.pause(2.5)
    hide screen mission_splash

    scene toko
    with fade
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

label act1_quiz1:
    show friendidle2

    menu:
        
        mc2 "hmm... pertama-tama, kita cek apanya dulu, ya?"

        "Ganti RAM":
            hide friendidle2
            show friendconfuse
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
            mc2 "Aah, benar juga, walau bisa menyala, kalau kabel monitor longgar atau rusak, layar tetap mati."
            $ score+=5

        "Reset UEFI":
            hide friendidle2
            show friendconfuse
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
    show screen thinkingpoint
    scene toko

    show friendidle2

    menu:
        mc2 "Benar, mungkin bisa kita urut dari awal seperti POST {i}(Power-On Self Test) yang dilakukan oleh...{/i}"

        "UEFI":
            hide friendidle2
            show friendidle
            mc2 "Oooh! Oke, akan ku kirim ke Lobi UEFI, ya!"
            $ score+=5

        "CPU":
            hide friendidle2
            show friendconfuse
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

    jump act1_whatsnova
    return

#label opening:
    $ renpy.movie_cutscene("oa4_launch.webm")
    jump act1_whatsnova

    return

label act1_whatsnova:
    scene lorong
    #What is NOVA
    a "{b}NOVA{/b} atau Neural Operation Virtual Access adalah teknologi terbaru yang akhir-akhir viral, khususnya dikalangan penggiat informatika. Untuk mendapatkan device ini dibutuhkan 6 bulan antri."

    a "Pengguna NOVA minimal ada dua orang, yang masuk ke dalam dunia virtual, disebut sebagai {b}“Diver”{/b}, dan yang menjaga dari dunia nyata, disebut sebagai {b}“Navigator”{/b}. Orang yang menggunakan NOVA akan memasuki zona waktu khusus yang bisa diatur oleh navigator."

    a "NOVA berisi empat komponen. Komponen pertama dan kedua adalah {b}NeuroDriver{/b}, alat seperti bando yang bisa menghubungkan sinyal otak dengan sistem NOVA untuk ditransfer ke dalam NeuroLink USB dan EchoLink Hub dengan metode penyamaan frekuensi otak."

    a "NeuroDriver digunakan diver untuk mentransfer kesadarannya ke dalam komputer melalui NeuroLink USB, sementara bagi navigator, alat ini berfungsi untuk menavigasi dan memantau informasi menyeluruh tentang kondisi komputer secara langsung saat proses terjadi."

    a "Komponen ketiga, {b}NeuroLink USB{/b}, yang berguna untuk memungkinkan pemilik USB tersebut berinteraksi langsung ke dalam komputer. NeuroLink USB menangkap frekuensi otak yang sudah dikonversi oleh NeuroDriver lalu menyalurkannya ke sistem NOVA."

    a "Kesadaran atau sinyal tersebut menjelma menjadi avatar virtual dan bisa menjelajahi sistem komputer dengan leluasa. Pemilik bisa menggerakkan avatar untuk menemukan, memperbaiki, atau mengecek error pada komputer secara interaktif agar pemilik bisa lebih paham dengan keadaan komputer."

    a "Komponen keempat, {b}EchoLink Hub{/b} yang digunakan asisten dari pemakai NeuroLink USB, digunakan untuk komunikasi dan navigasi dari dunia luar."

    italic "[nama1] menancapkan NeuroLink USB ke laptop klien lalu memakai NeuroDriver di kepala."
    
    mc1 "Aku serahkan padamu, ya, Tuan Navigator."

    mc2 "Santai, Diver. lagian siapa yang ngajarin kamu, heh?"

    mc1 "Iya, iya."

    italic "[nama2] memakai EchoLink Hub yang terlihat penuh dikepalanya.[nama2] bersiap di set up mejanya untuk memulai menavigasi Diver. [nama1] menyamankan diri di atas kursi malas, memejamkan mata bersiap untuk Diving."

    jump act1_post
    return

label act1_post:
    scene lobiuefi

    show screen locinfo("Lobi Inisiasi : UEFI")
    with dissolve

    mc1 "Uwaah..."
    window hide
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    italic "Lobi UEFI terlihat sibuk, banyak Petugas IO berlalu-lalang untuk mempersiapkan laptop."

    italic "Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan."

    show iotech1
    with dissolve

    uefi1 "Euh..."

    italic "Teknisi yang berada dibalik counter terlihat sedikit cemas, apa mungkin ada kendala?"

    jump act1_quiz3
    return

label act1_quiz3:
    show screen thinkingpoint
    with dissolve
    
    menu :
        mc1 "Biasanya, jika POST di UEFI memiliki kendala, itu karena..."

        "Komputer kehabisan baterai CMOS":
            with vpunch
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
            mc2 "Jika {i}Hardware{/i} (perangkat keras) gagal dideteksi oleh sistem saat POST, maka akan gagal booting."
            italic "Suara [nama2] berdengung di kepalamu."
            $ score+=5

        "Driver belum diinstal":
            with vpunch
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

    mc1 "Bagaimana? Apa ada kendala?"
    uefi1 "Ah Tuan [nama1], kami belum dapat laporan status dari CPU..."
    mc1 "Hmm? Baik akan ku cek."
    mc1 "[nama2], bisa aku akses CPU?"
    mc2 "..."
    $ renpy.pause(2.0)
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
    #add sfx langkah disini
    italic "Menuju Ruang CPU dengan Connecting Bridge."

    jump act1_cpu
    return

label act1_cpu:
    #scene bg CPU disini
    show screen locinfo("Ruang Kendali : CPU")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    mc1 "...!!"
    with hpunch
    mc1 "apa-apaan!"
    mc2 "kenapa [nama1]? Ada apa?"
    italic "Ruang CPU dipenuhi oleh pekerja yang berbaris rapih menghadap ke arah yang sama. Mereka diam seribu bahasa, mengantisipasi perintah yang entah kapan munculnya, tidak seperti petugas IO di Lobi UEFI yang sibuk berlalu-lalang."
    mc1 "Aah! Pantas saja Lobi UEFI tidak dapat kabar dari CPU..."

    jump act1_quiz4
    return

label act1_quiz4:
    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Ternyata, mereka tidak terjadwal dan terkoordinasi dengan baik dikarenakan..."

        "RAM tidak cukup besar":
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
            mc1 "Tanpa Clock Generator yang aktif, tidak ada yang mengatur kapan para pekerja CPU harus bergerak..."
            mc1 "Seperti orkestra tanpa konduktor."
            $ score+=5

    italic "Clock Generator menentukan kecepatan kerja komponen dalam satuan MHz atau GHz. Clock Generator mengirim sinyal denyut {i}(clock pulse){/i} agar data diproses secara teratur dan terkoordinasi."

    hide screen thinkingpoint
    with dissolve

    mc1 "...dan Clock Generatornya rusak"
    italic "[nama1] mengurut kening pusing."

    show iotechchiefcpu
    with dissolve

    chiefcpu "Tuan [nama1], sepertinya ada yang salah dengan Clock Generator-nya."
    mc1 "Ya, aku bisa lihat. Coba aku cek dulu, dimana panel kontrolnya?"
    chiefcpu "Sebelah sini..."

    jump act1_cpu_minigame
    return

label act1_cpu_minigame:
    $ setup_cable_game()
    call screen connect_the_cables
    return

label act1_cpudone:
    hide cable_game_success
    
    show iotechchiefcpu

    mc1 "Untung hanya masalah sedikit, tidak sampai perlu ganti komponennya di dunia nyata."
    mc1 "[nama2], catat untuk Bu Mary, kalau pakai laptop, pastikan sumber listriknya stabil. Tegangan yang nggak stabil bisa bikin clock generator error."
    mc2 "Siap!"
    chiefcpu "Terima kasih. Karena detak jam untuk jadwal kami sudah diperbaiki, kami akan memulai bekerja."

    hide iotechchiefcpu
    with dissolve

    italic "[chiefcpu] hilang begitu saja, membaur dengan teknisi lain, bekerja dengan giat."

    show iotech2
    with dissolve

    uefi2 "Baik, mari saya antar kembali ke Lobi."

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
    italic "[uefi1] mulai menjalankan perintah booting. Namun layar holografik di lobi menunjukkan peringatan merah. [uefi1] mulai terlihat gugup lagi."
    uefi1 "I- instruksi booting tidak bisa dilanjutkan."
    mc1 "Eh? Kenapa lagi?"
    uefi1 "CPU melaporkan bahwa instruksi tidak bisa dilanjutkan karena berkas bootloader todak ada di memori."
    mc1 "Tunggu. Kalau begitu... tempat terakhir data berada sebelum eksekusi dimulai adalah RAM, kan?"
    uefi1 "Benar. Tapi jika berkas bootloader memang tidak sempat tersalin, Tuan harus mencarinya langsung dari sumber utama..."

    jump act1_quiz5
    return

label act1_quiz5:
    show screen thinkingpoint
    with dissolve

    menu:
        mc1 "Sumber utama bootloader..."

        "SSD":
            mc1 "lebih spesifiknya, bootloader disimpan di partisi khusus ESP dalam SSD atau hard drive"
            $ thinking_value+=5

        "RAM":
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

    show screen locinfo("Ruang Arsip : RAM")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve

    with hpunch
    mc1 "Astaga, kenapa lagi?!"
    mc2 "Tenang, tenang..."
    italic "Arsip-arsip berhamburan di lantai, beberapa kertas terlihat kusut, bahkan ada yang tercabik-cabik. Namun rak penyimpanan arsip masih terlihat bagus."
    mc1 "..."
    mc1 "..."
    mc1 ".........!"
    mc1 "Hhhh! Oke, saatnya beres-beres dulu..."
    mc2 "... semangat."
    with hpunch
    mc1 "Ssh!"
    mc1 "Yang nggak bantuin beres-beres diem aja!"
    uefi2 "Akan saya bantu, Tuan."

    jump act2_ram_minigame
    return

label act2_ram_minigame:
    $ setup_files()
    call screen reassemble_files
    return

label act2_ramdone:
    mc1 "Sudah ku pindai, memang bootloader belum tersalin."
    mc1 "[nama2], apa jalur ke SSD bisa di akses?"
    mc2 "Bisa, namun ada sesuatu yang sedikit aneh. Beberapa kali peta di lorong menuju SSD glitch."
    mc1 "Glitch? Oke, terimakasih infonya. Kalau begitu, aku minta akses debugging tool."
    mc2 "Hm? Apa ada firasat?"
    mc1 "Untuk jaga-jaga."
    mc2 "Oke."
    a "{b}Debugging Tool{/b} digunakan untuk mendeteksi, menganalisis, dan memperbaiki kesalahan (bug) dalam program atau sistem, seperti menampilkan error, melacak alur program, memeriksa nilai variabel saat program, berjalan, dan lainnya."
    a "NOVA memberikan bentuk Debugging Tool sebagai senjata (weapon) yang digunakan Diver untuk mengatasi bug dalam sistem. Bentuknya menyerupai kursor raksasa, digunakan bagai pisau bilah pendek."
    mc2 "Akses sudah di approve, ya. Jangan sembarangan dipakai."
    mc1 "Oke, terima kasih."
    uefi2 "Anu, kertas-kertas yang tercabik ini dikemanakan, Tuan?"
    mc1 "Benar juga, tadi ada visual robekan kertas yang berhamburan."
    mc1 "Sebentar, ya..."
    mc1 "[nama2], waktu aku membereskan Ruang Arsip RAM, ada visualisasi berkas yang tampak seperti kertas robek. coba pindai dari sebelah sana sebagai Navigator, apa ada sesuatu yang kurang atau ada keanehan?"
    mc2 "Hmm? Aneh."
    mc2 "NOVA seharusnya hanya menyajikan simulasi visual untuk memudahkan pemahaman sehingga semua benda di-generate dalam kondisi ideal, bukan tampilan yang menunjukkan kerusakan fisik seperti kertas robek."
    mc1 "Kan? Ada yang janggal."
    mc2 "Ah!"
    mc2 "Sudah selesai ku pindai, tidak ada yang aneh. Langsung pergi juga tak apa."

    menu:
        mc1 "Hmm..."

        "Antar ke Partisi SSD untuk mengambil bootloader":
            mc1 "Anu, bisa antar saya ke Partisi SSD yang menyimpan bootloader?"
            uefi2 "Baik, Tuan [nama1]"
            italic "[nama1] segera meninggalkan Ruang Arsip RAM dan menuju ke arah Partisi SSD."
            jump act2_ssd

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

label act2_ssd:
    show screen locinfo("Connecting Bridge")
    with dissolve
    $ renpy.pause(2.5)
    hide screen locinfo
    with dissolve
    
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