label losebattle:
    scene black
    with fade
    italic "Kesadaranmu perlahan hilang. Tubuhmu tak bisa digerakkan."
    scene toko
    with fade
    mc1 "Uuuh..."
    italic "Saat kamu sadar, kamu sudah berada di dunia nyata."
    play sound "audio/sound/打撃・ビンタ音.mp3"
    show friendconfuse
    with hpunch
    mc2 "Untung aku tarik paksa tepat waktu!"
    play sound "audio/sound/打撃・ビンタ音.mp3"
    with hpunch
    mc2 "Kalau ngga, bisa-bisa kesadaranmu terperangkap di laptop Bu Mary!"
    hide friendconfuse
    with dissolve
    italic "[nama1] melihat sekeliling, kesadarannya mulai kembali."
    mc1 "Astaga..."
    show friendconfuse
    with hpunch
    mc2 "Sudah! Nanti kalau enakan baru kita perbaiki lagi laptopnya."
    mc2 "Kamu sementara jadi Navigator saja. Biar aku yang Dive."
    italic "[nama1] hanya bisa setuju. Sepertinya, dia memang butuh belajar lagi untuk menjadi Diver yang baik."

    jump selesai
    return

label game_over:
    scene toko
    with fade
    italic "Kamu kembali ke dunia nyata setelah log out dari NOVA."
    show friendidle
    with dissolve
    italic "Disana kamu mendapati [nama2] tersenyum menyambutmu."
    mc2 "Yap. Kamu istirahat dulu. Nanti kita coba lagi. Tapi, kamu cukup jadi Navigator dulu, ya."
    hide friendidle
    with dissolve
    italic "Walau [nama2] tersenyum, [nama1] tahu jika [nama2] kecewa padanya."
    mc1 "... kedepannya, aku akan berhati-hati."

    $ renpy.full_restart()
    return

label selesai:
    play music "audio/music/inner_flame.mp3" fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    scene toko
    with fade
    show friendidle
    if score<=0:
        hide friendidle
        show friendconfuse
        play sound "audio/sound/打撃・ビンタ音.mp3"
        with hpunch
        mc2 "Oi, oi, yang bener aje."
        mc2 "Sepertinya kamu harus belajar lagi dari awal."
        play sound "audio/sound/打撃・ビンタ音.mp3"
        with hpunch
        mc2 "Pelajari tentang {/b}Dasar-Dasar Arsitektur Komputer{/b} seperti:"
        play sound "audio/sound/打撃・ビンタ音.mp3"
        with hpunch
        mc2 "Urutan power-on dan inisiasi komputer."
        play sound "audio/sound/打撃・ビンタ音.mp3"
        with hpunch
        mc2 "Baca artikel dengan kata kunci 'How Computers Boot Up'"
        play sound "audio/sound/打撃・ビンタ音.mp3"
        with hpunch
        mc2 "Jangan lupa, ya!"
    elif score<=35:
        mc2 "Yah, gak papa, kamu udah berjuang."
        mc2 "Coba baca-baca tentang BIOS, UEFI, dan Boot Process lebih dalem."
        mc2 "Baca juga peran-peran tiap komponen seperti CPU, RAM, dan Storage, dan lainnya."
    elif score<70:
        hide friendidle
        show friendidle2
        mc2 "Kamu sudah tahu garis besarnya, tinggal memperdalam lagi sedikit."
        mc2 "Coba baca tentang Firmware dan Keamanan Sistem."
        mc2 "Cari tahu siapa saja yang bisa mengganggu proses inisiasi komputer."
        mc2 "Atau mungkin, pelajari tentang troubleshooting awal RAM, GPU, dan Storage."
    elif score==70:
        mc2 "Wow! Kamu sudah sangat memahami tentang arsitektuk komputer rupanya!"
        mc2 "Bisa nih jadi Diver utama jikalau ada klien lain!"
    else :
        play sound "audio/sound/え？どうしたの？.mp3"
        hide friendidle
        show friendconfuse
        with hpunch
        mc2 "Loh? Nge-Cheat ya?"

    $ renpy.full_restart()
    return