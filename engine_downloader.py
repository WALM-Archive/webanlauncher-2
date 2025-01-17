import os
import shutil
import wget
import get_game_list as ggs
from threading import Thread
import subprocess
import time
import engine
from importlib import reload
from customtkinter import filedialog
import webanlaucher2_messager as webmes

game_platform = os.name

def system_check():
    return game_platform

def download_runtime():
    try:
        runtime_base = ggs.runtime(platform=game_platform)
        wget.download(f'{runtime_base[0]}')
        shutil.unpack_archive(f'{runtime_base[1]}')
        os.remove(f'{runtime_base[1]}')
        return True
    except:
        return False
        
def asar_check(gamepath):
    if game_platform == 'nt':
        print('Use Microsoft Windows')
    elif game_platform == 'posix':
        print('Use Unix based system')

    game_info = ggs.set_game(game=gamepath, platform=game_platform)

    if os.path.isdir('download_game/'):
        if os.path.isfile(f'download_game/{gamepath}.asar'):
            return True
        else:
            try:
                wget.download(game_info[1], 'download_game/')
                return True
            except:
                return False
    else:
        os.mkdir('download_game/')
        try:
            wget.download(game_info[1], 'download_game/')
            return True
        except:
            return False

def game_start(gamepath):
    game_platform = os.name
    game = ggs.set_game(game=gamepath, platform=game_platform)
    runtime = ggs.runtime(platform=game_platform)

    if game_platform == 'nt':
        try:
            os.remove(f'{runtime[2]}/resources/app.asar')
        except:
            pass
        shutil.copyfile(f'download_game/{gamepath}.asar', f'{runtime[2]}/resources/app.asar')
        with subprocess.Popen([f'{runtime[2]}/runtime.exe']) as game_proc:
            game_proc.communicate()
            return 'ok'
    elif game_platform == 'posix':
        try:
            os.remove(f'{runtime[2]}/resources/app.asar')
        except:
            pass
        shutil.copyfile(f'download_game/{gamepath}.asar', f'{runtime[2]}/resources/app.asar')
        os.system(f'sudo chmod +x  "{runtime[2]}/runtime" ')
        

def start_posix(gamepath):
    runtime = ggs.runtime(platform=game_platform)
    os.system(f'./"{runtime[2]}/runtime"')
    return 'ok'

def game_init(gamepath):

    asar_check(gamepath=gamepath)

def game_verify(gamepath):
    
    if os.path.isfile(f'download_game/{gamepath}.asar'):
        return True
    else:
        return False
        
def delete_game(gamepath):
    game_select = ggs.set_game(game=gamepath, platform=game_platform)
    os.remove(f'download_game/{game_select[0]}')
    return True
        
def get_update_verity(ver):
    if os.path.isfile('update_list.py'):
        os.remove('update_list.py')
    else:
        pass
    try:
        wget.download('https://github.com/evembar/webanlauncher/raw/main/update_list.py')
        import update_list
        version_update = update_list.get_version(ver=ver)
        if version_update == 'no update':
            print('Use stable version launcher')
            return 'stable'
        elif version_update == 'update':
            if os.path.isfile('update.zip'):
                os.remove('update.zip')
            else:
                pass
            wget.download(f'{update_list.update_link}')
            
            return 'reboot'
    except:
        print('error')
        return 'error'
    
def install_update():
    print('\nInstalling update for launcher')
    shutil.unpack_archive('update.zip')
    os.remove('update.zip')
    print('reboot')
    reload(engine)
    import start
    return 'ok'
        
def insoff_update(title_update):
    global update_file_path
    update_file_path = filedialog.askopenfilename(title=title_update, filetypes=[['Update ZIP File', '*.zip']])
    print('checking update file')
    if os.path.isfile(update_file_path):
        print('\nInstalling offline update for launcher')
        return 'get insoff'
    else:
        print('\nBacking update')
        return 'back insoff'
    
def start_insoff():
    shutil.unpack_archive(update_file_path)
    print('reboot')
    reload(engine)
    import start
    return 'ok'

def get_is_backup():

    if os.path.isdir('backup/'):
        print('backup/ : OK')
        if os.path.isdir('backup/src/'):
            print('backup/src: OK')
            if os.path.isfile('backup/engine.py'):
                print('backup/engine.py : OK')
                if os.path.isfile('backup/engine_downloader.py'):
                    print('OK')
                    if os.path.isfile('backup/get_game_list.py'):
                        print('OK')
                        if os.path.isfile('backup/launch.pyw'):
                            print('OK')
                            if os.path.isfile('backup/setting.py'):
                                print('OK')
                                if os.path.isfile('backup/start.py'):
                                    print('OK')
                                    if os.path.isfile('backup/webanlaucher2_messager.py'):
                                        print('OK')
                                        return True
                                    else:
                                        print('NO')
                                        return False
                                else:
                                    print('NO')
                                    return False
                            else:
                                print('NO')
                                return False
                        else:
                            print('NO')
                            return False
                    else:
                        print('NO')
                        return False
                else:
                    print('NO')
                    return False
            else:
                print('NO')
                return False
        else:
            print('NO')
            return False
    else:
        print('NO')
        return False
        
    

def get_backup():
    print('check backup folder')
    if os.path.isdir('backup/'):
        shutil.rmtree('backup/')
        os.mkdir('backup/')
        shutil.copytree('src/', 'backup/src/')
        shutil.copyfile('engine.py', 'backup/engine.py')
        shutil.copyfile('engine_downloader.py', 'backup/engine_downloader.py')
        shutil.copyfile('get_game_list.py', 'backup/get_game_list.py')
        shutil.copyfile('launch.pyw', 'backup/launch.pyw')
        shutil.copyfile('setting.py','backup/setting.py')
        shutil.copyfile('start.py', 'backup/start.py')
        shutil.copyfile('webanlaucher2_messager.py', 'backup/webanlaucher2_messager.py')
    else:
        os.mkdir('backup/')
        shutil.copytree('src/', 'backup/src/')
        shutil.copyfile('engine.py', 'backup/engine.py')
        shutil.copyfile('engine_downloader.py', 'backup/engine_downloader.py')
        shutil.copyfile('get_game_list.py', 'backup/get_game_list.py')
        shutil.copyfile('launch.pyw', 'backup/launch.pyw')
        shutil.copyfile('setting.py','backup/setting.py')
        shutil.copyfile('start.py', 'backup/start.py')
        shutil.copyfile('webanlaucher2_messager.py', 'backup/webanlaucher2_messager.py')

    return 'backup ok'
    
def delete_backup():
    shutil.rmtree('backup/')

def get_recovery_backup(target):
    if target=='src':
        if os.path.isdir('/backup/src/'):
            shutil.copytree('backup/src/', 'src/')
        else:
            webmes.msg_window(title='WebAnLauncher 2', message='Launcher corruption error. Recovery is not to work!', image='src/logo_small.png')
            exit()

def recovery_launcher():
    print('recovering launcher')
    shutil.rmtree('src/')
    shutil.copytree('backup/src/', 'src/')
    os.remove('engine.py')
    shutil.copyfile('backup/engine.py', 'engine.py')
    os.remove('engine_downloader.py')
    shutil.copyfile('backup/engine_downloader.py', 'engine_downloader.py')
    os.remove('get_game_list.py')
    shutil.copyfile('backup/get_game_list.py', 'get_game_list.py')
    os.remove('launch.pyw')
    shutil.copyfile('backup/launch.pyw', 'launch.pyw')
    os.remove('setting.py')
    shutil.copyfile('backup/setting.py','setting.py')
    os.remove('start.py')
    shutil.copyfile('backup/start.py', 'start.py')
    os.remove('webanlaucher2_messager.py')
    shutil.copyfile('backup/webanlaucher2_messager.py', 'webanlaucher2_messager.py')
    critic_reboot()

def install_theme(target):
    if target == 'white':
        if os.path.isfile('theme/white.zip'):
            shutil.unpack_archive('theme/white.zip', 'src/')
        else:
            link = ggs.link_theme(target='white')
            try:
                wget.download(f'{link}', 'theme/')
                shutil.unpack_archive('theme/white.zip', 'src/')
                return 'OK'
            except:
                return 'error'
    elif target == 'black':
        if os.path.isfile('theme/black.zip'):
            shutil.unpack_archive('theme/black.zip', 'src/')
        else:
            link = ggs.link_theme(target='black')
            try:
                wget.download(f'{link}', 'theme/')
                shutil.unpack_archive('theme/black.zip', 'src/')
                return 'OK'
            except:
                return 'error'
    elif target == 'user':
        theme_file_path = filedialog.askopenfilename(title='Install Theme FILE/Установить ФАЙЛ Темы', filetypes=[['Theme ZIP File', '*.zip']])
        if os.path.isfile(theme_file_path):
            print('\nInstalling theme for launcher')
        else:
            print('\nBacking theming')
            return 'error'
        shutil.unpack_archive(f'{theme_file_path}', 'src/')
        return 'OK'

def critic_reboot():
    print('critic reboot')
    reload(engine)
    import start
    return 'ok'