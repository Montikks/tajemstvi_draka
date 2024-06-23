def interact_with_npc(character, npc):
    if npc == 'vesnický starosta':
        return f"{npc} vám dává úkol najít ztracený artefakt v temném lese."
    elif npc == 'obchodník':
        return f"{npc} vám nabízí k prodeji vzácné předměty. Chcete něco koupit?"
    else:
        return f"{npc} nemá nic zajímavého na říct."

def interact_with_npc(character, npc):
    if npc == 'vesnický starosta':
        return f'{character.name} mluví s vesnickým starostou o aktuální situaci ve vesnici.'
    elif npc == 'obchodník':
        return f'{character.name} prohlíží zboží u obchodníka a zvažuje koupi nějakých předmětů.'
    elif npc == 'kouzelník':
        return f'{character.name} se setkává s místním kouzelníkem a učí se nová kouzla.'
    elif npc == 'bojovník':
        return f'{character.name} trénuje bojové techniky s místním bojovníkem.'
    else:
        return 'NPC není k dispozici.'
