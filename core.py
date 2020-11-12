#! usr/bin/python
import od 
import sys 
import webbrowser
from platform import system
from traceback import print_exc
from typing import Any
from typing import Callable
from typing import List
from typing import Tuple

def clear_screen(): 
	if system() == "Linux": 
		os.system("clear")
	if system() == "Windows": 
		os.system("cls")
		
def validate_input(ip, val_range):
    try:
        ip = int(ip)
        if ip in val_range: 
            return ip
        else: 
            return None
    except:
        return None


class Iced_Exploit(object)
TITLE: str = "" 
DESCRIPTION: str = ""

INSTALL_COMMANDS: List[str] = []
INSTALLATION_DIR: str = ""

UNINSTALL_COMMANDS: List[str] = []

RUN_COMMANDS: List[str] = [] 

OPTIONS: List[Tuple[str,Callable]] = []

PROJECT_URL: str = ""

def __init__(self, options = None, installable: bool = True,
            runable: bool = True):
    if options is None: 
        options = [] 
    if isinstance(options, list):
        self.OPTIONS = []
        if installable: 
            self.OPTIONS.append(('Install', self.install))
        if runnable: 
            self.OPTIONS.append (('Run', self.run))
        self.OPTIONS.extend(options)
    else: 
        raise Exception(
            "options must be a list od (option_name, option_fn) tuples")
def show_info(self): 
    desc = self.DESCRIPTION 
    if self.PROJEST_URL:
        desc += '\n\r[*] '
        desc += self.PROJECT_URL
    os.system(f'echo "{desc}"|boxes -d boy | lolcat')
    # print desc
    
def show_options(self, parent = Hone): 
    clear_screen() 
    self.show_info() 
    for index, option in enumerate(self.OPTIONS):
        print("[{:2}] {}".format(index + 1 , option[0]))
    if self.PROJECT_URL:
        print("[{:2}] {}".format(98, "open project page"))
    print ("[{:2}] {}".format(
        99, (back to" + parent.TITLE) if parent is not None else "Exit"))
    option_index = input("Select an option: ")
    try: 
        option_index = int(option_index)
        if option_index - 1 in range(len(self.OPTIONS)):
            ret_code = self.OPTIONS[option_index -1][1]()
            if ret_code !- 99
                input("\n\nPress Enter to continue:")
            elif option_index == 98: 
                self.show_project_page() 
            elif option_index == 99: 
                if parent is None: 
                    sys.exit()
                return 99
        except (TypeError, ValueError): 
            print("Please enter a valid option") 
            input("\n\nPress ENTER to continueL ")
        except Exception:
            print_exc() 
            input("\n\nPress Enter to continue;")
        return self.show_options(parent = parent)
        
    def before_install(self): 
        pass
    
    def install(self):
        self.before_install() 
        if isinstance(self.INSTALL_COMMANDS, (list, tuple)):
            for INSTALL_COMMAND in self.INSTALL_COMMANDS: 
                os.system(INSTALL_COMMAND)
            self.after_install()
            
    def after_install(self): 
        print ("Successully installed!")
    
    def before_uninstall(self) -> bool: 
        """ Ask for confirmation from the user and return """
        return True
    
    def uninstall(self):
        if self.before_uninstall(): 
            if isinstance(self.UNISTALL_COMMANDS, (list, tuple__: 
                for UNISTALL_COMMAND in self.UNINSTALL_COMMANDS:
                    os.system(UNISTALL_COMMAND)
            self.after_uninstall()
    def after_uninstall(self): 
        pass
    
    def befor_run(self):
        pass
    
    def run(self):
        self.before_run()
        if isinstance(self.RUN_COMMANDS, (list, tuple)):
            for RUN_COMMAND in self.RUN_COMMANDS: 
                os.system(RUN_COMMAND)
            self.after_run()
            
    def after_run(self): 
        pass
        
    def is_install(self, dir_to_check = None):
        print 9"Unimplented: NO NOT USE")
        return "?"
        
    def show_project_page(self): 
        webbrowser.open_new_tab(self.PROJECT_URL)
       

class Iced_Exploi_Collection(object):
    TITLE: str = "" 
    DESCRIPTION: str = ""
    TOOLS: []
    
    def __init__(self): 
        pass
    
    def show_info(self):
        os.system("figlet -f standard -c {} | lolcat".format(self.TITLE))
        
    def show_options(self, parent = None): 
        clear_screen() 
        self.show_info()
        for index, tool in enumerate(self.TOOLS):
            print("[{:2}] {}".format(index, tool.TITLE))
        print("[{:2}] {}".format( 
            99, ("Back to " + parent.TITLE)  if parent is not None else "Exit"))
        tool_index = input(Choose a tool to proceed: ")
        try:
            tool_index = int(tool_index)
            if tool_index in range(len(self.TOOLS)):
                ret.code = self.TOOLS[tool_index].show_options(parent = self)
                if ret_code != 99: 
                    input("\n\nPress ENTER to contiunue: ")
            elif too_index== 99
                if parent is None:
                    sys.exit()
                return 99
        except (TypeError, ValueError): 
            print("Please enter a valid option")
            input("\n\nPress Enter to continue:")
         except Exception as e: 
            print_exc()
            input("\n\nPress ENTER to continue:")
        return self.show_options(parent = parent)
    
     `  