import pygame
#Initializes pygames
pygame.init()

#Imports keystokes for pygames
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Function for sensing collision between user and branches
def branch_collision(b_type, branch, circ, branch_dim, run):

    #Sets width and height for window
    WIDTH = 1200
    LENGTH = 960

    #Checks if loop is already closed and skips this if window is closed
    if (run == False):

        return False

    #Checks for type of branch
    if (b_type == 1):

        #Checks if user is in current branch type's dimensions
        if circ[0] <= branch_dim[0]:

            if branch <= circ[1] <= branch + branch_dim[1] or branch <= circ[1] + circ[2] <= branch + branch_dim[1]:

                return False

    elif (b_type == 2):

        if circ[0] >= WIDTH - branch_dim[0]:

            if branch <= circ[1] <= branch + branch_dim[1] or branch <= circ[1] + circ[2] <= branch + branch_dim[1]:

                return False

    elif (b_type == 3):

        if circ[0] <= branch_dim[2]:

            if branch <= circ[1] <= branch + branch_dim[3] or branch <= circ[1] + circ[2] <= branch + branch_dim[3]:

                return False

    elif (b_type == 4):

        #Horizontal dimensions for this type and next type aren't needed as they are the maximum lengths for
        #their respective side
        if branch <= circ[1] <= branch + branch_dim[3] or branch <= circ[1] + circ[2] <= branch + branch_dim[3]:

            return False

    elif (b_type == 5):

        if branch <= circ[1] <= branch + branch_dim[5] or branch <= circ[1] + circ[2] <= branch + branch_dim[5]:

            return False

    #Returns true if user is not in any of branches
    return True

def actual_game():
    #Loads all branch sprites
    branch_one = pygame.image.load("l_branch.png")
    branch_two = pygame.image.load("r_branch.png")
    branch_three = pygame.image.load("l_longbranch.png")
    branch_four = pygame.image.load("r_longbranch.png")
    branch_five = pygame.image.load("l_xlongbranch.png")

    #Initializes user's circle coordinates/radius
    circ = [760,250,20]

    #Heights of branches (obstacles)
    obs = [1000, 1300, 1500, 1850, 2000, 2200, 2500, 2900, 3200, 3400, 3700, 3900, 4200]

    #Sets y-level for snow level (End location)
    snow = 5000

    #Dimensions for branches [short horizontal, short vertical, long horizontal, long vertical, xlong horizontal, xlong vertical]
    branch_dim = [385, 159, 560, 159, 659, 159]

    #Sets width and height for window
    WIDTH = 1200
    LENGTH = 960

    #Initializes font and instruction text
    font = pygame.font.Font("freesansbold.ttf", 32)
    text_one = font.render("Avoid the branches and reach the snow at the bottom", True, (255,255,255))
    text_two = font.render("You are the red circle. Use LEFT and RIGHT arrow keys", True, (255,255,255))
    text_three = font.render("Press ENTER to start game", True, (255,255,255))

    #Sets window
    screen = pygame.display.set_mode([WIDTH,LENGTH])
    pygame.display.set_caption("Free Fall")


    #Run until the user asks to quit
    running = True
    #Variable for start message
    start = False
    win = False
    while running:

        #Checks for user pressing "x" button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()

        #Checks for ENTER key to initially start game
        if keys[pygame.K_RETURN]:

            start = True
        #Checks for left arrow key press and moves user circle left 1.25 pixel
        if keys[pygame.K_LEFT] and (circ[0] - (circ[2]+1) != 0):

            circ[0] = circ[0] - 1.25

        #Checks for right arrow key press and moves user circle right 1.25 pixel
        if keys[pygame.K_RIGHT] and (circ[0] + (circ[2]+1) != WIDTH):

            circ[0] = circ[0] + 1.25


        # Fill the background with dark blue colour
        screen.fill((12, 20, 69))

        #Blits all branch sprites onto window (Some are under the window that will be moved up)
        screen.blit(branch_one, (0, obs[0]))
        screen.blit(branch_two, (WIDTH - branch_dim[0], obs[1]))
        screen.blit(branch_five, (0, obs[2]))
        screen.blit(branch_four, (WIDTH - branch_dim[2], obs[3]))
        screen.blit(branch_one, (0, obs[4]))
        screen.blit(branch_three, (0, obs[5]))
        screen.blit(branch_two, (WIDTH - branch_dim[0], obs[6]))
        screen.blit(branch_five, (0,obs[7]))
        screen.blit(branch_four, (WIDTH - branch_dim[2] , obs[8]))
        screen.blit(branch_two, (WIDTH - branch_dim[0], obs[9]))
        screen.blit(branch_one, (0, obs[10]))
        screen.blit(branch_four, (WIDTH - branch_dim[2], obs[11]))
        screen.blit(branch_three, (0, obs[12]))

        #Draws user circle
        pygame.draw.circle(screen,(255,0,0),(circ[0],circ[1]),circ[2])

        #Draws snow rectangle (End Location)
        pygame.draw.rect(screen,(255,255,255),(0,snow,WIDTH,LENGTH))

        #Shows instructions before game starts until ENTER is pressed
        if start == False:
            screen.blit(text_one, (0,200))
            screen.blit(text_two, (0,400))
            screen.blit(text_three, (0,600))
            pygame.display.flip()


        else:
            #Checks if user is in dimension for longest branch on left side
            if circ[0] <= branch_dim[4]:

                #Runs collision funtion to check if user is in that certain branch
                running = branch_collision(1, obs[0], circ, branch_dim, running)
                running = branch_collision(1, obs[4], circ, branch_dim, running)
                running = branch_collision(3, obs[5], circ, branch_dim, running)
                running = branch_collision(1, obs[10], circ, branch_dim, running)
                running = branch_collision(3, obs[12], circ, branch_dim, running)
                running = branch_collision(5, obs[2], circ, branch_dim, running)
                running = branch_collision(5, obs[7], circ, branch_dim, running)


            #Checks if user is in dimension for longest branch on right side
            elif circ[0] >= WIDTH - branch_dim[2]:

                #Runs collision funtion to check if user is in that certain branch
                running = branch_collision(4, obs[3], circ, branch_dim, running)
                running = branch_collision(2, obs[1], circ, branch_dim, running)
                running = branch_collision(2, obs[6], circ, branch_dim, running)
                running = branch_collision(4, obs[8], circ, branch_dim, running)
                running = branch_collision (2, obs[9], circ, branch_dim, running)
                running = branch_collision(4, obs[11], circ, branch_dim, running)

            #Starts moving images after user starts game

            #Moves all branches up continuously
            obs[0] = obs[0] - 2.5
            obs[1] = obs[1] - 2.5
            obs[2] = obs[2] - 2.5
            obs[3] = obs[3] - 2.5
            obs[4] = obs[4] - 2.5
            obs[5] = obs[5] - 2.5
            obs[6] = obs[6] - 2.5
            obs[7] = obs[7] - 2.5
            obs[8] = obs[8] - 2.5
            obs[9] = obs[9] - 2.5
            obs[10] = obs[10] - 2.5
            obs[11] = obs[11] - 2.5
            obs[12] = obs[12] - 2.5

            #Moves user circle down to y=650 so it lands in the snow when snow gets to that level
            if (circ[1] != 650):
                circ[1] = circ[1] + 0.25

            #Moves snow level up until y=650 (When mini game ends)
            if (snow != 650):
                snow = snow - 2.5

            #When snow hits 650, end minigame)
            if (snow == 650):
                running = False
                win = True


        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

    return win

