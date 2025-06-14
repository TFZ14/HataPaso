default page_pieces = 12
default full_page_size = (711, 996)
default pieces_coordinates = [(451,149), (719, 139), (868, 238), (421, 399), (658, 318), (700, 488), (796, 538), (453, 718), (776, 773), (464, 925), (743, 958), (921, 888)]
default initial_place_coordinates=[]
default finished_pieces=0

init python:
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc=(renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_place_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name==dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable=False
            finished_pieces+=1

            if finished_pieces==page_pieces:
                renpy.jump("reassemble_complete")

label reassemble_complete:
    scene ramroom
    stop music fadeout 2.0
    play sound "sound/システムSE_決定音1.mp3"
    mc1 "Hmm? Apa ini?"
    play sound "audio/sound/本をめくる音・閉じる音.mp3"
    show full-page
    with dissolve
    $ renpy.pause(5.0)
    italic "Walau masih bingung, [nama1] menyimpan serpihan kertas itu ke dalam saku digitalnya."
    hide full-page
    with dissolve

    show screen thinkingpoint
    with dissolve
    play sound "audio/sound/システム決定音_9.mp3"
    italic "Menerima info baru, Thinking Point bertambah +5."
    $ thinking_value+=5
    hide screen thinkingpoint
    with dissolve

    mc1 "Baik, bisa antar saya ke Partisi SSD yang menyimpan bootloader?"
    uefi2 "Baik, Tuan [nama1]"
    italic "[nama1] segera meninggalkan Ruang Arsip RAM dan menuju ke arah Partisi SSD."
    jump act2_1_connecting
    return

screen reassemble_puzzle:
    image "minigame3/background.png"
    frame:
        background "minigame3/puzzle-frame.png"
        xysize full_page_size
        anchor (0.5, 0.5)
        pos (650, 535)

    draggroup:
        #paper pieces
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_place_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "minigame3/piece-%s.png"%(i+1)

        #snappable spots
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos pieces_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "minigame3/piece-%s.png"%(i+1) alpha 0.0 #for invisible
