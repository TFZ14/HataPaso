screen connect_the_cables:
    image "minigame1/bgminigame1.png"

    grid cable_columns cable_rows:
        spacing 0
        pos(640, 140)
        anchor(0.0, 0.0)
        for cable in cables:
            if cable in connected_cables:
                imagebutton idle Transform("minigame1/%s-cable-connected.png"%cable[1], rotate=cable[4], rotate_pad=False) action Function(rotate_cable, cell=cable[3])
            else:
                imagebutton idle Transform(cable[0], rotate=cable[4], rotate_pad=False) action Function(rotate_cable, cell=cable[3])


default cable_rows=4
default cable_columns=4
default amount_of_cables = cable_rows*cable_columns
default grid_path=[]
default cables=[]
default cable_types={"straight":("top", "bottom"), "square":("right", "bottom"), "t":("top", "bottom", "left"), "cross":("top", "bottom", "left", "right")}
default connected_cables=[]

init python:
    def setup_cable_game():
        global cables
        global connected_cables

        cables=[]
        connected_cables=[]

        generated_grid_path()

        create_cables()

    def create_cables():
        for i in range(1, amount_of_cables+1):
            if i==1:
                if grid_path[0]+1==grid_path[1]:
                    create_cable(type="straight",cell=i)
                elif grid_path[0]+cable_columns==grid_path[1]:
                    create_cable(type="square",cell=i)

            elif i>1 and i<amount_of_cables:
                if i in grid_path:
                    current_cell_index=grid_path.index(i)
                    next_cell_index=current_cell_index+1
                    prev_cell_index=current_cell_index-1
                    if grid_path[current_cell_index]%cable_columns==1:
                        if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                            create_cable(type="square", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]+cable_columns==grid_path[next_cell_index]:
                            create_cable(type="straight", cell=grid_path[current_cell_index])
                    elif grid_path[current_cell_index]%cable_columns==0 and grid_path[current_cell_index]<=cable_columns:
                        create_cable(type="square", cell=grid_path[current_cell_index])
                    elif grid_path[current_cell_index]%cable_columns==0 and grid_path[current_cell_index]>cable_columns:
                        if grid_path[current_cell_index]-cable_columns==grid_path[prev_cell_index]:
                            create_cable(type="straight", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                            create_cable(type="square", cell=grid_path[current_cell_index])
                    else:
                        if grid_path[current_cell_index]<=cable_rows:
                            if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                create_cable(type="straight", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]+cable_columns==grid_path[next_cell_index]:
                                create_cable(type="square", cell=grid_path[current_cell_index])
                        elif grid_path[current_cell_index]>=amount_of_cables-cable_columns:
                            if grid_path[current_cell_index]-cable_columns==grid_path[prev_cell_index]:
                                create_cable(type="square", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                                create_cable(type="straight", cell=grid_path[current_cell_index])
                        else:
                            if grid_path[current_cell_index]-1==grid_path[prev_cell_index]:
                                if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                    create_cable(type="straight", cell=grid_path[current_cell_index])
                                elif grid_path[current_cell_index]+cable_columns==grid_path[next_cell_index]:
                                    create_cable(type="square", cell=grid_path[current_cell_index])
                            elif grid_path[current_cell_index]-cable_columns==grid_path[prev_cell_index]:
                                if grid_path[current_cell_index]+1==grid_path[next_cell_index]:
                                    create_cable(type="square", cell=grid_path[current_cell_index])
                                elif grid_path[current_cell_index]+cable_columns==grid_path[next_cell_index]:
                                    create_cable(type="straight", cell=grid_path[current_cell_index])
                else:
                    random_type=renpy.random.choice(list(cable_types.keys()))
                    create_cable(type=random_type, cell=i)
            elif i==amount_of_cables:
                current_cell_index=grid_path.index(i)
                if grid_path[current_cell_index]-1==grid_path[-2]:
                    create_cable(type="straight", cell=grid_path[current_cell_index])
                else:
                    create_cable("square", cell=grid_path[current_cell_index])

    def create_cable(type, cell):
        cable_image="minigame1/%s-cable.png"%type
        cable_end_points=list(cable_types[type])
        final_cable=[cable_image, type, cable_end_points, cell, 0]
        cables.append(final_cable)

    def generated_grid_path():
        global grid_path

        grid_path=[1]

        for i in range(cable_columns+cable_rows-2):
            if grid_path[-1]%cable_columns==0 and grid_path[-1]<=amount_of_cables-cable_columns:
                grid_path.append(grid_path[-1]+cable_columns)

            elif grid_path[-1]%cable_columns!=0 and grid_path[-1]<= amount_of_cables-cable_columns:
                potential_cells=["right", "down"]
                random_pick=renpy.random.choice(potential_cells)
                if random_pick=="right":
                    grid_path.append(grid_path[-1]+1)
                elif random_pick=="down":
                    grid_path.append(grid_path[-1]+cable_columns)

            elif grid_path[-1]>amount_of_cables-cable_columns:
                grid_path.append(grid_path[-1]+1)
    
    def update_cable_endpoints(cell):
        for cable in cables:
            if cable[3]==cell:
                for endpoint in cable[2]:
                    if endpoint=="top":
                        endpoints_index=cable[2].index("top")
                        cable[2][endpoints_index]="right"
                    elif endpoint=="right":
                        endpoints_index=cable[2].index("right")
                        cable[2][endpoints_index]="bottom"
                    elif endpoint=="bottom":
                        endpoints_index=cable[2].index("bottom")
                        cable[2][endpoints_index]="left"
                    elif endpoint=="left":
                        endpoints_index=cable[2].index("left")
                        cable[2][endpoints_index]="top"
                break

    def rotate_cable(cell):
        if cables[cell-1][4]==360:
            cables[cell-1][4]=90
        else:
            cables[cell-1][4]+=90

        update_cable_endpoints(cell)
        check_cable_connections()
    
    def check_cable_connections():
        global connected_cables

        connected_cables=[]

        if "left" in cables[0][2] and cables[0] not in connected_cables:
            connected_cables.append(cables[0])

        if len(connected_cables)>0 and connected_cables[0][3]==1:
            for cable in connected_cables:
                cable_to_add=None
                if cable[3]%cable_columns==1 and cable[3]!=1 and "left" in cable[2]:
                    break
                if cable[3]%cable_columns!=0:
                    if "right" in cable[2]:
                        if "left" in cables[cable[3]][2]:
                            if cables[cable[3]] not in connected_cables:
                                cable_to_add=cables[cable[3]]
                        else:
                            break
                if cable[3]<=amount_of_cables-cable_columns:
                    if "bottom" in cable[2]:
                        if "top" in cables[cable[3]-1+cable_columns][2]:
                            if cables[cable[3]-1+cable_columns] not in connected_cables:
                                cable_to_add=cables[cable[3]-1+cable_columns]
                        else:
                            break

                elif cable[3]>amount_of_cables-cable_columns and "bottom" in cable[2]:
                    break
                if cable[3]>cable_columns:
                    if "top" in cable[2]:
                        if "bottom" in cables[cable[3]-1-cable_columns][2]:
                            if cables[cable[3]-1-cable_columns] not in connected_cables:
                                cable_to_add=cables[cable[3]-1-cable_columns]
                        else:
                            break

                elif cable[3]<=cable_columns and "top" in cable[2]:
                    break
                
                if cable[3]%cable_columns!=1 and cable[3]!=amount_of_cables:
                    if "left" in cable[2]:
                        if "right" in cables[cable[3]-2][2]:
                            if cables[cable[3]-2] not in connected_cables:
                                cable_to_add=cables[cable[3]-2]
                        else:
                            break

                if cable_to_add!=None:
                    connected_cables.append(cable_to_add)

        if len(connected_cables)>0:
            if amount_of_cables==connected_cables[-1][3]:
                if "right" not in connected_cables[-1][2]:
                    connected_cables.pop(-1)
                else:
                    renpy.jump("cable_game_success")

label cable_game_success:
    mc1 "kabel selesai"
    jump act1_cpudone