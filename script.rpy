#Character
define mc1=Character("[nama1]", who_bold=True)
define mc2=Character("[nama2]", who_bold=True)
define klien=Character("Mary", who_bold=True)
define uefi1=Character("uefi 1023345", who_bold=True)
#define uefi2=Character("uefi 1023123", who_bold=True)
define chiefcpu=Character("Chief CPU", who_bold=True)

#styling narrator
define a=Character(
    None,
    window_background=None,
    what_outlines=[( 1, "#06405b", 0, 0 )],
    what_italic=True,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define italic=Character(
    None,
    what_italic=True,
)

#styling mission splash
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
    scene bg room

    #Opening
    klien "Iya, sudah saya bawa ke service center sebelumnya, awalnya bisa dinyalakan, namun, tidak berapa lama, kembali mati lagi, jadi saya coba ke toko ini."

    "Ooh, begitu. Masalahnya apa, Bu Mary?"

    klien "Layarnya mati walau lampu di tombol powernya sudah nyala, bahkan mesinnya pun sudah terdengar."

    a "Kamu mendengarkan keluhan-keluhan Bu Mary panjang lebar sambil mengira-ngira akar dari kendala tersebut, sementara rekanmu disamping mencatat detail-detail dari keluhan Bu Mary, jaga-jaga jika kamu terlewat atau melupakan beberapa detail."

    klien "Baik, berarti saya ambil paling cepat berapa hari, ya? Anu, dengan kak siapa?"

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

    klien "Baik Kak [nama1], Kak [nama2], kalian, kan, punya NOVA, seharusnya bisa selesai cepat, kan?"

    italic "[nama2] menutup note digitalnya dengan seringai tipis."

    mc1 "Tentu saja. Bu Mary."

    italic "Ucap [nama1] penuh percaya diri."

    window hide
    show screen mission_splash("Misi SchnellFix Service Center menggunakan teknologi NOVA DIMULAI!")
    $ renpy.pause(2.5)
    hide screen mission_splash

    jump act1_quiz1

label act1_quiz1:
    show screen thinkingpoint

    italic "Mary pamit undur diri, keluar melalui pintu kaca. Kebetulan ini masih sangat pagi dan belum ada klien lain, [nama2] mengusulkan untuk segera mengecek laptop Mary."

    mc1 "Sesuai kata Bu Mary, memang terlihat nyala laptopnya, tetapi layarnya tetap hitam."

    menu:
        mc2 "hmm... pertama-tama, kita cek apanya dulu, ya?"

        "Ganti RAM":
            with vpunch
            mc2 "Oi, oi, yang bener aja..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz1 #Kembali ke menu pilihan

        "Cek kabel monitor":
            mc2 "Aah, benar juga, walau bisa menyala, kalau kabel monitor longgar atau rusak, layar tetap mati."
            $ score+=5
            jump act1_quiz2

        "Reset UEFI":
            with vpunch
            mc2 "... langsung banget nih?"
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz1

    return

label act1_quiz2:
    show screen thinkingpoint

    italic "Aku dan [nama2] membongkar dan mengecek hardware laptop Bu Mary, namun semuanya terlihat baik-baik saja, hanya butuh sedikit bersih-bersih saja."

    mc2 "Hhh... kalau sudah begini, saatnya lihat dari dalam."

    menu:
        mc2 "Benar, mungkin bisa kita urut dari awal seperti POST {i}(Power-On Self Test) yang dilakukan oleh...{/i}"

        "UEFI":
            mc2 "Oooh! Oke, akan ku kirim ke Lobi UEFI, ya!"
            $ score+=5

        "CPU":
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan

        "ALU":
            with vpunch
            mc2 "... kayaknya bukan, deh..."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz2 #Kembali ke menu pilihan
    
    mc1 "Ok, aku siapkan NOVA-nya."
    hide screen thinkingpoint
    with dissolve

    jump act1_whatsnova
    return

#label opening:
    play movie "opening.mp4"
    jump act1_whatsnova

    return

label act1_whatsnova:
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
    scene bg room

    #LobiUEFI
    mc1 "Uwaah..."
    window hide
    $ renpy.pause(2.0, hard=True)

    italic "Lobi UEFI terlihat sibuk, banyak Petugas IO berlalu-lalang untuk mempersiapkan laptop."

    italic "Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan."

    uefi1 "Euh..."

    jump act1_quiz3
    return

label act1_quiz3:
    menu :
        mc1 "Biasanya, jika POST di UEFI memiliki kendala, itu karena..."

        "Komputer kehabisan baterai CMOS":
            with vpunch
            mc2 "... kayaknya bukan, deh. Baterai CMOS berpengaruh pada penyimpanan pengaturan, bukan langsung ke POST."
            $ thinking_value-=5
            $ score-=5
            if thinking_value <= 0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz3

        "Perangkat keras gagal terdeteksi oleh sistem":
            mc2 "Jika {i}Hardware{/i} (perangkat keras) gagal dideteksi oleh sistem saat POST, maka akan gagal booting."
            $ score+=5

        "Driver belum diinstal":
            with vpunch
            mc2 "... hmm, driver penting setelah OS jalan, tapi POST bekerja sebelum sistem operasi aktif."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz3

    mc1 "Bagaimana? Apa ada kendala?"
    uefi1 "Ah Tuan [nama1], kami belum dapat laporan status dari CPU..."
    mc1 "Hmm? Baik akan ku cek."

    jump act1_cpu
    return

label act1_cpu:
    italic "Tiba di Ruang CPU"
    mc1 "...!!"
    with hpunch
    mc1 "apa-apaan!"
    mc2 "kenapa [nama1]? Ada apa?"
    italic "Ruang CPU dipenuhi oleh pekerja yang berbaris rapih menghadap ke arah yang sama. Mereka diam seribu bahasa, tidak seperti petugas IO di Lobi UEFI yang sibuk berlalu-lalang."
    mc1 "Aah! Pantas saja Lobi UEFI tidak dapat kabar baik dari CPU..."

    jump act1_quiz4
    return

label act1_quiz4:
    menu:
        mc1 "Ternyata, mereka tidak terjadwal dan terkoordinasi dengan baik dikarenakan..."

        "RAM tidak cukup besar":
            with vpunch
            mc2 "... kayaknya bukan, deh... RAM memang penting, tapi ini soal koordinasi kerja."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<= 0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
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
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz4

        "Clock Generatornya rusak":
            mc1 "Tanpa Clock Generator yang aktif, tidak ada yang mengatur kapan para pekerja CPU harus bergerak..."
            mc1 "Seperti orkestra tanpa konduktor."
            $ score+=5

    italic "Clock Generator menentukan kecepatan kerja komponen dalam satuan MHz atau GHz. Clock Generator mengirim sinyal denyut {i}(clock pulse){/i} agar data diproses secara teratur dan terkoordinasi."
    mc1 "...dan Clock Generatornya rusak"
    italic "[nama1] mengurut kening pusing."
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
    mc1 "Untung hanya masalah sedikit, tidak sampai perlu ganti komponennya di dunia nyata."
    mc1 "[nama2], catat untuk Bu Mary, kalau pakai laptop, pastikan sumber listriknya stabil. Tegangan yang nggak stabil bisa bikin clock generator error."
    mc2 "Siap!"
    italic "[nama1] kembali ke Lobi UEFI."
    mc1 "Silakan coba booting lagi"
    uefi1 "Baik."
    italic "[uefi1] mulai menjalankan perintah booting. Namun layar holografik di lobi menunjukkan peringatan merah. [uefi1] mulai terlihat gugup lagi."
    uefi1 "I- instruksi booting tidak bisa dilanjutkan."
    mc1 "Eh? Kenapa lagi?"
    uefi1 "CPU melaporkan bahwa instruksi tidak bisa dilanjutkan karena berkas bootloader todak ada di memori."
    mc1 "Tunggu. Kalau begitu... tempat terakhir data berada sebelum eksekusi dimulai adalah RAM, kan?"
    uefi1 "Benar. Tapi jika berkas bootloader memang tidak sempat tersalin, kamu harus mencarinya langsung dari sumber utama..."

    jump act1_quiz5
    return

label act1_quiz5:
    menu:
        mc1 "Sumber utama bootloader..."

        "Hard Drive":
            mc1 "lebih spesifiknya, bootloader disimpan di partisi khusus ESP dalam hard drive"
            $ thinking_value+=5

        "RAM":
            with vpunch
            mc2 "Bootloader memang diload dalam RAM, namun itu bukan tempat awal bootloader"
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz5
        "GPU":
            with vpunch
            mc2 "Hei! GPU berfungsi untuk rendering grafis, bukan tempat penyimpanan bootloader."
            $ thinking_value-=5
            $ score-=5
            if thinking_value<=0 or score<=0:
                $ thinking_value-=100
                "Gagal, belajar lagi"
                jump game_over
            else:
                jump act1_quiz5

    italic "ESP atau Extensible Firmware Interface System Partition adalah partisi khusus pada hard drive yang berisi file bootloader dan konfigurasi lainnya. Jika ESP hilang atau rusak, maka sistem tidak bisa booting meskipun OS masih utuh."

    jump act2_bootloader
    return

label act2_bootloader:
    return

label minigame2:
    scene room
    mc1 "gass puzzle"
    $ setup_puzzle()
    call screen reassemble_puzzle
    return

label game_over:
    scene room
    "gagal"
    return

label selesai:
    scene room
    if score<=0:
        "Oi, oi, yang bener aje."
    elif score<=5:
        "waduh, belajar lagi"
    else :
        "Loh?"
    "selesai"
    return