import random


def combat(player, enemy):
    log = []
    while player['hp'] > 0 and enemy['hp'] > 0:
        player_attack = random.randint(1, player['strength'])
        enemy_attack = random.randint(1, enemy['strength'])

        enemy['hp'] -= player_attack
        log.append(f"{player['name']} útočí a způsobí {player_attack} zranění.")

        if enemy['hp'] <= 0:
            log.append(f"{enemy['name']} je poražen!")
            break

        player['hp'] -= enemy_attack
        log.append(f"{enemy['name']} útočí a způsobí {enemy_attack} zranění.")

        if player['hp'] <= 0:
            log.append(f"{player['name']} je poražen!")

    return log
