# File of constants
###########################################
import datetime

# themes names

PRISMARINE = 'Prismarine'
LEMON = 'Lemon'
SAUCE = 'Sauce'
HERO = 'Hero'

# Os constants
data = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\data'
path = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship'
Code = '123456789'
path_main = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\Main_v1.0.py'
register_path = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\Register.py'
login_path = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\Login.py'
logo_path = r'C:\Users\scorb\OneDrive\Documents\GitHub\Member_Ship\files\Untitled-1.png'


months = {'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31}

months_over = {'January': 31,
            'February': 29,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31}

Year = datetime.datetime.now().year
Month = datetime.datetime.now().strftime('%B')
current_day = str(datetime.datetime.now().day)
Days = list(range(1,months[f'{datetime.datetime.now().strftime("%B")}']+1))
