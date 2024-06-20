from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Character, Item
from app.ai import generate_story
from app.combat import combat
from app.npc import interact_with_npc

@app.route('/')
def index():
    character = Character.query.first()
    if not character:
        return redirect(url_for('create_character'))

    situation = {
        'location': 'les',
        'event': 'najde skrytou jeskyni',
        'character': character.character_class
    }
    story = generate_story(situation)
    inventory = Item.query.filter_by(owner=character).all()
    return render_template('index.html', story=story, inventory=inventory)

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
    player = {
        'name': character.name,
        'hp': 100 + character.level * 10,
        'strength': character.strength
    }
    enemy = {
        'name': 'Ork',
        'hp': 50,
        'strength': 15
    }
    log = combat(player, enemy)
    if 'Nepřítel je poražen!' in log:
        character.experience += 50
        if character.experience >= 100:
            character.level += 1
            character.experience = 0
        db.session.commit()
    return jsonify({'log': log})
