import time


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = ALPHABET[:5]

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
            

        print('Please type the following characters in order...')
        for i in reversed(range(1,4)):
            print(f'Starting in {i} seconds..')
            time.sleep(1)
        input('Press enter to start, then start typing as fast as you can!')

        # Start timer 
        timer = Stopwatch()
        timer.start()
        
        typed_letters = input(f'{ALPHABET}: ')
        
        time_passed = timer.stop()
        
        # User is done, now check if it was correct
        for i, letter in enumerate(ALPHABET):
            typed_letter = typed_letters[i]

            if typed_letter == letter:
                # correct letter was typed, continue to next
                continue
            else:
                raise GameOverException(f'Sorry, you typed {typed_letter} instead of {letter}, you lose!')
        
        finished = True
        
        print(f'Well done! All letters were in correct order.')
        print(f'{time_passed} seconds elapsed')

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

