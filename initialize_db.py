from app import db, app
from app.models import Character, Quest, Item, ShopItem, Skill  # Přidáno

with app.app_context():
    db.drop_all()
    db.create_all()

    # Přidání vzorových postav, úkolů a obchodních předmětů
    character = Character(name='Montikk', character_class='mág')
    db.session.add(character)
    db.session.commit()

    quests = [
        Quest(name='Najít magický artefakt', description='Najdi a přines magický artefakt z lesa.', reward='50 zlatých mincí', character_id=character.id),
        Quest(name='Porazit draka', description='Poraz draka v Dračí jeskyni.', reward='100 zlatých mincí', character_id=character.id),
        Quest(name='Pomoci vesničanovi', description='Pomoz vesničanovi najít jeho ztracenou ovci.', reward='20 zlatých mincí', character_id=character.id),
    ]
    db.session.add_all(quests)
    db.session.commit()

    shop_items = [
        ShopItem(name='Meč', description='Ostrý meč.', item_type='zbraň', price=100),
        ShopItem(name='Štít', description='Odolný štít.', item_type='brnění', price=150),
        ShopItem(name='Lektvar zdraví', description='Léčí zranění.', item_type='lektvar', price=50)
    ]
    db.session.add_all(shop_items)
    db.session.commit()

    print("Database tables created and sample data added")
