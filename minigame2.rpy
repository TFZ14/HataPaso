default file_pieces = 5
default all_files_size = (618, 477)
default files_coordinates = [(508, 685), (559, 584), (601, 489), (663, 388), (700, 285)]
default initial_files_coordinates=[]
default finished_files=0

init python:
    def setup_files():
        for i in range(file_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc=(renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_files_coordinates.append(rand_loc)

    def file_drop(dropped_on, dragged_file):
        global finished_files

        if dragged_file[0].drag_name==dropped_on.drag_name:
            dragged_file[0].snap(dropped_on.x, dropped_on.y)
            dragged_file[0].draggable=False
            finished_files+=1

            if finished_files==file_pieces:
                renpy.jump("manage_complete")

label manage_complete:
    scene room
    mc1 "Hmm? Apa ini?"
    show full-page
    with dissolve
    $ renpy.pause(2.5)
    italic "Walau masih bingung, [nama1] menyimpan serpihan kertas itu ke dalam saku digitalnya."
    hide full-page
    with dissolve

    show screen thinkingpoint
    with dissolve
    italic "Menerima info baru, Thinking Point bertambah +5."
    $ thinking_point+=5
    hide screen thinkingpoint
    with dissolve

    mc1 "Baik, bisa antar saya ke Partisi SSD yang menyimpan bootloader?"
    uefi2 "Baik, Tuan [nama1]"
    italic "[nama1] segera meninggalkan Ruang Arsip RAM dan menuju ke arah Partisi SSD."
    jump start
    return

screen manage_files:
    image "minigame2/minigame2bg.png"
    frame:
        background "minigame2/file-frame.png"
        xysize all_files_size
        anchor (0.99, 0.99)
        pos (618, 477)

    draggroup:
        #file
        for i in range(file_pieces):
            drag:
                drag_name i
                pos initial_files_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "minigame2/file-%s.png"%(i+1)
                
        #snappable spots
        for i in range(file_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos files_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "minigame2/file-%s.png"%(i+1) alpha 0.0