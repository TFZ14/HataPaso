screen connect_the_pipes:
    image "background.png"

    grid pipe_columns pipe_rows:
        spacing 0
        pos(640, 140)
        anchor(0.0, 0.0)
        for pipe in pipes:
            if pipe in connected_pipes:
                imagebutton idle Transform(pipe[1]+"-pipe-connected.png", rotate=pipe[4], rotate_pad=False) action Function(rotate_pipe, cell=pipe[3])
            else:
                imagebutton idle Transform(pipe[0], rotate=pipe[4], rotate_pad=False) action Function(rotate_pipe, cell=pipe[3])

#minigames 1 : connecting cable
default pipe_rows=4
default pipe_columns=4
default amount_of_pipes = pipe_rows*pipe_columns
default grid_path=[]
default pipes=[]
default pipe_types={"straight":("top", "bottom"), "curved":("right", "bottom"), "t":("top", "bottom", "left")}
###
default connected_pipes=[]

init python:
    def setup_pipe_game():
        global pipes
        global connected_pipes

        pipes=[]
        connected_pipes=[]

        generated_grid_path()

        create_pipes()

    def create_pipes():
        for i in range(1, amount_of_pipes+1):
            if i==1:
                if grid_path[0]+1==grid_path[1]:
                    create_pipe(type="straight",cell=i)
                elif grid_path[0]+pipe_columns==grid_path[1]:
                    create_pipe(type="curved",cell=i)

            elif i>1 and i<amount_of_pipes:
                if i in grid_path:
                    current_cell_index=grid_path.index(i)
                    next_cell_index=current_cell_index+1
                    prev_cell_index=current_cell_index-1
                    if grid_path[current_cell_index]%pipe_columns==1:
                        if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                            create_pipe(type="curved", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]+pipe_columns==grid_path[next_cell_index]:
                            create_pipe(type="straight", cell=grid_path[current_cell_index])
                    elif grid_path[current_cell_index]%pipe_columns==0 and grid_path[current_cell_index]<=pipe_columns:
                        create_pipe(type="curved", cell=grid_path[current_cell_index])
                    elif grid_path[current_cell_index]%pipe_columns==0 and grid_path[current_cell_index]>pipe_columns:
                        if grid_path[current_cell_index]-pipe_columns==grid_path[prev_cell_index]:
                            create_pipe(type="straight", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                            create_pipe(type="curved", cell=grid_path[current_cell_index])
                    else:
                        if grid_path[current_cell_index]<=pipe_rows:
                            if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                create_pipe(type="straight", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]+pipe_columns==grid_path[next_cell_index]:
                                create_pipe(type="curved", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]>=amount_of_pipes-pipe_columns:
                            if grid_path[current_cell_index]-pipe_columns==grid_path[prev_cell_index]:
                                create_pipe(type="curved", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                                create_pipe(type="straight", cell=grid_path[current_cell_index])
                        else:
                            if grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                                if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                    create_pipe(type="straight", cell=grid_path[current_cell_index])
                                elif grid_path[current_cell_index]+pipe_columns==grid_path[next_cell_index]:
                                    create_pipe(type="curved", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]-pipe_columns==grid_path[prev_cell_index]:
                                if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                    create_pipe(type="curved", cell=grid_path[current_cell_index])
                                elif grid_path[current_cell_index]+pipe_columns==grid_path[next_cell_index]:
                                    create_pipe(type="straight", cell=grid_path[current_cell_index])
                else:
                    random_type=renpy.random.choice(list(pipe_types.keys()))
                    create_pipe(type=random_type, cell=i)
            elif i==amount_of_pipes:
                current_cell_index=grid_path.index(i)
                if grid_path[current_cell_index]-1==grid_path[-2]:
                    create_pipe(type="straight", cell=grid_path[current_cell_index])
                else:
                    create_pipe("curved", cell=grid_path[current_cell_index])

    def create_pipe(type, cell):
        pipe_image="%s-pipe.png"%type
        pipe_end_points=list(pipe_types[type])
        final_pipe=[pipe_image, type, pipe_end_points, cell, 0]
        pipes.append(final_pipe)

    def generated_grid_path():
        global grid_path

        grid_path=[1]

        for i in range(pipe_columns+pipe_rows-2):
            if grid_path[-1]%pipe_columns==0 and grid_path[-1]<=amount_of_pipes-pipe_columns:
                grid_path.append(grid_path[-1]+pipe_columns)

            elif grid_path[-1]%pipe_columns!=0 and grid_path[-1]<= amount_of_pipes-pipe_columns:
                potential_cells=["right", "down"]
                random_pick=renpy.random.choice(potential_cells)
                if random_pick=="right":
                    grid_path.append(grid_path[-1]+1)
                elif random_pick=="down":
                    grid_path.append(grid_path[-1]+pipe_columns)

            elif grid_path[-1]>amount_of_pipes-pipe_columns:
                grid_path.append(grid_path[-1]+1)
    
    def update_pipe_endpoints(cell):
        for pipe in pipes:
            if pipe[3]==cell:
                for endpoint in pipe[2]:
                    if endpoint=="top":
                        endpoints_index=pipe[2].index("top")
                        pipe[2][endpoints_index]="right"
                    elif endpoint=="right":
                        endpoints_index=pipe[2].index("right")
                        pipe[2][endpoints_index]="bottom"
                    elif endpoint=="bottom":
                        endpoints_index=pipe[2].index("bottom")
                        pipe[2][endpoints_index]="left"
                    elif endpoint=="left":
                        endpoints_index=pipe[2].index("left")
                        pipe[2][endpoints_index]="top"
                break

    def rotate_pipe(cell):
        if pipes[cell-1][4]==360:
            pipes[cell-1][4]=90
        else:
            pipes[cell-1][4]+=90

        update_pipe_endpoints(cell)
        check_pipe_connections()
    
    def check_pipe_connections():
        global connected_pipes

        connected_pipes=[]

        if "left" in pipes[0][2] and pipes[0] not in connected_pipes:
            connected_pipes.append(pipes[0])

        if len(connected_pipes)>0 and connected_pipes[0][3]==1:
            for pipe in connected_pipes:
                pipe_to_add=None
                if pipe[3]%pipe_columns==1 and pipe[3]!=1 and "left" in pipe[2]:
                    break
                if pipe[3]%pipe_columns!=0:
                    if "right" in pipe[2]:
                        if "left" in pipes[pipe[3]][2]:
                            if pipes[pipe[3]] not in connected_pipes:
                                pipe_to_add=pipes[pipe[3]]
                        else:
                            break
                if pipe[3]<=amount_of_pipes-pipe_columns:
                    if "bottom" in pipe[2]:
                        if "top" in pipes[pipe[3]-1+pipe_columns][2]:
                            if pipes[pipe[3]-1+pipe_columns] not in connected_pipes:
                                pipe_to_add=pipes[pipe[3]-1+pipe_columns]
                        else:
                            break

                elif pipe[3]>amount_of_pipes-pipe_columns and "bottom" in pipe[2]:
                    break
                if pipe[3]>pipe_columns:
                    if "top" in pipe[2]:
                        if "bottom" in pipes[pipe[3]-1-pipe_columns][2]:
                            if pipes[pipe[3]-1-pipe_columns] not in connected_pipes:
                                pipe_to_add=pipes[pipe[3]-1-pipe_columns]
                        else:
                            break

                elif pipe[3]<=pipe_columns and "top" in pipe[2]:
                    break
                
                if pipe[3]%pipe_columns!=1 and pipe[3]!=amount_of_pipes:
                    if "left" in pipe[2]:
                        if "right" in pipes[pipe[3]-2][2]:
                            if pipes[pipe[3]-2] not in connected_pipes:
                                pipe_to_add=pipes[pipe[3]-2]
                        else:
                            break

                if pipe_to_add!=None:
                    connected_pipes.append(pipe_to_add)

        if len(connected_pipes)>0:
            if amount_of_pipes==connected_pipes[-1][3]:
                if "right" not in connected_pipes[-1][2]:
                    connected_pipes.pop(-1)
                else:
                    renpy.show_screen("pipe_game_success")

screen pipe_game_success:
    modal True
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            xsize 450
            ysize 200
            padding(20, 15)
            align(0.5, 0.5)
            text "Success! Play Again?" color "#FFFFFF" size 30 align(0.5, 0.2)
            grid 2 1:
                spacing 100
                align(0.5, 0.5)
                textbutton "yes" text_color "#FFFFFF" text_size 30 xalign 0.5 action [Function(setup_pipe_game), Hide("pipe_ga")]
                textbutton "no" text_color "#FFFFFF" text_size 30 xalign 0.5 action Function(renpy.full_restart)