from TikTokApi import TikTokApi
import platform
import os
import random  
import inspect
import sys
import time
from pathlib import Path

api = TikTokApi()
TikTokApi.get_instance(use_selenium=True)

def get_file_dirname() -> Path:
    """Returns the callee (`__file__`) directory name"""
    module_name = inspect.currentframe().f_back.f_globals["__name__"]
    module = sys.modules[module_name]
    assert module
    return Path(module.__file__).parent.absolute()



class App:
    @staticmethod
    def watermark():             
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print('┌─────────────┬───────────────────────────┐\n'
              '│╔╦╗╔╦╗╦ ╦╔═╗ │ TikTok: d3vpy             │\n'
              '│ ║  ║ ║ ║║   │ Discord: d3vpy#3399       │\n'
              '│ ╩  ╩ ╚═╝╚═╝ │ GitHub: d3vpy             │\n'
              '├─────────────┴─────────┬─────────────────┤\n'
              '│TikTok Username checker│ Version 0.0.1b  │\n'
              '├───────────────────────┴─────────────────┤')
        
        if platform.system() == 'Windows':
            print('│ Platform: Windows                       │') 
        elif platform.system() == 'Linux':
            print('│ Platform: Linux                         │') 
        elif platform.system() == 'Darwin':
            print('│ Platform: Darwin                        │') 
        else:
            print('│ Platform: Other                         │') 

        print('└─────────────────────────────────────────┘')
        
    @staticmethod
    def generate(length):
        sample_string = 'abcdefghijklmnopqrstuvwxyz1234567890'
        result = ''.join((random.choice(sample_string)) for x in range(int(length)))  

        return result

    @staticmethod
    def check_username(length):
        username = App.generate(length)
        try:
            user = api.getUserObject(username)
            return f'[-] Username @{username} is not available'
        except:
            return f'[+] Username @{username} is available'

            
        
# 672x796

    @staticmethod
    def run():
        if platform.system() == 'Windows':
            os.system('mode 84,40')
            os.system('title TTUC - 0.0.1b - by philliphqs')

        App.watermark()
        
        length = input('Length: ')

        limit = input('Checking limit (in seconds): ')

        while True:
            print(App.check_username(length))

            try:
                time.sleep(int(limit))
            except:
                pass

if __name__ == '__main__':
    App.run()
