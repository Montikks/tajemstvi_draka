def generate_story(situation):
    location = situation['location']
    event = situation['event']
    character_class = situation['character']

    print(f"Generating story for: location={location}, event={event}, character_class={character_class}")  # Ladicí výstup

    stories = {
        'les': {
            'najde skrytou jeskyni': f'{character_class} zkoumá mystické tajemství les, kde najde skrytou jeskyni.',
            'narazí na zraněného vlka': f'{character_class} prochází lesem a narazí na zraněného vlka. Rozhodne se mu pomoci.'
        },
        'město': {
            'setká se s tajemným cizincem': f'{character_class} se potuluje po městě a setká se s tajemným cizincem, který nabízí neobvyklé úkoly.',
            'navštíví místní trh': f'{character_class} navštíví místní trh a zkoumá různé stánky s exotickým zbožím.'
        },
        'hory': {
            'objeví starou jeskyni': f'{character_class} prochází horami a objeví starou jeskyni plnou pokladů.',
            'bojuje s ledovým drakem': f'{character_class} čelí ledovému drakovi ve vysokých horách.'
        },
        'řeka': {
            'najde opuštěnou loď': f'{character_class} najde opuštěnou loď na břehu řeky a rozhodne se ji prozkoumat.',
            'bojuje s vodním duchem': f'{character_class} bojuje s vodním duchem, který chrání řeku.'
        }
    }

    story = stories.get(location, {}).get(event, 'Příběh se nepodařilo vygenerovat.')
    print(f"Generated story: {story}")  # Ladicí výstup
    return story
