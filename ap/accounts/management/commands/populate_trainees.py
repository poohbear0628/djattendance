from django.core.management.base import BaseCommand
from accounts.models import Trainee
from terms.models import Term
import datetime

def new_trainee(trainees=[], gender='B', current_term=1):
  for trainee in trainees:
    email = '.'.join(trainee.lower().split(' ')) + "@gmail.com"
    firstname, lastname = trainee.split(' ', 1)
    password = 'ap'
    date_of_birth = '1993-11-13'
    u = Trainee(email=email, firstname=firstname, lastname=lastname, gender=gender, type='R', date_of_birth=date_of_birth, current_term=current_term, is_active=True)
    u.set_password(password)
    u.save()

class Command(BaseCommand):
  # to use: python ap/manage.py populate_trainees --settings=ap.settings.dev
  def _create_trainees(self):
    # change the array below to get different trainees
    trainees = ["Adam Sy", "Alex Cantu", "Carlos Marin", "Andres Mendoza", "Brandon Alford", "Carson Maher", "Chris Bi", "Christian Diaz", "Daniel Tai", "David Lee", "Dominic Tey", "Drew Kohnle", "Elijah Chang", "Frank Martinez", "Garrett Macnee", "George Goodwin", "Henry C. Chen", "Isaac Kuo", "Isaac Tsou", "Jacob Roberts", "Jasper Han", "Jasper Kuhn", "Jesse Avila", "Jonathan Robbins", "Josh Carbunck", "Josh Cherng", "Josue Pacheco", "Julius Chang", "Luke Cui", "Marcus Couch", "Mark Fan", "Micah Sy Lato", "Nestor Zepeda", "Nkhosi Gama", "Peter Ho", "Rafael Diaz", "Rick Petkau", "Rui Jiang", "Ryan Li", "Samuel Gutierrez", "Samuel Kwong", "Samuel Swei", "Samuel Yeh", "Stephen Kwan", "Titus Ting", "Will Wang", "William Jeng", "Yi Sun"]
    new_trainee(trainees, 'B', 1)

    trainees = ["Austin Anderson", "Brian Muller", "Sean David", "Carlos Salamanca", "Charles Pan", "Chris Jackson", "Jacob Lin", "Clarence So", "Connor Robinson", "Daniel Jenkins", "Daniel Martin", "David Hanson", "David Ye", "Ebenezer Lee", "Ben Findeisen", "Eric Song", "Joseph Hernandez", "Joe Yu", "Joshua Tjokrosurjo", "Kenny Nguyen", "Mark Allijohn", "Ray Ding", "Ryan Armstrong", "Sven Lee", "Tommy Lockwood"]
    new_trainee(trainees, 'B', 2)

    trainees = ["Abraham Goshay", "Andrew Jen", "Austin Zhang", "Basel Almachraki", "Benjamin Liu", "Bill Yeh", "Christian Yu", "Christopher Valencia", "Daniel Wu", "David Sun", "David Welk", "Dennis Huang", "Dhaval Kashyap", "Ed Galaska", "Edgardo Mendoza", "Enoch Huang", "Eric Pan", "George Ashebo", "Henry Chen", "Jack Hu", "Jack Ji", "Allen Liu", "Jason Yeung", "Jasper Duan", "JayWynn Dueck", "Jeff Yang", "Jeffrey Cheung", "Johnathan Lin", "Johnny Stone", "Johnny Zhao", "Jonathan Karr", "Drew Hawthorn", "Jun Heo", "Justin Washington", "Kevin Sung", "Kevin Yum", "Kyle Yen", "Matthew Lee", "Luke Lu", "Marvin Igwe", "Matt Martin", "Matthew Au", "Nathan Bodrug", "Michael Cofino", "Miles Mistler", "Misael Trejo", "Mauricio Gonzalez", "Nazarite Goh"]
    new_trainee(trainees, 'B', 3)

    trainees = ["Andreas Andreas", "Ben Wang", "Daniel Teng", "David Tai", "Dustin Davis", "Ian Wolf", "Jacob Chen", "Jarrod Frankum", "Jean Jeong", "John Ferrante", "Jonathan Tey", "Joseph Duque", "Joseph Meng", "Joshua Obidah", "Julian Arango", "Kevin Ger", "Leo Medina", "Michael Ng", "Paul Sutton", "Peter Cheng", "Philip Lam", "Rodney Rodriguez", "Samuel Chiu", "Joon Jo", "Terry Hung"]
    new_trainee(trainees, 'B', 4)

    trainees = ["Adilenne Garcia", "Amy Cantu", "Allison Lin", "Amanda Vetter", "Amarachi Ibe", "Amber Petrillo", "Amber Sun", "Amy Yung", "Ana Carolina Corey", "Liliana Marin", "Angela Oliva", "Anna Bachand", "April Park", "Boeun Lee", "Brenda Penner", "Bridget Dou", "Charimar Valentin", "Chili Lee", "Christa Jeschke", "Claire Huang", "Clara Lee", "Connie Chen", "Crystal Cabral", "Crystal Goh", "Dana Martin", "Daniela Cheung", "Deborah Chen", "Elisa Melo", "Elizabeth Chan", "Elizabeth Gonzales", "Eunice Tay", "Flor Manzanares", "Grace Liang", "Hannah Lee", "Hannah Penner", "Isabel Mora", "Janine Xiang", "Jenny Liang", "Jessica Chen", "Joanna Pan", "Joanna Rumbley", "Joanna Tan", "Joy Herman", "Julia Chung", "JZ Hung", "Kaylin Wiseman", "Keila Rios", "Kelli Mann"]
    new_trainee(trainees, 'S', 1)

    trainees = ["Annie Liang", "Anastasia David", "Cindy Mariano", "Jura Lin", "Elim Oh", "Emily Hu", "Gabrielle Pryor", "Johanna Findeisen", "Rachael Hernandez", "Janis Freeman", "Jenn Phu", "Joanna Wiguna", "Lydia Lim", "Megan Ku", "Nuria Dubon", "Priscilla Wang", "Rachel Chavana", "Rebecca Y. Chen", "Sandy Wang", "Shirleen Fang", "Yang Cheng", "Zoe Zhang"]
    new_trainee(trainees, 'S', 2)

    trainees = ["Aaliyah Shen", "Abby Miner", "Abib Cao", "Alice Qin", "Alice Wu", "Amanda Sulistyo", "Amber Jamerson", "Angela Wang", "Ann Huang", "Anna Johnsen", "Anna Olson", "Athena Clark", "Camille Bianan", "Caric Chow", "Carmen Delgado", "Carrie Chambers", "Chelsea Corpuz", "Christie Pagan", "Danielle Jones", "Elaine Hoang", "Elim Feng", "Emily Liu", "Eve Wang", "Gladicel Flores", "Grace Cheng", "Grace Jou", "Hannah Oh", "Indigo Lu", "Jackie Arevalo", "Jacqueline Elizondo", "Jessica Yoon", "Jinhee Han", "Joana Morales", "Tiffany Liu", "Joo Hee Eom", "Hannah Hawthorn", "Joyce Low", "Claire Lee", "Kaitlin Hairston", "Karina Lozada", "Katya Becker", "Kayla Guilliams", "Laura Wilde", "Lisa Matamoros", "Lisa Welk", "Lorena Roca", "Lydia Wong", "Mary Amelia Fichter"]
    new_trainee(trainees, 'S', 3)

    trainees = ["Angel Vattakunnel", "Benedicta Lee", "Conomy Wang", "Ellie Hsu", "Erika Yang", "Esther Tsai", "Grace Sun", "Hannah Smith", "Lisa Lin", "Melody Yang", "Meng Ge", "Peace Lu", "Rachel Woo", "Renewing Xu", "Rossy Ramos", "Sara Petkau", "Sarah Li", "Sarah Olson", "Sarah Yu", "Tam Le", "Nayeon Jo", "Viviana Figueroa", "Ya-Chien Chan", "Yi Yuan"]
    new_trainee(trainees, 'S', 4)

  def handle(self, *args, **options):
    print("* Populating trainees...")
    self._create_trainees()
