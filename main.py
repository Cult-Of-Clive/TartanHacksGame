import time
from Constants import *
from Enemy import Enemy
from Powerup import Powerup
from WeirdMath import *
from Ship import Ship
import pygame


# Renders the victory screen after a player wins
def render_victory_screen(victory_screen, victory_font, player, color):
    victory_screen.fill(backgroundColor)
    victory_text = victory_font.render(f'Player {player} has won!', False, color)
    victory_screen.blit(victory_text, ((screenSize[0] / 4), (screenSize[1] / 4)))
    pygame.display.flip()


# The main function
if __name__ == '__main__':
    # Set up pygame
    pygame.init()
    font = pygame.font.SysFont(fontType, fontScale)

    # Set up music
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1)
    collision_sound = pygame.mixer.Sound(impact_file)
    collision_sound.set_volume(0.3)
    force_field_impact = pygame.mixer.Sound(force_field_file)
    enemy_death = pygame.mixer.Sound(enemy_death_file)

    # Set up the drawing window
    screen = pygame.display.set_mode(screenSize)

    # Set up Players
    # Note: Ship 1 = green ship, Ship 2 = red ship by default
    ship1 = Ship(player1StartX, player1StartY, player1Color, shipSpeed, startingBullets, True)
    player1Lives = startingLives
    ship2 = Ship(player2StartX, player2StartY, player2Color, shipSpeed, startingBullets, False)
    player2Lives = startingLives

    # Create powerups and enemies
    powerups = []
    enemies = []

    # Start game timers
    powerup_timer_start = time.time()
    enemy_timer_start = time.time()
    clock = pygame.time.Clock()

    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(2000)

        # If it's time to create a new powerup
        if time.time() - powerup_timer_start > powerupCreationTimeSeconds:
            if len(powerups) < maxPowerups:
                powerups.append(Powerup())
            powerup_timer_start = time.time()

        # If it's time to create a new enemy
        if time.time() - enemy_timer_start > enemyCreationTime:
            if len(enemies) < maxEnemies:
                enemies.append(Enemy())
            enemy_timer_start = time.time()

        # Gets currently pressed keys
        pressed_keys = pygame.key.get_pressed()

        # Handles ship movement controls
        if pressed_keys[upKey1]:
            ship1.move_up()
        if pressed_keys[downKey1]:
            ship1.move_down()
        if pressed_keys[rightKey1]:
            ship1.move_right()
        if pressed_keys[leftKey1]:
            ship1.move_left()
        if pressed_keys[upKey2]:
            ship2.move_up()
        if pressed_keys[downKey2]:
            ship2.move_down()
        if pressed_keys[rightKey2]:
            ship2.move_right()
        if pressed_keys[leftKey2]:
            ship2.move_left()

        # Handles "one off" key presses, where holding
        # down a key should only make its effect happen once
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == shootKey1:
                    ship1.shoot_bullet()
                elif event.key == shootKey2:
                    ship2.shoot_bullet()

        # Fill the background with white
        screen.fill(backgroundColor)

        # Handles bullet collision for bullets shot by ship 1
        for bullet in ship1.bullets:
            # If the bullet hit ship 2
            if point_in_triangle((bullet.x, bullet.y), ship2.ship_coordinates()):
                ship1.bullets.remove(bullet)

                # Handle force field case
                if ship2.force_field:
                    ship2.force_field_uses -= 1
                    force_field_impact.play()
                else:
                    player2Lives -= 1
                    collision_sound.play()

            # Check if ship 1's bullet hit a powerup
            for ship in powerups:
                if distance((bullet.x, bullet.y), (ship.x, ship.y)) < powerupRadius:
                    ship1.bullets.remove(bullet)
                    ship.take_green_damage(powerupDamage)

            # Check if ship 1's bullet hit an enemy
            for enemy in enemies:
                if distance((bullet.x, bullet.y), (enemy.x, enemy.y)) < enemyRadius:
                    ship1.bullets.remove(bullet)
                    enemy.take_damage()
                    collision_sound.play()

        # Handles bullet collision for bullets shot by ship 2
        for bullet in ship2.bullets:
            # If the bullet hit ship 1
            if point_in_triangle((bullet.x, bullet.y), ship1.ship_coordinates()):
                ship2.bullets.remove(bullet)

                # Handle force field case
                if ship1.force_field:
                    ship1.force_field_uses -= 1
                    force_field_impact.play()
                else:
                    player1Lives -= 1
                    collision_sound.play()

            # Check if ship 2's bullet hit a powerup
            for ship in powerups:
                if distance((bullet.x, bullet.y), (ship.x, ship.y)) < powerupRadius:
                    ship2.bullets.remove(bullet)
                    ship.take_red_damage(powerupDamage)

            # Check if ship 2's bullet hit an enemy
            for enemy in enemies:
                if distance((bullet.x, bullet.y), (enemy.x, enemy.y)) < enemyRadius:
                    ship2.bullets.remove(bullet)
                    enemy.take_damage()
                    collision_sound.play()

        # Check if the enemy's bullets hit one of the ships
        for enemy in enemies:
            for bullet in enemy.bullets:
                # If one hit ship 1
                if point_in_triangle((bullet.x, bullet.y), ship1.ship_coordinates()):
                    enemy.bullets.remove(bullet)

                    # Handle force field case
                    if ship1.force_field:
                        ship1.force_field_uses -= 1
                        force_field_impact.play()
                    else:
                        player1Lives -= 1
                        collision_sound.play()

                # If one hit ship 2
                if point_in_triangle((bullet.x, bullet.y), ship2.ship_coordinates()):
                    enemy.bullets.remove(bullet)

                    # Handle force field case
                    if ship2.force_field:
                        ship2.force_field_uses -= 1
                        force_field_impact.play()
                    else:
                        player2Lives -= 1
                        collision_sound.play()

        # Handles powerups
        for powerup in powerups:
            powerup.move()
            powerup.draw(screen)

            # Awards shield to destroying ship if broken
            if powerup.color[0] == 255:
                ship2.activate_force_field()
                powerups.remove(powerup)
            elif powerup.color[1] == 255:
                ship1.activate_force_field()
                powerups.remove(powerup)

        # Draw a players
        ship1.draw(screen)
        ship2.draw(screen)

        # Draw the enemies and have them shoot bullets
        # Also handle enemy death
        for enemy in enemies:
            if enemy.alive:
                enemy.draw(screen)
                enemy.shoot_bullet()
            else:
                enemies.remove(enemy)
                enemy_death.play()

        # Create lives counter
        player1LivesText = font.render(f'Player 1: {player1Lives}', False, textColor)
        player2LivesText = font.render(f'Player 2: {player2Lives}', False, textColor)
        screen.blit(player1LivesText, (screenSize[1] - 170, 0))
        screen.blit(player2LivesText, (screenSize[1] - 170, screenSize[1] - 50))

        # Case where someone won the game
        if player1Lives == 0 or player2Lives == 0:
            if player1Lives == 0:
                winner = 2
                winner_color = player2Color
            else:
                winner = 1
                winner_color = player1Color

            pygame.mixer.music.stop()
            pygame.mixer.Sound(ending_explosion_file).play()

            # Start victory screen
            while running:
                render_victory_screen(screen, font, winner, winner_color)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
pygame.quit()
