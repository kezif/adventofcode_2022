#from tqdm import tqdm
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import numpy as np
from os import system
from time import sleep

INPUT_PATH = 'input\\input14.txt'

TEST_INPUT = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split('\n')

SAND_GEN_LOC = 500,0
SIMULATION_LEN = 10_000_000




def part_one(data: list[str]):
    #loading data
    walls_pos = []
    all_cords = []
    for line in data[:]:
        for coords in zip(line.split('->')[:-1], line.split('->')[1:]):
            coords =  [(int(c1), int(c2)) for (c1,c2) in  (coord.split(',') for coord in coords)]
            coord1, coord2  = sorted(coords, key=lambda ab: ab[0]+ ab[1])
            walls_pos.append((coord1, coord2))

            all_cords.extend([coord1, coord2])

    xs = [xy[0] for xy in all_cords]
    ys = [xy[1] for xy in all_cords]
    min_x, min_y = min(xs), min(ys)
    max_x, max_y = max(xs), max(ys)
    #print('min',min_x, max_x)
    #print('max',min_y, max_y)


    p_shape = (550, 200)
    offset_x = 494
    
    additional_x = 200
    p_shape = (max_x-min_x+2 + additional_x *2, max_y-0+2 + 1 )  # second +2 for extra space for floor
    offset_x = min_x-1 - additional_x
    offset_y = 0#min_y
    playground = np.zeros(p_shape, dtype=np.byte)
    playground[:,-1] = np.ones(p_shape[0], dtype=np.byte)  # floor for part two


    for pos in walls_pos[:]:
        c1, c2 = pos
        c1 = c1[0] - offset_x, c1[1] - offset_y
        c2 = c2[0] - offset_x, c2[1] - offset_y
        playground[c1[0]:c2[0]+1, c1[1]:c2[1]+1] = np.ones(playground[c1[0]:c2[0]+1, c1[1]:c2[1]+1].shape)


    #playground[SAND_GEN_LOC[0]-offset_x, SAND_GEN_LOC[1]] = 9

    #simulating
    # i didnt accout that x and y axis is inverted. So so display array corrently - im transposing it.
    # for convenience of simulation i would do it now
    
    playground[SAND_GEN_LOC[0]-offset_x, SAND_GEN_LOC[1]] = 3
    playground = playground.T
    np.savetxt('test14.txt',playground, fmt='%d')

    history = [(0, playground.copy())]
    sand_gen =  SAND_GEN_LOC[1] - offset_y, SAND_GEN_LOC[0] - offset_x
    sand_loc = current_sand_loc = sand_gen
    satled_sand = 0
    part_one_done = False
    for _ in range(SIMULATION_LEN):
        down_pos = sand_loc[0]+1, sand_loc[1]
        left_diag = sand_loc[0]+1, sand_loc[1]-1
        right_diag = sand_loc[0]+1, sand_loc[1]+1

        
        if sand_loc[0] == playground.shape[0]-2 and not part_one_done:
            part_one_ans = satled_sand
            part_one_done = True  # one way swith to save value when sand would overflow to the bottom
            #break
        if sand_loc == sand_gen  and np.all(playground[sand_loc[0]+1, sand_loc[1]-1:sand_loc[1]+2] == 3):
            #print(satled_sand)
            satled_sand += 1  # i dont accounting last sand settling. So i'll do it here
            break # no more space for sand
        try:    
            if playground[down_pos] == 0:
                playground[down_pos] = 3
                playground[sand_loc] = 0
                sand_loc = down_pos
            elif playground[left_diag] == 0:
                playground[left_diag] = 3
                playground[sand_loc] = 0
                sand_loc = left_diag
            elif playground[right_diag] == 0:
                playground[right_diag] = 3
                playground[sand_loc] = 0
                sand_loc = right_diag
            else:
                #print(_)
                satled_sand += 1
                sand_loc = sand_gen
        except IndexError:
            break
        
        if  _ % 1000 == 0:
            history.append((satled_sand, playground.copy()))
        print(f'Progress: {_}', end='\r')
        

    print('                   ')
    print(f'Anwser to day fourteen: `{part_one_ans}`') 
    print(f'Anwser to day fourteen p2: `{satled_sand}`')  
    animate(history, save=False)
    #assert 961 == part_one_ans, 'not right anwser'
   
    

def animate(history, save=False):
    fig, ax = plt.subplots(figsize=(12, 8))
    cmap = colors.ListedColormap(['white', '#212121', '#d2aa6d'])
    is_manual = False
    first_text, first_data = history[0]
    ln = ax.imshow(first_data,interpolation='none', animated=True, cmap=cmap)
    label = ax.text(0, 0, first_text, fontsize=14, color="#000000", horizontalalignment='left', verticalalignment='bottom')
    
    ax.set_ylim(first_data.shape[0],0 )
    ax.set_xlim(0,first_data.shape[1])
    ax.axis('off')
    interval = 1
    scale = interval * 6
    axamp = plt.axes([0.25, .03, 0.50, 0.02])
    samp = Slider(axamp, 'Time:', 0, len(history)-1, valinit=0)  # https://stackoverflow.com/questions/46325447/animated-interactive-plot-using-matplotlib

    def update_slider(val):
        nonlocal is_manual
        is_manual=True
        update_(val)

    def update_(val):
        i = int(val)
        sand_count, data = history[i]
        #label.set_text('')
        label.set_text(f'Settled sand: {sand_count}')

        ln.set_array(data)

        fig.canvas.draw_idle()

    
    def on_click(event):
        # Check where the click happened
        (xm,ym),(xM,yM) = samp.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            nonlocal is_manual
            is_manual=False


    def update(i):
        nonlocal is_manual
        if is_manual:
            return ln,

        val = (samp.val + scale) % samp.valmax
        samp.set_val(val)  # value get updated every frame, update_slider is called
        is_manual = False
        return ln,

    def save_call(current_frame: int, total_frames: int) -> any: 
        print(f'Saving {current_frame+1} / {total_frames}    {(current_frame) /total_frames }', end='\r')
    samp.on_changed(update_slider)
    fig.canvas.mpl_connect('button_press_event', on_click)
    ani = FuncAnimation(fig, update, frames=range(len(history)),
                        interval=interval,repeat_delay=150, blit=True)

    plt.show()
    if save:
        ani.save('test_anim.mp4', extra_args=['-vcodec', 'libx264'], fps=interval*3, progress_callback=save_call)
    
    

def part_two(data: list[str]):
   
    print(f'Anwser to day fourteen p2: `{0}`') 


if __name__ == '__main__':
    data = [line.strip() for line in TEST_INPUT]

    with open(INPUT_PATH, 'r') as file:
        data = [line.strip() for line in file.readlines()]


    
    part_one(data)
    #part_two(data)
        