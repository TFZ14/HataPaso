default file_pieces=5
default all_files_size=(618, 477)
default files_coordinates=[(700, 285), (663, 388), (601, 489), (559, 584), (508, 685)]
default initial_files_coordinates=[]
default finished_files=0

init python:
    def setup_files():
        for i in range(file_pieces):
            start_x = 1500
            start_y = 600
            end_x = 1700
            end_y = 800
            rand_loc=(renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_files_coordinates.append(rand_loc)

    def file_drop(dropped_file, dragged_file):
        global finished_files

        if dragged_file[0].drag_name==dropped_file.drag_name:
            dragged_file[0].snap(dropped_file.x, dropped_file.y)
            dragged_file[0].draggable=False
            finished_files+=1

            if finished_files==file_pieces:
                renpy.jump("manage_complete")

label manage_complete:
    play sound "sound/システムSE_決定音1.mp3"
    scene ramroom
    with dissolve
    mc1 "Huft..."
    jump act2_1_ramdone
    return

screen manage_files:
    image "minigame2/lacibg.png"

    draggroup:
        drag:
            draggable False
            droppable False
            pos (0, 0)
            anchor(0.0, 0.0)
            image "minigame2/minigame2bg.png"

        #file
        for i in range(file_pieces):
            drag:
                drag_name i
                pos initial_files_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise False
                image "minigame2/file-%s.png"%(i+1)
                
        #snappable spots
        for i in range(file_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped file_drop
                pos files_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "minigame2/file-%s.png"%(i+1) alpha 0.0

        drag:
            draggable False
            droppable False
            pos (0, 0)
            anchor(0.0, 0.0)
            image "minigame2/laci.png"