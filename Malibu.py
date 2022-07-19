import random
import string
from time import sleep
import keyboard
import mouse
import subprocess
import keyboard
from time import sleep
import webbrowser

from New_Command import ListOfCommands

Welcome = "Welcome to Malibu! Please login."
print(Welcome)
username = input("Username: ")
password = input("Password: ")
account_listing = {
        "admin" : "admin",
         "root" : "root"
}
art1 = (r"""\
          _____                    _____                    _____            _____                    _____                    _____          
         /\    \                  /\    \                  /\    \          /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\        /::\    \                /::\    \                /::\____\        
       /::::|   |               /::::\    \              /:::/    /        \:::\    \              /::::\    \              /:::/    /        
      /:::::|   |              /::::::\    \            /:::/    /          \:::\    \            /::::::\    \            /:::/    /         
     /::::::|   |             /:::/\:::\    \          /:::/    /            \:::\    \          /:::/\:::\    \          /:::/    /          
    /:::/|::|   |            /:::/__\:::\    \        /:::/    /              \:::\    \        /:::/__\:::\    \        /:::/    /           
   /:::/ |::|   |           /::::\   \:::\    \      /:::/    /               /::::\    \      /::::\   \:::\    \      /:::/    /            
  /:::/  |::|___|______    /::::::\   \:::\    \    /:::/    /       ____    /::::::\    \    /::::::\   \:::\    \    /:::/    /      _____  
 /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  /:::/    /       /\   \  /:::/\:::\    \  /:::/\:::\   \:::\ ___\  /:::/____/      /\    \ 
/:::/    |:::::::::\____\/:::/  \:::\   \:::\____\/:::/____/       /::\   \/:::/  \:::\____\/:::/__\:::\   \:::|    ||:::|    /      /::\____\
\::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    /\:::\    \       \:::\  /:::/    \::/    /\:::\   \:::\  /:::|____||:::|____\     /:::/    /
 \/____/      /:::/    /  \/____/ \:::\/:::/    /  \:::\    \       \:::\/:::/    / \/____/  \:::\   \:::\/:::/    /  \:::\    \   /:::/    / 
             /:::/    /            \::::::/    /    \:::\    \       \::::::/    /            \:::\   \::::::/    /    \:::\    \ /:::/    /  
            /:::/    /              \::::/    /      \:::\    \       \::::/____/              \:::\   \::::/    /      \:::\    /:::/    /   
           /:::/    /               /:::/    /        \:::\    \       \:::\    \               \:::\  /:::/    /        \:::\__/:::/    /    
          /:::/    /               /:::/    /          \:::\    \       \:::\    \               \:::\/:::/    /          \::::::::/    /     
         /:::/    /               /:::/    /            \:::\    \       \:::\    \               \::::::/    /            \::::::/    /      
        /:::/    /               /:::/    /              \:::\____\       \:::\____\               \::::/    /              \::::/    /       
        \::/    /                \::/    /                \::/    /        \::/    /                \::/____/                \::/____/        
         \/____/                  \/____/                  \/____/          \/____/                  ~~                       ~~              
                                                                                                                                              

                """)
art2 = (r"""\
        
                       #######
            ######    ########       #####
        ###########/#####\#####  #############
    ############/##########--#####################
  ####         ######################          #####
 ##          ####      ##########/@@              ###
#          ####        ,-.##/`.#\#####               ##
          ###         /  |$/  |,-. ####                 #
         ##           \_,'$\_,'|  \  ###
         #              \_$$$$$`._/   ##
                          $$$$$_/     ##
                          $$$$$        #
                          $$$$$
                          $$$$$
                          $$$$$
                          $$$$$
                         $$$$$
                         $$$$$
                         $$$$$
                         $$$$$        ___
                         $$$$$    _.-'   `-._
                           """)
art = (art1,art2)
listofnames = [ #List for names
    "Liam",
    "Noah",
    "William",
    "James",
    "Logan",
    "Benjamin",
    "Mason",
    "Elijah",
    "Oliver",
    "Jacob",
    "Lucas",
    "Michael",
    "Alexander",
    "Ethan",
    "Daniel",
    "Matthew",
    "Aiden",
    "Henry",
    "Joseph",
    "Jackson",
    "Samuel",
    "Sebastian",
    "David",
    "Carter",
    "Wyatt",
    "Jayden",
    "John",
    "Owen",
    "Dylan",
    "Luke",
    "Gabriel",
    "Anthony",
    "Isaac",
    "Grayson",
    "Jack",
    "Julian",
    "Levi",
    "Christopher",
    "Joshua",
    "Andrew",
    "Lincoln",
    "Mateo",
    "Ryan",
    "Jaxon",
    "Nathan",
    "Aaron",
    "Isaiah",
    "Thomas",
    "Charles",
    "Caleb",
    "Josiah",
    "Christian",
    "Hunter",
    "Eli",
    "Jonathan",
    "Connor",
    "Landon",
    "Adrian",
    "Asher",
    "Cameron",
    "Leo",
    "Theodore",
    "Jeremiah",
    "Hudson",
    "Robert",
    "Easton",
    "Nolan",
    "Nicholas",
    "Ezra",
    "Colton",
    "Angel",
    "Brayden",
    "Jordan",
    "Dominic",
    "Austin",
    "Ian",
    "Adam",
    "Elias",
    "Jaxson",
    "Greyson",
    "Jose",
    "Ezekiel",
    "Carson",
    "Evan",
    "Maverick",
    "Bryson",
    "Jace",
    "Cooper",
    "Xavier",
    "Parker",
    "Roman",
    "Jason",
    "Santiago",
    "Chase",
    "Sawyer",
    "Gavin",
    "Leonardo",
    "Kayden",
    "Ayden",
    "Jameson",
    "Kevin",
    "Bentley",
    "Zachary",
    "Everett",
    "Axel",
    "Tyler",
    "Micah",
    "Vincent",
    "Weston",
    "Miles",
    "Wesley",
    "Nathaniel",
    "Harrison",
    "Brandon",
    "Cole",
    "Declan",
    "Luis",
    "Braxton",
    "Damian",
    "Silas",
    "Tristan",
    "Ryder",
    "Bennett",
    "George",
    "Emmett",
    "Justin",
    "Kai",
    "Max",
    "Diego",
    "Luca",
    "Ryker",
    "Carlos",
    "Maxwell",
    "Kingston",
    "Ivan",
    "Maddox",
    "Juan",
    "Ashton",
    "Jayce",
    "Rowan",
    "Kaiden",
    "Giovanni",
    "Eric",
    "Jesus",
    "Calvin",
    "Abel",
    "King",
    "Camden",
    "Amir",
    "Blake",
    "Alex",
    "Brody",
    "Malachi",
    "Emmanuel",
    "Jonah",
    "Beau",
    "Jude",
    "Antonio",
    "Alan",
    "Elliott",
    "Elliot",
    "Waylon",
    "Xander",
    "Timothy",
    "Victor",
    "Bryce",
    "Finn",
    "Brantley",
    "Edward",
    "Abraham",
    "Patrick",
    "Grant",
    "Karter",
    "Hayden",
    "Richard",
    "Miguel",
    "Joel",
    "Gael",
    "Tucker",
    "Rhett",
    "Avery",
    "Steven",
    "Graham",
    "Kaleb",
    "Jasper",
    "Jesse",
    "Matteo",
    "Dean",
    "Zayden",
    "Preston",
    "August",
    "Oscar",
    "Jeremy",
    "Alejandro",
    "Marcus",
    "Dawson",
    "Lorenzo",
    "Messiah",
    "Zion",
    "Maximus",
    "River",
    "Zane",
    "Mark",
    "Brooks",
    "Nicolas",
    "Paxton",
    "Judah",
    "Emiliano",
    "Kaden",
    "Bryan",
    "Kyle",
    "Myles",
    "Peter",
    "Charlie",
    "Kyrie",
    "Thiago",
    "Brian",
    "Kenneth",
    "Andres",
    "Lukas",
    "Aidan",
    "Jax",
    "Caden",
    "Milo",
    "Paul",
    "Beckett",
    "Brady",
    "Colin",
    "Omar",
    "Bradley",
    "Javier",
    "Knox",
    "Jaden",
    "Barrett",
    "Israel",
    "Matias",
    "Jorge",
    "Zander",
    "Derek",
    "Josue",
    "Cayden",
    "Holden",
    "Griffin",
    "Arthur",
    "Leon",
    "Felix",
    "Remington",
    "Jake",
    "Killian",
    "Clayton",
    "Sean",
    "Adriel",
    "Riley",
    "Archer",
    "Legend",
    "Erick",
    "Enzo",
    "Corbin",
    "Francisco",
    "Dallas",
    "Emilio",
    "Gunner",
    "Simon",
    "Andre",
    "Walter",
    "Damien",
    "Chance",
    "Phoenix",
    "Colt",
    "Tanner",
    "Stephen",
    "Kameron",
    "Tobias",
    "Manuel",
    "Amari",
    "Emerson",
    "Louis",
    "Cody",
    "Finley",
    "Iker",
    "Martin",
    "Rafael",
    "Nash",
    "Beckham",
    "Cash",
    "Karson",
    "Rylan",
    "Reid",
    "Theo",
    "Ace",
    "Eduardo",
    "Spencer",
    "Raymond",
    "Maximiliano",
    "Anderson",
    "Ronan",
    "Lane",
    "Cristian",
    "Titus",
    "Travis",
    "Jett",
    "Ricardo",
    "Bodhi",
    "Gideon",
    "Jaiden",
    "Fernando",
    "Mario",
    "Conor",
    "Keegan",
    "Ali",
    "Cesar",
    "Ellis",
    "Jayceon",
    "Walker",
    "Cohen",
    "Arlo",
    "Hector",
    "Dante",
    "Kyler",
    "Garrett",
    "Donovan",
    "Seth",
    "Jeffrey",
    "Tyson",
    "Jase",
    "Desmond",
    "Caiden",
    "Gage",
    "Atlas",
    "Major",
    "Devin",
    "Edwin",
    "Angelo",
    "Orion",
    "Conner",
    "Julius",
    "Marco",
    "Jensen",
    "Daxton",
    "Peyton",
    "Zayn",
    "Collin",
    "Jaylen",
    "Dakota",
    "Prince",
    "Johnny",
    "Kayson",
    "Cruz",
    "Hendrix",
    "Atticus",
    "Troy",
    "Kane",
    "Edgar",
    "Sergio",
    "Kash",
    "Marshall",
    "Johnathan",
    "Romeo",
    "Shane",
    "Warren",
    "Joaquin",
    "Wade",
    "Leonel",
    "Trevor",
    "Dominick",
    "Muhammad",
    "Erik",
    "Odin",
    "Quinn",
    "Jaxton",
    "Dalton",
    "Nehemiah",
    "Frank",
    "Grady",
    "Gregory",
    "Andy",
    "Solomon",
    "Malik",
    "Rory",
    "Clark",
    "Reed",
    "Harvey",
    "Zayne",
    "Jay",
    "Jared",
    "Noel",
    "Shawn",
    "Fabian",
    "Ibrahim",
    "Adonis",
    "Ismael",
    "Pedro",
    "Leland",
    "Malakai",
    "Malcolm",
    "Alexis",
    "Kason",
    "Porter",
    "Sullivan",
    "Raiden",
    "Allen",
    "Ari",
    "Russell",
    "Princeton",
    "Winston",
    "Kendrick",
    "Roberto",
    "Lennox",
    "Hayes",
    "Finnegan",
    "Nasir",
    "Kade",
    "Nico",
    "Emanuel",
    "Landen",
    "Moises",
    "Ruben",
    "Hugo",
    "Abram",
    "Adan",
    "Khalil",
    "Zaiden",
    "Augustus",
    "Marcos",
    "Philip",
    "Phillip",
    "Cyrus",
    "Esteban",
    "Braylen",
    "Albert",
    "Bruce",
    "Kamden",
    "Lawson",
    "Jamison",
    "Sterling",
    "Damon",
    "Gunnar",
    "Kyson",
    "Luka",
    "Franklin",
    "Ezequiel",
    "Pablo",
    "Derrick",
    "Zachariah",
    "Cade",
    "Jonas",
    "Dexter",
    "Kolton",
    "Remy",
    "Hank",
    "Tate",
    "Trenton",
    "Kian",
    "Drew",
    "Mohamed",
    "Dax",
    "Rocco",
    "Bowen",
    "Mathias",
    "Ronald",
    "Francis",
    "Matthias",
    "Milan",
    "Maximilian",
    "Royce",
    "Skyler",
    "Corey",
    "Kasen",
    "Drake",
    "Gerardo",
    "Jayson",
    "Sage",
    "Braylon",
    "Benson",
    "Moses",
    "Alijah",
    "Rhys",
    "Otto",
    "Oakley",
    "Armando",
    "Jaime",
    "Nixon",
    "Saul",
    "Scott",
    "Brycen",
    "Ariel",
    "Enrique",
    "Donald",
    "Chandler",
    "Asa",
    "Eden",
    "Davis",
    "Keith",
    "Frederick",
    "Rowen",
    "Lawrence",
    "Leonidas",
    "Aden",
    "Julio",
    "Darius",
    "Johan",
    "Deacon",
    "Cason",
    "Danny",
    "Nikolai",
    "Taylor",
    "Alec",
    "Royal",
    "Armani",
    "Kieran",
    "Luciano",
    "Omari",
    "Rodrigo",
    "Arjun",
    "Ahmed",
    "Brendan",
    "Cullen",
    "Raul",
    "Raphael",
    "Ronin",
    "Brock",
    "Pierce",
    "Alonzo",
    "Casey",
    "Dillon",
    "Uriel",
    "Dustin",
    "Gianni",
    "Roland",
    "Landyn",
    "Kobe",
    "Dorian",
    "Emmitt",
    "Ryland",
    "Apollo",
    "Aarav",
    "Roy",
    "Duke",
    "Quentin",
    "Sam",
    "Lewis",
    "Tony",
    "Uriah",
    "Dennis",
    "Moshe",
    "Isaias",
    "Braden",
    "Quinton",
    "Cannon",
    "Ayaan",
    "Mathew",
    "Kellan",
    "Niko",
    "Edison",
    "Izaiah",
    "Jerry",
    "Gustavo",
    "Jamari",
    "Marvin",
    "Mauricio",
    "Ahmad",
    "Mohammad",
    "Justice",
    "Trey",
    "Elian",
    "Mohammed",
    "Sincere",
    "Yusuf",
    "Arturo",
    "Callen",
    "Rayan",
    "Keaton",
    "Wilder",
    "Mekhi",
    "Memphis",
    "Cayson",
    "Conrad",
    "Kaison",
    "Kyree",
    "Soren",
    "Colby",
    "Bryant",
    "Lucian",
    "Alfredo",
    "Cassius",
    "Marcelo",
    "Nikolas",
    "Brennan",
    "Darren",
    "Jasiah",
    "Jimmy",
    "Lionel",
    "Reece",
    "Ty",
    "Chris",
    "Forrest",
    "Korbin",
    "Tatum",
    "Jalen",
    "Santino",
    "Case",
    "Leonard",
    "Alvin",
    "Issac",
    "Bo",
    "Quincy",
    "Mack",
    "Samson",
    "Rex",
    "Alberto",
    "Callum",
    "Curtis",
    "Hezekiah",
    "Finnley",
    "Briggs",
    "Kamari",
    "Zeke",
    "Raylan",
    "Neil",
    "Titan",
    "Julien",
    "Kellen",
    "Devon",
    "Kylan",
    "Roger",
    "Axton",
    "Carl",
    "Douglas",
    "Larry",
    "Crosby",
    "Fletcher",
    "Makai",
    "Nelson",
    "Hamza",
    "Lance",
    "Alden",
    "Gary",
    "Wilson",
    "Alessandro",
    "Ares",
    "Kashton",
    "Bruno",
    "Jakob",
    "Stetson",
    "Zain",
    "Cairo",
    "Nathanael",
    "Byron",
    "Harry",
    "Harley",
    "Mitchell",
    "Maurice",
    "Orlando",
    "Kingsley",
    "Kaysen",
    "Sylas",
    "Trent",
    "Ramon",
    "Boston",
    "Lucca",
    "Noe",
    "Jagger",
    "Reyansh",
    "Vihaan",
    "Randy",
    "Thaddeus",
    "Lennon",
    "Kannon",
    "Kohen",
    "Tristen",
    "Valentino",
    "Maxton",
    "Salvador",
    "Abdiel",
    "Langston",
    "Rohan",
    "Kristopher",
    "Yosef",
    "Rayden",
    "Lee",
    "Callan",
    "Tripp",
    "Deandre",
    "Joe",
    "Morgan",
    "Dariel",
    "Colten",
    "Reese",
    "Jedidiah",
    "Ricky",
    "Bronson",
    "Terry",
    "Eddie",
    "Jefferson",
    "Lachlan",
    "Layne",
    "Clay",
    "Madden",
    "Jamir",
    "Tomas",
    "Kareem",
    "Stanley",
    "Brayan",
    "Amos",
    "Kase",
    "Kristian",
    "Clyde",
    "Ernesto",
    "Tommy",
    "Casen",
    "Ford",
    "Crew",
    "Braydon",
    "Brecken",
    "Hassan",
    "Axl",
    "Boone",
    "Leandro",
    "Samir",
    "Jaziel",
    "Magnus",
    "Abdullah",
    "Yousef",
    "Branson",
    "Jadiel",
    "Jaxen",
    "Layton",
    "Franco",
    "Ben",
    "Grey",
    "Kelvin",
    "Chaim",
    "Demetrius",
    "Blaine",
    "Ridge",
    "Colson",
    "Melvin",
    "Anakin",
    "Aryan",
    "Lochlan",
    "Jon",
    "Canaan",
    "Dash",
    "Zechariah",
    "Alonso",
    "Otis",
    "Zaire",
    "Marcel",
    "Brett",
    "Stefan",
    "Aldo",
    "Jeffery",
    "Baylor",
    "Talon",
    "Dominik",
    "Flynn",
    "Carmelo",
    "Dane",
    "Jamal",
    "Kole",
    "Enoch",
    "Graysen",
    "Kye",
    "Vicente",
    "Fisher",
    "Ray",
    "Fox",
    "Jamie",
    "Rey",
    "Zaid",
    "Allan",
    "Emery",
    "Gannon",
    "Joziah",
    "Rodney",
    "Juelz",
    "Sonny",
    "Terrance",
    "Zyaire",
    "Augustine",
    "Cory",
    "Felipe",
    "Aron",
    "Jacoby",
    "Harlan",
    "Marc",
    "Bobby",
    "Joey",
    "Anson",
    "Huxley",
    "Marlon",
    "Anders",
    "Guillermo",
    "Payton",
    "Castiel",
    "Damari",
    "Shepherd",
    "Azariah",
    "Harold",
    "Harper",
    "Henrik",
    "Houston",
    "Kairo",
    "Willie",
    "Elisha",
    "Ameer",
    "Emory",
    "Skylar",
    "Sutton",
    "Alfonso",
    "Brentley",
    "Toby",
    "Blaze",
    "Eugene",
    "Shiloh",
    "Wayne",
    "Darian",
    "Gordon",
    "London",
    "Bodie",
    "Jordy",
    "Jermaine",
    "Denver",
    "Gerald",
    "Merrick",
    "Musa",
    "Vincenzo",
    "Kody",
    "Yahir",
    "Brodie",
    "Trace",
    "Darwin",
    "Tadeo",
    "Bentlee",
    "Billy",
    "Hugh",
    "Reginald",
    "Vance",
    "Westin",
    "Cain",
    "Arian",
    "Dayton",
    "Javion",
    "Terrence",
    "Brysen",
    "Jaxxon",
    "Thatcher",
    "Landry",
    "Rene",
    "Westley",
    "Miller",
    "Alvaro",
    "Cristiano",
    "Eliseo",
    "Ephraim",
    "Adrien",
    "Jerome",
    "Khalid",
    "Aydin",
    "Mayson",
    "Alfred",
    "Duncan",
    "Junior",
    "Kendall",
    "Zavier",
    "Koda",
    "Maison",
    "Caspian",
    "Maxim",
    "Kace",
    "Zackary",
    "Rudy",
    "Coleman",
    "Keagan",
    "Kolten",
    "Maximo",
    "Dario",
    "Davion",
    "Kalel",
    "Briar",
    "Jairo",
    "Misael",
    "Rogelio",
    "Terrell",
    "Heath",
    "Micheal",
    "Wesson",
    "Aaden",
    "Brixton",
    "Draven",
    "Xzavier",
    "Darrell",
    "Keanu",
    "Ronnie",
    "Konnor",
    "Will",
    "Dangelo",
    "Frankie",
    "Kamryn",
    "Salvatore",
    "Santana",
    "Shaun",
    "Coen",
    "Leighton",
    "Mustafa",
    "Reuben",
    "Ayan",
    "Blaise",
    "Dimitri",
    "Keenan",
    "Van",
    "Achilles",
    "Channing",
    "Ishaan",
    "Wells",
    "Benton",
    "Lamar",
    "Nova",
    "Yahya",
    "Dilan",
    "Gibson",
    "Camdyn",
    "Ulises",
    "Alexzander",
    "Valentin",
    "Shepard",
    "Alistair",
    "Eason",
    "Kaiser",
    "Leroy",
    "Zayd",
    "Camilo",
    "Markus",
    "Foster",
    "Davian",
    "Dwayne",
    "Jabari",
    "Judson",
    "Koa",
    "Yehuda",
    "Lyric",
    "Tristian",
    "Agustin",
    "Bridger",
    "Vivaan",
    "Brayson",
    "Emmet",
    "Marley",
    "Mike",
    "Nickolas",
    "Kenny",
    "Leif",
    "Bjorn",
    "Ignacio",
    "Rocky",
    "Chad",
    "Gatlin",
    "Greysen",
    "Kyng",
    "Randall",
    "Reign",
    "Vaughn",
    "Jessie",
    "Louie",
    "Shmuel",
    "Zahir",
    "Ernest",
    "Javon",
    "Khari",
    "Reagan",
    "Avi",
    "Ira",
    "Ledger",
    "Simeon",
    "Yadiel",
    "Maddux",
    "Seamus",
    "Jad",
    "Jeremias",
    "Kylen",
    "Rashad",
    "Santos",
    "Cedric",
    "Craig",
    "Dominique",
    "Gianluca",
    "Jovanni",
    "Bishop",
    "Brenden",
    "Anton",
    "Camron",
    "Giancarlo",
    "Lyle",
    "Alaric",
    "Decker",
    "Eliezer",
    "Ramiro",
    "Yisroel",
    "Howard",
    "Jaxx"
    ]
welcome1 = f"Welcome to Malibu, {username}!"
welcome2 = "For a list of available commands, type 'help'."
options = [
        1,
        2,
        3,
        4,
        5,
        6
]
execute = ListOfCommands

class Commands:
    def help():
        print("Command 1: Help")
        print("Command 2: Exit")
        print("Command 3: Account generator")
        print("Command 4: Auto clicker")
        print("Command 5: Auto presser")
        print("Command 6: Account finder")
    
    def accountgenerator():
        print("Would you like to create a file?: [y/N]")
        
    def y_command():
        username = random.choice(listofnames) + str(random.randint(1,100000))
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        password = ''.join(random.choice(chars) for i in range(8))
        with open("account.txt","w") as i:
         i.write(f"Your username generated is: {username}")
         i.write(f"Your password generated is: {password}")

    def n_command():
        username = random.choice(listofnames) + str(random.randint(1,100000))
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        password = ''.join(random.choice(chars) for i in range(8))
        print(f"Your username generated is: {username}")
        print(f"Your password generated is: {password}")
    
    def autopresser():
     option = int(input("How many keys do you want pressed: "))
     if option not in options:
        print("Sorry for the inconvience, the auto clicker can only handle up to 5 keys for now.")
        option = int(input("How many keys do you want pressed: "))
     option2 = int(input("How many secounds do you want inbetween?: "))
     option4 = input("Would you like the AutoPresser to 'repeat' until stopped or have a 'limit'?: ")
     if option4.lower() == "repeat":
        print("Still being worked on.")
        option3 = int(input("How many times do you want the button to be pressed?: ")) 
     if option4.lower() == "limit":
        option3 = int(input("How many times do you want the button to be pressed?: ")) 
     firstkey = input("What is your first key: ")
     if option == options.index(2): 
        startkey = input("Please type start to begin: ")
        if startkey.lower() == "exit":
            print("Thank you for using Malibu's Auto Presser!")
        if startkey.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(option3):
                 sleep(option2)
                 keyboard.write(firstkey)
     if option == options.index(3):
        secondkey = input("What is your second key?: ")
        startkey2 = input("Please type start to begin: ")
        if startkey2.lower() == "exit":
            print("Thank you for using Malibu's Auto Presser!")
        if startkey2.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(option3):
                 sleep(option2)
                 keyboard.write(firstkey)
                 sleep(option2)
                 keyboard.write(secondkey)
     if option == options.index(4):
        secondkey = input("What is your second key?: ")
        thirdkey = input("What is your third key?: ")
        startkey2 = input("Please type start to begin: ")
        if startkey2.lower() == "exit":
            print("Thank you for using Malibu's Auto Presser!")
        if startkey2.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(option3):
                 sleep(option2)
                 keyboard.write(firstkey)
                 sleep(option2)
                 keyboard.write(secondkey)
                 sleep(option2)
                 keyboard.write(thirdkey)
     if option == options.index(5):
        secondkey = input("What is your second key?: ")
        thirdkey = input("What is your third key?: ")
        fourthkey = input("What is your fourth key?: ")
        startkey2 = input("Please type start to begin: ")
        if startkey2.lower() == "exit":
            print("Thank you for using Malibu's Auto Presser!")
        if startkey2.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(option3):
                 sleep(option2)
                 keyboard.write(firstkey)
                 sleep(option2)
                 keyboard.write(secondkey)
                 sleep(option2)
                 keyboard.write(thirdkey)
                 sleep(option2)
                 keyboard.write(fourthkey)
     if option == options.index(6):
        secondkey = input("What is your second key?: ")
        thirdkey = input("What is your third key?: ")
        fourthkey = input("What is your fourth key?: ")
        fifthkey = input("What is your fifth key?: ")
        startkey2 = input("Please type start to begin: ")
        if startkey2.lower() == "exit":
            print("Thank you for using Malibu's Auto Presser!")
        if startkey2.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(option3):
                 sleep(option2)
                 keyboard.write(firstkey)
                 sleep(option2)
                 keyboard.write(secondkey)
                 sleep(option2)
                 keyboard.write(thirdkey)
                 sleep(option2)
                 keyboard.write(fourthkey)
                 sleep(option2)
                 keyboard.write(fifthkey)

    def autoclicker():
     left_right = input("Left or right?: ")
     limited = input("Would you like to have a 'limit' or go until 'stopped'?: ")
     if left_right.lower() == "left" and limited.lower() == "stopped":
        whatkey = input("What key would you like to use to stop the Auto Clicker?: ")
        startkey3 = input("Please type start to begin: ")
        if startkey3.lower() == "exit":
            print("Thanks for using Malibu's Auto Clicker!")
        if startkey3.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                while True:
                 mouse.click()
                 if keyboard.is_pressed(whatkey):
                   break
     if left_right.lower() == "right" and limited.lower() == "stopped":
        whatkey = input("What key would you like to use to stop the Auto Clicker?: ")
        startkey3 = input("Please type start to begin: ")
        if startkey3.lower() == "exit":
            print("Thanks for using Malibu's Auto Clicker!")
        if startkey3.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                while True:
                 mouse.right_click()
                 if keyboard.is_pressed(whatkey):
                   break
     if left_right.lower() == "left" and limited.lower() == "limit":
        howmany = int(input("How many times do you want to click?: "))
        startkey3 = input("Please type start to begin: ")
        if startkey3.lower() == "exit":
            print("Thanks for using Malibu's Auto Clicker!")
        if startkey3.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(howmany):
                 mouse.click()
     if left_right.lower() == "right" and limited.lower() == "limit":
        howmany = int(input("How many times do you want to click?: "))
        startkey3 = input("Please type start to begin: ")
        if startkey3.lower() == "exit":
            print("Thanks for using Malibu's Auto Clicker!")
        if startkey3.lower() == "start":
                print("Auto clicker will begin in: 3")
                sleep(1)
                print("Auto clicker will begin in: 2")
                sleep(1)
                print("Auto clicker will begin in: 1")
                sleep(1)
                print("Auto clicker has began.")
                for i in range(howmany):
                 mouse.right_click()

    def private():
        print("Welcome to Malibu's Secret Engine!")
        private_access = input("Before we go any further is the password: ")
        

    def accountfinder():
        userseach = input("What is the username: ")

        class ListOfCommands():
            def findinstagram():
             instagram = f"https://www.instagram.com/{userseach}"
             webbrowser.open(instagram)
             sleep(2)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+c")
             programName = "notepad.exe"
             fileName = "instagram.txt"
             subprocess.Popen([programName, fileName])
             sleep(1)
             keyboard.send("ctrl+a")
             sleep(0.5)
             keyboard.send("ctrl+v")
             sleep(0.5)
             keyboard.send("ctrl+w")
             sleep(0.5)
             keyboard.send("enter")
             sleep(1)
             with open("instagram.txt") as f:
              if "Sorry," in f.read():
                print("Instagram account doesn't exist.")
              else:
                print("Instagram account exists.")

            def findfacebook():
             facebook = f"https://www.facebook.com/{userseach}"
             webbrowser.open(facebook)
             sleep(2)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+c")
             programName = "notepad.exe"
             fileName = "facebook.txt"
             subprocess.Popen([programName, fileName])
             sleep(1)
             keyboard.send("enter")
             sleep(1)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+v")
             sleep(1)
             keyboard.send("ctrl+w")
             sleep(1)
             keyboard.send("enter")
             sleep(1)
             with open("facebook.txt") as l:
              if "This Page" in l.read():
               print("Facebook doesn't account exist.")
              else:
                print("Facebook account exists.")

            def findtwitter():
             twitter = f"https://www.twitter.com/{userseach}"
             webbrowser.open(twitter)
             sleep(2)
             keyboard.send("esc")
             sleep(2)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+c")
             programName = "notepad.exe"
             fileName = "twitter.txt"
             subprocess.Popen([programName, fileName])
             sleep(1)
             keyboard.send("enter")
             sleep(1)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+v")
             sleep(1)
             keyboard.send("ctrl+w")
             sleep(1)
             keyboard.send("enter")
             sleep(1)
            with open("twitter.txt") as o:
             if userseach.lower() in o.read():
               print("Twitter account exist.")
             else:
                print("Twitter doesn't account exists.")

            def findtiktok():
             tiktok = f"https://tiktok.com/@{userseach}"
             webbrowser.open(tiktok)
             sleep(2)
             keyboard.send("esc")
             sleep(2)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+c")
             programName = "notepad.exe"
             fileName = "tiktok.txt"
             subprocess.Popen([programName, fileName])
             sleep(1)
             keyboard.send("enter")
             sleep(1)
             keyboard.send("ctrl+a")
             sleep(1)
             keyboard.send("ctrl+v")
             sleep(1)
             keyboard.send("ctrl+w")
             sleep(1)
             keyboard.send("enter")
             sleep(1)
             with open("tiktok.txt") as q:
              if userseach.lower() in q.read():
               print("Tiktok account exist.")
              else:
                print("Tiktok account exists.")

def Malibu():
    print("Loading....")
    sleep(1.4)
    welcome = print('\n'.join(' '.join(pair) for pair in zip(*(s.split('\n') for s in art))))
    sleep(2)
    print(welcome1)
    sleep(1.5)
    print(welcome2)
    
    while True:
        malibu_ai =  input("Enter a command to begin: ")
        if malibu_ai.lower() == "help":
         Commands.help()
        if malibu_ai.lower() == "exit":
            print("Thank you for using Malibu!")
            break
        if malibu_ai.lower() == "account generator":
            Commands.accountgenerator
        if malibu_ai.lower() == "y":
            Commands.y_command()
        if malibu_ai.lower() == "N":
            Commands.n_command()
        if malibu_ai.lower() == "auto presser":
            Commands.autopresser()
        if malibu_ai.lower() == "auto clicker":
            Commands.autoclicker()
        if malibu_ai.lower() == "account finder":
            Commands.accountfinder()
            execute.findinstagram()
            execute.findfacebook()
            execute.findtiktok()

class Login_System():

    def Login():
        if username and password in account_listing:
            Malibu()
        if username and password not in account_listing:
            print("Sorry, please contact Ducked off#6370 on discord to be create an account.")

Login_System.Login()

