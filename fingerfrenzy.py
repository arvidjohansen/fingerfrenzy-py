import time


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'abc'

class Stopwatch():
    def start(self):
        self.start_time = time.time()
    def stop(self):
        return time.time() - self.start_time



class GameOverException(Exception):
    pass

def quit():
    raise SystemExit('Exiting...')

def game_start():
    
    print('Starting game...')

    finished = False
    first_letter = True
    
    while not finished:
        for letter in ALPHABET:
            
            typed_letter = input(f'Please type the letter ({letter}): ')
            
            if first_letter:
                # Start timer on first character
                timer = Stopwatch()
                timer.start()
                first_letter = False
            
            if typed_letter == letter:
                # correct letter was typed, continue to next
                continue
            else:
                raise GameOverException('Sorry, that was the wrong letter!')
        
        finished = True
        time_passed = timer.stop()
        
        print(f'Well done! You finished in {time_passed} seconds!')
        
         
        
        
                



def menu_print(choices):
    print('Hello, would you like to do?')
    for number, (title, func) in enumerate(choices,start=1):
            print(f'({number}) - {title}')

def menu():
    choices = [
        ('Start game',game_start),
        ('Exit',quit),]
    
    menu_choice = None

    while not menu_choice:

        menu_print(choices)
        
        try: 
            menu_choice = int(input(f'Please select an option: '))
            choices[menu_choice-1][1]() #run function
        except ValueError:
            # user typed something other than a number
            print('Please choose a valid menu item!')
            continue
        except IndexError:
            # user typed a number outside valid choices
            print('Menu item did not exist!')
            continue
        except GameOverException:
            print('Sorry, that was the wrong letter!')
            quit()
                
    
    quit()

menu()

