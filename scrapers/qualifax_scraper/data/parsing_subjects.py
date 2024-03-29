import re

"""
The idea is to gather as much classified data as possible, then we can use this to assist in classifying modules from UL.
We can then use classified modules to classify courses, to which we can cluster and assume similarities.

Author: Emmett Lawlor
Date: 20/11/21
"""

from json import dump

# source -> http://choices4learning.com/home/quick-stop-resources-2/articles-on-learning/school-subjects-list/
def parseChoicesForLearning():
    subjects = ['Language Arts','Mathematics','Science','Health','Handwriting','Physical Education (P.E.)','Art','Music','Instrumental Music – specific instrument','Movement or Eurythmy','Handwork or handcrafts','Life Lab or gardening','Dramatics','Dance','Spanish or other foreign language','Leadership','Special Education Day Class','Resource Program','Speech','Adaptive P.E.','Occupational Therapy','CORE – core subjects class','Reading','Language arts','Speech and Debate','English','Basic Math','Pre-algebra','Consumer Math','Algebra','Geometry','Honors Math in Algebra or Geometry','Life Science','Earth Science','Physical Science','Health','Social Studies','Geography','Ancient Civilizations','Medieval and Renaissance','U.S. History and Government','French / Spanish / Latin','Computer Science or Lab','Art','Home Economics','Woodshop','Metal Shop','Business Technology','Instrumental Music','Band','Choir','Drama','Physical Education','Sports','Special Education Day Class','Resource Program','Speech Therapy','Occupational Therapy',' ','ENGLISH','English I','English II','English III','English IV','Remedial English','ESL – English as second language','World Literature','Ancient Literature','Medieval Literature','Renaissance Literature','Modern Literature','British Literature','American Literature','Short Story','Classical literature','Shakespeare','Heroes',' Myth and Legend','Film as Literature','Composition','Creative Writing','Poetry','Grammar','Vocabulary','Debate','Speech','Journalism','Publishing Skills','Photojournalism','Yearbook','Study Skills','Research Skills','FINE ARTS','Art I','Art II','Art III','Art IV','Art Appreciation','Art History','Drawing','Painting','Sculpture','Ceramics','Pottery','Instrumental Music','Music Appreciation','Music History','Music Theory','Music Fundamentals','Band','Orchestra','Choir','Voice','Classical Music Studies','Performing Arts','Theatre Arts -Beg.',' interm.',' and advanced','Improvisational Theater','Dance','APPLIED ARTS','Computer Aided Design Digital Media','Photography','Videography','History of Film','Film Production','Leather Working','Drafting','Metal Work','Small Engine Mechanics','Auto Mechanics','SCIENCE ','General Science','Physics','Physical Science','Chemistry','Organic Chemistry','Life Science','Biology','Zoology','Marine Biology','Botany','Earth Science','Geology','Oceanography','Meteorology','Astronomy','Animal Science','Equine Science','Veterinary Science','Forensic Science','Ecology','Environmental Science','Gardening','Food Science','FOREIGN LANGUAGE','Spanish','French','Japanese','German','Latin','Greek','Hebrew','Chinese','Conversational LANGUAGE','(LANGUAGE) Literature','(LANGUAGE) Culture','(LANGUAGE) History','Sign Language','MATH','Remedial Math','Fundamental Math or Basic Math','Mathematics','Pre-Algebra','Introduction to Algebra','Algebra','Algebra I','Algebra II','Intermediate Algebra','Geometry','Trigonometry','Precalculus','Calculus','Statistics','Business Math','Consumer Math','Accounting','Personal Finance and Investing','SOCIAL STUDIES','Ancient History','Medieval History','Greek and Roman History','Renaissance History with US History','Modern History with US History','World History','History of (——-)','World Geography','US History','World Religions','World Current Events Global Issues','Government','Civics','Economics','Political Science','Social Sciences','Psychology','Sociology','Anthropology','Genealogy','Philosophy','LOGIC','Logic I','Logic II','Critical Thinking','Rhetoric','HEALTH','Health','Basic First Aid and Safety','Nutrition','Healthful Living Personal Health','PHYSICAL EDUCATION','Team Sports (Soccer',' volleyball',' football',' etc)','Gymnastics','Track and Field','Archery','Fencing','Golf','Rock Climbing','Outdoor Survival Skills','Hiking','Equestrian Skills','Weightlifting','Physical Fitness','Aerobics','Yoga','Martial Arts','Ice Skating','Figure skating','Cycling','Bowling','Drill Team',' Honor Guard',' Pageantry',' Flag',' Cheer','Adapted P.E','COMPUTERS','Keyboarding','Word Processing','Computer Aided Drafting','Computer Applications:  (——)','Certification in (—–)','Computer Graphics','Digital Arts','Photoshop','Programming','Computer Repair','Web Design','Desktop Publishing','LIFE SKILLS','Culinary Arts','Child Development','Home Management','Home Organization','Basic Yard Care','Financial Management','Driver’s Education','Personal Organization','Social Skills','Career Planning','OTHER','AP Courses in any core subject','Honors Courses in any core subject','Study Skills','SAT Prep','Work-Study','SPECIAL EDUCATION','Lifeskills','Resource Program','Speech','Special Day Class']

    course_catalogues = {}

    category = 'core'
    buffer = []

    for subject in subjects:
        subject = subject.strip().replace('-', ' ')
        if(len([i for i in subject if i.capitalize() == i]) == len(subject)):
            course_catalogues[category] = buffer
            category = subject.lower()
            buffer = []
            continue
        
        buffer.append(subject.lower())

    with open('course_category.json', mode='w+') as of:
        dump(course_catalogues, of, indent=4)