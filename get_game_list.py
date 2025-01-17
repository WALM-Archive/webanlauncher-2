def set_game(game, platform):
    
    
    if game == 'nightsoul':

        print('Use Night soul')

        if platform == 'nt':
            
            game_link = 'https://github.com/evembar/webanlauncher/releases/download/gameruntime/nightsoul.asar'       

            game_name = 'nightsoul.asar'

        elif platform == 'posix':

            game_link = 'https://github.com/evembar/webanlauncher/releases/download/gameruntime/nightsoul.asar'

            game_name = 'nightsoul.asar'

        return [game_name, game_link]
    
    
    if game == 'ortano':
        print('Use ORTANO')

        if platform == 'nt':
            
            game_link = 'https://github.com/evembar/webanlauncher/releases/download/gameruntime/ortano.asar'       

            game_name = 'ortano.asar'

        elif platform == 'posix':

            game_link = 'https://github.com/evembar/webanlauncher/releases/download/gameruntime/ortano.asar'

            game_name = 'ortano.asar'

        return [game_name, game_link]

def runtime(platform):
    if platform == 'nt':
        return ['https://github.com/evembar/webanlauncher/releases/download/gameruntime/webanlimaks_runtime_windows.zip', 'webanlimaks_runtime_windows.zip', 'webanlimaks runtime windows']
    elif platform == 'posix':
        return ['https://github.com/evembar/webanlauncher/releases/download/gameruntime/webanlimaks_runtime_linux.zip', 'webanlimaks_runtime_linux.zip', 'webanlimaks runtime linux']
    
def link_theme(target):
    if target=='white':
        return 'https://github.com/evembar/webanlauncher/raw/main/theme/white.zip'
    elif target=='black':
        return 'https://github.com/evembar/webanlauncher/raw/main/theme/black.zip'