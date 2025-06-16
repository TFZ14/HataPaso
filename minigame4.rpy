#timer
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
init:
    $ timer=0
    $ tick=0
    $ virus_turn_count=0
    $ mebromi_turn_count=0

screen countdown_battle:
    timer 0.01 repeat True action If(tick>0, true=SetVariable('tick', tick - 0.01), false=[Hide('countdown_battle'), Jump('timeout')])
    bar value tick range timer xalign 0.5 yalign 0.04 xmaximum 900 at alpha_dissolve

label timeout:
    $ spacing = True

    hide screen countdown_battle
    stop sound
    
#connecting battle
    if virus_turn_count%3==1:
        play sound "audio/sound/斬撃音.mp3"
        show kena-virus
        with hpunch
        a "Kamu lengah, musuh berhasil menyerang."
        $ health_value-=10
        window hide
        hide kena-virus
        jump expression arena
    elif virus_turn_count%3==2:
        play sound "audio/sound/斬撃音.mp3"
        show kena-virus
        with hpunch
        a "Kamu lengah, musuh berhasil menyerang."
        $ health_value-=10
        window hide
        hide kena-virus
        jump expression arena
    else:
        play sound "audio/sound/どうしたの？？.mp3"
        show tatap-virus
        with dissolve
        a "Kalian hanya saling tatap"
        window hide
        hide tatap-virus
        jump expression arena

#mebromi battle ED 1

    return

label virusbattle:
    $ arena='act2_1_connecting_moveset'
    $ spacing=False
    $ tick=5
    $ timer=5.5
    show screen countdown_battle

#connecting battle
    if virus_turn_count%3==1:
        menu:
            "Serang":
                hide screen countdown_battle
                stop sound
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
                    jump act2_1_connectingdone
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
                    jump expression arena        
            "Tahan":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/銃声・銃の音.mp3"
                show serang-virus
                with hpunch
                a "Musuh menyerang, kamu bertahan."
                window hide
                hide serang-virus
                jump expression arena
            "Pulihkan diri":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/斬撃音.mp3"
                show kena-virus
                with hpunch
                a "Kamu lengah, musuh berhasil menyerang."
                $ health_value-=10
                window hide
                hide kena-virus
                jump expression arena
    elif virus_turn_count%3==2:
        menu:
            "Serang":
                hide screen countdown_battle
                stop sound
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
                    jump act2_1_connectingdone
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
                    jump expression arena        
            "Tahan":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/銃声・銃の音.mp3"
                show serang-virus
                with hpunch
                a "Musuh menyerang, kamu bertahan."
                window hide
                hide serang-virus
                jump expression arena
            "Pulihkan diri":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/斬撃音.mp3"
                show kena-virus
                with hpunch
                a "Kamu lengah, musuh berhasil menyerang."
                $ health_value-=10
                window hide
                hide kena-virus
                jump expression arena
    else:
        menu:
            "Serang":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/斬撃音.mp3"
                show strike-virus
                with vpunch
                $ enemyhp_value-=15
                if enemyhp_value<=0:
                    hide strike-virus
                    mc1 "Anomali telah dikalahkan."
                    hide screen enemyhp
                    hide screen healthpoint
                    jump act2_1_connectingdone
                else:
                    a "Seranganmu berhasil mengenai musuh."
                    window hide
                    hide strike_virus
                    jump expression arena        
            "Tahan":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/ひゅるりら～.mp3"
                show aho-virus
                a "Kamu bertahan namun musuh tidak menyerang."
                window hide
                hide aho-virus
                jump expression arena
            "Pulihkan diri":
                hide screen countdown_battle
                stop sound
                play sound "audio/sound/神々しい神楽鈴の音.mp3"
                show heal
                with dissolve
                $ health_value+=5
                a "Berhasil menyembuhkan diri ketika musuh lengah."
                window hide
                hide heal
                jump expression arena
            
#mebromi battle ED1

    return

#rute ending 1
label act2_1_connecting_moveset:
    scene lorong
    show screen healthpoint
    with dissolve
    show screen enemyhp
    with dissolve
    
    $ virus_turn_count+=1

    call virusbattle

    jump act2_1_connecting_moveset
    return

label act3_mebromi_moveset:
    return    