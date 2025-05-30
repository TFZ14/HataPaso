label act2_connecting_moveset:
    scene lorong
    with fade
    show screen healthpoint
    show screen enemyhp

    #satu
    menu:
        "Serang":
            play sound "audio/sound/銃声・銃の音.mp3"
            with vpunch
            $ health_value-=10
            $ enemyhp_value-=10
            if health_value<=0 and enemyhp_value<=0:
                a "kalian berdua mati bersama."
                hide screen enemyhp
                hide screen healthpoint
                mc2 "[nama1]!"
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            elif enemyhp_value<=0:
                mc1 "Anomali telah dikalahkan."
                $ renpy.pause(1.0)
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            elif health_value<=0:
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
        "Tahan":
            play sound "audio/sound/銃声・銃の音.mp3"
            with hpunch
            a "Musuh menyerang, kamu bertahan."
            window hide
            
    #dua
    menu:
        "Serang":
            play sound "audio/sound/銃声・銃の音.mp3"
            with vpunch
            $ health_value-=10
            $ enemyhp_value-=10
            if health_value<=0 and enemyhp_value<=0:
                a "kalian berdua mati bersama."
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            elif enemyhp_value<=0:
                mc1 "Anomali telah dikalahkan."
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            elif health_value<=0:
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
        "Tahan":
            play sound "audio/sound/銃声・銃の音.mp3"
            with hpunch
            a "Musuh menyerang, kamu bertahan."
            window hide
            
    #tiga
    menu:
        "Serang":
            play sound "audio/sound/斬撃音.mp3"
            with vpunch
            $ enemyhp_value-=15
            if health_value<=0 and enemyhp_value<=0:
                a "kalian berdua mati bersama."
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            elif enemyhp_value<=0:
                mc1 "Anomali telah dikalahkan."
                hide screen enemyhp
                hide screen healthpoint
                jump act2_connectingdone
            elif health_value<=0:
                mc2 "[nama1]!"
                hide screen enemyhp
                hide screen healthpoint
                scene toko
                with fade
                a "kamu tertarik ke dunia nyata."
                jump losebattle
            else:
                a "Seranganmu berhasil mengenai musuh."
                window hide
        "Tahan":
            a "..."
            a "Kamu bertahan namun musuh tidak menyerang."
            window hide

    jump act2_connecting_moveset
    return
    