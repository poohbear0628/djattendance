from django.core.management.base import BaseCommand
from accounts.models import Trainee
from terms.models import Term

def new_trainee(trainees=[], gender='B', current_term=1):
  for trainee in trainees:
    print trainee
    email = '.'.join(trainee.lower().split(' ')) + "@gmail.com"
    firstname = trainee.split(' ')[0]
    lastname = trainee.split(' ')[1]
    gender = gender
    password = 'ap'
    date_of_birth = '1993-11-13'
    u = Trainee(email=email, firstname=firstname, lastname=lastname, gender=gender, type='R', date_of_birth=date_of_birth, current_term=current_term)
    u.set_password(password)
    u.save()

class Command(BaseCommand):
  # to use: python ap/manage.py populate_trainees --settings=ap.settings.dev
  def _create_trainees(self):
    # change the array below to get different trainees
    trainees = ["Basel Almachraki", "George Ashebo", "Yohanes Ashenafi", "Matthew Au", "Nathan Bodrug", "Peng Chen", "Henry Chen", "Howard Chen", "Jeffrey Cheung", "Michael Cofino", "Sam Cummings", "Samuel Duan", "Jasper Duan", "JayWynn Dueck", "Ed Galaska", "Nazarite Goh", "Mauricio Gonzalez", "Abraham Goshay", "Drew Hawthorn", "Jun Heo", "Charles Hii", "Ryan Holt", "Jack Hu", "Dennis Huang", "Enoch Huang", "Marvin Igwe", "Andrew Jen", "Jack Ji", "Randy Juste", "Jonathan Karr", "Preston Kung", "Gregory Lee", "Matthew Lee", "Ezra Li", "Johnathan Lin", "Robert Liu", "Benjamin Liu", "Luke Lu", "Matt Martin", "Edgardo Mendoza", "Miles Mistler", "Shaun Pan", "Eric Pan", "Richy Platt", "RJ Ponder", "Dhaval Kashyap", "Johnny Stone", "David Sun", "Kevin Sung", "Misael Trejo", "Edberg Uy", "Christopher Valencia", "Preston Wang", "Justin Washington", "David Welk", "Paul Wen", "Ty Wilson", "Daniel Wu", "Bill Yeh", "Kyle Yen", "Jason Yeung", "Christian Yu", "Kevin Yum", "Austin Zhang", "Johnny Zhao"]
    new_trainee(trainees, 'B', 1)

    trainees = ["Andreas Andreas", "Julian Arango", "Jacob Chen", "Peter Cheng", "Samuel Chiu", "Ryan Danek", "Dustin Davis", "John Ferrante", "Jarrod Frankum", "Kevin Ger", "Terry Hung", "Jean Jeong", "Joon Jo", "Philip Lam", "Leo Medina", "Joseph Meng", "Michael Ng", "Joshua Obidah", "Rodney Rodriguez", "Abraham Romero", "Paul Sutton", "David Tai", "Daniel Teng", "Jonathan Tey", "Ben Wang", "Ian Wolf", "Joseph Duque"]
    new_trainee(trainees, 'B', 2)

    trainees = ["Gabe Gagne", "Jerry Alvarez", "Sam Bae", "Samuel Chai", "Jeffrey Chan", "Joshua Chang", "Dinglu Chen", "Cephas Chen", "Eric Chong", "Isaac Choo", "Xavier Christian", "Tony Damian", "Andrew Dina", "John Gim", "Tommy Giordano", "Travis Hall", "Jared Hermelin", "Tim Higashi", "Wei Lung Ho", "Joseph Hur", "Ugo Ibe", "Osric Jen", "David Jung", "Daniel Kim", "John Ku", "Leonard Lan", "Samuel Lee", "David Li", "Andy Li", "Nelson Liu", "Brian Lu", "Hugo Martinez Jr.", "Alfred Meng", "David Miyamoto", "Matthew Nichols", "Juanito Novikov", "Samuel Oh", "Carlos Ospina", "Seth Packwood", "Vince Pau", "Peter Pensuwan", "Travis Rigsby", "Ben Schulz", "Kyle Seay", "Josh Shen", "Chris Shyy", "Andrew Sun", "Samuel Sun", "Ruiyu Wu", "Samuel Yu", "Samuel Yusuf", "Joe Zhou"]
    new_trainee(trainees, 'B', 3)

    trainees = ["Daniel Catindig", "Alvin Cheng", "Jeremiah Fichter", "Sean Gupta", "Anthony Hernandez", "Ira Hyun", "Eliezer Kang", "Josh Lee", "Joshua Ling", "Brady McCleese", "Matthew McGrady", "Dernanto Mirwan", "Pablo Valenzuela", "Jorge Yamashiro", "Peter Zhang", "Yang Zheng", "Joseph Wu"]
    new_trainee(trainees, 'B', 4)

    trainees = ["Rachel Ard", "Jackie Arevalo", "Stephanie Azubuike", "Katya Becker", "Camille Bianan", "Hilary Bodrug", "Selcy Borromeo", "Shea Braddock", "Olivia Broussard", "Susanna Bruso", "Abib Cao", "Stacy Castillo", "Tina Chang", "Rebecca Chao", "Sophie Chen", "Sarah Chen", "Grace Cheng", "Mercy Chi", "Caric Chow", "Stephanie Chukwuma", "Athena Clark", "Ariel Cobb", "Chelsea Corpuz", "Carmen Delgado", "Jacqueline Elizondo", "Joo Hee Eom", "Elim Feng", "Mary Amelia Fichter", "Gladicel Flores", "Priscila Gonzalez", "Kayla Guilliams", "Kaitlin Hairston", "Jinhee Han", "Hannah Hawthorn", "Sophia He", "Elaine Hoang", "Crystal Huang", "Ann Huang", "Alex Huerta", "Amber Jamerson", "Anna Johnsen", "Danielle Jones", "Grace Jou", "Lina Kim", "Kora Kwok", "Esther Lai", "Natalie Lau", "Claire Lee", "Raven Lester", "Ruth Liang", "Emily Liu", "Michelle Liu", "Joyce Low", "Karina Lozada", "Indigo Lu", "Lisa Matamoros", "Abby Miner", "Joana Morales", "Raquel Morales", "Ruth Nan", "Michelle Nevarez", "Hannah Oh", "Anna Olson", "Marishka Oquendo", "Christie Pagan", "Alice Qin", "Lorena Roca", "Mayra Santiago", "Aaliyah Shen", "Vorah Shin", "Mary Strange", "Amanda Sulistyo", "Tiffaney Tatro", "Angela Wang", "Eve Wang", "Stephanie Wang", "Lisa Welk", "Paige Wheaton", "Laura Wilde", "Lydia Wong", "Shannon Wong", "Alice Wu", "Jessica Yoon", "Elizabeth Lee"]
    new_trainee(trainees, 'S', 1)

    trainees = ["Tam Le", "Jenny Bachand", "Ya-Chien Chan", "Viviana Figueroa", "Raquel Friedmann", "Adrienne Hii", "Ellie Hsu", "Nayeon Jo", "Leah Johnson", "Benedicta Lee", "Sarah Li", "Ling Liao", "Lisa Lin", "Peace Lu", "Anna Ly", "Sarah Olson", "Sara Petkau", "Rossy Ramos", "Cassie Robinson", "Hannah Smith", "Grace Sun", "Esther Tsai", "Angel Vattakunnel", "Conomy Wang", "Rachel Woo", "Renewing Xu", "Melody Yang", "Erika Yang", "Sarah Yu", "Yi Yuan"]
    new_trainee(trainees, 'S', 2)

    trainees = ["Nana Alli", "Nancy Alvarez", "Alissa Baldon", "Emily Benson", "Zoe Cao", "Erica Chao", "Wendy Chao", "Amaris Chen", "Rebecca Chen", "Christy Chen", "Elaine Chen", "Nicaela Chen", "Michelle Cheong", "Jessica Cheung", "Cindy Choo", "Allie Choy", "Miriam Cockrell", "Allison Cooley", "Emily Cortez", "Lucy De La Rocha", "Lucille De Soto", "Jessica Diaz", "Lisa Dina", "Chloe Favors", "Sarah Folk", "Jasmin Garcia", "Jordan Gibson", "Becky Gonzalez", "Molly Gossard", "Carla Gutierrez", "Shekinah Hendry", "Agape Hsieh", "Jodie Huang", "Christine Jeong", "Phoebe Johnson", "Melody Kao", "Sara Kwan", "Ellie Lee", "Nebai Leon", "Karen Li", "Tanya Lien", "Joyce Lio", "Liezl Longaquit", "Crystal Mandudi", "Kathryn Molina", "Hannah Morris", "Amy Moulthrop", "Camila Navarrete", "Katie Packwood", "Annie Petkau", "Eve Pham", "Yanting Qian", "Gracie Qiu", "Sabrina Ramos-Morales", "Tia Revolte", "Elisa Rodriguez", "Rachel Seay", "Madeline Shapiro", "Henna Shin", "Hui Jen Sii", "Lia Suarez", "Nikki Sumaydeng", "Alex Tai", "Corena Wang", "Sophie Wang", "Grace Wang", "Jasper Wen", "Fung Wong", "Avril Xiong", "Ariel Yang", "Olivia Yang", "Sara Yeaman", "Cassie Yeh", "Crystal Yim", "Tina Yip", "Esther Zhang", "Christine Zhao", "Elsa Zhou", "Zoe Zhu", "Sherry Lin", "SeEun Kwon"]
    new_trainee(trainees, 'S', 3)

    trainees = ["Christine Raabe", "Lauren Bachand", "Victoria Bejarano", "Lucy Chang", "Joselyne Chia", "Stephanie Franco", "Katie Gupta", "Nicole Ho", "Alexandra Jones", "Michaela Lai", "Felicia Lin", "Bekah Logan", "Prisca Lu", "Cori McGrady", "Lily Min", "Sophia Mo", "Amy Ngui", "Gabriela Olguin", "Rebekah Penner", "Paola Rosell", "Hannah Sayono", "Deborah Smith", "Julie Sobowale", "Esther Son", "Elisha Voysest", "Constance Woo", "Hana Yang", "Dandan Zheng", "Jessica Rauhuff"]
    new_trainee(trainees, 'S', 4)

    print 'done'

  def handle(self, *args, **options):
    self._create_trainees()
