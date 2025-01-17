from customtkinter import *
from pygame import mixer
from PIL.ImageTk import PhotoImage as PhotoImage
from PIL import Image 
import os.path
from random import randint
import webbrowser
import engine_downloader as edg
from importlib import reload
import runtime_meneger as runmen
import time

play_mus = True
fullscreen_mode = False

game_os = edg.game_platform


def start():
    gui()

def gui():
    

    def start_menu_launch():
        logo_label.place_forget()
        studio_label.place_forget()
        menu_launch()

    def musrand_play():
        global play_mus
        musrand = randint(1,9)

        if play_mus == True:
            if musrand == 1:
                mixer.music.load('src/theme 1.ogg')
                mixer.music.play(-1)
            elif musrand == 2:
                mixer.music.load('src/theme 2.ogg')
                mixer.music.play(-1)
            elif musrand == 3:
                mixer.music.load('src/world 2.ogg')
                mixer.music.play(-1)
            elif musrand == 4:
                mixer.music.load('src/project_2.mp3')
                mixer.music.play(-1)
            elif musrand == 5:
                mixer.music.load('src/theme 3.ogg')
                mixer.music.play(-1)
            elif musrand == 6:
                mixer.music.load('src/theme 4.ogg')
                mixer.music.play(-1)
            elif musrand == 7:
                mixer.music.load('src/ALT.mp3')
                mixer.music.play(-1)
            elif musrand == 8:
                mixer.music.load('src/detective.ogg')
                mixer.music.play(-1)
            elif musrand == 9:
                mixer.music.load('src/alternative.ogg')
                mixer.music.play(-1)
        elif play_mus == False:
            mixer.music.stop()

    def menu_launch():
        global get_right_left, xgl, game_number, game_image, about_click, reboot_click, support_click, gamepath, dowde_click, upda_click, dowde_frame, fonter
        global fullscreen_mode, global_color, text_global_color, music_work
        try:
            about_en_image = PhotoImage(file='src/about/about_en.png')
            about_ru_image = PhotoImage(file='src/about/about_ru.png')
            left_image = PhotoImage(file='src/left.png')
            right_image = PhotoImage(file='src/right.png')
            play_ru_image = PhotoImage(file='src/play/play_ru.png')
            play_en_image = PhotoImage(file='src/play/play_en.png')
            lang_en_image = PhotoImage(file='src/lang/lang_en.png')
            lang_ru_image = PhotoImage(file='src/lang/lang_ru.png')
            sound_on_ru = PhotoImage(file='src/sound/on/sound_on_ru.png')
            sound_off_ru = PhotoImage(file='src/sound/off/sound_off_ru.png')
            sound_on_en = PhotoImage(file='src/sound/on/sound_on_en.png')
            sound_off_en = PhotoImage(file='src/sound/off/sound_off_en.png')
            nightsoul = PhotoImage(file='src/game_preview/nightsoul.png')
            ortano = PhotoImage(file='src/game_preview/ortano.png')
            about_game_en = PhotoImage(file='src/about_game/about_game_en.png')
            about_game_ru = PhotoImage(file='src/about_game/about_game_ru.png')
            support_en = PhotoImage(file='src/support/support_en.png')
            support_ru = PhotoImage(file='src/support/support_ru.png')
            stop_en = PhotoImage(file='src/stop/stop_en.png')
            stop_ru = PhotoImage(file='src/stop/stop_ru.png')
            delete_game_image_en = PhotoImage(file='src/delete/delete_en.png')
            delete_game_image_ru = PhotoImage(file='src/delete/delete_ru.png')
            update_en = PhotoImage(file='src/update/update_en.png')
            update_ru = PhotoImage(file='src/update/update_ru.png')
            online_en = PhotoImage(file='src/online/online_en.png')
            online_ru = PhotoImage(file='src/online/online_ru.png')
            offline_en = PhotoImage(file='src/offline/offline_en.png')
            offline_ru = PhotoImage(file='src/offline/offline_ru.png')
            backup_en = PhotoImage(file='src/backup/backup_en.png')
            backup_ru = PhotoImage(file='src/backup/backup_ru.png')
            recovery_en = PhotoImage(file='src/recovery/recovery_en.png')
            recovery_ru = PhotoImage(file='src/recovery/recovery_ru.png')
            delete_backup_en = PhotoImage(file='src/delete_backup/delete_backup_en.png')
            delete_backup_ru = PhotoImage(file='src/delete_backup/delete_backup_ru.png')
            themes_en = PhotoImage(file='src/themes/themes_en.png')
            standart_themes_en = PhotoImage(file='src/standart_themes/standart_themes_en.png')
            user_themes_en = PhotoImage(file='src/user_themes/user_themes_en.png')
            themes_ru = PhotoImage(file='src/themes/themes_ru.png')
            standart_themes_ru = PhotoImage(file='src/standart_themes/standart_themes_ru.png')
            user_themes_ru = PhotoImage(file='src/user_themes/user_themes_ru.png')
            white_theme_en = PhotoImage(file='src/white_theme/white_theme_en.png')
            black_theme_en = PhotoImage(file='src/black_theme/black_theme_en.png')
            white_theme_ru = PhotoImage(file='src/white_theme/white_theme_ru.png')
            black_theme_ru = PhotoImage(file='src/black_theme/black_theme_ru.png')
            close_image = PhotoImage(file='src/close.png')
        except:
            edg.get_recovery_backup(target='src')
            des.destroy()
            mixer.music.unload()
            edg.critic_reboot()
        
        
        game_image=nightsoul
        game_number=1
        get_right_left=1
        about_click=0
        reboot_click=0
        support_click=0
        dowde_click=0
        upda_click=0
        
        xgl=145.0

        def game_right():   
            global get_right_left, xgl, game_image, game_number, gamepath    

            if get_right_left == 1:
                get_right_left = 0
                for i in range(20):
                    des.after(30)
                    xgl +=32.75
                    game_button.place(x=xgl, y=80)
                    des.update()
                
                if game_number == 1:
                    game_number = 2
                    game_image=ortano
                    gamepath = 'ortano'
                elif game_number == 2:
                    game_number = 1
                    game_image = nightsoul
                    gamepath = 'nightsoul'

                if game_number == 1:
                    play_button.place(x=355, y=430)
                elif game_number == 2:
                    play_button.place(x=355, y=430)
                elif game_number == 3:
                    play_button.place_forget()
                elif game_number == 4:
                    play_button.place_forget()

                xgl=-645.0
                game_button.place(x=xgl,y=80)
                game_button.configure(image = game_image)
                des.update()
                des.after(30)
                for i in range(20):
                    des.after(30)
                    xgl+=39.5
                    game_button.place(x=xgl,y=80)
                    des.update()

                delete_showhider = edg.game_verify(gamepath=gamepath)

                if delete_showhider == True:
                    delete_game_button.place(x=355, y=20)
                elif delete_showhider == False:
                    delete_game_button.place_forget()

                get_right_left = 1
            elif get_right_left == 0:
                pass

        def get_verity():
            global gamepath
            delete_showhider = edg.game_verify(gamepath=gamepath)

            if delete_showhider == True:
                delete_game_button.place(x=355, y=20)
            elif delete_showhider == False:
                delete_game_button.place_forget()

        def game_left():   
            global get_right_left, xgl, game_image, game_number,gamepath    
            if get_right_left == 1:
                get_right_left = 0
                for i in range(20):
                    des.after(30)
                    xgl -=39.5
                    game_button.place(x=xgl, y=80)
                    des.update()
                
                if game_number == 1:
                    game_number = 2
                    game_image=ortano
                    gamepath = 'ortano'
                elif game_number == 2:
                    game_number = 1
                    game_image = nightsoul
                    gamepath = 'nightsoul'

                if game_number == 1:
                    play_button.place(x=355, y=430)
                elif game_number == 2:
                    play_button.place(x=355, y=430)

                xgl=800.0
                game_button.place(x=xgl,y=80)
                game_button.configure(image = game_image)
                des.update()
                des.after(30)
                for i in range(20):
                    des.after(30)
                    xgl-=32.75
                    game_button.place(x=xgl,y=80)
                    des.update()

                delete_showhider = edg.game_verify(gamepath=gamepath)

                if delete_showhider == True:
                    delete_game_button.place(x=355, y=20)
                elif delete_showhider == False:
                    delete_game_button.place_forget()

                get_right_left = 1
            elif get_right_left == 0:
                pass

        def langering():    

            global langvar

            global about_image, play_image, lang_image, sound_on, sound_off, sound_im, about_game, text_nightsoul, text_andlc, text_anfull, text_ortano
            global font_game_about, support_image, donas, stop, delete_game_image, download_msg, dowde, update_image, update_text, sudolin
            global online_update_image,offline_update_image,get_update_type_text, choise_update_file_text, backup_image
            global recovery_image, get_backup_recovery_text, delete_backup_image, themes_image, standart_themes_image, user_themes_image
            global white_theme_image, black_theme_image, get_themes_text, get_standart_themes_text

            if langvar == "en":
                about_image = about_en_image
                play_image = play_en_image
                lang_image = lang_en_image
                sound_on = sound_on_en
                sound_off = sound_off_en
                sound_im = sound_on
                about_game = about_game_en
                text_nightsoul='Game name: Night soul\nPublish date: 15 August 2023\nDescription: Night. You wake up in one place, but you are aware of it. You have to understand this phenomenon in many ways as a dream. '
                text_ortano='Game name: ORTANO\nPublish date: 5 Februrary 2024\nDescription:A clicker where you have to click on a mug and earn points by listening to cool music. You can rent a skin at a local mug shop.'
                font_game_about = enfont
                support_image = support_en
                donas='https://evembar.github.io/webanlimaks/support_en.html'
                stop = stop_en
                delete_game_image = delete_game_image_en
                download_msg = '         Downloading package...\n     Please wait!'
                dowde = '         Error Downloading package!'
                update_image = update_en
                update_text = '                  Launcher updated!'
                sudolin = '         Please enter\n    to sudo password'
                get_update_type_text = '     Choise\n    type update'
                online_update_image=online_en
                offline_update_image=offline_en
                choise_update_file_text='Choise update file'
                backup_image = backup_en
                recovery_image = recovery_en
                get_backup_recovery_text = '  Make backup\n  or recovery with backup\n or delete backup'
                delete_backup_image = delete_backup_en
                themes_image = themes_en
                standart_themes_image = standart_themes_en
                user_themes_image = user_themes_en
                white_theme_image = white_theme_en
                black_theme_image = black_theme_en
                get_themes_text = '  Select users\n or standart themes'
                get_standart_themes_text = 'Select standart themes'
            elif langvar == "ru":
                about_image = about_ru_image
                play_image = play_ru_image
                lang_image = lang_ru_image
                sound_on = sound_on_ru
                sound_off = sound_off_ru
                sound_im = sound_on
                about_game = about_game_ru
                text_ortano='Название игры: ORTANO\nДата релиза: 5 февраля 2024\nОписание: Кликер, где вам предстоит нажимать по кружку и зарабатывать очки, слушая классную музыку. Можно арендовать скин в местном лавке кружков'
                text_nightsoul='Название игры: Night soul\nДата релиза: 15 Августа 2023\nОписание: Ночь. Вы просыпайтесь в каком-то месте и осознаёте это. Вам предстоит разобраться об явлении как сон.'
                font_game_about = rufont
                support_image = support_ru
                donas='https://evembar.github.io/webanlimaks/support_ru.html'
                stop = stop_ru
                delete_game_image = delete_game_image_ru
                download_msg = '       Скачивание пакетов...\n   Пожалуйста, подождите!'
                dowde = '         Ошибка скачивания пакетов!'
                update_image = update_ru
                update_text = '                Лаунчер обновлен!'
                sudolin = '         Пожайлуста введите\n    пароль от sudo'
                get_update_type_text = '     Выберите\n  тип обновления'
                online_update_image=online_ru
                offline_update_image=offline_ru
                choise_update_file_text = 'Выберите файл обновления'
                backup_image = backup_ru
                recovery_image = recovery_ru
                get_backup_recovery_text = ' Создание резерва\nили восстановление из резерва\nили удаление резерва'
                delete_backup_image = delete_backup_ru
                themes_image = themes_ru
                standart_themes_image = standart_themes_ru
                user_themes_image = user_themes_ru
                white_theme_image = white_theme_ru
                black_theme_image = black_theme_ru
                get_themes_text = '  Выберите пользовательскую\n или стандартную тему'
                get_standart_themes_text = 'Выберите стандартную тему'

            des.update()
                
        system_os = edg.system_check()
        if system_os == 'nt':
            enfont = ('Segoe UI Light', 21)
            rufont = ('Segoe UI Light', 20)
            fonter = 'Segoe UI Light'
        elif system_os == 'posix':
            enfont = ('Ubuntu Light', 21)
            rufont = ('Ubuntu Light', 20)
            fonter = 'Ubuntu Light'
    
        if os.path.isfile('setting.py'):
            import setting 
            global langvar

            if setting.lang == 'en':
                langvar = 'en'
            elif setting.lang == 'ru':
                langvar = 'ru'
            
            langering()
        else:
            settinger = open('setting.py', 'w+')
            settinger.write('lang = "en"')
            settinger.close()
            import setting
            menu_launch()

        def msg_about():
            global msg_frame, about_click, get_right_left

            if get_right_left == 1:
                if about_click == 0:
                    about_click = 1

                    def hide_msg_info():
                        global msg_frame, about_click
                        msg_frame.place_forget()
                        about_click = 0

                    ok_image = PhotoImage(file='src/ok.png')
                    logo_small = PhotoImage(file='src/logo_small.png')

                    msg_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                    msg_frame.place(x=200, y=150)

                    studio_info_label = CTkLabel(msg_frame, text_color='white',  text='                    WebAnlauncher 2\n                   WALM 2024', font=(f'{fonter}', 21))
                    studio_info_label.place(x = 15, y = 30)

                    logo_small_button = CTkLabel(msg_frame, text_color='white',  image=logo_small, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}')
                    logo_small_button.place(x=155, y=100)

                    version_info_label = CTkLabel(msg_frame, text_color='white',  text='ver 1.2.0 Release', font=(f'{fonter}', 21))
                    version_info_label.place(x = 147, y = 170)
                    
                    ok_button = CTkButton(msg_frame, image=ok_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=hide_msg_info)
                    ok_button.place(x=300, y=150)
                elif about_click == 1:
                    pass
            elif get_right_left == 0:
                pass

        def msg_dowde(text_update=None):
            global dowde_frame, dowde_click

            if dowde_click == 0:
                dowde_click = 1

                def hide_msg_info():
                    global msg_frame, dowde_click, get_right_left
                    dowde_frame.place_forget()
                    dowde_click = 0
                    get_right_left = 1

                ok_image = PhotoImage(file='src/ok.png')
                logo_small = PhotoImage(file='src/logo_small.png')

                dowde_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                dowde_frame.place(x=200, y=150)

                if text_update==None:
                    dowde_text=dowde
                else:
                    dowde_text=text_update

                studio_info_label = CTkLabel(dowde_frame, text_color='white',  text=dowde_text, font=(f'{fonter}', 21))
                studio_info_label.place(x = 15, y = 30)

                logo_small_button = CTkLabel(dowde_frame, text_color='white',  image=logo_small, text='', width=100, height=40, bg_color='black', fg_color='black')
                logo_small_button.place(x=155, y=100)
                
                dowde_ok_button = CTkButton(dowde_frame, image=ok_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=hide_msg_info)
                dowde_ok_button.place(x=300, y=150)
            elif dowde_click == 1:
                pass

        def msg_support():
            global msg_support_frame, support_click, get_right_left
            
            if get_right_left == 1:
                if support_click == 0:
                    support_click = 1

                    def hide_msg_info():
                        global msg_frame, support_click
                        msg_support_frame.place_forget()
                        support_click = 0

                    ok_image = PhotoImage(file='src/ok.png')

                    msg_support_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                    msg_support_frame.place(x=200, y=150)

                    studio_info_label = CTkLabel(msg_support_frame, text_color='white',  text='Donut/Донат:\n\nSite/Сайт:\n\nContact/Связь:', font=(f'{fonter}', 21))
                    studio_info_label.place(x = 20, y = 10)

                    get_donat_button = CTkButton(msg_support_frame, text='Donut/Донат', corner_radius=0,  bg_color='#212121', fg_color='#212121', hover_color='#212121', font=('Arial', 16), command=lambda: webbrowser.open_new_tab(donas))
                    get_donat_button.place(x=200,y=15)

                    get_site_button = CTkButton(msg_support_frame, text='Site/Сайт', corner_radius=0,  bg_color='#212121', fg_color='#212121', hover_color='#212121', font=('Arial', 16), command=lambda: webbrowser.open_new_tab('https://evembar.github.io/webanlimaks'))
                    get_site_button.place(x=200,y=72)

                    get_site_button = CTkButton(msg_support_frame, text='Contact/Связь', corner_radius=0,  bg_color='#212121', fg_color='#212121', hover_color='#212121', font=('Arial', 16), command=lambda: webbrowser.open_new_tab('https://t.me/Original_Maksimys'))
                    get_site_button.place(x=200,y=130)

                    ok_button = CTkButton(msg_support_frame, image=ok_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=hide_msg_info)
                    ok_button.place(x=300, y=150)
                elif support_click == 1:
                    pass
            elif get_right_left == 0:
                pass

        def update_type():
            global get_right_left

            if get_right_left == 1:
                get_right_left = 0

                def online_active_update():
                    msg_type_update_frame.place_forget()
                    get_update(target='online')
                def offline_active_update():
                    msg_type_update_frame.place_forget()
                    get_update(target='offline')
                def close_frame():
                    global get_right_left
                    msg_type_update_frame.place_forget()
                    get_right_left = 1

                msg_type_update_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                msg_type_update_frame.place(x=200, y=150)

                close_msg = CTkButton(msg_type_update_frame, text='', width=40,height=40, image=close_image, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=close_frame)
                close_msg.place(x=350, y=0)

                type_update_info_label = CTkLabel(msg_type_update_frame, text_color='white',  text=get_update_type_text, font=(f'{fonter}', 21))
                type_update_info_label.place(x = 125, y = 50)

                online_update_button = CTkButton(msg_type_update_frame, image=online_update_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=online_active_update)
                online_update_button.place(x=100, y=150)

                offline_update_button = CTkButton(msg_type_update_frame, image=offline_update_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=offline_active_update)
                offline_update_button.place(x=200, y=150)

                
            
            elif get_right_left == 0:
                pass

        def backup_recovery_type():
            global get_right_left

            if get_right_left == 1:
                get_right_left = 0

                is_backup = edg.get_is_backup()


                def recovery_launcher():
                    des.destroy()
                    mixer.music.unload()
                    edg.recovery_launcher()

                def delete_backup_launcher():
                    global get_right_left
                    edg.delete_backup()
                    msg_type_update_frame.place_forget()
                    get_right_left = 1

                def backup_launcher():
                    global get_right_left
                    edg.get_backup()
                    msg_type_update_frame.place_forget()
                    get_right_left = 1

                def close_frame():
                    global get_right_left
                    msg_type_update_frame.place_forget()
                    get_right_left = 1

                msg_type_update_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                msg_type_update_frame.place(x=200, y=150)

                close_msg = CTkButton(msg_type_update_frame, text='', width=40,height=40, image=close_image, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=close_frame)
                close_msg.place(x=350, y=0)

                type_update_info_label = CTkLabel(msg_type_update_frame, text_color='white',  text=get_backup_recovery_text, font=(f'{fonter}', 21))
                type_update_info_label.place(x = 75, y = 50)

                recovery_frame_button = CTkButton(msg_type_update_frame, image=recovery_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=recovery_launcher)
                
                delete_backup_button = CTkButton(msg_type_update_frame, image=delete_backup_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=delete_backup_launcher)

                if is_backup == False:
                    print('not backup')
                    recovery_frame_button.place_forget()
                    delete_backup_button.place_forget()
                else:
                    print('yes backup')
                    recovery_frame_button.place(x=250, y=150)
                    delete_backup_button.place(x=150, y=150)

                backup_frame_button = CTkButton(msg_type_update_frame, image=backup_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=backup_launcher)
                backup_frame_button.place(x=50, y=150)
  
            elif get_right_left == 0:
                pass

        def msg_get_themes():
            global get_right_left

            if get_right_left == 1:
                get_right_left = 0

                def standart_type_themes():
                    type_themes_info_label.configure(text=get_standart_themes_text)
                    standart_themes_button.place_forget()
                    user_themes_button.place_forget()
                    black_theme_button.place(x=250, y=150)
                    white_theme_button.place(x=50, y=150)
                    des.update()

                def type_themes_user():
                    global get_right_left
                    themeedg = edg.install_theme(target='user')
                    if themeedg == 'error':
                        msg_themes_frame.place_forget()
                        get_right_left = 1
                    else:
                        des.destroy()
                        mixer.music.unload()
                        edg.critic_reboot()

                def get_white_theme():
                    global get_right_left
                    themeedg = edg.install_theme(target='white')
                    if themeedg == 'error':
                        msg_themes_frame.place_forget()
                        get_right_left = 1
                        msg_dowde()
                    else:
                        des.destroy()
                        mixer.music.unload()
                        edg.critic_reboot()
                    
                def get_black_theme():
                    global get_right_left
                    themeedg = edg.install_theme(target='black')
                    if themeedg == 'error':
                        msg_themes_frame.place_forget()
                        get_right_left = 1
                        msg_dowde()
                    else:
                        des.destroy()
                        mixer.music.unload()
                        edg.critic_reboot()

                def close_frame():
                    global get_right_left
                    msg_themes_frame.place_forget()
                    get_right_left = 1

                msg_themes_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
                msg_themes_frame.place(x=200, y=150)

                close_msg = CTkButton(msg_themes_frame, text='', width=40,height=40, image=close_image, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=close_frame)
                close_msg.place(x=350, y=0)

                type_themes_info_label = CTkLabel(msg_themes_frame, text_color='white',  text=get_themes_text, font=(f'{fonter}', 21))
                type_themes_info_label.place(x = 75, y = 50)

                standart_themes_button = CTkButton(msg_themes_frame, image=standart_themes_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command = standart_type_themes)
                standart_themes_button.place(x=50, y=150)

                user_themes_button = CTkButton(msg_themes_frame, image=user_themes_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=type_themes_user)
                user_themes_button.place(x=250, y=150)

                white_theme_button = CTkButton(msg_themes_frame, image=white_theme_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=get_white_theme)
                black_theme_button = CTkButton(msg_themes_frame, image=black_theme_image, text='', width=100, height=50, bg_color='#212121', fg_color='#212121', hover_color='#212121', command=get_black_theme)

            elif get_right_left == 0:
                pass

        def get_update(target='update_type'):
            global get_right_left

            if target=='update_type':
                update_type()
                des.update()
            elif target == 'online':
                download_msg_frame()
                des.update()
                update_verity = edg.get_update_verity(ver=1.12)
                if update_verity == 'reboot':
                    des.destroy()
                    mixer.music.unload()
                    edg.get_backup()
                    edg.install_update()
                elif update_verity == 'error':
                    dow_support_frame.place_forget()
                    msg_dowde()
                    des.update()
                if update_verity == 'stable':
                    dow_support_frame.place_forget()
                    msg_dowde(text_update=update_text)
                    des.update()
            elif target == 'offline':
                insoff = edg.insoff_update(title_update=choise_update_file_text)
                if insoff == 'get insoff':
                    des.destroy()
                    mixer.music.unload()
                    edg.get_backup()
                    edg.start_insoff()
                elif insoff == 'back insoff':
                    get_right_left = 1

        def hide_about_game_info():
            global xgl, msg_about_game_frame, get_right_left, about_click, reboot_click, support_click, dowde_click, upda_click
            msg_about_game_frame.place_forget()
            
            for i in range(20):
                des.after(30)
                xgl +=7.25
                game_button.place(x=xgl,y=80)
                des.update()
            about_button.place(x=705, y=30)
            left_button.place(x=-5, y=250)
            right_button.place(x=780, y=250)
            themes_button.place(x=105, y=30)
            if game_number == 1:
                play_button.place(x=355, y=430)
            elif game_number == 2:
                play_button.place(x=355, y=430)
            elif game_number == 3:
                play_button.place_forget()
            elif game_number == 4:
                play_button.place_forget()
            sound_button.place(x=490, y=430)
            about_game_button.place(x=705, y=430)
            support_button.place(x=580, y=30)
            update_launcher_button.place(x=5, y=430)
            backup_button.place(x=5, y=30)
            get_right_left = 1
            about_click = 0
            support_click = 0
            dowde_click = 0
            upda_click = 0
            if reboot_click == 0:
                lang_button.place(x=220, y=430)
            elif reboot_click == 1:
                pass
            get_verity()

        def download_msg_frame(texthead=None):
            global dow_support_frame
            if texthead == None:
                dowhead_msg_download = download_msg
            else:
                dowhead_msg_download = texthead

            dow_support_frame = CTkFrame(des, width=400, height=200, corner_radius=0, bg_color='#212121', fg_color='#212121')
            dow_support_frame.place(x=200, y=150)
            studio_info_label = CTkLabel(dow_support_frame, text_color='white',  text=dowhead_msg_download, font=(f'{fonter}', 21))
            studio_info_label.place(x = 70, y = 50)


        def sound_refacter():
            global sound_im, play_mus, get_right_left, music_work
            if music_work == True:
                if get_right_left == 1:
                    if play_mus == False:
                        play_mus = True
                        sound_im = sound_on
                        sound_button.configure(image = sound_im)
                        des.update()
                        musrand_play()
                    elif play_mus == True:
                        play_mus = False
                        sound_im = sound_off
                        sound_button.configure(image = sound_im)
                        des.update()
                        musrand_play()
                elif get_right_left == 0:
                    pass
            elif music_work == False:
                pass


        def play_game():
            global get_right_left,dow_support_frame, game_number, play_mus, gamepath
            
            if get_right_left == 1:
                get_right_left = 0

                if game_number == 1:
                    runtime_verity = runmen.verify()
                    if runtime_verity == False:
                        download_msg_frame()
                        des.update()
                        runtime_proc = edg.download_runtime()
                        if runtime_proc == False:
                            dow_support_frame.place_forget()
                            msg_dowde()
                        else:
                            pass
                    elif runtime_verity == True:
                        pass

                    game_verity = edg.game_verify(gamepath='nightsoul')
                    if game_verity == False:
                        download_msg_frame()
                        des.update()
                        try:
                            game_pul_verif = edg.game_init(gamepath='nightsoul')
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            play_button.configure(image=stop)
                            get_right_left = 1
                            if play_mus == True:
                                sound_refacter()
                            get_right_left = 0
                            des.update()
                            if game_os == 'posix':
                                download_msg_frame(texthead=sudolin)
                                des.update()
                            game_pul_start = edg.game_start(gamepath='nightsoul')
                            if game_os == 'posix':
                                dow_support_frame.place_forget()
                                edg.start_posix(gamepath = 'nightsoul')
                            get_right_left = 1
                            sound_refacter()
                            play_button.configure(image=play_image)
                            des.update()
                        except:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            msg_dowde()
                        des.update()
                        get_right_left = 1
                    if game_verity == True:
                        try:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            play_button.configure(image=stop)
                            get_right_left = 1
                            if play_mus == True:
                                sound_refacter()
                            get_right_left = 0
                            des.update()
                            if game_os == 'posix':
                                download_msg_frame(texthead=sudolin)
                                des.update()
                            game_pul_start = edg.game_start(gamepath='nightsoul')
                            if game_os == 'posix':
                                dow_support_frame.place_forget()
                                edg.start_posix(gamepath = 'nightsoul')
                            get_right_left = 1
                            sound_refacter()
                            play_button.configure(image=play_image)
                            des.update()
                        except:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            msg_dowde()
                        des.update()
                        get_right_left = 1
                elif game_number == 2:
                    runtime_verity = runmen.verify()
                    if runtime_verity == False:
                        download_msg_frame()
                        des.update()
                        runtime_proc = edg.download_runtime()
                        if runtime_proc == False:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            msg_dowde()
                    elif runtime_verity == True:
                        pass
                    game_verity = edg.game_verify(gamepath='ortano')
                    if game_verity == False:
                        download_msg_frame()
                        des.update()
                        try:
                            game_pul_verif = edg.game_init(gamepath='ortano')
                            des.update()
                            dow_support_frame.place_forget()
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            play_button.configure(image=stop)
                            des.update()
                            get_right_left = 1
                            if play_mus == True:
                                sound_refacter()
                            get_right_left = 0
                            if game_os == 'posix':
                                download_msg_frame(texthead=sudolin)
                                des.update()
                            game_pul_start = edg.game_start(gamepath='ortano')
                            if game_os == 'posix':
                                dow_support_frame.place_forget()
                                des.update()
                                edg.start_posix(gamepath = 'ortano')
                            sound_refacter()
                            play_button.configure(image=play_image)
                            des.update()
                        except:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            msg_dowde()
                        des.update()
                        get_right_left = 1
                    elif game_verity == True:
                        try:
                            try:
                                dow_support_frame.place_forget()
                                des.update()
                            except:
                                pass
                            play_button.configure(image=stop)
                            des.update()
                            get_right_left = 1
                            if play_mus == True:
                                sound_refacter()
                            get_right_left = 0
                            if game_os == 'posix':
                                download_msg_frame(texthead=sudolin)
                                des.update()
                            game_pul_start = edg.game_start(gamepath='ortano')
                            if game_os == 'posix':
                                dow_support_frame.place_forget()
                                des.update()
                                edg.start_posix(gamepath = 'ortano')
                            get_right_left = 1
                            sound_refacter()
                            play_button.configure(image=play_image)
                            des.update()
                        except:
                            try:
                                dow_support_frame.place_forget()
                            except:
                                pass
                            msg_dowde()
                        des.update()
                        get_right_left = 1
                else:
                   get_right_left = 1 
            elif get_right_left == 0:
                pass

        def delete_game():
            global game_number
            if game_number == 1:
                edg.delete_game(gamepath='nightsoul')
                delete_game_button.place_forget()
            if game_number == 2:
                edg.delete_game(gamepath='ortano')
                delete_game_button.place_forget()

        def about_game_info():
            global get_right_left, game_number, xgl, msg_about_game_frame, msg_frame, msg_support_frame, dowde_frame
            
            if get_right_left == 1:

                try:
                    msg_frame.place_forget()
                except:
                    pass
                try:
                    msg_support_frame.place_forget()
                except:
                    pass
                try:
                    dowde_frame.place_forget()
                except:
                    pass

                get_right_left = 0
                right_button.place_forget()
                left_button.place_forget()
                lang_button.place_forget()
                play_button.place_forget()
                sound_button.place_forget()
                about_button.place_forget()
                about_game_button.place_forget()
                support_button.place_forget()
                delete_game_button.place_forget()
                update_launcher_button.place_forget()
                backup_button.place_forget()
                themes_button.place_forget()
                for i in range(20):
                    des.after(30)
                    xgl -=7.25
                    game_button.place(x=xgl,y=80)
                    des.update()
                if game_number == 1:
                    game_text = text_nightsoul
                elif game_number == 2:
                    game_text = text_ortano
                msg_about_game_frame = CTkFrame(des, width=301, height=303, corner_radius=0, bg_color=f'{global_color}', fg_color=f'{global_color}', border_color=f'{text_global_color}', border_width=3)
                msg_about_game_frame.place(x=514, y=84)
                button_about_game_ok = CTkButton(msg_about_game_frame, text_color=f'{text_global_color}', width=80, height=32, corner_radius=0, bg_color=f'{global_color}', fg_color=f'{global_color}', border_color=f'{text_global_color}', hover_color=f'{global_color}', border_width=3, text='OK', font=('Arial', 17), command=hide_about_game_info)
                button_about_game_ok.place(x=219,y=270)
                about_game_label=CTkLabel(msg_about_game_frame, text_color=f'{text_global_color}',  wraplength=290, text=game_text, font=font_game_about)
                about_game_label.place(x=10,y=5)
                
            elif get_right_left == 0:
                pass

        def reconfiger_buttons():
            about_button.configure(image=about_image)
            lang_button.configure(image=lang_image)
            sound_button.configure(image=sound_im)
            about_game_button.configure(image=about_game)
            support_button.configure(image=support_image)
            delete_game_button.configure(image=delete_game_image)
            update_launcher_button.configure(image=update_image)
            play_button.configure(image=play_image)
            backup_button.configure(image=backup_image)
            themes_button.configure(image=themes_image)

            des.update()

    

        def change_lang():
            global langvar, get_right_left
            import setting
            if get_right_left == 1:
                if langvar == "en":
                    os.remove('setting.py')
                    settinger = open('setting.py', 'w+')
                    settinger.write('lang = "ru"')
                    settinger.close()
                    langvar = 'ru'
                    reload(setting)
                elif langvar == "ru":
                    os.remove('setting.py')
                    settinger = open('setting.py', 'w+')
                    settinger.write('lang = "en"')
                    settinger.close()
                    langvar = 'en'
                    reload(setting)
                langering()
                reconfiger_buttons()
            elif get_right_left == 0:
                pass

        

        

        about_button = CTkButton(des, image=about_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=msg_about)
        about_button.place(x=705, y=30)

        left_button = CTkButton(des, image=left_image, text='', width=40, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=game_left)
        left_button.place(x=-5, y=250)

        right_button = CTkButton(des, image=right_image, text='', width=40, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=game_right)
        right_button.place(x=780, y=250)

        play_button = CTkButton(des, image=play_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=play_game)
        play_button.place(x=355, y=430)

        lang_button = CTkButton(des, image=lang_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=change_lang)
        lang_button.place(x=220, y=430)

        sound_button = CTkButton(des, image=sound_im, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=sound_refacter)
        if music_work == True:
            sound_button.place(x=490, y=430)
        elif music_work == False:
            pass

        game_button = CTkButton(des, width=500, height=325, text='', image=game_image, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=play_game)
        game_button.place(x=xgl, y=80)

        about_game_button = CTkButton(des, image=about_game, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=about_game_info)
        about_game_button.place(x=705, y=430)

        support_button = CTkButton(des, image=support_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=msg_support)
        support_button.place(x=580, y=30)

        delete_game_button = CTkButton(des, image=delete_game_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=delete_game)

        update_launcher_button = CTkButton(des, image=update_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=get_update)
        update_launcher_button.place(x=5, y=430)

        backup_button = CTkButton(des, image=backup_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=backup_recovery_type)
        backup_button.place(x=5, y=30)

        themes_button = CTkButton(des, image=themes_image, text='', width=100, height=40, bg_color=f'{global_color}', fg_color=f'{global_color}', hover_color=f'{global_color}', command=msg_get_themes)
        themes_button.place(x=105, y=30)
        
        gamepath = 'nightsoul'

        delete_showhider = edg.game_verify(gamepath=gamepath)

        if delete_showhider == True:
            delete_game_button.place(x=355, y=20)
        elif delete_showhider == False:
            delete_game_button.place_forget()

        if music_work == True:
            musrand_play()
        elif music_work == False:
            pass

    def boot():
        global logo_label, studio_label, global_color, text_global_color, music_work

        try:
            mixer.init()
            music_work = True
        except:
            music_work = False

        if music_work == True:    
            try:
                mixer.music.load('src/startup.ogg')
            except:
                edg.get_recovery_backup(target='src')
                des.destroy()
                mixer.music.unload()
                edg.critic_reboot()
            mixer.music.play()
        elif music_work == False:
            pass

        try:
            logo=PhotoImage(file='src/logo.png')
        except:
            edg.get_recovery_backup(target='src')
            des.destroy()
            mixer.music.unload()
            edg.critic_reboot()
        try:
            color_launcher = open('src/theme.txt', 'r+')
            global_color = color_launcher.read()
            color_launcher.close()
            text_color_launcher = open('src/text_theme.txt', 'r+')
            text_global_color= text_color_launcher.read()
            text_color_launcher.close()
        except:
            global_color = 'black'
            text_global_color = 'white'

        logo_label=CTkLabel(des, image=logo, text='')
        studio_label=CTkLabel(des, text_color=f'{text_global_color}',  text='WebAnLauncher 2', font=(f'{fonter}', 30), bg_color=f'{global_color}')
        yl1=900
        studio_label.place(x=270, y=yl1)
        yl=-300
        logo_label.place(x=200, y=yl)
        des.update()
        for i in range(17):
            des.after(40)
            yl+=20
            logo_label.place(x=295, y=yl)
            des.update()
        des.after(1000)
        yl1 = 400
        studio_label.place(x=305, y=yl1)
        des.update()
        des.after(5000, start_menu_launch)

    system_os = edg.system_check()
    if system_os == 'nt':
        fonter = 'Segoe UI Light'
    elif system_os == 'posix':
        fonter = 'Ubuntu Light'

    des=CTk()
    des.title('WebAnLauncher 2')
    des.geometry('825x500')

    try:
        des.iconbitmap('src/iconbitmap/logo.ico')
    except:
        pass
    des.resizable(width=False, height=False)

    try:
        reload(edg)
    except:
        pass

    des.after(3000, boot)

    try:
        bg = PhotoImage(file='src/bg.png')
    except:
        edg.get_recovery_backup(target='src')
        des.destroy()
        mixer.music.unload()
        edg.critic_reboot()

    bg_label = CTkLabel(des, text='', image=bg)
    bg_label.place(x=0,y=0)

    des.mainloop()
