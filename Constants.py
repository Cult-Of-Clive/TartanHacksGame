# Constants
import pygame

# Graphics Constants
backgroundColor = (0, 0, 0)
textColor = (255, 255, 255)
screenSize = [500, 500]

# Game Constants
startingLives = 10
fontType = 'Comic Sans MS'
fontScale = 30

# Ship Constants
shipSpeed = 0.1
shipWidth = 20
shipHeight = 28
force_field_color = (173, 216, 230)
force_field_damaged_color = (181, 111, 5)
force_field_thickness = 3

# Bullet Constants
bulletSpeed = 0.1
startingBullets = 5
bulletWidth = 4

# Powerup Radius
powerupColor = (255, 255, 0)
powerupRadius = 15
powerupThickness = 3
powerupDamage = 70
powerupSpeed = 0.07
powerupCreationTimeSeconds = 10
maxPowerups = 2

# Enemy Constants
enemySpeed = 0.1
enemyRotationSpeed = 0.1
enemyRotationSpeedIncrement = 0.05
enemyRadius = 20
enemyColor = (255, 0, 255)
enemyThickness = 3
enemyBulletSpeed = 0.1
enemyBullets = 20
enemyBulletIncrement = 5
enemyHealth = 5
enemyDamageTaken = 1
enemyCreationTime = 20
maxEnemies = 2

# Sound Constants
laser_sound_file = "sounds/laser.mp3"
background_music_file = "sounds/space.mp3"
impact_file = "sounds/impact.mp3"
force_field_file = "sounds/force_field.mp3"
enemy_death_file = "sounds/enemy_destroyed.mp3"
ending_explosion_file = "sounds/ending.mp3"

# Player 1
player1Color = (0, 255, 0)
player1StartX = screenSize[0] / 2
player1StartY = screenSize[1] / 4
leftKey1 = pygame.K_j
rightKey1 = pygame.K_l
upKey1 = pygame.K_i
downKey1 = pygame.K_k
shootKey1 = pygame.K_BACKSPACE

# Player 2
player2Color = (255, 0, 0)
player2StartX = screenSize[0] / 2
player2StartY = screenSize[1] * 3 / 4
leftKey2 = pygame.K_a
rightKey2 = pygame.K_d
upKey2 = pygame.K_w
downKey2 = pygame.K_s
shootKey2 = pygame.K_SPACE
