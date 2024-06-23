import random
from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Character, Item, Enemy, Quest, Skill, ShopItem
from app.ai import generate_story
from app.combat import combat
from app.npc import interact_with_npc

@app.route('/')
def index():
    character = Character.query.first()
    if not character:
        return redirect(url_for('create_character'))

    situations = {
        'les': ['najde skrytou jeskyni', 'narazí na zraněného vlka'],
        'město': ['setká se s tajemným cizincem', 'navštíví místní trh'],
        'hory': ['objeví starou jeskyni', 'bojuje s ledovým drakem'],
        'řeka': ['najde opuštěnou loď', 'bojuje s vodním duchem']
    }

    location = random.choice(list(situations.keys()))
    event = random.choice(situations[location])

    situation = {
        'location': location,
        'event': event,
        'character': character.character_class
    }

    print(f"Generated situation: {situation}")  # Ladicí výstup
    story = generate_story(situation)
    inventory = Item.query.filter_by(owner=character).all()
    quests = Quest.query.filter_by(assignee=character).all()
    skills = Skill.query.filter_by(owner=character).all()
    return render_template('index.html', story=story, inventory=inventory, quests=quests, skills=skills)






@app.route('/create_character', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        name = request.form['name']
        character_class = request.form['class']
        new_character = Character(name=name, character_class=character_class)
        db.session.add(new_character)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_character.html')

@app.route('/interact/<npc>')
def interact(npc):
    character = Character.query.first()
    response = interact_with_npc(character, npc)
    return response


@app.route('/combat')
def start_combat():
    character = Character.query.first()
    if not character:
        return jsonify({'error': 'No character found'}), 400

    player = {
        'name': character.name,
        'hp': 100 + character.level * 10,
        'strength': character.strength
    }
    enemies = Enemy.query.all()
    if not enemies:
        return jsonify({'error': 'No enemies found'}), 400

    enemy = random.choice(enemies)
    enemy_data = {
        'name': enemy.name,
        'hp': enemy.hp,
        'strength': enemy.strength
    }

    try:
        log = combat(player, enemy_data)
        if 'Nepřítel je poražen!' in log:
            character.experience += 50
            if character.experience >= 100:
                character.level += 1
                character.experience = 0
            db.session.commit()
        return jsonify({'log': log})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add_enemies')
def add_enemies():
    enemies = [
        Enemy(name='Ork', hp=50, strength=15),
        Enemy(name='Goblin', hp=30, strength=10),
        Enemy(name='Troll', hp=80, strength=20)
    ]
    db.session.add_all(enemies)
    db.session.commit()
    return 'Enemies added'


@app.route('/character_stats')
def character_stats():
    character = Character.query.first()
    if not character:
        return redirect(url_for('create_character'))

    stats = {
        'name': character.name,
        'class': character.character_class,
        'strength': character.strength,
        'intelligence': character.intelligence,
        'dexterity': character.dexterity,
        'level': character.level,
        'experience': character.experience
    }
    return render_template('character_stats.html', stats=stats)

@app.route('/add_items')
def add_items():
    items = [
        Item(name='Meč', description='Ostrý meč.', item_type='zbraň', owner_id=1),
        Item(name='Štít', description='Odolný štít.', item_type='brnění', owner_id=1),
        Item(name='Lektvar zdraví', description='Léčí zranění.', item_type='lektvar', owner_id=1),
    ]
    db.session.add_all(items)
    db.session.commit()
    return 'Items added'

@app.route('/add_quests')
def add_quests():
    character = Character.query.first()
    if not character:
        return 'No character found'

    quests = [
        Quest(name='Najít magický artefakt', description='Najdi a přines magický artefakt z lesa.', character_id=character.id),
        Quest(name='Porazit draka', description='Poraz draka v Dračí jeskyni.', character_id=character.id),
        Quest(name='Pomoci vesničanovi', description='Pomoz vesničanovi najít jeho ztracenou ovci.', character_id=character.id),
    ]
    db.session.add_all(quests)
    db.session.commit()
    return 'Quests added'


@app.route('/add_skills')
def add_skills():
    character = Character.query.first()
    if not character:
        return 'No character found'

    skills = [
        Skill(name='Ohnivá koule', description='Kouzlo, které způsobí velké poškození ohněm.', skill_type='kouzlo', power=50, owner_id=character.id),
        Skill(name='Uzdravující lektvar', description='Kouzlo, které uzdravuje zranění.', skill_type='kouzlo', power=30, owner_id=character.id),
        Skill(name='Mocný úder', description='Silný fyzický útok.', skill_type='dovednost', power=40, owner_id=character.id),
    ]
    db.session.add_all(skills)
    db.session.commit()
    return 'Skills added'


@app.route('/shop')
def shop():
    shop_items = ShopItem.query.all()
    return render_template('shop.html', shop_items=shop_items)

@app.route('/buy/<int:item_id>')
def buy_item(item_id):
    character = Character.query.first()
    if not character:
        return redirect(url_for('create_character'))

    item = ShopItem.query.get(item_id)
    if not item:
        return 'Item not found'

    # Zde byste mohli přidat kontrolu, zda má hráč dostatek peněz
    # Příklad: if character.gold < item.price: return 'Nedostatek peněz'

    new_item = Item(name=item.name, description=item.description, item_type=item.item_type, owner_id=character.id)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('shop'))

@app.route('/complete_quest/<int:quest_id>')
def complete_quest(quest_id):
    character = Character.query.first()
    if not character:
        return redirect(url_for('create_character'))

    quest = Quest.query.get(quest_id)
    if not quest:
        return 'Quest not found'

    quest.is_completed = True
    # Přidání logiky pro udělení odměny, například zvýšení zlata postavy
    # Příklad: character.gold += int(quest.reward.split()[0])  # Předpoklad, že odměna je ve formátu "50 zlatých mincí"
    db.session.commit()
    return redirect(url_for('index'))
