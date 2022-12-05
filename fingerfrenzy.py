import time
import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="fingerfrenzy",
      password="Arvid123",
      database="fingerfrenzy"
    )



ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = ALPHABET[:5] # making it shorter for testing purposes

class Stopwatch():
    def start(self):
        self.start_time = time.time()
    def stop(self):
        return time.time() - self.start_time

class GameOverException(Exception):
    pass

def quit():
    raise SystemExit('Exiting...')

def menu_print(choices):
    print('Hello, would you like to do?')
    for number, (title, func) in enumerate(choices,start=1):
            print(f'({number}) - {title}')

def save_highscore(score, name):
    # Writes new highscores to database
    mycursor = mydb.cursor(score, name)

    sql = "INSERT INTO highscores (score, name) VALUES (%s, %s)"
    val = (score, name)
    print(f'SQL-STATEMENT: {sql}')
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def view_highscores():
    # Fetches and prints all highscores in database
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM highscores order by score")

    myresult = mycursor.fetchall()

    print('*'*20)
    print(f'---- HIGHSCORES ----' )
    print('*'*20)
    for x in myresult:
        print(f'{x[1]} {x[0]}')

def game_start():
    print('Starting game...')

    finished = False
    first_letter = True
    
    while not finished:
        for i in reversed(range(1,3)):
            print(f'Ready in {i} seconds..')
            time.sleep(1)
        input('Press enter to start, then start typing as fast as you can!')

        # Start timer 
        timer = Stopwatch()
        timer.start()
        
        # Taking the actual input from the user as one long string
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
        print('%.5f seconds elapsed' % (time_passed))

        name = input('What is your name?')

        # Insert record into database
        save_highscore(time_passed, name)

def menu():
    choices = [
        ('Start game',game_start),
        ('View highscores', view_highscores),
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

