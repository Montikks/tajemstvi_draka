def generate_story(situation):
    location = situation['location']
    event = situation['event']
    character = situation['character']

    if character == 'bojovník':
        story = f"{character} se nachází v {location} a právě {event}. "
        story += f"{character} se rozhodne prozkoumat dále."
    elif character == 'mág':
        story = f"{character} zkoumá mystické tajemství {location}, kde {event} se stalo. "
        story += f"{character} se rozhodne použít své kouzelné schopnosti k vyřešení problému."
    elif character == 'zloděj':
        story = f"{character} se skrývá v stínech {location}, kde se nedávno odehrál {event}. "
        story += f"{character} se rozhodne použít své lsti a zkušenosti k dalšímu průzkumu."
    else:
        story = f"{character} se nachází v {location}, kde {event} se stalo. "
        story += "Rozhodně se, co dělat dál."

    return story
