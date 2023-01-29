cone = [{"X":0,"Y":1,"Z":0,"links":[1,2,3,4]},
        {"X":1,"Y":0,"Z":1,"links":[0,2,3,4]},
        {"X":0,"Y":0,"Z":0,"links":[0,1,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,1,2,4]},
        {"X":0.5,"Y":0.5,"Z":1,"links":[0,1,2,3]}]

truc = [{"X":0,"Y":1,"Z":0,"links":[1,2,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,2,3,4]},
        {"X":0,"Y":0,"Z":1,"links":[0,1,3,4]},
        {"X":1,"Y":0,"Z":1,"links":[0,1,2,4]},
        {"X":0.5,"Y":0,"Z":1.5,"links":[0,1,2,3]}]

cube = [{"X":0,"Y":0,"Z":0,"links":[1,3,4]},
        {"X":10,"Y":0,"Z":0,"links":[0,2,5]},
        {"X":10,"Y":10,"Z":0,"links":[1,3,6]},
        {"X":0,"Y":10,"Z":0,"links":[0,2,7]},
        {"X":0,"Y":0,"Z":10,"links":[0,5,7]},
        {"X":10,"Y":0,"Z":10,"links":[1,4,6]},
        {"X":10,"Y":10,"Z":10,"links":[2,5,7]},
        {"X":0,"Y":10,"Z":10,"links":[3,4,6]}]


"""

Below is the questions that I kept/copy pasted to chat GPT. It's not cleaned nor necessarily those that generated the right answers.
More like a notepad so I wouldn't have to find the original discussions since OpenAI was overloaded.
I really just started by showing it the cone and asked for a cube. Which it created successfuly at the first try. Then I used the cube for most prompts.

I've got a shape defined like that :
cube = [{"X":0,"Y":0,"Z":0,"links":[1,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,2,5]},
        {"X":1,"Y":1,"Z":0,"links":[1,3,6]},
        {"X":0,"Y":1,"Z":0,"links":[0,2,7]},
        {"X":0,"Y":0,"Z":1,"links":[0,5,7]},
        {"X":1,"Y":0,"Z":1,"links":[1,4,6]},
        {"X":1,"Y":1,"Z":1,"links":[2,5,7]},
        {"X":0,"Y":1,"Z":1,"links":[3,4,6]}]

Now let's say I have the following virtual camera :
camera={"X":0,"Y":0,"Z":-10,"rot_X":0,"rot_Y":0,"rot_Z":0,"FOV_X":90,"FOV_Y":90}

and a screen of the following size (X,Y):
screen_size = [800,600]

Write a function that would give me the 2D coordinates of each dots of the previous shapes (I'm talking about the cone and cube for example, it would take them as an input).
The input of the function should just be the shape. The camera is a global variable since there is only one so it's already known, just like the screen size. The function should output the 2D coordinates of each dots and the 2D coordinates for the start and end of each links in these shapes.
Something like this (except that the X and Y should be the actual values, that's just a example of the format) {"dots":[(X,Y),(X,Y), ...],"links":[((X,Y),(X,Y)),((X,Y),(X,Y)),((X,Y),(X,Y)), ...]}

The goal is to be able to make a basic wireframe 3D engine. The camera being the point of view of the player in a 3D environment.

Don't forget to format your output as code. Make the code as short as possible. No need to # comment

Start the function like that :
shape_to_2D(shape, camera, screen_size)

 ------------------------------------------------------------------------

I've got a shape defined like that :
cube = [{"X":0,"Y":0,"Z":0,"links":[1,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,2,5]},
        {"X":1,"Y":1,"Z":0,"links":[1,3,6]},
        {"X":0,"Y":1,"Z":0,"links":[0,2,7]},
        {"X":0,"Y":0,"Z":1,"links":[0,5,7]},
        {"X":1,"Y":0,"Z":1,"links":[1,4,6]},
        {"X":1,"Y":1,"Z":1,"links":[2,5,7]},
        {"X":0,"Y":1,"Z":1,"links":[3,4,6]}]

write a python function that would return a spherical object, represented the same way
The sphere should be made of multiple circles with a radius that would variate relatively from their distance to the center (so it would look like an actual sphere).
The function should take as an input the radius, the central X Y Z coordinates and the number of dots per circle.
The dots should only be linked to the ones next to them on the same circle (the first and last of each circle should be linked too) and to those that are on the same index as them on the above and below circle.

 ------------------------------------------------------------------------

I have a camera defined like that :
camera={"X":0,"Y":0,"Z":-10,"rot_X":0,"rot_Y":0,"rot_Z":0,"FOV_X":90,"FOV_Y":90}

write a function made to be used with pygame that allows me to move the camera relatively to it's Y rotation angle (0-360)

 ------------------------------------------------------------------------

I've got a shape defined like that :
cube = [{"X":0,"Y":0,"Z":0,"links":[1,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,2,5]},
        {"X":1,"Y":1,"Z":0,"links":[1,3,6]},
        {"X":0,"Y":1,"Z":0,"links":[0,2,7]},
        {"X":0,"Y":0,"Z":1,"links":[0,5,7]},
        {"X":1,"Y":0,"Z":1,"links":[1,4,6]},
        {"X":1,"Y":1,"Z":1,"links":[2,5,7]},
        {"X":0,"Y":1,"Z":1,"links":[3,4,6]}]

Create a function that creates more complex cubes. It should take as an input the size, the number of dots per cube, the (X,Y,Z) center coordinate and the (X,Y,Z) rotation.

Don't forget to output as code.

 ------------------------------------------------------------------------

I've got a shape defined like that :
cube = [{"X":0,"Y":0,"Z":0,"links":[1,3,4]},
        {"X":1,"Y":0,"Z":0,"links":[0,2,5]},
        {"X":1,"Y":1,"Z":0,"links":[1,3,6]},
        {"X":0,"Y":1,"Z":0,"links":[0,2,7]},
        {"X":0,"Y":0,"Z":1,"links":[0,5,7]},
        {"X":1,"Y":0,"Z":1,"links":[1,4,6]},
        {"X":1,"Y":1,"Z":1,"links":[2,5,7]},
        {"X":0,"Y":1,"Z":1,"links":[3,4,6]}]

Create a function that can rotate any shape around it's center.

Don't forget to output as code.

 ------------------------------------------------------------------------

I have a function that rotates my camera in a game that I made like this :

def capture_mouse_moves(mouse_move):
    dx, dy = mouse_move
    cam_angle = camera["rot_Y"]/180*math.pi*-1
    camera["rot_X"] -= dy/100 * math.cos(cam_angle) * rotation_speed
    camera["rot_Z"] -= dy/100 * math.sin(cam_angle) * rotation_speed
    camera["rot_Y"] += dx/100 * rotation_speed

Rewrite it so the camera is never tilted on the side.
It should still be able to tilt forward, relatively to the Y rotation axis. Use trigonometry.
Don't forget to output as code.

 ------------------------------------------------------------------------

I have a camera defined like that :
camera={"X":0,"Y":0,"Z":-142,"rot_X":0,"rot_Y":0,"rot_Z":0,"FOV_X":116,"FOV_Y":90}

write a function so I can rotate it sideways relatively to the Y axis.
Don't forget to output as code.

 ------------------------------------------------------------------------

I have a function that rotates my camera in a game that I made like this :

def capture_mouse_moves(mouse_move):
    dx, dy = mouse_move
    cam_angle = camera["rot_Y"]/180*math.pi*-1
    camera["rot_X"] -= dy/100 * math.cos(cam_angle) * rotation_speed
    camera["rot_Z"] -= dy/100 * math.sin(cam_angle) * rotation_speed
    camera["rot_Y"] += dx/100 * rotation_speed

Rewrite it so I can still tilt the camera forward relatively to it's Y orientation but in a way that it is always upright. Y being the vertical axis.
Avoid direct < or > comparisons.

Don't forget to output as code.
"""

import math
import pygame
from random import randint
from copy import deepcopy
import colorsys
import threading
import time

text_indent=10
movement_speed = 1
rotation_speed = 10
screen_size = [1920,1080]
fov_x = 90
fov_y = 90/screen_size[0]*(screen_size[1]*1.16)
camera={"X":0,"Y":0,"Z":-360,"rot_X":0,"rot_Y":0,"rot_Z":0,"FOV_X":fov_x,"FOV_Y":fov_y}
cam_init=deepcopy(camera)

cam_tilt=False
auto_cam=True
show_dots=True
show_lines=True
show_grid=True

def daemonizer(fName, *args):
    try:
        daemon = threading.Thread(target=fName, args=args)
        daemon.daemon = True
        daemon.start()
        return daemon
    except Exception as e:
        print(e)

def cube_refresher():
    global cubes, cubes_rotations, n_cubes
    while True:
        cubes, cubes_rotations = make_cubes(n_cubes)
        time.sleep(12)

def remap_range(value, minIn, MaxIn, minOut, maxOut):
            if value > MaxIn: value = MaxIn;
            if value < minIn: value = minIn;
            finalValue = ((value - minIn) / (MaxIn - minIn)) * (maxOut - minOut) + minOut;
            return finalValue;

def text_to_screen(screen, text, x=32, y=0, size = 24,
            color = (255, 255, 255)):
    global text_indent
    try:
        text = str(text)
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(text, True, color)
        screen.blit(text, (x, text_indent))
        text_indent+=size+4
    except Exception as e:
        print(e)

def move_shape(shape,move,mult=1):
    for dot in shape:
        dot["X"]+=move[0]*mult
        dot["Y"]+=move[1]*mult
        dot["Z"]+=move[2]*mult

def average_center(shape):
    center_x = sum(d['X'] for d in shape) / len(shape)
    center_y = sum(d['Y'] for d in shape) / len(shape)
    center_z = sum(d['Z'] for d in shape) / len(shape)
    return center_x, center_y, center_z

def distance(x1, y1, z1, x2, y2, z2):
    d = 0.0
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return d

def rotate_shape(shape, angles):
    center_x = sum(d['X'] for d in shape) / len(shape)
    center_y = sum(d['Y'] for d in shape) / len(shape)
    center_z = sum(d['Z'] for d in shape) / len(shape)

    for point in shape:
        # Translate to origin
        x = point['X'] - center_x
        y = point['Y'] - center_y
        z = point['Z'] - center_z

        # Perform rotations
        x_new = x
        y_new = y * math.cos(angles[0]) - z * math.sin(angles[0])
        z_new = y * math.sin(angles[0]) + z * math.cos(angles[0])
        x, y, z = x_new, y_new, z_new

        y_new = y * math.cos(angles[1]) - z * math.sin(angles[1])
        z_new = y * math.sin(angles[1]) + z * math.cos(angles[1])
        y, z = y_new, z_new

        x_new = x * math.cos(angles[2]) - y * math.sin(angles[2])
        y_new = x * math.sin(angles[2]) + y * math.cos(angles[2])
        x, y = x_new, y_new

        # Translate back to original position
        point['X'] = x + center_x
        point['Y'] = y + center_y
        point['Z'] = z + center_z

    return shape


def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def create_sphere(radius, center_x, center_y, center_z, dots_per_circle):
    sphere = []
    for i in range(dots_per_circle+1):
        phi = math.pi * (i / dots_per_circle)
        for j in range(dots_per_circle):
            theta = 2 * math.pi * (j / dots_per_circle)
            x = radius * math.sin(phi) * math.cos(theta) + center_x
            y = radius * math.sin(phi) * math.sin(theta) + center_y
            z = radius * math.cos(phi) + center_z
            links = []
            links.append((j+dots_per_circle) + i * dots_per_circle)
            links.append((j + 1) % dots_per_circle + i * dots_per_circle)
            sphere.append({"X": x, "Y": y, "Z": z, "links": links})
    return sphere

def create_grid_with_center(size, dots_per_row, center_x, center_y, center_z):
    grid = []
    for i in range(dots_per_row):
        for j in range(dots_per_row):
            x = i * size + center_x - (size * dots_per_row) / 2
            y = j * size + center_y - (size * dots_per_row) / 2
            z = center_z
            links = []
            if i > 0:
                links.append((i-1) * dots_per_row + j)
            if i < dots_per_row - 1:
                links.append((i+1) * dots_per_row + j)
            if j > 0:
                links.append(i * dots_per_row + (j-1))
            if j < dots_per_row - 1:
                links.append(i * dots_per_row + (j+1))
            grid.append({"X": x, "Y": z, "Z": y, "links": links})
    return grid

def shape_to_2D(shape, camera, screen_size):
    result = {"dots": [], "links": []}
    for dot in shape:
        dot_2D = project_3D_to_2D(dot, camera, screen_size)
        result["dots"].append(dot_2D)
        for link in dot["links"]:
            try:
                link_dot = shape[link]
                link_2D = (dot_2D, project_3D_to_2D(link_dot, camera, screen_size))
                result["links"].append(link_2D)
            except Exception as e:
                pass
    return result

def project_3D_to_2D(dot, camera, screen_size):
    x = dot["X"] - camera["X"]
    y = dot["Y"] - camera["Y"]
    z = dot["Z"] - camera["Z"]
    rot_X = camera["rot_X"]
    rot_Y = camera["rot_Y"]
    rot_Z = camera["rot_Z"]
    x, y = rotate_2D(x, y, rot_Z)
    y, z = rotate_2D(y, z, rot_X)
    x, z = rotate_2D(x, z, rot_Y)
    fov_x = camera["FOV_X"]
    fov_y = camera["FOV_Y"]
    screen_x = screen_size[0]
    screen_y = screen_size[1]
    zx=z * math.tan(math.radians(fov_x / 2))
    zy=z * math.tan(math.radians(fov_y / 2))
    if zx > 0 and zy > 0:
        x =  x * screen_x / (zx) + screen_x / 2
        y = -y * screen_y / (zy) + screen_y / 2
    else:
        x = -10000000
        y = -10000000
    return (x, y)

def rotate_2D(x, y, angle):
    rad = math.radians(angle)
    cosa = math.cos(rad)
    sina = math.sin(rad)
    return x * cosa - y * sina, x * sina + y * cosa

def capture_mouse_moves(mouse_move):
    dx, dy = mouse_move
    cam_angle_x = camera["rot_X"]/180*math.pi*-1
    cam_angle_y = camera["rot_Y"]/180*math.pi*-1
    # cam_angle_z = camera["rot_Z"]/180*math.pi*-1
    if cam_tilt:
        camera["rot_X"] -= dy/100 * math.cos(cam_angle_y) * rotation_speed
        camera["rot_Z"] -= dy/100 * math.sin(cam_angle_y) * math.cos(cam_angle_x) * rotation_speed
    camera["rot_Y"] += dx/100 * rotation_speed

def handle_camera_movement(camera,go_left=False):
    keys = pygame.key.get_pressed()
    camera = deepcopy(camera)
    cam_angle = camera["rot_Y"]/180*math.pi*-1

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        camera["X"] -= math.sin(cam_angle) * movement_speed
        camera["Z"] += math.cos(cam_angle) * movement_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        camera["X"] += math.sin(cam_angle) * movement_speed
        camera["Z"] -= math.cos(cam_angle) * movement_speed
    if keys[pygame.K_a] or go_left:
        camera["X"] -= math.cos(cam_angle) * movement_speed
        camera["Z"] -= math.sin(cam_angle) * movement_speed
    if keys[pygame.K_d]:
        camera["X"] += math.cos(cam_angle) * movement_speed
        camera["Z"] += math.sin(cam_angle) * movement_speed
    if keys[pygame.K_LEFT]:
        camera["rot_Y"] -= rotation_speed/20
    if keys[pygame.K_RIGHT]:
        camera["rot_Y"] += rotation_speed/20
    if keys[pygame.K_SPACE]:
        camera["Y"] += 1.3
    if keys[pygame.K_LSHIFT]:
        camera["Y"] -= 1.3

    if keys[pygame.K_e]:
        camera["FOV_X"] += movement_speed
        camera["FOV_Y"] += movement_speed
    if keys[pygame.K_q]:
        camera["FOV_X"] -= movement_speed
        camera["FOV_Y"] -= movement_speed
    if keys[pygame.K_r]:
        camera = cam_init

    return camera

def check_dot(dot):
    margin=150
    screen_x,screen_y=screen_size
    return (dot[0] < -margin or dot[0] > screen_x+margin or dot[1] < 0-margin or dot[1] > screen_y+margin) or (dot[0] == 0 and dot[1]==0)

rgb_col=0
def draw_shape(shape, col_add=0):
    global rgb_col

    # Draw the dots
    rgb_col_diff = 0
    for dot in shape["dots"]:
        color_rgb=hsv2rgb((rgb_col+rgb_col_diff)%255/255,1,1)
        rgb_col_diff+=0.1
        if not check_dot(dot) and show_dots:
            pygame.draw.circle(screen, color_rgb, dot, 3)

    # Draw the links
    for link in shape["links"]:
        color_rgb=hsv2rgb((rgb_col+rgb_col_diff+24*col_add)%255/255,1,1)
        rgb_col+=0.0007
        rgb_col_diff+=0.3
        start, end = link
        if not check_dot(start) and not check_dot(end) and show_lines:
            pygame.draw.line(screen, color_rgb, start, end, 2)

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode(screen_size)

# Set the title of the window
pygame.display.set_caption("3D shape")
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

grid = create_grid_with_center(24,14,0,0,-80)

variation_speed=0.03
sphere_variation=0
sphere_xyz=[0,0,0]
sphere_xyz_target_start=[0,0,0]
sphere_xyz_target_end  =[randint(-10,10),randint(-10,10),randint(-10,10)]
def smoothie(coord,start,end,progress):
    progress = progress%1
    text_to_screen(screen,"p : "+str(progress),50,text_indent)
    coord = remap_range(progress,0,1,start,end)
    # print(progress,coord,start,end)
    if progress > (1-variation_speed):
        start=end
        end=randint(-50,50)
    return coord,start,end

n_cubes = 12
def make_cubes(n_cubes):
    cubes = []
    cubes_rotations = []
    for x in range(n_cubes):
        c = deepcopy(cube)
        random_pos = 150
        speed_divider=3000
        move_shape(c,(randint(-random_pos,random_pos),randint(-int(random_pos/3),int(random_pos/1.5)),randint(-random_pos,random_pos)))
        cubes.append(c)
        cubes_rotations.append([randint(-10,10)/speed_divider*rotation_speed,randint(-10,10)/speed_divider*rotation_speed,randint(-10,10)/speed_divider*rotation_speed])
    return cubes, cubes_rotations
cubes, cubes_rotations = make_cubes(n_cubes)

n_spheres=1
sphere_sizes= [4,8,16,32,42,64,128,256]
sphere_rez  = [4,8,16,20,24,32,50,64]
sphere_size=4
sphere_dots=4
def make_spheres(n_spheres,sphere_size,sphere_dots):
    spheres=[]
    spheres_rotations=[]
    speed_divider=22000
    for x in range(n_spheres):
        faster_inside = speed_divider + (x)*3000
        spheres.append(create_sphere(sphere_size+x*(sphere_size/2),0,0,0,int(sphere_dots*((x/n_spheres)+1))))
        spheres_rotations.append([randint(5,10)/faster_inside*rotation_speed,randint(5,10)/faster_inside*rotation_speed,randint(5,10)/faster_inside*rotation_speed])
    return spheres, spheres_rotations
spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])

def autocam(camera):
    camera=handle_camera_movement(camera,True)
    angle = math.atan2(camera["X"],camera["Z"])/math.pi*180-180
    camera["rot_Y"]=angle
    return camera
    # text_to_screen(screen,"Cam angle to center : "+str(angle))

daemonizer(cube_refresher)

# Run the game loop
running = True
while running:
    threads = []
    text_indent=32
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
                    exit()
                if event.key == pygame.K_KP_PLUS:
                    n_spheres+=1
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_KP_MINUS:
                    n_spheres-=1
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_1:
                    sphere_dots-=1
                    print(sphere_dots%len(sphere_rez))
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_2:
                    sphere_dots+=1
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_3:
                    sphere_size-=1
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_4:
                    sphere_size+=1
                    spheres, spheres_rotations = make_spheres(n_spheres,sphere_sizes[sphere_size%len(sphere_sizes)],sphere_rez[sphere_dots%len(sphere_rez)])
                if event.key == pygame.K_KP6:
                    n_cubes-=1
                    cubes, cubes_rotations = make_cubes(n_cubes)
                if event.key == pygame.K_KP9:
                    n_cubes+=1
                    cubes, cubes_rotations = make_cubes(n_cubes)
                if event.key == pygame.K_c:
                    cam_tilt= not cam_tilt
                if event.key == pygame.K_t:
                    auto_cam= not auto_cam
                if event.key == pygame.K_z:
                    show_dots= not show_dots
                if event.key == pygame.K_u:
                    show_lines= not show_lines
                if event.key == pygame.K_g:
                    show_grid= not show_grid
                if event.key == pygame.K_f:
                    camera = roll_camera(camera,0)

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                movement_speed+=1
            else:
                movement_speed-=1

        if event.type == pygame.MOUSEMOTION:
            capture_mouse_moves(event.rel)

    screen.fill((0,0,0))
    camera = handle_camera_movement(camera)
    if auto_cam:
        camera = autocam(camera)
    # Clear the screen

    # moving sphere coordinates :
    # for xyz in range(len(sphere_xyz)):
    #     sphere_xyz[xyz],sphere_xyz_target_start[xyz],sphere_xyz_target_end[xyz]=smoothie(sphere_xyz[xyz],sphere_xyz_target_start[xyz],sphere_xyz_target_end[xyz],sphere_variation)

    try:
        for s in range(len(spheres)):
            rotate_shape(spheres[s],spheres_rotations[s])
            draw_shape(shape_to_2D(spheres[s], camera, screen_size))
        # moving sphere display :
        # draw_shape(shape_to_2D(create_sphere(7*(math.sin(sphere_variation*math.pi)/2+4),sphere_xyz[0],sphere_xyz[1],sphere_xyz[2],20), camera, screen_size))
        if show_grid:
            draw_shape(shape_to_2D(grid, camera, screen_size))
        for c in range(len(cubes)):
            rotate_shape(cubes[c],cubes_rotations[c])
            move_shape(cubes[c],cubes_rotations[c],10)
            draw_shape(shape_to_2D(cubes[c], camera, screen_size),c)
    except Exception as e:
        print(e)
    sphere_variation+=variation_speed

    for cam in camera:
        text_to_screen(screen,cam+" : "+str(round(camera[cam],2)))
    text_to_screen(screen, "cam_tilt (c) : "+str(cam_tilt))
    text_to_screen(screen, "auto cam (t) : "+str(auto_cam))
    text_to_screen(screen, "show_grid (g) : "+str(show_grid))
    text_to_screen(screen,"Reset pos (r)")
    text_to_screen(screen,"More spheres (keypad+)")
    text_to_screen(screen,"Less spheres (keypad -)")
    text_to_screen(screen,"More cubes (keypad 9)")
    text_to_screen(screen,"Less cubes (keypad 6)")
    text_to_screen(screen,"Cubes : "+str(n_cubes))
    text_to_screen(screen, "movement_speed (mouse wheel) : "+str(movement_speed))


    pygame.display.flip()
    time.sleep(1/120)

pygame.quit()
