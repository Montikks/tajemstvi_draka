def interact_with_npc(character, npc):
    if npc == 'vesnický starosta':
        return f"{npc} vám dává úkol najít ztracený artefakt v temném lese."
    elif npc == 'obchodník':
        return f"{npc} vám nabízí k prodeji vzácné předměty. Chcete něco koupit?"
    else:
        return f"{npc} nemá nic zajímavého na říct."
