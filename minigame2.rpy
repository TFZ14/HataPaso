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
    scene room
    mc1 "i did it"

screen reassemble_puzzle:
    image "background.png"
    frame:
        background "puzzle-frame.png"
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
                image "Pieces/piece-%s.png"%(i+1)

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
                image "Pieces/piece-%s.png"%(i+1) alpha 0.0 #for invisible

default page_pieces = 12
default full_page_size = (711, 996)
default pieces_coordinates = [(451,149), (719, 139), (868, 238), (421, 399), (658, 318), (700, 488), (796, 538), (453, 718), (776, 773), (464, 925), (743, 958), (921, 888)]
default initial_place_coordinates=[]
default finished_pieces=0

define gui.name_xpos=520
define gui.dialogue_xpos=520