#Character
define mc1=Character("[nama1]", who_bold=True)
define mc2=Character("[nama2]", who_bold=True)
define klien=Character("Mary", who_bold=True)
define bios1=Character("BIOS 1023345", who_bold=True)
define bios2=Character("BIOS 1023123", who_bold=True)

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

#bar mechanics
init python:
    health_value=100
    thinking_value=100
    score=10 #untuk penilaian pemain di akhir

screen healthpoint():
    frame:
        xalign 0.98
        ypos 50
        ysize 700
        hbox:
            spacing 10
            vbar value AnimatedValue(health_value, 100, 0.5)

screen thinkingpoint():
    frame:
        xalign 0.94
        ypos 50
        ysize 700
        hbox:
            spacing 10
            vbar value AnimatedValue(thinking_value, 100, 0.5)

screen score():
    frame:
        xalign 0.5 ypos 50
        text "[score]":
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

    a "{size=+3}{b}Misi Franoa Service Center menggunakan teknologi NOVA dimulai!{/b}{/size}"

    #setiap selesaikan label (section) dapat skor
    $ score+=10
    if score<=0:
        "Baru mulai."
        jump game_over
    else:
        jump act1_whatsnova

    return

#label opening:
    play movie "opening.mp4"
    jump act1_whatsnova

    return

label act1_whatsnova:
    show screen healthpoint
    show screen thinkingpoint

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

    $ score+=10
    if score <= 0:
        "Baru mulai."
        jump game_over
    else:
        jump act1_post

    return

scene bg room
label act1_post:
    #LobiBIOS
    mc1 "Uwaah..."
    window hide
    $ renpy.pause(2.0, hard=True)

    italic "Lobi BIOS terlihat sibuk, banyak Petugas IO berlalu-lalang untuk mempersiapkan laptop."

    italic "Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan."

    bios1 "Euh..."

    mc1 "Bagaimana? Apa ada kendala?"

    bios1 "Ah Tuan [nama1], kami belum dapat laporan status dari CPU..."

    mc1 "Hmm? Baik akan ku cek."

    jump act1_cpu

    return

    label act1_cpu:
        jump act1_cpu_game

label act1_cpu_game:
    $ setup_cable_game()
    call screen connect_the_cables
    return

label act1_cpu2:
    hide cable_game_success
    "This is act1_cpu2"
    "next is minigame 2"

    jump minigame2

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