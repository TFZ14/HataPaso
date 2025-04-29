define mc1 = Character("[nama1]")
define mc2 = Character("[nama2]")
define klien = Character("Mary")
define bios1 = Character("BIOS 1023345")
define bios2 = Character("BIOS 1023123")

label start:
    scene bg room
    #show eileen happy

    #mc2 "kalimat."
    #window hide
    #pause 2.0
    #mc2 "hayo."
    #$ renpy.pause(3.0, hard=True)
    #"yihaa {w=2.0} lelele"
    #window show

    #Opening
    klien "iya, sudah saya bawa ke service center sebelumnya, awalnya bisa dinyalakan, namun, tidak berapa lama, kembali mati lagi, jadi saya coba ke toko ini."

    "ooh, begitu. Masalahnya apa, Bu Mary?"

    klien "layarnya mati walau lampu di tombol powernya sudah nyala, bahkan mesinnya pun sudah terdengar."

    "{i} kamu mendengarkan keluhan-keluhan Bu Mary panjang lebar sambil mengira-ngira akar dari kendala tersebut, sementara rekanmu disamping mencatat detail-detail dari keluhan Bu Mary, jaga-jaga jika kamu terlewat atau melupakan beberapa detail.{/i}"

    klien "baik, berarti saya ambil paling cepat berapa hari, ya? Anu, dengan kak siapa?"

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

    "{i}[nama2] menutup note digitalnya dengan seringai tipis{/i}"

    mc1 "tentu saja. Bu Mary."

    "{i}ucap [nama1] penuh percaya diri{/i}"

    "{size=+5}{b}Misi Franoa Service Center menggunakan teknologi NOVA dimulai!{/b}{/size}"

    #jump
    jump game_act1_whatsnova

    return

#label opening:
    play movie "opening.mp4"
    jump game_act1_whatsnova

    return

label game_act1_whatsnova:
    #What is NOVA
    "{i}{b}NOVA{/b} atau Neural Operation Virtual Access adalah teknologi terbaru yang akhir-akhir viral, khususnya dikalangan penggiat informatika. Untuk mendapatkan device ini dibutuhkan 6 bulan antri.{/i}"

    "{i}Pengguna NOVA minimal ada dua orang, yang masuk ke dalam dunia virtual, disebut sebagai {i}“Diver”{/i}, dan yang menjaga dari dunia nyata, disebut sebagai {b}“Navigator”{/b}. Orang yang menggunakan NOVA akan memasuki zona waktu khusus yang bisa diatur oleh navigator.{/i}"

    "{i}NOVA berisi empat komponen. Komponen pertama dan kedua adalah {b}NeuroDriver{/b}, alat seperti bando yang bisa menghubungkan sinyal otak dengan sistem NOVA untuk ditransfer ke dalam NeuroLink USB dan EchoLink Hub dengan metode penyamaan frekuensi otak.{/i}"

    "{i}NeuroDriver digunakan diver untuk mentransfer kesadarannya ke dalam komputer melalui NeuroLink USB, sementara bagi navigator, alat ini berfungsi untuk menavigasi dan memantau informasi menyeluruh tentang kondisi komputer secara langsung saat proses terjadi.{/i}"

    "{i}Komponen ketiga, {b}NeuroLink USB{/b}, yang berguna untuk memungkinkan pemilik USB tersebut berinteraksi langsung ke dalam komputer. NeuroLink USB menangkap frekuensi otak yang sudah dikonversi oleh NeuroDriver lalu menyalurkannya ke sistem NOVA.{/i}"

    "{i}Kesadaran atau sinyal tersebut menjelma menjadi avatar virtual dan bisa menjelajahi sistem komputer dengan leluasa. Pemilik bisa menggerakkan avatar untuk menemukan, memperbaiki, atau mengecek error pada komputer secara interaktif. NeuroLink USB juga memberikan ilusi visual interaktif agar pemilik bisa lebih paham dengan keadaan komputer.{/i}"

    "{i}Komponen keempat, {b}EchoLink Hub{/b} yang digunakan asisten dari pemakai NeuroLink USB, digunakan untuk komunikasi dan navigasi dari dunia luar.{/i}"

    "{i}[nama1] menancapkan NeuroLink USB ke laptop klien lalu memakai NeuroDriver di kepala{/i}"
    
    mc1 "aku serahkan padamu, ya, Tuan Navigator."

    mc2 "santai, Diver. lagian siapa yang ngajarin kamu, heh?"

    mc1 "iya, iya."

    "{i}[nama2] memakai EchoLink Hub yang terlihat penuh dikepalanya.[nama2] bersiap di{/i} set up {i}mejanya untuk memulai menavigasi Diver.  [nama1] menyamankan diri di atas kursi malas, memejamkan mata bersiap untuk{/i} Diving."

    jump game_act1_post

    return

label game_act1_post:
    #LobiBIOS
    mc1 "Uwaah..."
    $ renpy.pause(2.0, hard=True)

    "{i}Lobi BIOS terlihat sibuk, banyak Petugas IO berlalu-lalang untuk mempersiapkan laptop.{/i}"
    "{i}Saat ini, kegiatan {b}POST{/b} sedang berjalan. POST atau Power-On Self-Test adalah serangkaian pemeriksaan awal yang dilakukan komputer setiap kali dinyalakan untuk memastikan semua komponen berfungsi sebelum sistem berjalan.{/i}"

    mc1 ""


    return
