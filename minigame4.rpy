label act2_connecting_moveset:
    scene lorong
    show screen healthpoint
    show screen enemyhp

    #satu
    menu:
        "Serang":
            play sound "audio/sound/銃声・銃の音.mp3"
            show seri-virus
            with vpunch
            $ health_value-=10
            $ enemyhp_value-=10
            if health_value<=0 and enemyhp_value<=0:
                hide seri-virus
                a "kalian berdua mati bersama."
                hide screen enemyhp
                hide screen healthpoint
                mc2 "[nama1]!"
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            elif enemyhp_value<=0:
                hide seri-virus
                mc1 "Anomali telah dikalahkan."
                $ renpy.pause(1.0)
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            elif health_value<=0:
                hide seri-virus
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            else:
                window hide
                a "Kalian sama-sama menyerang."
                hide seri-virus        
        "Tahan":
            play sound "audio/sound/銃声・銃の音.mp3"
            show serang-virus
            with hpunch
            a "Musuh menyerang, kamu bertahan."
            window hide
            hide serang-virus
        "Pulihkan diri":
            play sound "audio/sound/斬撃音.mp3"
            show kena-virus
            with hpunch
            a "Kamu lengah, musuh berhasil menyerang."
            $ health_value-=10
            window hide
            hide kena-virus

            
    #dua
    menu:
        "Serang":
            play sound "audio/sound/銃声・銃の音.mp3"
            show seri-virus
            with vpunch
            $ health_value-=10
            $ enemyhp_value-=10
            if health_value<=0 and enemyhp_value<=0:
                hide seri-virus
                a "kalian berdua mati bersama."
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            elif enemyhp_value<=0:
                hide seri-virus
                mc1 "Anomali telah dikalahkan."
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            elif health_value<=0:
                hide seri-virus
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            else:
                a "Kalian sama-sama menyerang."
                window hide
                hide seri-virus  
        "Tahan":
            play sound "audio/sound/銃声・銃の音.mp3"
            show serang-virus
            with hpunch
            a "Musuh menyerang, kamu bertahan."
            window hide
            hide serang-virus
        "Pulihkan diri":
            play sound "audio/sound/斬撃音.mp3"
            show kena-virus
            with hpunch
            $ health_value-=10
            a "Kamu lengah, musuh berhasil menyerang."
            window hide
            hide kena-virus
            
    #tiga
    menu:
        "Serang":
            play sound "audio/sound/斬撃音.mp3"
            show strike-virus
            with vpunch
            $ enemyhp_value-=15
            if enemyhp_value<=0:
                hide strike-virus
                mc1 "Anomali telah dikalahkan."
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            else:
                a "Seranganmu berhasil mengenai musuh."
                window hide
                hide strike_virus
        "Tahan":
            play sound "audio/sound/ひゅるりら～.mp3"
            show aho-virus
            a "Kamu bertahan namun musuh tidak menyerang."
            window hide
            hide aho-virus
        "Pulihkan diri":
            play sound "audio/sound/神々しい神楽鈴の音.mp3"
            show heal
            with hpunch
            $ health_value+=5
            a "Berhasil menyembuhkan diri ketika musuh lengah."
            window hide
            hide heal

    jump act2_connecting_moveset
    return

label act3_mebromi_moveset:
    return    