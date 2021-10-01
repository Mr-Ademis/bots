from modules.sqlite.engine.add import generate_mob
from modules.sqlite.engine.select import *
#Выводы данных из баз данных
def print_profile(idvk):
    #вывод профиля
    profile = select('player', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    result = f'Ваш персонаж:\n 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Защита:{profile[0]["defence"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n\n'
    result += f' 🌟Очки параметров:{profile[0]["points"]} '
    return str(result)

def print_mob_profile(idvk):
    #вывод профиля мобв
    profile = select('mob', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    result = f'Характеристика моба:\n 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Защита:{profile[0]["defence"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n\n'
    #result += f' 🌟Очки параметров:{profile[0]["points"]} '
    return str(result)

def back(idvk):
    #путь назад
    status = f'Ничего не предвешало беды...'
    return str(status)

def command_attack(idvk):
    #проверка на ловкость
    battle_dexterity_equal(idvk)

def print_battle_turn_player(idvk):
    #конец хода игрока
    player = select('player', 'attack, defence, health,  dexterity', idvk)
    player_current = select('battlepve','healthplayer, dexterityplayer, manaplayer, intelligenceplayer', idvk)
    status = f'\n\nВы:'
    status += f' 🗡{player[0]["attack"]} 🛡{player[0]["defence"]}\n'
    status += f'❤{player_current[0]["healthplayer"]}/{player[0]["health"]}'
    status += f'⚡{player_current[0]["dexterityplayer"]}/{player[0]["dexterity"]}'
    status += f'🔷{player_current[0]["manaplayer"]}/{player_current[0]["intelligenceplayer"]}\n\n'
    return status

def print_battle_turn_mob(idvk):
    #конец хода моба
    player = select('mob', 'attack, defence, health,  dexterity', idvk)
    player_current = select('battlepve','healthmob, dexteritymob, manamob, intelligencemob', idvk)
    status = f'\n\nМоб: Слизень\n'
    status += f' 🗡{player[0]["attack"]} 🛡{player[0]["defence"]}\n'
    status += f'❤{player_current[0]["healthmob"]}/{player[0]["health"]}'
    status += f'⚡{player_current[0]["dexteritymob"]}/{player[0]["dexterity"]}'
    status += f'🔷{player_current[0]["manamob"]}/{player_current[0]["intelligencemob"]}\n\n'
    return status