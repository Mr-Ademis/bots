import vk_api
import random

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor



def sender(id, text, keyboard=None):
    post = {
        'chat_id': id,
        'message': text,
        'random_id': 0
    }
    if keyboard != None:
        post['keyboard'] = keyboard.get_keyboard()
    else:
        post = post

    vk_session.method('messages.send', post)
#181792081 Руслан
#403546358 Суворов

def turnir(longpoll, dict1 = {}, players=[], kol=0, gr1=" ",dict2 = {}, players1=[], kol1=0, gr2=" "):
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                boi=['бой1\n[id250796331|Плюшевый] ⚔ [id403546358|Андрей]','бой2\n[id250796331|Плюшевый]⚔[id211500453|Женя]','бой3\n[id403546358|Андрей]⚔[id211500453|Женя]']
                



                id = event.chat_id
                uid = event.object.message['from_id']

                msg = event.object.message['text']
                fwd = event.object.message['fwd_messages']
                #мой 403546358
                if fwd!=[]:
                    a=fwd[0]
                    b=a.get('text')
                print (fwd)
                print (msg)
                
                if uid==403546358:
                    if "добавить" in msg:
                        dict1[msg[msg.index('['):msg.index(']')+1]] = 0
                        players.append(msg[msg.index('['):msg.index(']')+1])

                    if msg == "сброс":
                        dict1 = {} #403546358 Андрей
                        players=[] #403546358 Андрей
                        kol=0 #403546358 Андрей
                        gr1=" "#403546358 Андрей
                        sorted_dict1 = {}
                    
                    if "побед" in msg:
                        if msg[msg.index('['):msg.index(']')+1] in dict1:
                            dict1[msg[msg.index('['):msg.index(']')+1]]+=(int(msg[-2:]))*2
                            print (dict1[msg[msg.index('['):msg.index(']')+1]])

                    if "ничьих" in msg:
                        if msg[msg.index('['):msg.index(']')+1] in dict1:
                            dict1[msg[msg.index('['):msg.index(']')+1]]+=(int(msg[-2:]))
                    
                    if "группа" in msg:
                        gr1=msg[msg.index('а')+2:]
         
                    if msg == "создать":
                        print (players)
                        sender (id, '🌟Группа '+gr1+'\n\n⚠Бои создают те, кто указан слева.\n📢После проведения всех своих боев, каждый отписывается куратору - тут ссылка, об общем количестве побед и ничьих\nНапример: если у вас был всего один бой и вы в 3 случаях одержали победу - пишите, что 3 победы. Считается каждый проведенный бой!')
                        while len(players)>1:
                            for item1 in players:
                                for item2 in players:
                                    if(item1 != item2):
                                       sender (id, str(item1)+' ⚔ '+str(item2))
                                players.remove(item1)

                    if msg == "таблица":
                        sender (id, '🌟Группа '+gr1+'\n(👊 - количество баллов)')
                        sorted_dict1 = {}
                        sorted_keys1 = sorted(dict1, key=dict1.get, reverse=True)
                        print(sorted_keys1)
                        for w in sorted_keys1:
                            sorted_dict1[w] = dict1[w]
                        print(sorted_dict1)
                        print(dict1)
                        dict1 = sorted_dict1
                        print(dict1)
                        for i in dict1:
                            sender (id, str(kol+1)+') '+str(sorted_keys1[kol])+' - 👊 '+str(sorted_dict1[sorted_keys1[kol]]))
                            kol+=1
                        kol=0

                if uid==181792081:
                    if "добавить" in msg:
                        dict2[msg[msg.index('['):msg.index(']')+1]] = 0
                        players1.append(msg[msg.index('['):msg.index(']')+1])

                    if msg == "сброс":
                        dict2 = {} #403546358 Андрей
                        players1=[] #403546358 Андрей
                        kol1=0 #403546358 Андрей
                        gr2=" "#403546358 Андрей
                        sorted_dict2 = {}
                    
                    if "побед" in msg:
                        if msg[msg.index('['):msg.index(']')+1] in dict2:
                            dict2[msg[msg.index('['):msg.index(']')+1]]+=(int(msg[-2:]))*2
                            print (dict2[msg[msg.index('['):msg.index(']')+1]])

                    if "ничьих" in msg:
                        if msg[msg.index('['):msg.index(']')+1] in dict2:
                            dict2[msg[msg.index('['):msg.index(']')+1]]+=(int(msg[-2:]))
                    
                    if "группа" in msg:
                        gr2=msg[msg.index('а')+2:]
         
                    if msg == "создать":
                        print (players1)
                        sender (id, '🌟Группа '+gr2+'\n\n⚠Бои создают те, кто указан слева.\n📢После проведения всех своих боев, каждый отписывается куратору - тут ссылка, об общем количестве побед и ничьих\nНапример: если у вас был всего один бой и вы в 3 случаях одержали победу - пишите, что 3 победы. Считается каждый проведенный бой!')
                        while len(players1)>1:
                            for item1 in players1:
                                for item2 in players1:
                                    if(item1 != item2):
                                       sender (id, str(item1)+' ⚔ '+str(item2))
                                players.remove(item1)

                    if msg == "таблица":
                        sender (id, '🌟Группа '+gr2+'\n(👊 - количество баллов)')
                        sorted_dict2 = {}
                        sorted_keys2 = sorted(dict2, key=dict2.get, reverse=True)
                        print(sorted_keys2)
                        for w in sorted_keys2:
                            sorted_dict2[w] = dict2[w]
                        print(sorted_dict2)
                        print(dict2)
                        dict2 = sorted_dict2
                        print(dict2)
                        for i in dict2:
                            sender (id, str(kol1+1)+') '+str(sorted_keys2[kol1])+' - 👊 '+str(sorted_dict2[sorted_keys2[kol1]]))
                            kol1+=1
                        kol1=0


token = "36e48b4947f24eae4db9fef2fc5f6a3687e8fc617b5559d66271e92509fe7ada8fa2815861b20d7c7fe0d"
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 207729954)

while True:
    try:
        longpoll = VkBotLongPoll(vk_session, 207729954)
        vk_session = vk_api.VkApi(token=token)
        turnir (longpoll)
    except Exception as e:
        print(e)