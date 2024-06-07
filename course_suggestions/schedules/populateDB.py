from .models import Schedule
import random

#populate only engineering majors, minors, and concentrations for now
#populate pennkey, gpa, semester, answers
#leave reivew and courses blank for now 

majors = [
    "Artificial Intelligence, BSE",
    "Bioengineering, BSE",
    "Biomedical Science, BAS",
    "Chemical and Biomolecular Engineering, BSE",
    "Computer Engineering, BSE",
    "Computer Science, BAS",
    "Computer Science, BSE",
    "Digital Media Design, BSE",
    "Electrical Engineering, BSE",
    "Individualized Program, BAS",
    "Materials Science and Engineering, BSE",
    "Mechanical Engineering and Applied Mechanics, BSE",
    "Networked and Social Systems Engineering, BSE",
    "Systems Science and Engineering, BSE"
]

minors = [
    "Chemical & Biomolecular Engineering, Minor",
    "Computer Science, Minor",
    "Data Science, Minor",
    "Digital Media Design, Minor",
    "Electrical Engineering, Minor",
    "Energy & Sustainability, Minor",
    "Engineering Entrepreneurship, Minor",
    "Materials Science and Engineering, Minor",
    "Mechanical Engineering and Applied Mechanics, Minor",
    "Systems Science and Engineering, Minor"
]

concentrations = [
    'Biomedical Data Science and Computational Medicine',
    'Biomedical Devices',
    'Biomedical Imaging and Radiation Physics',
    'Cellular/Tissue Engineering and Biomaterials',
    'Multiscale Biomechanics',
    'Neuroengineering',
    'Systems and Synthetic Biology',
    'Therapeutics, Drug Delivery & Nanomedicine',
    'Immune Engineering',
    'Robotics',
    'Vision/Language',
    'Machine Learning',
    'Data/Society',
    'Health/Systems',
    'Biochemical Engineering',
    'Nanotechnology',
    'Environmental Engineering',
    'Polymer Science',
    'Materials Engineering',
    'Process and Product Design',
    'Hardware and Software Design',
    'Embedded Systems',
    'Networking',
    'Security',
    'Robotics',
    'Artificial Intelligence',
    'Computer Graphics and Vision',
    'Computational Biology',
    'Software Foundations',
    'Networked and Distributed Systems',
    'Theory of Computation',
    'Animation',
    'Game Design',
    'Interactive Media',
    'Visual Computing',
    'Electronic Devices and Circuits',
    'Signal Processing',
    'Telecommunications',
    'Robotics',
    'Systems and Controls',
    'Biomaterials',
    'Electronic and Photonic Materials',
    'Nanotechnology',
    'Soft Materials',
    'Structural Materials',
    'Biomechanics',
    'Energy and Environment',
    'Manufacturing',
    'Mechanics of Materials',
    'Robotics and Control',
    'Thermal and Fluid Sciences',
    'Algorithmic Economics',
    'Network Science',
    'Data Science',
    'Systems and Security',
    'Control Systems',
    'Data Science',
    'Financial Engineering',
    'Operations Research',
    'Robotics and Cyber-Physical Systems',
    'Air Quality and Sustainable Energy',
    'Water Quality and Resources',
    'Environmental Biotechnology',
    'Environmental Chemistry and Health',
    'Quantum Engineering',
    'Nanoengineering',
    'Photonic Engineering',
    'Energy and Sustainability',
]

def getUsernames(): 
    fruits = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "mango", "watermelon", "peach"]

    usernames = set()  # Using a set to ensure uniqueness

    while len(usernames) < 300:
        username = random.choice(fruits) + str(random.randint(100, 999))
        usernames.add(username)

    usernames = list(usernames)
    return username

def populate():
    usernames = getUsernames()

    for username in usernames:
        schedule = Schedule()

        schedule.pennkey = username
        
        gpa = random.uniform(2, 4)
        schedule.gpa = round(gpa, 2)

        semester = random.randint(1, 9)
        schedule.semester = semester

        answers = {}

        if random.uniform(0,1) < 0.65: # one major
            answers['major'] = set(random.choice(majors))
        else: # double major
            first_choice, second_choice = random.sample(majors, 2)
            maj = set(first_choice, second_choice)
            answers['major'] = maj
        
        if random.uniform(0,1) > 0.65: # one minor 
            answers['minor'] = set(random.choice(minors))

        if random.uniform(0,1) > 0.65: # one concentration
            answers['concentration'] = set(random.choice(concentrations))
        else:
            answers['concentration'] = set()
        
        

        

        



