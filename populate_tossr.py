import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tossr.settings')
django.setup()

from accounts.models import User, Student
from modules.models import School, Degree, Module, StudentModule


def populate():
    print("Populating TOSSR...\n")
    """
    NOTE: I will intentionally leave out MAIN Comp Sci degrees and comp sci modules.
    This is for testing purposes.
    """
    # Clear existing
    User.objects.all().delete()
    School.objects.all().delete()

    # === SCHOOLS ===
    print('Creating schools...')

    add = School.objects.create(name='Academic and Digital Development')
    business = School.objects.create(name='Adam Smith Business School')
    mvls = School.objects.create(name='MVLS College Services')
    veterinary = School.objects.create(name='School of Biodiversity One Health Vet Med')
    cancer = School.objects.create(name='School of Cancer Sciences')
    cardio = School.objects.create(name='School of Cardiovascular and Metabolic')
    chemistry = School.objects.create(name='School of Chemistry')
    computing = School.objects.create(name='School of Computing Science')
    critical_studies = School.objects.create(name='School of Critical Studies')
    art = School.objects.create(name='School of Culture and Creative Arts')
    education = School.objects.create(name='School of Education')
    engineering = School.objects.create(name='School of Engineering')
    geography = School.objects.create(name='School of Geographical and Earth Sciences')
    health = School.objects.create(name='School of Health and Wellbeing')
    humanities = School.objects.create(name='School of Humanities')
    infection = School.objects.create(name='School of Infection and Immunity')
    law = School.objects.create(name='School of Law')
    maths = School.objects.create(name='School of Mathematics and Statistics')
    medicine = School.objects.create(name='School of Medicine Dentistry and Nursing')
    language = School.objects.create(name='School of Modern Languages and Cultures')
    bioscience = School.objects.create(name='School of Molecular Biosciences')
    physics = School.objects.create(name='School of Physics and Astronomy')
    psychology = School.objects.create(name='School of Psychology and Neuroscience')
    environmental = School.objects.create(name='School of Social and Environmental Sustainability')
    politics = School.objects.create(name='School of Social and Political Sciences')
    short_courses = School.objects.create(name='Short Courses')
    student_learning_development = School.objects.create(name='Student Learning Development')
    # ====== DEGREES ======
    degrees = {}
    degrees_data = []

    # ====== Art - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('VW46', deg_type, 'Archaeology/Film & Television Studies', [art, critical_studies]),
        ('V4W3', deg_type, 'Archaeology/Music', [art, critical_studies]),
        ('VW44', deg_type, 'Archaeology/Theatre Studies', [art, critical_studies]),
        ('LW73', deg_type, 'Geography/Music', [art, geography]),
        ('LW74', deg_type, 'Geography/Theatre Studies', [art, geography]),
    ])

    # ====== Art - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('W370', deg_type, 'Creative Arts & Industries', [art]),
        ('GP53', deg_type, 'Digital Media & Information Studies/Film & Television Studies', [art, critical_studies]),
        ('GW5H', deg_type, 'Digital Media & Information Studies/Music', [art, critical_studies]),
        ('GW5K', deg_type, 'Digital Media & Information Studies/Theatre Studies', [art, critical_studies]),
        ('P390', deg_type, 'Film & Television Studies', [art]),
        ('WW36', deg_type, 'Film & Television Studies/Music', [art]),
        ('LW26', deg_type, 'Film & Television Studies/Politics', [art, politics]),
        ('LW46', deg_type, 'Film & Television Studies/Social & Public Policy', [art, politics]),
        ('LW36', deg_type, 'Film & Television Studies/Sociology', [art, politics]),
        ('WW46', deg_type, 'Film & Television Studies/Theatre Studies', [art]),
        ('LA41', deg_type, 'Liberal Arts with Film & Television Studies', [art]),
        ('LA71', deg_type, 'Liberal Arts with Theatre Studies', [art]),
        ('W300', deg_type, 'Music', [art]),
        ('LW23', deg_type, 'Music/Politics', [art, politics]),
        ('LW43', deg_type, 'Music/Social & Public Policy', [art, politics]),
        ('WW34', deg_type, 'Music/Theatre Studies', [art]),
        ('W440', deg_type, 'Theatre Studies', [art]),
    ])

    # ====== Art - BMus ======
    deg_type = 'BMus'
    degrees_data.extend([
        ('W302', deg_type, 'Music', [art]),
    ])

    # ====== Art - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('LW24', deg_type, 'Politics/Theatre Studies', [art, politics]),
        ('LW44', deg_type, 'Social & Public Policy/Theatre Studies', [art, politics]),
        ('LW34', deg_type, 'Sociology/Theatre Studies', [art, politics]),
    ])

    # ====== Bioscience - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('B110', deg_type, 'Anatomy', [bioscience]),
        ('C400', deg_type, 'Genetics', [bioscience]),
        ('C1W3', deg_type, 'Human Biology & Physiology', [bioscience]),
        ('C550', deg_type, 'Immunology', [bioscience]),
        ('C164', deg_type, 'Marine & Freshwater Biology', [bioscience]),
        ('C500', deg_type, 'Microbiology', [bioscience]),
        ('C720', deg_type, 'Molecular & Cellular Biology', [bioscience]),
        ('C110', deg_type, 'Molecular & Cellular Biology (with Biotechnology)', [bioscience]),
        ('C200', deg_type, 'Molecular & Cellular Biology (with Plant Science)', [bioscience]),
        ('B210', deg_type, 'Pharmacology', [bioscience]),
        ('BC16', deg_type, 'Sport & Exercise Science', [bioscience]),
        ('C300', deg_type, 'Zoology', [bioscience]),
    ])

    # ====== Business - BAcc ======
    deg_type = 'BAcc'
    degrees_data.extend([
        ('N400', deg_type, 'Accountancy', [business]),
        ('N4N3', deg_type, 'Accountancy with Finance', [business]),
        ('N401', deg_type, 'Accountancy with International Accounting', [business]),
        ('N4T9', deg_type, 'Accountancy with Languages', [business, language]),
        ('LN14', deg_type, 'Accountancy/Economics', [business]),
    ])

    # ====== Business - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('NG4C', deg_type, 'Accounting & Mathematics', [business, maths]),
        ('GN34', deg_type, 'Accounting & Statistics', [business, maths]),
        ('LN16', deg_type, 'Archaeology/Business Economics', [business, critical_studies]),
        ('VL41', deg_type, 'Archaeology/Economics', [business, critical_studies]),
        ('NG3C', deg_type, 'Finance & Mathematics', [business, maths]),
        ('GN33', deg_type, 'Finance & Statistics', [business, maths]),
    ])

    # ====== Business - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('N200', deg_type, 'Business & Management', [business]),
        ('LNC2', deg_type, 'Business & Management/Business Economics', [business]),
        ('LN12', deg_type, 'Business & Management/Economics', [business]),
        ('LN72', deg_type, 'Business & Management/Geography', [business, geography]),
        ('NV21', deg_type, 'Business & Management/History', [business, humanities]),
        ('LN22', deg_type, 'Business & Management/Politics', [business, politics]),
        ('LN62', deg_type, 'Business & Management/Sociology', [business, politics]),
        ('NG21', deg_type, 'Business & Management/Mathematics', [business, maths]),
        ('MN19', deg_type, 'Business & Management/Common Law', [business, law]),
        ('MN12', deg_type, 'Business & Management/Scots Law', [business, law]),
        ('GN52', deg_type, 'Business & Management/Digital Media & Information Studies', [business, critical_studies]),
        ('QN32', deg_type, 'Business & Management/English Literature', [business, humanities]),
        ('NR21', deg_type, 'Business & Management/French', [business, language]),
        ('QN52', deg_type, 'Business & Management/Gaelic', [business, language]),
        ('NR22', deg_type, 'Business & Management/German', [business, language]),
        ('NVF1', deg_type, 'Business & Management/History', [business, humanities]),
        ('NVF3', deg_type, 'Business & Management/History of Art', [business, humanities, art]),
        ('NR23', deg_type, 'Business & Management/Italian', [business, language]),
        ('NQ26', deg_type, 'Business & Management/Latin', [business, humanities]),
        ('NW23', deg_type, 'Business & Management/Music', [business, art]),
        ('NVF5', deg_type, 'Business & Management/Philosophy', [business, humanities]),
        ('9K7B', deg_type, 'Business & Management/Portuguese', [business, language]),
        ('NR27', deg_type, 'Business & Management/Russian', [business, language]),
        ('N1R4', deg_type, 'Business & Management/Spanish', [business, language]),
        ('L112', deg_type, 'Business Economics', [business]),
        ('RL71', deg_type, 'Business Economics/Central & East European Studies', [business]),
        ('LG11', deg_type, 'Business Economics/Mathematics', [business, maths]),
        ('LV15', deg_type, 'Business Economics/Philosophy', [business, humanities]),
        ('LLC2', deg_type, 'Business Economics/Politics', [business, politics]),
        ('LVD2', deg_type, 'Business Economics/Scottish History', [business, humanities]),
        ('LLC4', deg_type, 'Business Economics/Social & Public Policy', [business, politics]),
        ('R900', deg_type, 'Central & East European Studies', [business]),
        ('L150', deg_type, 'Economics', [business]),
        ('LL17', deg_type, 'Economics/Geography', [business, geography]),
        ('GL11', deg_type, 'Economics/Mathematics', [business, maths]),
        ('LVC5', deg_type, 'Economics/Philosophy', [business, humanities]),
        ('LL12', deg_type, 'Economics/Politics', [business, politics]),
        ('LVC2', deg_type, 'Economics/Scottish History', [business, humanities]),
        ('LG1D', deg_type, 'Economics/Mathematics', [business, maths]),
        ('GL31', deg_type, 'Economics/Statistics', [business, maths]),
        ('LQ1H', deg_type, 'Economics/English Language & Linguistics', [business, language]),
        ('LQD3', deg_type, 'Economics/English Literature', [business, humanities]),
        ('LR11', deg_type, 'Economics/French', [business, language]),
        ('RL21', deg_type, 'Economics/German', [business, language]),
        ('LQ17', deg_type, 'Economics/Greek', [business, humanities]),
        ('LVC1', deg_type, 'Economics/History', [business, humanities]),
        ('LQ16', deg_type, 'Economics/Latin', [business, humanities]),
        ('LW13', deg_type, 'Economics/Music', [business, art]),
        ('LVD5', deg_type, 'Economics/Philosophy', [business, humanities]),
        ('LR17', deg_type, 'Economics/Russian', [business, language]),
        ('LVD1', deg_type, 'Economics/Scottish History', [business, humanities]),
        ('RL41', deg_type, 'Economics/Spanish', [business, language]),
        ('LW14', deg_type, 'Economics/Theatre Studies', [business, art]),
        ('LV16', deg_type, 'Economics/Theology & Religious Studies', [business, humanities]),
    ])

    # ====== Business - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('LQC2', deg_type, 'Comparative Literature/Economics', [business, humanities]),
    ])

    # ====== Business - BFin ======
    deg_type = 'BFin'
    degrees_data.extend([
        ('NL30', deg_type, 'Finance', [business]),
    ])

    # ====== Business - MA ======
    deg_type = 'MA'
    degrees_data.extend([
        ('D400', deg_type, 'Global Sustainable Development', [business]),
    ])

    # ====== Chemistry - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('C700', deg_type, 'Biochemistry', [chemistry, bioscience]),
        ('F100', deg_type, 'Chemistry', [chemistry]),
        ('F101', deg_type, 'Chemistry with work placement', [chemistry]),
        ('F103', deg_type, 'Chemistry with Medicinal Chemistry', [chemistry]),
        ('F104', deg_type, 'Chemistry with Medicinal Chemistry (work placement)', [chemistry]),
    ])

    # ====== Chemistry - MSci ======
    deg_type = 'MSci'
    degrees_data.extend([
        ('F107', deg_type, 'Materials Chemistry with work placement', [chemistry]),
    ])

    # ====== Chemistry - BSc ======
    deg_type = 'BSc'
    degrees_data.extend([
        ('F108', deg_type, 'Materials Chemistry', [chemistry]),
    ])

    # ====== Computing - BSc ======
    deg_type = 'BSc'
    degrees_data.extend([
        ('H763', deg_type, 'Artificial Intelligence', [computing, art]),
        ('G700', deg_type, 'Artificial Intelligence', [computing, art]),
    ])

    # ====== Computing - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('NG24', deg_type, 'Business & Management/Computing Science', [computing, business]),
    ])

    # ====== Computing - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('GQ48', deg_type, 'Classics/Computing Science', [computing, humanities]),
    ])

    # ====== Computing - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('G400', deg_type, 'Computing Science', [computing]),
        ('FG84', deg_type, 'Computing Science/Geography', [computing, geography]),
        ('GGK1', deg_type, 'Computing Science/Mathematics', [computing, maths]),
        ('FG34', deg_type, 'Computing Science/Physics', [computing, physics]),
        ('CG84', deg_type, 'Computing Science/Psychology', [computing, psychology]),
        ('GG34', deg_type, 'Computing Science/Statistics', [computing, maths]),
        ('G402', deg_type, 'Computing Science', [computing]),
        ('GG4C', deg_type, 'Computing Science/Mathematics', [computing, maths]),
        ('IF13', deg_type, 'Computing Science/Physics', [computing, physics]),
        ('GQ4J', deg_type, 'Computing Science/English Language & Linguistics', [computing, language]),
        ('GQ4H', deg_type, 'Computing Science/English Literature', [computing, humanities]),
        ('GR41', deg_type, 'Computing Science/French', [computing, language]),
        ('GVK3', deg_type, 'Computing Science/History of Art', [computing, humanities, art]),
        ('GQ46', deg_type, 'Computing Science/Latin', [computing, humanities]),
        ('GW43', deg_type, 'Computing Science/Music', [computing, art]),
        ('GW44', deg_type, 'Computing Science/Theatre Studies', [computing, art]),
        ('VG64', deg_type, 'Computing Science/Theology & Religious Studies', [computing, humanities]),
        ('3N7R', deg_type, 'Computing Science (faster route)', [computing]),
        ('7G3F', deg_type, 'Computing Science (faster route)', [computing]),
        ('G430', deg_type, 'Software Engineering', [computing, engineering]),
        ('G610', deg_type, 'Software Engineering', [computing, engineering]),
        ('I300', deg_type, 'Software Engineering with work placement', [computing, engineering]),
        ('0P31', deg_type, 'Software Engineering (faster route)', [computing, engineering]),
        ('0VB3', deg_type, 'Software Engineering (faster route)', [computing, engineering]),
        ('I301', deg_type, 'Software Engineering with work placement (faster route)', [computing, engineering]),
    ])

    # ====== Computing - BEng ======
    deg_type = 'BEng'
    degrees_data.extend([
        ('GHP6', deg_type, 'Electronic & Software Engineering', [computing, engineering]),
        ('GH66', deg_type, 'Electronic & Software Engineering', [computing, engineering]),
        ('HG66', deg_type, 'Electronic & Software Engineering', [computing, engineering]),
        ('H760', deg_type, 'Robotics & Artificial Intelligence', [computing, art]),
        ('H7RO', deg_type, 'Robotics & Artificial Intelligence', [computing, art]),
    ])

    # ====== Critical Studies - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('V402', deg_type, 'Archaeology', [critical_studies]),
        ('V400', deg_type, 'Archaeology', [critical_studies]),
        ('GV54', deg_type, 'Archaeology/Digital Media & Information Studies', [critical_studies]),
    ])

    # ====== Critical Studies - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('RG75', deg_type, 'Central & East European Studies/Digital Media & Information Studies', [critical_studies]),
    ])

    # ====== Critical Studies - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('I150', deg_type, 'Digital Media & Information Studies', [critical_studies]),
    ])

    # ====== Education - BA  (Hons) ======
    deg_type = 'BA  (Hons)'
    degrees_data.extend([
        ('XL35', deg_type, 'Community Development', [education]),
    ])

    # ====== Education - MDTechEd ======
    deg_type = 'MDTechEd'
    degrees_data.extend([
        ('H112', deg_type, 'Design & Technology Education', [education]),
    ])

    # ====== Education - MEduc ======
    deg_type = 'MEduc'
    degrees_data.extend([
        ('4Q21', deg_type, 'Education with Teacher Qualification Primary (Undergraduate)', [education]),
        ('4Q22', deg_type,
         'Education with Teacher Qualification Primary including Catholic Teacher’s Certificate (Undergraduate)',
         [education]),
    ])

    # ====== Education - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('X123', deg_type, 'Primary Education with Teaching Qualification (Dumfries)', [education]),
    ])

    # ====== Engineering - BEng ======
    deg_type = 'BEng'
    degrees_data.extend([
        ('H415', deg_type, 'Aeronautical Engineering', [engineering]),
        ('H410', deg_type, 'Aeronautical Engineering', [engineering]),
        ('H402', deg_type, 'Aerospace Systems', [engineering]),
        ('H401', deg_type, 'Aerospace Systems', [engineering]),
        ('J750', deg_type, 'Biomedical Engineering', [engineering, medicine]),
        ('J751', deg_type, 'Biomedical Engineering', [engineering, medicine]),
        ('H202', deg_type, 'Civil Engineering', [engineering]),
        ('H200', deg_type, 'Civil Engineering', [engineering]),
        ('H2KC', deg_type, 'Civil Engineering with Architecture', [engineering]),
        ('H2K1', deg_type, 'Civil Engineering with Architecture', [engineering]),
        ('H600', deg_type, 'Electronics & Electrical Engineering', [engineering]),
        ('H601', deg_type, 'Electronics & Electrical Engineering', [engineering]),
        ('H6W3', deg_type, 'Electronics with Music', [engineering, art]),
        ('H6WJ', deg_type, 'Electronics with Music', [engineering, art]),
        ('HH37', deg_type, 'Mechanical Design Engineering', [engineering]),
        ('HHJ7', deg_type, 'Mechanical Design Engineering', [engineering]),
        ('H300', deg_type, 'Mechanical Engineering', [engineering]),
        ('H302', deg_type, 'Mechanical Engineering', [engineering]),
        ('H3H4', deg_type, 'Mechanical Engineering with Aeronautics', [engineering]),
        ('H3HK', deg_type, 'Mechanical Engineering with Aeronautics', [engineering]),
        ('H730', deg_type, 'Mechatronics', [engineering]),
        ('H731', deg_type, 'Mechatronics', [engineering]),
        ('H3W2', deg_type, 'Product Design Engineering', [engineering]),
        ('H3WG', deg_type, 'Product Design Engineering', [engineering]),
    ])

    # ====== Engineering - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('V1Q5', deg_type, 'Ancient History/Celtic Civilisation', [engineering, language, humanities]),
        ('RQR5', deg_type, 'Celtic Civilisation/Central & East European Studies', [engineering, language]),
        ('Q821', deg_type, 'Celtic Civilisation/Classics', [engineering, language, humanities]),
        ('GQ5N', deg_type, 'Celtic Civilisation/Digital Media & Information Studies',
         [engineering, language, critical_studies]),
        ('QQM3', deg_type, 'Celtic Civilisation/English Language & Linguistics', [engineering, language]),
        ('QQ5J', deg_type, 'Celtic Civilisation/English Literature', [engineering, language, humanities]),
        ('Q590', deg_type, 'Celtic Civilisation/Gaelic', [engineering, language]),
        ('LQ75', deg_type, 'Celtic Civilisation/Geography', [engineering, language, geography]),
        ('QVM1', deg_type, 'Celtic Civilisation/History', [engineering, language, humanities]),
        ('QR53', deg_type, 'Celtic Civilisation/Italian', [engineering, language]),
        ('GQ15', deg_type, 'Celtic Civilisation/Mathematics', [engineering, maths, language]),
        ('QV55', deg_type, 'Celtic Civilisation/Philosophy', [engineering, language, humanities]),
        ('QVN2', deg_type, 'Celtic Civilisation/Scottish History', [engineering, language, humanities]),
        ('QQF5', deg_type, 'Celtic Civilisation/Scottish Literature', [engineering, language, humanities]),
        ('LQK5', deg_type, 'Celtic Civilisation/Social & Public Policy', [engineering, language, politics]),
        ('QV56', deg_type, 'Celtic Civilisation/Theology & Religious Studies', [engineering, language, humanities]),
    ])

    # ====== Engineering - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('QVM4', deg_type, 'Archaeology/Celtic Civilisation', [engineering, language, critical_studies]),
    ])

    # ====== Geography - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('FF64', deg_type, 'Archaeology/Environmental Geoscience', [geography, critical_studies]),
        ('FV84', deg_type, 'Archaeology/Geography', [geography, critical_studies]),
        ('LV74', deg_type, 'Archaeology/Geography', [geography, critical_studies]),
        ('F600', deg_type, 'Environmental Geoscience', [geography]),
        ('D447', deg_type, 'Environmental Science & Sustainability (Dumfries)', [geography]),
        ('F800', deg_type, 'Geography', [geography]),
        ('L702', deg_type, 'Geography', [geography]),
        ('L700', deg_type, 'Geography', [geography]),
        ('LL72', deg_type, 'Geography/Politics', [geography, politics]),
        ('LL47', deg_type, 'Geography/Social & Public Policy', [geography, politics]),
        ('F610', deg_type, 'Geology', [geography]),
    ])

    # ====== Geography - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('RL77', deg_type, 'Central & East European Studies/Geography', [geography]),
    ])

    # ====== Geography - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('GL57', deg_type, 'Digital Media & Information Studies/Geography', [geography, critical_studies]),
    ])

    # ====== Humanities - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('V160', deg_type, 'Ancient History', [humanities]),
        ('V1V4', deg_type, 'Ancient History/Archaeology', [humanities, critical_studies]),
        ('VQ13', deg_type, 'Ancient History/English Literature', [humanities]),
        ('VV12', deg_type, 'Ancient History/History', [humanities]),
        ('VV15', deg_type, 'Ancient History/Philosophy', [humanities]),
        ('VL12', deg_type, 'Ancient History/Politics', [humanities, politics]),
        ('Q820', deg_type, 'Classics', [humanities]),
        ('QQ3V', deg_type, 'Classics/English Literature', [humanities]),
        ('QP83', deg_type, 'Classics/Film & Television Studies', [humanities, art]),
        ('LQ78', deg_type, 'Classics/Geography', [humanities, geography]),
        ('QV81', deg_type, 'Classics/History', [humanities]),
        ('QW83', deg_type, 'Classics/Music', [humanities, art]),
        ('QV85', deg_type, 'Classics/Philosophy', [humanities]),
        ('LQ28', deg_type, 'Classics/Politics', [humanities, politics]),
        ('QVV2', deg_type, 'Classics/Scottish History', [humanities]),
        ('LQ48', deg_type, 'Classics/Social & Public Policy', [humanities, politics]),
        ('QV86', deg_type, 'Classics/Theology & Religious Studies', [humanities]),
        ('QQF8', deg_type, 'Comparative Literature/Classics', [humanities]),
        ('LQ83', deg_type, 'Sociology/Classics', [humanities, politics]),
        ('WQ48', deg_type, 'Theatre Studies/Classics', [humanities, art]),
        ('LQF8', deg_type, 'Classics/Politics', [humanities, politics]),
        ('LQK8', deg_type, 'Classics/Social & Public Policy', [humanities, politics]),
        ('Q200', deg_type, 'Comparative Literature', [humanities]),
        ('Q290', deg_type, 'Comparative Literature/English Literature', [humanities]),
        ('PQ32', deg_type, 'Comparative Literature/Film & Television Studies', [humanities, art]),
        ('QVF1', deg_type, 'Comparative Literature/History', [humanities]),
        ('QVF3', deg_type, 'Comparative Literature/History of Art', [humanities, art]),
        ('QWF3', deg_type, 'Comparative Literature/Music', [humanities, art]),
        ('QVF5', deg_type, 'Comparative Literature/Philosophy', [humanities]),
        ('Q291', deg_type, 'Comparative Literature/Scottish Literature', [humanities]),
        ('QWF4', deg_type, 'Comparative Literature/Theatre Studies', [humanities, art]),
        ('VQ62', deg_type, 'Comparative Literature/Theology & Religious Studies', [humanities]),
        ('GQ5H', deg_type, 'Digital Media & Information Studies/English Literature', [humanities, critical_studies]),
        ('GV5H', deg_type, 'Digital Media & Information Studies/History of Art', [humanities, art, critical_studies]),
        ('P3Q5', deg_type, 'Digital Media & Information Studies/Latin', [humanities, critical_studies]),
        ('GV55', deg_type, 'Digital Media & Information Studies/Philosophy', [humanities, critical_studies]),
        ('GV5P', deg_type, 'Digital Media & Information Studies/Theology & Religious Studies',
         [humanities, critical_studies]),
        ('Q301', deg_type, 'English Literature', [humanities]),
        ('QW3P', deg_type, 'English Literature/Film & Television Studies', [humanities, art]),
        ('QV3C', deg_type, 'English Literature/History', [humanities]),
        ('QVHH', deg_type, 'English Literature/History of Art', [humanities, art]),
        ('QQ3P', deg_type, 'English Literature/Latin', [humanities]),
        ('QW3H', deg_type, 'English Literature/Music', [humanities, art]),
        ('QV3M', deg_type, 'English Literature/Philosophy', [humanities]),
        ('LQ2H', deg_type, 'English Literature/Politics', [humanities, politics]),
        ('QVHF', deg_type, 'English Literature/Scottish History', [humanities]),
        ('QQ2H', deg_type, 'English Literature/Scottish Literature', [humanities]),
        ('LQ4H', deg_type, 'English Literature/Social & Public Policy', [humanities, politics]),
        ('LQ3H', deg_type, 'English Literature/Sociology', [humanities, politics]),
        ('WQ4H', deg_type, 'English Literature/Theatre Studies', [humanities, art]),
        ('VQ63', deg_type, 'English Literature/Theology & Religious Studies', [humanities]),
        ('VW16', deg_type, 'Film & Television Studies/History', [humanities, art]),
        ('VW36', deg_type, 'Film & Television Studies/History of Art', [humanities, art]),
        ('P3Q6', deg_type, 'Film & Television Studies/Latin', [humanities, art]),
        ('VW56', deg_type, 'Film & Television Studies/Philosophy', [humanities, art]),
        ('VWF6', deg_type, 'Film & Television Studies/Scottish History', [humanities, art]),
        ('QW26', deg_type, 'Film & Television Studies/Scottish Literature', [humanities, art]),
        ('Q700', deg_type, 'Greek', [humanities]),
        ('Q7V1', deg_type, 'Greek/History', [humanities]),
        ('QVR3', deg_type, 'Greek/History of Art', [humanities, art]),
        ('QQ67', deg_type, 'Greek/Latin', [humanities]),
        ('LQ27', deg_type, 'Greek/Politics', [humanities, politics]),
        ('LQ47', deg_type, 'Greek/Social & Public Policy', [humanities, politics]),
        ('Q7W4', deg_type, 'Greek/Theatre Studies', [humanities, art]),
        ('Q7V6', deg_type, 'Greek/Theology & Religious Studies', [humanities]),
        ('V100', deg_type, 'History', [humanities]),
        ('VVD3', deg_type, 'History/History of Art', [humanities, art]),
        ('QV61', deg_type, 'History/Latin', [humanities]),
        ('VW13', deg_type, 'History/Music', [humanities, art]),
        ('VVC5', deg_type, 'History/Philosophy', [humanities]),
        ('LVF1', deg_type, 'History/Politics', [humanities, politics]),
        ('QV21', deg_type, 'History/Scottish Literature', [humanities]),
        ('LV61', deg_type, 'History/Sociology', [humanities, politics]),
        ('VW14', deg_type, 'History/Theatre Studies', [humanities, art]),
        ('VV16', deg_type, 'History/Theology & Religious Studies', [humanities]),
        ('LV21', deg_type, 'History/Politics', [humanities, politics]),
        ('LV31', deg_type, 'History/Sociology', [humanities, politics]),
        ('V350', deg_type, 'History of Art', [humanities, art]),
        ('QVP3', deg_type, 'History of Art/Latin', [humanities, art]),
        ('VWH3', deg_type, 'History of Art/Music', [humanities, art]),
        ('VVH5', deg_type, 'History of Art/Philosophy', [humanities, art]),
        ('LVF3', deg_type, 'History of Art/Politics', [humanities, art, politics]),
        ('VVF3', deg_type, 'History of Art/Scottish History', [humanities, art]),
        ('QV23', deg_type, 'History of Art/Scottish Literature', [humanities, art]),
        ('LVK3', deg_type, 'History of Art/Social & Public Policy', [humanities, art, politics]),
        ('LV6H', deg_type, 'History of Art/Sociology', [humanities, art, politics]),
        ('VWH4', deg_type, 'History of Art/Theatre Studies', [humanities, art]),
        ('VV36', deg_type, 'History of Art/Theology & Religious Studies', [humanities, art]),
        ('Q600', deg_type, 'Latin', [humanities]),
        ('Q6W3', deg_type, 'Latin/Music', [humanities, art]),
        ('QQ26', deg_type, 'Latin/Scottish Literature', [humanities]),
        ('LQ46', deg_type, 'Latin/Social & Public Policy', [humanities, politics]),
        ('Q6V6', deg_type, 'Latin/Theology & Religious Studies', [humanities]),
        ('LA21', deg_type, 'Liberal Arts with Comparative Literature', [humanities, art]),
        ('LA31', deg_type, 'Liberal Arts with English Literature', [humanities, art]),
        ('LA51', deg_type, 'Liberal Arts with History', [humanities, art]),
        ('LA61', deg_type, 'Liberal Arts with Philosophy', [humanities, art]),
        ('VW53', deg_type, 'Music/Philosophy', [humanities, art]),
        ('VWF3', deg_type, 'Music/Scottish History', [humanities, art]),
        ('QW23', deg_type, 'Music/Scottish Literature', [humanities, art]),
        ('WV36', deg_type, 'Music/Theology & Religious Studies', [humanities, art]),
        ('V502', deg_type, 'Philosophy', [humanities]),
        ('LVF5', deg_type, 'Philosophy/Politics', [humanities, politics]),
        ('VVD5', deg_type, 'Philosophy/Scottish History', [humanities]),
        ('LV65', deg_type, 'Philosophy/Sociology', [humanities, politics]),
        ('VW54', deg_type, 'Philosophy/Theatre Studies', [humanities, art]),
        ('VV56', deg_type, 'Philosophy/Theology & Religious Studies', [humanities]),
        ('LV25', deg_type, 'Philosophy/Politics', [humanities, politics]),
        ('LVH5', deg_type, 'Philosophy/Sociology', [humanities, politics]),
        ('QVF2', deg_type, 'Scottish History/Scottish Literature', [humanities]),
        ('LVP1', deg_type, 'Scottish History/Sociology', [humanities, politics]),
        ('VWF4', deg_type, 'Scottish History/Theatre Studies', [humanities, art]),
        ('VVF6', deg_type, 'Scottish History/Theology & Religious Studies', [humanities]),
        ('Q201', deg_type, 'Scottish Literature', [humanities]),
        ('LQ32', deg_type, 'Scottish Literature/Sociology', [humanities, politics]),
        ('QW24', deg_type, 'Scottish Literature/Theatre Studies', [humanities, art]),
        ('QV26', deg_type, 'Scottish Literature/Theology & Religious Studies', [humanities]),
        ('VW64', deg_type, 'Theatre Studies/Theology & Religious Studies', [humanities, art]),
    ])

    # ====== Humanities - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('QV84', deg_type, 'Archaeology/Classics', [humanities, critical_studies]),
        ('VV34', deg_type, 'Archaeology/Economic & Social History', [humanities, politics, critical_studies]),
        ('QV3K', deg_type, 'Archaeology/English Literature', [humanities, critical_studies]),
        ('VV14', deg_type, 'Archaeology/History', [humanities, critical_studies]),
        ('VVH4', deg_type, 'Archaeology/History of Art', [humanities, art, critical_studies]),
        ('V4Q6', deg_type, 'Archaeology/Latin', [humanities, critical_studies]),
        ('VVF4', deg_type, 'Archaeology/Scottish History', [humanities, critical_studies]),
        ('VV46', deg_type, 'Archaeology/Theology & Religious Studies', [humanities, critical_studies]),
        ('VV43', deg_type, 'Archaeology/Economic & Social History', [humanities, politics, critical_studies]),
        ('LV71', deg_type, 'Geography/History', [humanities, geography]),
        ('LVR3', deg_type, 'Geography/History of Art', [humanities, art, geography]),
        ('QL67', deg_type, 'Geography/Latin', [humanities, geography]),
        ('LV75', deg_type, 'Geography/Philosophy', [humanities, geography]),
        ('LVR2', deg_type, 'Geography/Scottish History', [humanities, geography]),
        ('LQ72', deg_type, 'Geography/Scottish Literature', [humanities, geography]),
    ])

    # ====== Humanities - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('RVT5', deg_type, 'Central & East European Studies/Philosophy', [humanities]),
        ('RQ78', deg_type, 'Central & East European Studies/Classics', [humanities]),
        ('RQ28', deg_type, 'Central & East European Studies/Comparative Literature', [humanities]),
        ('RQ7J', deg_type, 'Central & East European Studies/English Literature', [humanities]),
        ('RV7C', deg_type, 'Central & East European Studies/History', [humanities]),
        ('RVP3', deg_type, 'Central & East European Studies/History of Art', [humanities, art]),
        ('VR85', deg_type, 'Central & East European Studies/Philosophy', [humanities]),
        ('RVP1', deg_type, 'Central & East European Studies/Scottish History', [humanities]),
        ('RQR2', deg_type, 'Central & East European Studies/Scottish Literature', [humanities]),
        ('V300', deg_type, 'Economic & Social History', [humanities, politics]),
        ('VG33', deg_type, 'Economic & Social History with Quantitative Methods', [humanities, politics]),
        ('L253', deg_type, 'Economic & Social History/International Relations', [humanities, politics]),
        ('LV23', deg_type, 'Economic & Social History/Politics', [humanities, politics]),
        ('VV32', deg_type, 'Economic & Social History/Scottish History', [humanities, politics]),
        ('LV33', deg_type, 'Economic & Social History/Sociology', [humanities, politics]),
        ('QV3H', deg_type, 'Economic & Social History/English Literature', [humanities, politics]),
        ('VVC3', deg_type, 'Economic & Social History/History', [humanities, politics]),
        ('VW33', deg_type, 'Economic & Social History/Music', [humanities, art, politics]),
        ('VVJ5', deg_type, 'Economic & Social History/Philosophy', [humanities, politics]),
        ('VVG3', deg_type, 'Economic & Social History/Scottish History', [humanities, politics]),
        ('LVF2', deg_type, 'Politics/Scottish History', [humanities, politics]),
        ('LV22', deg_type, 'Politics/Scottish History', [humanities, politics]),
        ('LQ22', deg_type, 'Politics/Scottish Literature', [humanities, politics]),
        ('VL62', deg_type, 'Politics/Theology & Religious Studies', [humanities, politics]),
        ('VL64', deg_type, 'Social & Public Policy/Theology & Religious Studies', [humanities, politics]),
        ('LV66', deg_type, 'Sociology/Theology & Religious Studies', [humanities, politics]),
    ])

    # ====== Humanities - BD  (Hons) ======
    deg_type = 'BD  (Hons)'
    degrees_data.extend([
        ('V600', deg_type, 'Theology & Religious Studies', [humanities]),
        ('V621', deg_type, 'Theology & Religious Studies', [humanities]),
    ])

    # ====== Language - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('VQ15', deg_type, 'Ancient History/Celtic Studies', [language, humanities]),
        ('V1R1', deg_type, 'Ancient History/French', [language, humanities]),
        ('VR13', deg_type, 'Ancient History/Italian', [language, humanities]),
        ('Q504', deg_type, 'Celtic Studies', [language]),
        ('RQ75', deg_type, 'Celtic Studies/Central & East European Studies', [language]),
        ('QQ58', deg_type, 'Celtic Studies/Classics', [language, humanities]),
        ('VQ35', deg_type, 'Celtic Studies/Economic & Social History', [language, humanities, politics]),
        ('QQ3N', deg_type, 'Celtic Studies/English Language & Linguistics', [language]),
        ('QQ3M', deg_type, 'Celtic Studies/English Literature', [language, humanities]),
        ('QRM1', deg_type, 'Celtic Studies/French', [language]),
        ('QL57', deg_type, 'Celtic Studies/Geography', [language, geography]),
        ('QV51', deg_type, 'Celtic Studies/History', [language, humanities]),
        ('QW53', deg_type, 'Celtic Studies/Music', [language, art]),
        ('QVM5', deg_type, 'Celtic Studies/Philosophy', [language, humanities]),
        ('QVM2', deg_type, 'Celtic Studies/Scottish History', [language, humanities]),
        ('QQ25', deg_type, 'Celtic Studies/Scottish Literature', [language, humanities]),
        ('Q5V6', deg_type, 'Celtic Studies/Theology & Religious Studies', [language, humanities]),
        ('QR81', deg_type, 'Classics/French', [language, humanities]),
        ('QR83', deg_type, 'Classics/Italian', [language, humanities]),
        ('QR87', deg_type, 'Classics/Russian', [language, humanities]),
        ('7M2U', deg_type, 'Portuguese/Classics', [language, humanities]),
        ('QQF3', deg_type, 'Comparative Literature/English Language & Linguistics', [language, humanities]),
        ('QRF1', deg_type, 'Comparative Literature/French', [language, humanities]),
        ('QQ5F', deg_type, 'Comparative Literature/Gaelic', [language, humanities]),
        ('QRF2', deg_type, 'Comparative Literature/German', [language, humanities]),
        ('QRF3', deg_type, 'Comparative Literature/Italian', [language, humanities]),
        ('RQT2', deg_type, 'Comparative Literature/Russian', [language, humanities]),
        ('RQ42', deg_type, 'Comparative Literature/Spanish', [language, humanities]),
        ('GQ5J', deg_type, 'Digital Media & Information Studies/English Language & Linguistics',
         [language, critical_studies]),
        ('GR5C', deg_type, 'Digital Media & Information Studies/French', [language, critical_studies]),
        ('4K2W', deg_type, 'Digital Media & Information Studies/Portuguese', [language, critical_studies]),
        ('P3R4', deg_type, 'Digital Media & Information Studies/Spanish', [language, critical_studies]),
        ('Q300', deg_type, 'English Language & Linguistics', [language]),
        ('Q304', deg_type, 'English Language & Linguistics/English Literature', [language, humanities]),
        ('QR3D', deg_type, 'English Language & Linguistics/French', [language]),
        ('QQ53', deg_type, 'English Language & Linguistics/Gaelic', [language]),
        ('QR3G', deg_type, 'English Language & Linguistics/German', [language]),
        ('Q3Q7', deg_type, 'English Language & Linguistics/Greek', [language, humanities]),
        ('QV3D', deg_type, 'English Language & Linguistics/History', [language, humanities]),
        ('QR3J', deg_type, 'English Language & Linguistics/Italian', [language]),
        ('QQ3Q', deg_type, 'English Language & Linguistics/Latin', [language, humanities]),
        ('QW3J', deg_type, 'English Language & Linguistics/Music', [language, art]),
        ('QV3N', deg_type, 'English Language & Linguistics/Philosophy', [language, humanities]),
        ('LQ2J', deg_type, 'English Language & Linguistics/Politics', [language, politics]),
        ('4W7V', deg_type, 'English Language & Linguistics/Portuguese', [language]),
        ('QRHT', deg_type, 'English Language & Linguistics/Russian', [language]),
        ('QV3F', deg_type, 'English Language & Linguistics/Scottish History', [language, humanities]),
        ('QQ2J', deg_type, 'English Language & Linguistics/Scottish Literature', [language, humanities]),
        ('QL3L', deg_type, 'English Language & Linguistics/Social & Public Policy', [language, politics]),
        ('LQ63', deg_type, 'English Language & Linguistics/Sociology', [language, politics]),
        ('WQ4J', deg_type, 'English Language & Linguistics/Theatre Studies', [language, art]),
        ('QV36', deg_type, 'English Language & Linguistics/Theology & Religious Studies', [language, humanities]),
        ('QR3C', deg_type, 'English Literature/French', [language, humanities]),
        ('Q3Q5', deg_type, 'English Literature/Gaelic', [language, humanities]),
        ('QR3F', deg_type, 'English Literature/German', [language, humanities]),
        ('6L8B', deg_type, 'English Literature/Portuguese', [language, humanities]),
        ('QRHR', deg_type, 'English Literature/Russian', [language, humanities]),
        ('RQ43', deg_type, 'English Literature/Spanish', [language, humanities]),
        ('RW16', deg_type, 'Film & Television Studies/French', [language, art]),
        ('RW26', deg_type, 'Film & Television Studies/German', [language, art]),
        ('8Y7M', deg_type, 'Film & Television Studies/Portuguese', [language, art]),
        ('P3R5', deg_type, 'Film & Television Studies/Spanish', [language, art]),
        ('R120', deg_type, 'French', [language]),
        ('QR5C', deg_type, 'French/Gaelic', [language]),
        ('LR71', deg_type, 'French/Geography', [language, geography]),
        ('RR12', deg_type, 'French/German', [language]),
        ('VR11', deg_type, 'French/History', [language, humanities]),
        ('RVC3', deg_type, 'French/History of Art', [language, humanities, art]),
        ('RR13', deg_type, 'French/Italian', [language]),
        ('QR61', deg_type, 'French/Latin', [language, humanities]),
        ('RW13', deg_type, 'French/Music', [language, art]),
        ('LR21', deg_type, 'French/Politics', [language, politics]),
        ('5V8M', deg_type, 'French/Portuguese', [language]),
        ('RR17', deg_type, 'French/Russian', [language]),
        ('LR6C', deg_type, 'French/Sociology', [language, politics]),
        ('RR41', deg_type, 'French/Spanish', [language]),
        ('RW14', deg_type, 'French/Theatre Studies', [language, art]),
        ('RV16', deg_type, 'French/Theology & Religious Studies', [language, humanities]),
        ('Q530', deg_type, 'Gaelic', [language]),
        ('QR5F', deg_type, 'Gaelic/German', [language]),
        ('QV5C', deg_type, 'Gaelic/History', [language, humanities]),
        ('Q5V5', deg_type, 'Gaelic/Philosophy', [language, humanities]),
        ('7G4L', deg_type, 'Gaelic/Portuguese', [language]),
        ('QV52', deg_type, 'Gaelic/Scottish History', [language, humanities]),
        ('QL54', deg_type, 'Gaelic/Social & Public Policy', [language, politics]),
        ('VQ56', deg_type, 'Gaelic/Theology & Religious Studies', [language, humanities]),
        ('R220', deg_type, 'German', [language]),
        ('RVF3', deg_type, 'German/History of Art', [language, humanities, art]),
        ('RR23', deg_type, 'German/Italian', [language]),
        ('RW23', deg_type, 'German/Music', [language, art]),
        ('RV25', deg_type, 'German/Philosophy', [language, humanities]),
        ('LR22', deg_type, 'German/Politics', [language, politics]),
        ('5H3Z', deg_type, 'German/Portuguese', [language]),
        ('RR27', deg_type, 'German/Russian', [language]),
        ('LR6F', deg_type, 'German/Sociology', [language, politics]),
        ('RR42', deg_type, 'German/Spanish', [language]),
        ('R2W4', deg_type, 'German/Theatre Studies', [language, art]),
        ('R2V6', deg_type, 'German/Theology & Religious Studies', [language, humanities]),
        ('6V5T', deg_type, 'Greek/Portuguese', [language, humanities]),
        ('Q7R4', deg_type, 'Greek/Spanish', [language, humanities]),
        ('RV31', deg_type, 'History/Italian', [language, humanities]),
        ('5E3J', deg_type, 'History/Portuguese', [language, humanities]),
        ('RV71', deg_type, 'History/Russian', [language, humanities]),
        ('RV4C', deg_type, 'History/Spanish', [language, humanities]),
        ('RVH3', deg_type, 'History of Art/Italian', [language, humanities, art]),
        ('8C7D', deg_type, 'History of Art/Portuguese', [language, humanities, art]),
        ('RV73', deg_type, 'History of Art/Russian', [language, humanities, art]),
        ('V3R4', deg_type, 'History of Art/Spanish', [language, humanities, art]),
        ('R310', deg_type, 'Italian', [language]),
        ('QR63', deg_type, 'Italian/Latin', [language, humanities]),
        ('RW33', deg_type, 'Italian/Music', [language, art]),
        ('RV35', deg_type, 'Italian/Philosophy', [language, humanities]),
        ('4L2M', deg_type, 'Italian/Portuguese', [language]),
        ('RR43', deg_type, 'Italian/Spanish', [language]),
        ('R3W4', deg_type, 'Italian/Theatre Studies', [language, art]),
        ('R3V6', deg_type, 'Italian/Theology & Religious Studies', [language, humanities]),
        ('2A6F', deg_type, 'Latin/Portuguese', [language, humanities]),
        ('Q6R4', deg_type, 'Latin/Spanish', [language, humanities]),
        ('RW73', deg_type, 'Music/Russian', [language, art]),
        ('RW4H', deg_type, 'Music/Spanish', [language, art]),
        ('7A3W', deg_type, 'Philosophy/Portuguese', [language, humanities]),
        ('RV75', deg_type, 'Philosophy/Russian', [language, humanities]),
        ('V5R4', deg_type, 'Philosophy/Spanish', [language, humanities]),
        ('9Q8Z', deg_type, 'Portuguese/Russian', [language]),
        ('3W2Q', deg_type, 'Portuguese/Scottish History', [language, humanities]),
        ('R642', deg_type, 'Portuguese/Scottish Literature', [language, humanities]),
        ('6Y5X', deg_type, 'Portuguese/Social & Public Policy', [language, politics]),
        ('R578', deg_type, 'Portuguese/Spanish', [language]),
        ('R647', deg_type, 'Portuguese/Theatre Studies', [language, art]),
        ('R854', deg_type, 'Portuguese/Theology & Religious Studies', [language, humanities]),
        ('QR27', deg_type, 'Russian/Scottish Literature', [language, humanities]),
        ('LR37', deg_type, 'Russian/Sociology', [language, politics]),
        ('VR67', deg_type, 'Russian/Theology & Religious Studies', [language, humanities]),
        ('V2R4', deg_type, 'Scottish History/Spanish', [language, humanities]),
        ('RQ4M', deg_type, 'Scottish Literature/Spanish', [language, humanities]),
        ('R410', deg_type, 'Spanish', [language]),
        ('RW4K', deg_type, 'Spanish/Theatre Studies', [language, art]),
        ('RV4P', deg_type, 'Spanish/Theology & Religious Studies', [language, humanities]),
    ])

    # ====== Language - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('QV54', deg_type, 'Archaeology/Celtic Studies', [language, critical_studies]),
        ('V4Q3', deg_type, 'Archaeology/English Language & Linguistics', [language, critical_studies]),
        ('V4Q5', deg_type, 'Archaeology/Gaelic', [language, critical_studies]),
        ('V4R2', deg_type, 'Archaeology/German', [language, critical_studies]),
        ('7F1A', deg_type, 'Archaeology/Portuguese', [language, critical_studies]),
        ('V4R4', deg_type, 'Archaeology/Spanish', [language, critical_studies]),
        ('LR72', deg_type, 'Geography/German', [language, geography]),
        ('3T5Y', deg_type, 'Geography/Portuguese', [language, geography]),
        ('RL47', deg_type, 'Geography/Spanish', [language, geography]),
    ])

    # ====== Language - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('QR5R', deg_type, 'Central & East European Studies/Gaelic', [language]),
        ('RR72', deg_type, 'Central & East European Studies/German', [language]),
        ('RR73', deg_type, 'Central & East European Studies/Italian', [language]),
        ('R791', deg_type, 'Central & East European Studies/Russian', [language]),
        ('RV13', deg_type, 'Economic & Social History/French', [language, humanities, politics]),
        ('RV23', deg_type, 'Economic & Social History/German', [language, humanities, politics]),
        ('9W7L', deg_type, 'Economic & Social History/Portuguese', [language, humanities, politics]),
        ('5Y4F', deg_type, 'Politics/Portuguese', [language, politics]),
        ('L2R4', deg_type, 'Politics/Spanish', [language, politics]),
        ('RL44', deg_type, 'Social & Public Policy/Spanish', [language, politics]),
        ('RL46', deg_type, 'Sociology/Spanish', [language, politics]),
    ])

    # ====== Law - LLB  (Hons) ======
    deg_type = 'LLB  (Hons)'
    degrees_data.extend([
        ('M100', deg_type, 'Common Law', [law]),
        ('M9R1', deg_type, 'Common Law with French Language', [law, language]),
        ('M9R2', deg_type, 'Common Law with German Language', [law, language]),
        ('M9R3', deg_type, 'Common Law with Italian Language', [law, language]),
        ('M9R4', deg_type, 'Common Law with Spanish Language', [law, language]),
        ('ML13', deg_type, 'Common Law/Economic & Social History', [law, humanities, politics]),
        ('MQ93', deg_type, 'Common Law/English Literature', [law, humanities]),
        ('MV91', deg_type, 'Common Law/History', [law, humanities]),
        ('MV95', deg_type, 'Common Law/Philosophy', [law, humanities]),
        ('ML92', deg_type, 'Common Law/Politics', [law, politics]),
        ('M114', deg_type, 'Scots Law', [law]),
        ('M1R1', deg_type, 'Scots Law with French Language', [law, language]),
        ('M1R2', deg_type, 'Scots Law with German Language', [law, language]),
        ('M1R3', deg_type, 'Scots Law with Italian Language', [law, language]),
        ('M1R4', deg_type, 'Scots Law with Spanish Language', [law, language]),
        ('MQ13', deg_type, 'Scots Law/English Literature', [law, humanities]),
        ('MV11', deg_type, 'Scots Law/History', [law, humanities]),
        ('MV15', deg_type, 'Scots Law/Philosophy', [law, humanities]),
        ('ML14', deg_type, 'Scots Law/Social & Public Policy', [law, politics]),
    ])

    # ====== Law - LLB ======
    deg_type = 'LLB'
    degrees_data.extend([
        ('M900', deg_type, 'Common Law (accelerated', [law]),
        ('M115', deg_type, 'Scots Law (fast track', [law]),
    ])

    # ====== Law - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('ML12', deg_type, 'Politics/Scots Law', [law, politics]),
    ])

    # ====== Maths - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('GV14', deg_type, 'Archaeology/Mathematics', [maths, critical_studies]),
        ('FGM1', deg_type, 'Astronomy/Mathematics', [maths, physics]),
        ('FG5D', deg_type, 'Astronomy/Mathematics', [maths, physics]),
        ('GF11', deg_type, 'Chemistry/Mathematics', [maths, chemistry]),
        ('FG11', deg_type, 'Chemistry/Mathematics', [maths, chemistry]),
        ('FG81', deg_type, 'Geography/Mathematics', [maths, geography]),
        ('G100', deg_type, 'Mathematics', [maths]),
        ('GVD5', deg_type, 'Mathematics/Philosophy', [maths, humanities]),
        ('GF14', deg_type, 'Mathematics/Physics', [maths, physics]),
        ('GGC3', deg_type, 'Mathematics/Statistics', [maths]),
        ('G102', deg_type, 'Mathematics', [maths]),
        ('GW13', deg_type, 'Mathematics/Music', [maths, art]),
        ('GV15', deg_type, 'Mathematics/Philosophy', [maths, humanities]),
        ('4A9P', deg_type, 'Mathematics/Portuguese', [maths, language]),
        ('GR17', deg_type, 'Mathematics/Russian', [maths, language]),
        ('GVC2', deg_type, 'Mathematics/Scottish History', [maths, humanities]),
        ('GQ12', deg_type, 'Mathematics/Scottish Literature', [maths, humanities]),
        ('RG41', deg_type, 'Mathematics/Spanish', [maths, language]),
        ('GW14', deg_type, 'Mathematics/Theatre Studies', [maths, art]),
        ('GV16', deg_type, 'Mathematics/Theology & Religious Studies', [maths, humanities]),
        ('G101', deg_type, 'Mathematics', [maths]),
        ('FGJ1', deg_type, 'Mathematics/Physics', [maths, physics]),
        ('GGH1', deg_type, 'Mathematics/Statistics', [maths]),
        ('2GM1', deg_type, 'Mathematics (faster route)', [maths]),
        ('3GC3', deg_type, 'Mathematics/Statistics (faster route)', [maths]),
        ('MF20', deg_type, 'Mathematics (faster route)', [maths]),
        ('MSF1', deg_type, 'Mathematics/Statistics (faster route)', [maths]),
        ('G300', deg_type, 'Statistics', [maths]),
        ('G302', deg_type, 'Statistics', [maths]),
        ('1G30', deg_type, 'Statistics (faster route)', [maths]),
        ('SF10', deg_type, 'Statistics (faster route)', [maths]),
    ])

    # ====== Maths - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('GQC5', deg_type, 'Celtic Studies/Mathematics', [maths, language]),
        ('GQ18', deg_type, 'Classics/Mathematics', [maths, humanities]),
        ('GGM1', deg_type, 'Digital Media & Information Studies/Mathematics', [maths, critical_studies]),
        ('QG3D', deg_type, 'English Language & Linguistics/Mathematics', [maths, language]),
        ('QG3C', deg_type, 'English Literature/Mathematics', [maths, humanities]),
        ('GR11', deg_type, 'French/Mathematics', [maths, language]),
        ('QG51', deg_type, 'Gaelic/Mathematics', [maths, language]),
        ('GR12', deg_type, 'German/Mathematics', [maths, language]),
        ('GV11', deg_type, 'History/Mathematics', [maths, humanities]),
        ('GVC3', deg_type, 'History of Art/Mathematics', [maths, humanities, art]),
        ('GR13', deg_type, 'Italian/Mathematics', [maths, language]),
        ('GQ16', deg_type, 'Latin/Mathematics', [maths, humanities]),
    ])

    # ====== Maths - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('VG31', deg_type, 'Economic & Social History/Mathematics', [maths, humanities, politics]),
    ])

    # ====== Maths - BSc ======
    deg_type = 'BSc'
    degrees_data.extend([
        ('G500', deg_type, 'Machine Learning, Mathematics & Statistics', [maths]),
        ('G501', deg_type, 'Machine Learning, Mathematics & Statistics', [maths]),
    ])

    # ====== Medicine - BDS ======
    deg_type = 'BDS'
    degrees_data.extend([
        ('A200', deg_type, 'Dentistry', [medicine]),
    ])

    # ====== Medicine - CertHE ======
    deg_type = 'CertHE'
    degrees_data.extend([
        ('A900', deg_type, 'Gateway to Medical Studies', [medicine]),
    ])

    # ====== Medicine - MBChB ======
    deg_type = 'MBChB'
    degrees_data.extend([
        ('A100', deg_type, 'Medicine', [medicine]),
    ])

    # ====== Medicine - BN  (Hons) ======
    deg_type = 'BN  (Hons)'
    degrees_data.extend([
        ('B700', deg_type, 'Nursing', [medicine]),
    ])

    # ====== Medicine - BVMS ======
    deg_type = 'BVMS'
    degrees_data.extend([
        ('D100', deg_type, 'Veterinary Medicine & Surgery', [medicine, veterinary]),
        ('D210', deg_type, 'Veterinary Medicine & Surgery (graduate entry)', [medicine, veterinary]),
    ])

    # ====== Physics - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('FF53', deg_type, 'Astronomy/Physics', [physics]),
        ('FF5H', deg_type, 'Astronomy/Physics', [physics]),
        ('F335', deg_type, 'Chemical Physics', [physics]),
        ('F322', deg_type, 'Chemical Physics', [physics]),
        ('F320', deg_type, 'Chemical Physics with work placement', [physics]),
        ('F300', deg_type, 'Physics', [physics]),
        ('F344', deg_type, 'Theoretical Physics', [physics]),
        ('F301', deg_type, 'Physics', [physics]),
        ('F340', deg_type, 'Theoretical Physics', [physics]),
        ('F303', deg_type, 'Physics (Faster Route)', [physics]),
        ('F345', deg_type, 'Theoretical Physics (Faster Route)', [physics]),
        ('F302', deg_type, 'Physics (Faster Route)', [physics]),
        ('F341', deg_type, 'Theoretical Physics (Faster Route)', [physics]),
        ('F3F5', deg_type, 'Physics with Astrophysics', [physics]),
        ('F3FM', deg_type, 'Physics with Astrophysics', [physics]),
        ('F3F2', deg_type, 'Physics with Astrophysics (Faster Route)', [physics]),
        ('F3F1', deg_type, 'Physics with Astrophysics (Faster Route)', [physics]),
    ])

    # ====== Politics - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('LV24', deg_type, 'Archaeology/Politics', [politics, critical_studies]),
        ('VL42', deg_type, 'Archaeology/Politics', [politics, critical_studies]),
    ])

    # ====== Politics - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('RG73', deg_type, 'Central & East European Studies with Quantitative Methods', [politics]),
        ('L252', deg_type, 'Central & East European Studies/International Relations', [politics]),
        ('RL82', deg_type, 'Central & East European Studies/Politics', [politics]),
        ('RL84', deg_type, 'Central & East European Studies/Social & Public Policy', [politics]),
        ('L250', deg_type, 'International Relations', [politics]),
        ('L2G3', deg_type, 'International Relations with Quantitative Methods', [politics]),
        ('L254', deg_type, 'International Relations/Social & Public Policy', [politics]),
        ('L251', deg_type, 'International Relations/Sociology', [politics]),
        ('L202', deg_type, 'Politics', [politics]),
        ('LG23', deg_type, 'Politics with Quantitative Methods', [politics]),
        ('LL42', deg_type, 'Politics/', [politics]),
        ('LL62', deg_type, 'Politics/Sociology', [politics]),
        ('LG43', deg_type, 'Social & Public Policy with Quantitative Methods', [politics]),
        ('LG33', deg_type, 'Sociology with Quantitative Methods', [politics]),
        ('L430', deg_type, 'Social & Public Policy', [politics]),
        ('LL64', deg_type, 'Social & Public Policy/Sociology', [politics]),
        ('L300', deg_type, 'Sociology', [politics]),
    ])

    # ====== Politics - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('GL52', deg_type, 'Digital Media & Information Studies/Politics', [politics, critical_studies]),
        ('GL54', deg_type, 'Digital Media & Information Studies/Social & Public Policy', [politics, critical_studies]),
        ('GL56', deg_type, 'Digital Media & Information Studies/Sociology', [politics, critical_studies]),
    ])

    # ====== Psychology - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('CV84', deg_type, 'Archaeology/Psychology', [psychology, critical_studies]),
        ('CG81', deg_type, 'Mathematics/Psychology', [psychology, maths]),
        ('B140', deg_type, 'Neuroscience', [psychology]),
        ('C800', deg_type, 'Psychology', [psychology]),
        ('CG83', deg_type, 'Psychology/Statistics', [psychology, maths]),
        ('C801', deg_type, 'Psychology', [psychology]),
        ('CVW2', deg_type, 'Psychology/Scottish History', [psychology, humanities]),
        ('CQ82', deg_type, 'Psychology/Scottish Literature', [psychology, humanities]),
        ('8U9K', deg_type, 'Psychology/Spanish', [psychology, language]),
        ('CW84', deg_type, 'Psychology/Theatre Studies', [psychology, art]),
        ('CV86', deg_type, 'Psychology/Theology & Religious Studies', [psychology, humanities]),
        ('C802', deg_type, 'Psychology', [psychology]),
        ('LC38', deg_type, 'Psychology/Sociology', [psychology, politics]),
    ])

    # ====== Psychology - MA(SocSci)  (Hons) ======
    deg_type = 'MA(SocSci)  (Hons)'
    degrees_data.extend([
        ('CN82', deg_type, 'Business & Management/Psychology', [psychology, business]),
        ('LC18', deg_type, 'Business Economics/Psychology', [psychology, business]),
        ('RG68', deg_type, 'Central & East European Studies/Psychology', [psychology]),
        ('CV83', deg_type, 'Economic & Social History/Psychology', [psychology, humanities, politics]),
        ('CL81', deg_type, 'Economics/Psychology', [psychology, business]),
    ])

    # ====== Psychology - MA  (Hons) ======
    deg_type = 'MA  (Hons)'
    degrees_data.extend([
        ('CQV5', deg_type, 'Celtic Civilisation/Psychology', [psychology, engineering, language]),
        ('CQ85', deg_type, 'Celtic Studies/Psychology', [psychology, language]),
        ('CQ88', deg_type, 'Classics/Psychology', [psychology, humanities]),
        ('GC5V', deg_type, 'Digital Media & Information Studies/Psychology', [psychology, critical_studies]),
        ('CQ8J', deg_type, 'English Language & Linguistics/Psychology', [psychology, language]),
        ('CR81', deg_type, 'French/Psychology', [psychology, language]),
        ('QC58', deg_type, 'Gaelic/Psychology', [psychology, language]),
        ('CR82', deg_type, 'German/Psychology', [psychology, language]),
        ('CV81', deg_type, 'History/Psychology', [psychology, humanities]),
        ('CVV3', deg_type, 'History of Art/Psychology', [psychology, humanities, art]),
        ('CW83', deg_type, 'Music/Psychology', [psychology, art]),
        ('CVV5', deg_type, 'Philosophy/Psychology', [psychology, humanities]),
        ('3H2N', deg_type, 'Portuguese/Psychology', [psychology, language]),
    ])

    # ====== Veterinary - BSc  (Hons) ======
    deg_type = 'BSc  (Hons)'
    degrees_data.extend([
        ('D300', deg_type, 'Veterinary Biosciences', [veterinary]),
    ])

    # Create all degrees
    print('Creating degrees...')
    for code, deg_type, name, schools_list in degrees_data:
        degree = Degree.objects.create(code=code, degree_type=deg_type, name=name)
        degree.schools.add(*schools_list)
        degrees[code] = degree

    print(f'Created {School.objects.count()} schools')

    # ====== MODULES ======
    print('Creating modules...')

    # Academic and Digital Development (16 modules)
    Module.objects.create(id='EDUC5993', name='Masters Project in Academic Practice', school=add, level=5, credits=60)
    Module.objects.create(id='EDUC5983', name='Course Design in your Discipline', school=add, level=5, credits=10)
    Module.objects.create(id='EDUC5991', name='Design your SoTL Enquiry', school=add, level=5, credits=20)
    Module.objects.create(id='EDUC1138', name='Collaborations in Practice (C4L)', school=add, level=1, credits=20)
    Module.objects.create(id='EDUC5982', name='Supervising Students', school=add, level=5, credits=10)
    Module.objects.create(id='EDUC51091', name='Intercultural Learning and Teaching in Higher Education', school=add,
                          level=5, credits=10)
    Module.objects.create(id='EDUC5984', name='Assessment and Feedback', school=add, level=5, credits=10)
    Module.objects.create(id='EDUC51058',
                          name='Designing Online Education: MOOCs, micro-credentials and online, distance learning',
                          school=add, level=5, credits=10)
    Module.objects.create(id='EDUC5990', name='Contextualising your Educational Enquiry', school=add, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5992', name='Analysing your Enquiry Data', school=add, level=5, credits=10)
    Module.objects.create(id='EDUC51036', name='Inclusive Learning and Teaching in Higher Education', school=add,
                          level=5, credits=10)
    Module.objects.create(id='EDUC5981', name='Introduction to Learning and Teaching in Higher Education', school=add,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5989', name='Impact and Influence in Learning and Teaching', school=add, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5988', name='Scholarship of Teaching and Learning II: undertaking a practice enquiry',
                          school=add, level=5, credits=10)
    Module.objects.create(id='EDUC5985', name='Creative Pedagogies for Active Learning', school=add, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5987', name='Scholarship of Teaching and Learning I: designing a practice enquiry',
                          school=add, level=5, credits=10)

    # Adam Smith Business School (460 modules)
    Module.objects.create(id='ACCFIN4004', name='Management Control Systems', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN5202', name='Derivative Securities', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4029', name='Corporate Insolvency and Restructuring', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5266',
                          name='Management Accounting for Sustainability and Strategic Decision Making',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN2003', name='Financial Accounting 2', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN5034', name='Issues in Accounting Research', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5045', name='International Corporate Governance & Accountability', school=business,
                          level=5, credits=20)
    Module.objects.create(id='ACCFIN4031', name='Accountability and Human Rights', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4009', name='Auditing', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4087', name='Fundamentals of Crowdfunding', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN5256', name='Business Financial Management', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN5273', name='Research in FinTech', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN4085', name='Advanced Financial Modelling', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4017', name='Issues in Social and Environmental Accounting', school=business,
                          level=4, credits=20)
    Module.objects.create(id='ACCFIN5230', name='Artificial Intelligence in Finance', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ACCFIN4063', name='Psychology and Financial Markets', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5043', name='Behavioural Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN1007', name='Management Accounting 1: A Business Decision Emphasis',
                          school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN4096', name='Financial Technology and Applications', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN2002', name='Finance 2', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN4079', name='Econometric Methods for Accounting and Finance', school=business,
                          level=4, credits=20)
    Module.objects.create(id='ACCFIN5055', name='Audit, Risk and Control', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4010', name='Capital Markets and Portfolio Management', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN4002', name='Ethics in Accounting and Business', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5229', name='Advances in Machine Learning in Finance', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ACCFIN4092', name='Climate Accounting and ESG Reporting', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5039', name='Principles of Financial Econometrics', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5014', name='Asset Pricing and Macro-Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4015', name='International Financial Management', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5024', name='International Financial Accounting for Multi-National Companies',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5271P', name='Industry Project', school=business, level=5, credits=60)
    Module.objects.create(id='ACCFIN4044', name='Tax Theory and Practice', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4041', name='Issues in the Accountancy Profession', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5234', name='Foundations of Financial Technology', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ACCFIN5013', name='Financial Reporting and Interpretation', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN2024', name='Finance and Society', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN5257', name='Fundamental Analysis and Stock Valuation', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5008P', name='Dissertation and Research Methods', school=business, level=5,
                          credits=60)
    Module.objects.create(id='ACCFIN1004', name='Financial Accounting 1', school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN5002', name='Advanced International Corporate Reporting', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN4082', name='Accounting Theories in Research and Practice', school=business,
                          level=4, credits=20)
    Module.objects.create(id='ACCFIN5231', name='Big Data Analytics', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN5208', name='Issues in International Corporate Taxation', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5203', name='Foundations of International Corporate Finance', school=business,
                          level=5, credits=20)
    Module.objects.create(id='ACCFIN5264', name='Contemporary Issues in Climate Accounting and ESG Reporting',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5249', name='Capital Markets and Investment', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5001', name='Accounting & Business Ethics', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5272', name='Business Financial Management', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN5059', name='Governing Risk and Uncertainty', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5246', name='Data Science and Machine Learning in Finance', school=business,
                          level=5, credits=20)
    Module.objects.create(id='ACCFIN5265', name='Contemporary Issues in Sustainability and Corporate Reporting',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5219', name='Corporate Finance and Valuation', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4016', name='Management Accounting in Organisations and Society', school=business,
                          level=4, credits=20)
    Module.objects.create(id='ACCFIN5255', name='Climate Finance and ESG Investment', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN1016', name='Introduction to Finance, Investments and Institutions',
                          school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN4013', name='Financial Statement Analysis and Valuation', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5274P', name='Dissertation and Research Methods', school=business, level=5,
                          credits=60)
    Module.objects.create(id='ACCFIN1001', name='Introduction to Business Reporting & Financial Accounting',
                          school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN2023', name='Business Systems and Assurance', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN5058', name='Mergers and Acquisitions', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4051', name='Strategic Management Accounting', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4091', name='Banking Theory and Practice', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN4001P', name='Accounting and Finance Dissertation', school=business, level=4,
                          credits=40)
    Module.objects.create(id='ACCFIN5030', name='International Fixed Income Markets', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN4090', name='Data Analytics for Accounting and Finance', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5207', name='Financial Risk Management', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5217', name='Financial Econometrics', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4070', name='Corporate Finance', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN5258', name='Sustainable Finance:Risk & Reporting', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN1017', name='The Accountancy Profession', school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN4007', name='Advanced Financial Accounting', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN2025', name='Financial Modelling', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN4053', name='Public Sector Accounting', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN5254', name='Data Analytics for Accounting and Audit', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5057', name='Financial Management in Banking', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5259', name='Climate Change and Green Banking', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ACCFIN5036', name='Management Accounting and Control', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN4008', name='Advanced Theory and Practice of Taxation', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN4095', name='Financial Analysis and Valuation', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN2022', name='Taxation', school=business, level=2, credits=20)
    Module.objects.create(id='ACCFIN5200', name='Financial Analysis and Equity Valuation', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5056', name='Social and Environmental Accounting', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN4093', name='Corporate Disclosure and Sustainability', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN4012', name='Financial Markets & Financial Institutions', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5214', name='Public Sector Financial Management', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5232', name='FinTech Risk Management', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN5017', name='International Capital Markets', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5012', name='Financial Regulation and Ethics', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN4072', name='Judgement and Decision-Making in Accounting and Auditing',
                          school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN1003', name='Finance 1', school=business, level=1, credits=20)
    Module.objects.create(id='ACCFIN4014', name='International Financial Accounting', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5261', name='Crowdfunding and Token Issues', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN4064', name='Mergers and Acquisitions', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN2018', name='Statistical Analysis and Methods', school=business, level=2,
                          credits=20)
    Module.objects.create(id='ACCFIN4094', name='Finance Case Study', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN2005', name='Management Accounting 2: Organisational Performance', school=business,
                          level=2, credits=20)
    Module.objects.create(id='ACCFIN5242', name='Accounting for Management', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5060', name='Human Rights and Business', school=business, level=5, credits=20)
    Module.objects.create(id='ACCFIN5233', name='Financial Information Retrieval', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN4086', name='Audit & Society', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN5218', name='Corporate Finance and Securities', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ACCFIN5243', name='Business Finance', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN4088', name='Private Equity & Venture Capital', school=business, level=4,
                          credits=20)
    Module.objects.create(id='ACCFIN5205', name='Corporate Finance', school=business, level=5, credits=10)
    Module.objects.create(id='ACCFIN4040', name='Derivative Securities', school=business, level=4, credits=20)
    Module.objects.create(id='ACCFIN1006', name='Introduction to Management Accounting and Control', school=business,
                          level=1, credits=20)
    Module.objects.create(id='BUS5005', name='Decision Making Under Uncertainty', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5052', name='MBA Group Consultancy Project', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5045P', name='MBA Project: Industry Pathway', school=business, level=5, credits=60)
    Module.objects.create(id='BUS5056', name='Managing Operations', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5041P', name='Fintech Pathways Project: Research Pathway', school=business, level=5,
                          credits=60)
    Module.objects.create(id='BUS5021', name='Supply Chain Management', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5053', name='Mergers and Acquisitions', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5051', name='Financial Markets & Risk Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='BUS5067', name='Generative AI for Productivity and Growth', school=business, level=5,
                          credits=10)
    Module.objects.create(id='BUS5003', name='Global Economy', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5014', name='International Strategy For Multinational Enterprise', school=business,
                          level=5, credits=10)
    Module.objects.create(id='BUS5057', name='People & Organisations: Understanding and applying the science',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5019P', name='Dissertation (MBA- Project)', school=business, level=5, credits=60)
    Module.objects.create(id='BUS5069', name='ESG (environmental, social and governance) Leadership', school=business,
                          level=5, credits=10)
    Module.objects.create(id='BUS5059', name='Innovation Management', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5054', name='MBA Business Simulation Game', school=business, level=5, credits=0)
    Module.objects.create(id='BUS5044', name='Hacking the MoD (H4MoD)', school=business, level=5, credits=20)
    Module.objects.create(id='BUS5013', name='International Financial Analysis', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5020', name='Entrepreneurial Finance', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5042P', name='Fintech Pathways Project: Start-up Pathway', school=business, level=5,
                          credits=60)
    Module.objects.create(id='BUS5066', name='Corporate Finance and Financial Markets', school=business, level=5,
                          credits=10)
    Module.objects.create(id='BUS5007', name='Business to Business Relationship Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='BUS5004', name='Marketing Management', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5002', name='Financial Information and Analysis', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5022', name='Strategic Management', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5024P', name='Fintech Pathways Project: Industry Pathway', school=business, level=5,
                          credits=60)
    Module.objects.create(id='BUS5011', name='Strategic Human Resource Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='BUS5055', name='Strategic Brand Management', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5050', name='Social Media Marketing: building customer relationships', school=business,
                          level=5, credits=5)
    Module.objects.create(id='BUS5047P', name='MBA Project: Start-up Pathway', school=business, level=5, credits=60)
    Module.objects.create(id='BUS5019', name='Digital Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='BUS5046P', name='MBA Project: Research Pathway', school=business, level=5, credits=60)
    Module.objects.create(id='BUS5010', name='Consumer Behaviour', school=business, level=5, credits=10)
    Module.objects.create(id='ECON4011', name='Environmental Economics', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4017', name='International Finance', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5156', name='Behavioural Macroeconomics', school=business, level=5, credits=10)
    Module.objects.create(id='ECON5169', name='Behavioural Economics for Sustainability', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ECON5086', name='Topics in Computational Macroeconomics', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5030', name='The Economics Of Inequality And Deprivation', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5009', name='Financial Markets, Securities and Derivatives', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON4056', name='Market Failures and Mechanism Design', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON4072', name='Economics of Poverty, Discrimination and Development', school=business,
                          level=4, credits=15)
    Module.objects.create(id='ECON5147P', name='Dissertation BS Research Pathway', school=business, level=5, credits=60)
    Module.objects.create(id='ECON2002', name='Economics 2B', school=business, level=2, credits=20)
    Module.objects.create(id='ECON5101', name='Understanding Development: A Multidisciplinary Approach',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ECON4101', name='Economic Analysis with MATLAB', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5118', name='Business Cycles: Theory, Evidence and Macroeconomic Policy',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ECON4049', name='Behavioural Economics: Theory and Applications', school=business,
                          level=4, credits=15)
    Module.objects.create(id='ECON5081', name='Microeconomic Theory 1', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4009', name='Economics of Industry', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5102P', name='Dissertation GCEFS', school=business, level=5, credits=60)
    Module.objects.create(id='ECON5096', name='Topics in Microeconomic Theory 2', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5150', name='High-frequency Trading', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5094', name='Topics in Applied Microeconomics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4073', name='Alternative Perspectives on Topics in Economics', school=business,
                          level=4, credits=15)
    Module.objects.create(id='ECON5080', name='Macroeconomic Theory 1', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4078', name='Financial Crises', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4018', name='International Trade', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5144', name='Experimental Design and Methods for Behavioural Science',
                          school=business, level=5, credits=10)
    Module.objects.create(id='ECON4010', name='Markets and Competition Policy', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5068', name='Investment, Finance and Asset Pricing', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON4071', name='Economics of Banking', school=business, level=4, credits=15)
    Module.objects.create(id='ECON1011', name='Introduction to Alternative Perspectives in Economics', school=business,
                          level=1, credits=20)
    Module.objects.create(id='ECON5021', name='Microeconomics for Financial Markets', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON4053', name='Game Theory for Economists', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4006P', name='Economics Dissertation', school=business, level=4, credits=30)
    Module.objects.create(id='ECON4046', name='Economic Growth and Development', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4074', name='Mathematical Methods for Economists', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON5162', name='Mathematical Methods 2', school=business, level=5, credits=10)
    Module.objects.create(id='ECON5145', name='Introduction to Behavioural Economics', school=business, level=5,
                          credits=10)
    Module.objects.create(id='ECON5117', name='The Economics of Migration', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5022', name='Modelling and Forecasting Financial Time Series', school=business,
                          level=5, credits=20)
    Module.objects.create(id='ECON5120', name='Bayesian Data Analysis', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5026', name='Policies For Sustainability And Development', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON4020',
                          name='Microeconomic Analysis: General Equilibrium, Public Decision and Information.',
                          school=business, level=4, credits=15)
    Module.objects.create(id='ECON5128', name='Econometrics 2', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5073', name='Behavioral Economics:Theory and Applications', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5158P', name='Applied Project', school=business, level=5, credits=60)
    Module.objects.create(id='ECON4080', name='Central Bank Models: A Critical Assessment', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON5142', name='Advanced Topics in Behavioural Economics', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5157', name='AI & Digital Economics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5121', name='Microeconometrics: Impact Evaluation and Causal Analysis',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ECON5152', name='Network Analysis', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5078P', name='1st Year Research Project', school=business, level=5, credits=40)
    Module.objects.create(id='ECON2001', name='Economics 2A', school=business, level=2, credits=20)
    Module.objects.create(id='ECON5088P', name='Economics MRes Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='ECON4052', name='Health Economics.', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5148P', name='Dissertation BS Industry Pathway', school=business, level=5, credits=60)
    Module.objects.create(id='ECON5123P', name='Dissertation DAEF Research Pathway', school=business, level=5,
                          credits=60)
    Module.objects.create(id='ECON1002', name='Economics 1B', school=business, level=1, credits=20)
    Module.objects.create(id='ECON5146', name='Neuroeconomics', school=business, level=5, credits=10)
    Module.objects.create(id='ECON5082', name='Mathematical Methods 1', school=business, level=5, credits=10)
    Module.objects.create(id='ECON5119', name='Applied Time Series and Forecasting', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5024', name='Monetary Policy And The Role Of Central Banks', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5129', name='Statistical Machine Learning', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5160', name='Macroeconomic Theory 2', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5095', name='Topics in Microeconomic Theory 1', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4104P', name='Practice-Based Economics Dissertation', school=business, level=4,
                          credits=30)
    Module.objects.create(id='ECON4054', name='Labour Economics', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5020', name='Mathematical Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON1013', name='Introductory Statistics for Economists', school=business, level=1,
                          credits=10)
    Module.objects.create(id='ECON5133', name='Health Economics in Developing Countries', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5019', name='Economic Growth and Productivity', school=business, level=5, credits=20)
    Module.objects.create(id='ECON1010', name='Introductory Economics', school=business, level=1, credits=20)
    Module.objects.create(id='ECON3023', name='Economics 3: Contemporary Topics in Economics', school=business, level=3,
                          credits=30)
    Module.objects.create(id='ECON4004', name='Econometrics 2: Multiple Regression and Applications', school=business,
                          level=4, credits=15)
    Module.objects.create(id='ECON5025', name='Money, Finance And Growth', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5164', name='Macro-Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5132P', name='Economics PGT External Partner Project', school=business, level=5,
                          credits=60)
    Module.objects.create(id='ECON5003', name='Development Policy', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5016', name='International Finance And Money', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5065', name='Applied Computational Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4019', name='Macroeconomic Analysis: Inflation, Unemployment And Growth',
                          school=business, level=4, credits=15)
    Module.objects.create(id='ECON5103', name='Policies For Sustainability And Development (Food Security)',
                          school=business, level=5, credits=10)
    Module.objects.create(id='ECON4003', name='Econometrics 1: Introduction to Econometrics', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON4007', name='Economics of Business: Contracts and Governance', school=business,
                          level=4, credits=15)
    Module.objects.create(id='ECON5023', name='Modern Theory Of Banking And Finance', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5002', name='Basic Econometrics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5004P', name='Dissertation GCDS', school=business, level=5, credits=60)
    Module.objects.create(id='ECON4008', name='Economics of Business Strategy and Regulation', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON5079', name='Econometrics 1', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4013', name='Financial Markets and Corporate Finance', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON5066', name='Corporate Finance and Investment', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5027', name='Investments & Portfolio Management', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5125', name='Sustainability and Green Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5161', name='Microeconomic Theory 2', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5006', name='Environmental Economics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4103', name='Economic Geography', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4033', name='Government Debt and the Macroeconomy', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON1001', name='Economics 1A', school=business, level=1, credits=20)
    Module.objects.create(id='ECON5015', name='Growth And Development', school=business, level=5, credits=20)
    Module.objects.create(id='ECON3022', name='Economics 3: Economic Policies and Growth', school=business, level=3,
                          credits=30)
    Module.objects.create(id='ECON5089', name='Industrial Organisation', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5149', name='Agent-based Modelling in Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4079', name='Economic History', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5130', name='Machine Learning in Finance with Python', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5085', name='Advanced Mathematical Methods in Economics', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5069', name='Asset Pricing: Theory and Empirics', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON1012', name='Introductory Mathematics for Economists', school=business, level=1,
                          credits=10)
    Module.objects.create(id='ECON5163', name='Financial Econometrics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5165', name='Venture Capital and Private Equity', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5155', name='The New Economics of Inequality', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5143', name='Econometrics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5017', name='International Macroeconomics And Policy', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5108', name='Issues in Economic Research', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5166', name='Robo-Advising and Blockchain Technology', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5032', name='Theory And Principles Of Sustainability', school=business, level=5,
                          credits=20)
    Module.objects.create(id='ECON5167', name='Financial Risk Analytics', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5168', name='Real Estate Economics and Finance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4032', name='Contemporary Issues in Inequality', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4012', name='Financial Derivatives', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5122P', name='Dissertation DAEF Industry Pathway', school=business, level=5,
                          credits=60)
    Module.objects.create(id='ECON5012', name='Financial Services', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5008', name='Financial Institutions and Markets in Developing Countries',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ECON5153', name='Applications of Behavioural Economics in Personal Finance',
                          school=business, level=5, credits=20)
    Module.objects.create(id='ECON4021', name='Natural Resource Economics', school=business, level=4, credits=15)
    Module.objects.create(id='ECON4040', name='Advanced Macroeconomics.', school=business, level=4, credits=15)
    Module.objects.create(id='ECON5098', name='Topics in Macroeconomic Theory 2', school=business, level=5, credits=20)
    Module.objects.create(id='ECON5151', name='Corporate Governance', school=business, level=5, credits=20)
    Module.objects.create(id='ECON4050', name='Collective Welfare and Distributive Justice', school=business, level=4,
                          credits=15)
    Module.objects.create(id='ECON4045', name='Public Economics', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5372', name='Data Science for Marketing Analytics', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT4018', name='Management Research Methods', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5363', name='International Marketing Foresight', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5442P', name='Marketing Dissertation (Summer)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5415', name='Marketing Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5395',
                          name='A Systems Approach to Technology Management: Knowledge, Expertise and Understanding',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5045', name='Internationalisation of SMEs', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5491', name='Business Intelligence Practice', school=business, level=5, credits=20)
    Module.objects.create(id='MGT2011', name='Fundamentals of Human Resource Management', school=business, level=2,
                          credits=10)
    Module.objects.create(id='MGT3023', name='Business Competition', school=business, level=3, credits=20)
    Module.objects.create(id='MGT4022', name='Strategic Marketing', school=business, level=4, credits=30)
    Module.objects.create(id='MGT5229', name='Global Perspectives in Marketing Ethics', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5444', name='Managing for a Sustainable World', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5261P', name='ISM Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT4063', name='Economic Crises and Depressions', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5344',
                          name='Human Resource Management in Context: Understanding Organisations and External Environments',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5259', name='Market Analysis', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5448P', name='Project (Finance and Management)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5182', name='International Strategic Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5439P', name='Marketing Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5455', name='Marketing: Ethics, Consumption and Technology', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5449P', name='Dissertation (EBG)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT4019', name='Entrepreneurial Ventures: Management and Growth', school=business,
                          level=4, credits=15)
    Module.objects.create(id='MGT5350', name='Operational and Strategic HRM', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5327', name='Marketing Research', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5295P', name='Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5057', name='Marketing Communications Strategies and Tactics', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT5129', name='MBA Summer School (1)', school=business, level=5, credits=20)
    Module.objects.create(id='MGT4108', name='The Art of Influencing', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5345P', name='IHRMD Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT4003', name='Global Business', school=business, level=4, credits=15)
    Module.objects.create(id='MGT4006', name='Human Resource Management', school=business, level=4, credits=30)
    Module.objects.create(id='MGT5450P', name='Dissertation (HR)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5496P', name='Applied Project in Business Analytics', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5130', name='MBA Summer School (2)', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5311',
                          name='Manging Creativity and Innovation (Creative Industries and Cultural Policy)',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT4038', name='Managing Equality, Diversity and Inclusion in Organisations',
                          school=business, level=4, credits=15)
    Module.objects.create(id='MGT4109', name='Entrepreneurship and Business Planning', school=business, level=4,
                          credits=15)
    Module.objects.create(id='MGT5475P', name='Management Project (Engineering Pathway)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5353', name='Service Delivery Risk and Resilience', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5358P', name='Project (HR)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5413', name='Digital Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5477P', name='Management Project (IMDI Pathway)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5487', name='Social Media Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT1026', name='Foundations of Finance', school=business, level=1, credits=10)
    Module.objects.create(id='MGT5433', name='Retail Marketing (Semester 1)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5027', name='Export Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5400P', name='MGB Global Research Project', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5271P', name='Project (MGT)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT4090', name='Introduction to Management Research Methods Online (exchange students)',
                          school=business, level=4, credits=15)
    Module.objects.create(id='MGT5360', name='Applied Multivariate Analysis', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5457', name='Social Media Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5273', name='Managing Strategic Change (ASBS)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT4009', name='Digital Marketing Strategy', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5414', name='Marketing Communications Strategies and Tactics', school=business,
                          level=5, credits=20)
    Module.objects.create(id='MGT5490P', name='Project (MKT)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5354', name='Managing Creativity and Innovation (Sustainable Tourism)',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5352', name='Understanding Transnational Corporations', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT4028', name='Ethics and Business', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5355', name='Managing Careers in the 21st Century', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT4117', name='Employment Law in Action: Observing the Employment Tribunal',
                          school=business, level=4, credits=15)
    Module.objects.create(id='MGT5399', name='Digital Technology and Strategic Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5482P', name='Management Project (MVLS Pathway)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5373', name='Marketing and Emerging Markets', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5435', name='Services Marketing (Semester 1)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5317', name='International Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5349', name='Managing and Leading People in International Contexts', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT5351', name='Research Skills for Managers', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5383', name='Managing Innovation and Technology Transfer', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT1023', name='Principles of Management', school=business, level=1, credits=10)
    Module.objects.create(id='MGT4002P', name='Business and Management Dissertation', school=business, level=4,
                          credits=30)
    Module.objects.create(id='MGT4104', name='Performance Improvement through Systems Thinking and Simulation',
                          school=business, level=4, credits=15)
    Module.objects.create(id='MGT5409', name='Fintech Ecosystem Study Trip', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5419', name='User Experience (UX) Design', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5465', name='Data Driven Leadership Skills for Practitioners', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT4051', name='Management in the Voluntary and Community Sector', school=business,
                          level=4, credits=15)
    Module.objects.create(id='MGT5032', name='International Human Resource Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5274', name='Marketing Management (ASBS)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5054', name='Managing Diversity In Organisations', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5297', name='Research Master Class', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5445', name='Technology Strategy and Patent Analysis', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5184', name='Global Consumer Behaviour', school=business, level=5, credits=10)
    Module.objects.create(id='MGT4013', name='Marketing Communications', school=business, level=4, credits=30)
    Module.objects.create(id='MGT5035', name='International Brand Management', school=business, level=5, credits=10)
    Module.objects.create(id='MGT4114', name='Building and Managing Technology Based International New Ventures',
                          school=business, level=4, credits=15)
    Module.objects.create(id='MGT5426', name='Management Science for Business Decision-Making', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT5056', name='Multinational Management', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5429', name='Brand Management (Summer)', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5173', name='Marketing Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT4091', name='Integrating Business and Management in Practice', school=business,
                          level=4, credits=15)
    Module.objects.create(id='MGT4111', name='International Export Marketing, Strategy & Process', school=business,
                          level=4, credits=15)
    Module.objects.create(id='MGT5466', name='Leading Successful Teams', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5467', name='Operations Management: Theory to Practice', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5447', name='Social Media Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5485', name='Introduction to Business Analytics', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5495', name='Management in the Social Economy', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5431', name='Digital Marketing (Semester 1)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5488', name='Responsible Leadership', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5411', name='Brand Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5270', name='Contemporary Issues in Human Resource Management: Theory and Practice',
                          school=business, level=5, credits=20)
    Module.objects.create(id='MGT5275', name='Operations Management', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5264', name='Management Issues and Controversies', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5472', name='Cultural Change Management in Organisations', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT4066', name='Contemporary Employment Relations', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5478P', name='Management Dissertation (MST Pathway)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5417', name='Retail Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5473',
                          name='Advanced JEDI: Glasgow-Radboud Virtual International Collaborative Consultancy',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT4054', name='Contemporary Issues in Consumer Behaviour', school=business, level=4,
                          credits=15)
    Module.objects.create(id='MGT4107', name='Futures in Leadership', school=business, level=4, credits=15)
    Module.objects.create(id='MGT4058', name='Social and Community Entrepreneurship', school=business, level=4,
                          credits=15)
    Module.objects.create(id='MGT5474P', name='Management Dissertation (Engineering Pathway)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5343', name='Human Resource Development', school=business, level=5, credits=20)
    Module.objects.create(id='MGT1005', name='Introduction to Management', school=business, level=1, credits=20)
    Module.objects.create(id='MGT5396', name='Business Models for Innovation in Finance', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5068', name='Professional and Entrepreneurial Practice', school=business, level=5,
                          credits=20)
    Module.objects.create(id='MGT5412', name='Consumer Behaviour', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5375', name='Coaching in Organisations', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5228', name='International Services Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT4053', name='New Ventures Challenge', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5479P', name='Management Project (MST Pathway)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5357P', name='Project (EBG)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5492', name='Data Management and Engineering', school=business, level=5, credits=20)
    Module.objects.create(id='MGT2014', name='Entrepreneurship', school=business, level=2, credits=10)
    Module.objects.create(id='MGT1022', name='Organisational Behaviour', school=business, level=1, credits=10)
    Module.objects.create(id='MGT5263', name='Entrepreneurial Finance for SMEs', school=business, level=5, credits=10)
    Module.objects.create(id='MGT2012', name='Service and Operations Management', school=business, level=2, credits=10)
    Module.objects.create(id='MGT5480P', name='Management Dissertation (MVLS Pathway)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5498', name='Introduction to Business Analytics', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5179', name='Global Business Environment', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5174', name='Research Methods in International Business', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5494', name='Text Mining for Business', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5329', name='Strategic Marketing Consultancy', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5397', name='Digital Entrepreneurship', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5452P', name='Dissertation (MGT)', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5206', name='Digital Marketing Strategy', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5427', name='CPD Change Management', school=business, level=5, credits=0)
    Module.objects.create(id='MGT5272', name='Contemporary Issues in Human Resource Management', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT6001', name='Project Management - Turning Theory into Practice', school=business,
                          level=6, credits=10)
    Module.objects.create(id='MGT5443', name='Entrepreneural Finance (Continuous Professional Development)',
                          school=business, level=5, credits=0)
    Module.objects.create(id='MGT5315', name='Project Management (Creative Industries and Cultural Policy)',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT4115', name='New Product Development and Innovation', school=business, level=4,
                          credits=15)
    Module.objects.create(id='MGT4093', name='Entrepreneurial Selling', school=business, level=4, credits=15)
    Module.objects.create(id='MGT4099', name='Strategic Alliances and Joint Ventures', school=business, level=4,
                          credits=15)
    Module.objects.create(id='MGT3024', name='Marketing Campaign Development: Research and Tactics', school=business,
                          level=3, credits=20)
    Module.objects.create(id='MGT5321', name='The Eurozone Political Economy', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5342', name='Developing Skills for Business Leadership', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT2010', name='Business Decision Analysis', school=business, level=2, credits=10)
    Module.objects.create(id='MGT5418', name='Services Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5425',
                          name='Organisational Security: the challenges of managing intentional and accidental threat Factors',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5303', name='Managing Strategic Change', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5422', name='Data Driven Leadership Skills', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5180', name='International Entrepreneurship and Innovation', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5468', name='Project Management for Practitioners', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5499', name='Operations Management: Theory to Practice', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT4023', name='Strategic Management', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5178P', name='IB Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5181', name='International Management Solutions', school=business, level=5, credits=20)
    Module.objects.create(id='MGT4005', name='Financial Management', school=business, level=4, credits=30)
    Module.objects.create(id='MGT5346', name='International Perspectives on Employment Relations', school=business,
                          level=5, credits=10)
    Module.objects.create(id='MGT1021', name='Introduction to Marketing', school=business, level=1, credits=10)
    Module.objects.create(id='MGT5043', name='Strategic Marketing Management', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5410', name='Systems Thinking and Simulation for Performance Improvement',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT4100', name='Supply Chain Management', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5464', name='A Practical Approach to Change Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5265', name='Delivering Performance', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5348', name='Managing Diversity and Inclusion', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5330P', name='F&M Dissertation', school=business, level=5, credits=60)
    Module.objects.create(id='MGT5176', name='Business Planning', school=business, level=5, credits=20)
    Module.objects.create(id='MGT6002', name='Project Management - Turning Theory into Practice (Run II)',
                          school=business, level=6, credits=10)
    Module.objects.create(id='MGT1003', name='Entrepreneurship: New Venture Creation', school=business, level=1,
                          credits=20)
    Module.objects.create(id='MGT5296', name='Management Research Methods', school=business, level=5, credits=30)
    Module.objects.create(id='MGT5416', name='Marketing Research & Analytics', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5441P', name='Marketing Dissertation (Semester 2)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT4116', name='Democratising the Economy', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5266', name='Digital Transformation: New Models of Business', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5063', name='Organisational Behaviour', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5493', name='Programming in Business Analytics', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5497', name='A Practical Approach to Change Management', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT3003', name='Project Management', school=business, level=3, credits=20)
    Module.objects.create(id='MGT5219', name='Marketing Management (Engineering)', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5446', name='Marketing: Ethics, Consumption and Technology', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5476P', name='Management Dissertation (IMDI Pathway)', school=business, level=5,
                          credits=60)
    Module.objects.create(id='MGT5420', name='Change Management', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5406', name='International Business and Entreprenership in Emerging Economies',
                          school=business, level=5, credits=10)
    Module.objects.create(id='MGT5328', name='Retail Marketing', school=business, level=5, credits=10)
    Module.objects.create(id='MGT5037', name='Digital Marketing Strategy (Specialist)', school=business, level=5,
                          credits=10)
    Module.objects.create(id='MGT5131', name='MBA Summer School (3)', school=business, level=5, credits=20)
    Module.objects.create(id='MGT4057', name='Services Marketing', school=business, level=4, credits=15)
    Module.objects.create(id='MGT5268', name='Strategic Management', school=business, level=5, credits=20)
    Module.objects.create(id='MGT5489P', name='Dissertation (MKT)', school=business, level=5, credits=60)
    Module.objects.create(id='SIT5001', name='Professional Practice 5N', school=business, level=5, credits=20)
    Module.objects.create(id='SIT5004', name='Professional Practice 5S', school=business, level=5, credits=20)
    Module.objects.create(id='SIT2001', name='Marketing E1N', school=business, level=2, credits=10)

    # MVLS College Services (41 modules)
    Module.objects.create(id='BIOL5443', name='Biomedical Image Analysis with applications using AI/ML', school=mvls,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5472', name='Developing Robust Bioinformatics Software', school=mvls, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5412', name='Digital Media', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5420', name='In Vivo Research Skills', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5356', name='Principles of Immunology', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5198', name='Diagnostic technologies and devices', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5416', name='Science Journalism', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5399', name='Introduction to Medical Communications', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5359', name='World Changers: Precision Medicine Seminar Series', school=mvls, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5357', name='Precision Diagonostics and Therapeutics', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5456', name='Medical Ethics and Regulations', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5451', name='Clinical Trials Management', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5455', name='Introduction to Clinical Trial Types and Design', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5450', name='Industrial Fermentation', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5459', name='Science in Public Spaces', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5469', name='Precision Genomics', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5445', name='Habitat creation, monitoring and assessment', school=mvls, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5470', name='One Health & Food Security', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5358', name='Research Skills for Precision Medicine', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5414P', name='Science Communications Project', school=mvls, level=5, credits=60)
    Module.objects.create(id='BIOL5424', name='Climate change and One Health', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5442', name='Science in Public Spaces', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5411', name='Scientific Writing for Medical Communications', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5458', name='Interdisciplinary Learning in Public Spaces', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5395P', name='Laboratory Management Dissertation', school=mvls, level=5, credits=60)
    Module.objects.create(id='BIOL5466', name='Fundamentals of Experimental Design and Data Analysis', school=mvls,
                          level=5, credits=10)
    Module.objects.create(id='BIOL5452P', name='Clinical Trials Research Project', school=mvls, level=5, credits=60)
    Module.objects.create(id='BIOL5454', name='How to Conduct and Monitor a Clinical Trial', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5439', name='Generative AI in Scientific Communications', school=mvls, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5444', name='Human Fungal Pathogens', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5453', name='Communication and Dissemination of Clinical Trial Findings', school=mvls,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5432', name='Emerging Infectious Diseases', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5434', name='Themes in One Health', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5355', name='Inflammatory Disease', school=mvls, level=5, credits=20)
    Module.objects.create(id='BIOL5448', name='Product Life Cycle Management', school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5199', name='Current trends and challenges in biomedical research and health',
                          school=mvls, level=5, credits=10)
    Module.objects.create(id='BIOL5433',
                          name='Epidemiology, Prevention and Control of Infectious Diseases - A One Health Approach',
                          school=mvls, level=5, credits=20)
    Module.objects.create(id='MED5608P', name='Precision Medicine Research Project', school=mvls, level=5, credits=60)
    Module.objects.create(id='MED5501P', name='One Health: Dissertation', school=mvls, level=5, credits=60)
    Module.objects.create(id='PSYCH2016', name='Applied data skills for processing and presenting data', school=mvls,
                          level=2, credits=10)
    Module.objects.create(id='VETMED5067', name='Zoonotic Diseases', school=mvls, level=5, credits=20)

    # School of Biodiversity One Health Vet Med (108 modules)
    Module.objects.create(id='BIOL5431', name='Conservation in Practice', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL5325', name='Economic tools for conservation', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL5132', name='Biodiversity Informatics', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL4050', name='Freshwater Ecology & Evolution (with Field Course) 4D option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL4288',
                          name='Ecology & Conservation of African Ecosystems (with Field Course) 4Y option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL4287', name='Fisheries, Aquaculture and Marine Conservation 4C option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='VETMED5053', name='Zoonotic Diseases', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL4005', name='Applying Ecology (Conservation and Management of Populations) 4A option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5446P', name='MSc ACS Research Project', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL4308',
                          name='Coastal Conservation: Hebridean Landscapes, Culture and Ecology (Field Course) 4Y option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5211', name='Quantitative Methods in Food Security', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5326', name='Core skills in epidemiology of infectious disease', school=veterinary,
                          level=5, credits=20)
    Module.objects.create(id='BIOL4008', name='Behavioural Ecology 4B option', school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5186P', name='MRes EEB Research Project 1', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL4303', name='Movement and Landscape Ecology 4B option', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5426', name='Animal Identification', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL5187P', name='MRes EEB Research Project 2', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL4294', name='Animal Ecophysiology 4Y option', school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5212', name='Global Animal Production', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL4285', name='Animal Biology Core Skills 4X core', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4126', name='Tropical Marine Biology (with Field Course) 4Y option',
                          school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5327', name='Epidemiology of Antimicrobial Resistance', school=veterinary, level=5,
                          credits=15)
    Module.objects.create(id='BIOL5134P', name='MSc QMBCE Research Project', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL5315', name='Integrated Infectious Disease Control', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4216', name='Disease Ecology 4C option', school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL4138', name='Zoology 3B', school=veterinary, level=4, credits=60)
    Module.objects.create(id='BIOL4212', name='Species Diversification and Conservation 4A option', school=veterinary,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4298', name='Business in the Biosciences 4Y option', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5130', name='Conservation Genetics', school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL5337P', name='MSc CMAE Research Project', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL5335', name='An Introduction to Global Food Security', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4183', name='Tropical Ecology 4Y option', school=veterinary, level=4, credits=20)
    Module.objects.create(id='BIOL5250', name='Geographic Information Systems for Ecologists', school=veterinary,
                          level=5, credits=10)
    Module.objects.create(id='BIOL5126', name='Key Research Skills', school=veterinary, level=5, credits=40)
    Module.objects.create(id='BIOL5423', name='Animal Ethics and Law', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL5115', name='Animal Welfare Science', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL4042', name='Evolution (Pattern and Process) 4Y option', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5427', name='Dynamics of Populations', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL4137', name='Zoology 3A', school=veterinary, level=4, credits=60)
    Module.objects.create(id='BIOL5429', name='Modern Inference Methods for Ecology', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='BIOL2041', name='Animal Biology, Evolution and Ecology 2', school=veterinary, level=2,
                          credits=30)
    Module.objects.create(id='BIOL5437', name='Principles of Conservation Ecology', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5430', name='Spatial Ecology', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL4302P', name='Study Abroad Work Based Learning (UG Life Sciences)', school=veterinary,
                          level=4, credits=60)
    Module.objects.create(id='BIOL4066', name='Marine & Freshwater Biology 3B', school=veterinary, level=4, credits=60)
    Module.objects.create(id='BIOL5123', name='Infectious Disease Ecology and the Dynamics of Emerging Disease',
                          school=veterinary, level=5, credits=10)
    Module.objects.create(id='BIOL5334', name='Antimicrobial Resistance: A One Health Approach', school=veterinary,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5447P', name='AWSEL Independent Project', school=veterinary, level=5, credits=60)
    Module.objects.create(id='BIOL5428', name='Fundamentals of programming and data generating processes',
                          school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL5119', name='Molecular Epidemiology and Phylodynamics', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='BIOL4065', name='Marine & Freshwater Biology 3A', school=veterinary, level=4, credits=60)
    Module.objects.create(id='BIOL1010', name='Environmental Biology 1', school=veterinary, level=1, credits=20)
    Module.objects.create(id='BIOL5435', name='One Health - From Research to Policy', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5422', name='Assessment of Animal Well-Being', school=veterinary, level=5, credits=20)
    Module.objects.create(id='BIOL4129P', name='Vacation Research Project In Biology', school=veterinary, level=4,
                          credits=10)
    Module.objects.create(id='BIOL5333', name='Care & Enrichment of Captive Animals', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5371', name='Statistics and Data Analysis for Bioinformatics', school=veterinary,
                          level=5, credits=10)
    Module.objects.create(id='VETSCI2011', name='Fundamental Topics in Veterinary Anatomy and Nutrition',
                          school=veterinary, level=2, credits=30)
    Module.objects.create(id='VETSCI5023P',
                          name='Epidemiology of Infectious Diseases and Antimicrobial Resistance: Project',
                          school=veterinary, level=5, credits=60)
    Module.objects.create(id='VETSCI5038', name='Nutrition and Health', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETSCI3009', name='Molecular Biology of Cancer', school=veterinary, level=3, credits=30)
    Module.objects.create(id='VETSCI5032', name='Digestive anatomy and physiology', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='VETSCI3011', name='Veterinary Diagnostic Strategies 3', school=veterinary, level=3,
                          credits=30)
    Module.objects.create(id='VETSCI5037', name='Feed processing (ruminants)', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETSCI5028P', name='Dissertation in animal nutrition', school=veterinary, level=5,
                          credits=60)
    Module.objects.create(id='VETSCI4023', name='Animal Welfare and Conservation 4', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='VETSCI5022', name='Societal aspects of AMR', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETSCI5031', name='Current topics in animal nutrition', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='VETSCI2008', name='Research Skills 2', school=veterinary, level=2, credits=20)
    Module.objects.create(id='VETSCI5039', name='Nutrition biochemistry and metabolism', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='VETSCI5021P', name='MSci Research Project 5', school=veterinary, level=5, credits=60)
    Module.objects.create(id='VETSCI5035', name='Feed industry', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETSCI3012', name='Hormones and Behaviour', school=veterinary, level=3, credits=30)
    Module.objects.create(id='VETSCI5033', name='Equine nutrition', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETSCI4024', name='Veterinary Public Health & Epidemiology', school=veterinary, level=4,
                          credits=20)
    Module.objects.create(id='VETSCI2009', name='Veterinary Body Systems 2', school=veterinary, level=2, credits=30)
    Module.objects.create(id='VETSCI5019', name='Work Placement Year in Veterinary Biosciences', school=veterinary,
                          level=5, credits=120)
    Module.objects.create(id='VETSCI5029', name='Applied nutrition and rationing (monogastrics)', school=veterinary,
                          level=5, credits=10)
    Module.objects.create(id='VETSCI3004', name='The Principles of Infection and Immunity 3', school=veterinary,
                          level=3, credits=30)
    Module.objects.create(id='VETSCI5034', name='Feed composition and evaluation', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='VETSCI1006', name='Digestive Physiology and Metabolism', school=veterinary, level=1,
                          credits=20)
    Module.objects.create(id='VETSCI4025', name='Professional Skills 4', school=veterinary, level=4, credits=20)
    Module.objects.create(id='VETSCI5024', name='Genetic and Genomic Aspects of Antimicrobial Resistance',
                          school=veterinary, level=5, credits=15)
    Module.objects.create(id='VETSCI5041', name='Small animal and exotics nutrition', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='VETSCI5030', name='Applied nutrition and rationing (ruminants)', school=veterinary,
                          level=5, credits=10)
    Module.objects.create(id='VETSCI5036', name='Feed processing (monogastrics)', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='VETSCI2010', name='Applied Animal Management-2', school=veterinary, level=2, credits=40)
    Module.objects.create(id='VETSCI4018P', name='Veterinary Biosciences Project 4', school=veterinary, level=4,
                          credits=60)
    Module.objects.create(id='VETSCI1005', name='Comparative Veterinary Anatomy 1', school=veterinary, level=1,
                          credits=20)
    Module.objects.create(id='VETMED4023', name='Research and Evidence Based Veterinary Nursing', school=veterinary,
                          level=4, credits=20)
    Module.objects.create(id='VETMED5059', name='Research Design and Dissemination', school=veterinary, level=5,
                          credits=20)
    Module.objects.create(id='VETMED5054', name='Animal and Veterinary Ethics', school=veterinary, level=5, credits=20)
    Module.objects.create(id='VETMED5066', name='One Health Economics', school=veterinary, level=5, credits=10)
    Module.objects.create(id='VETMED1022', name='Bachelor of Veterinary Medicine and Surgery 1', school=veterinary,
                          level=1, credits=120)
    Module.objects.create(id='VETMED3022', name='Bachelor of Veterinary Medicine and Surgery 3', school=veterinary,
                          level=3, credits=120)
    Module.objects.create(id='VETMED2023', name='Bachelor of Veterinary Medicine and Surgery 2', school=veterinary,
                          level=2, credits=0)
    Module.objects.create(id='VETMED5062', name='Production of Food from Animals', school=veterinary, level=5,
                          credits=10)
    Module.objects.create(id='VETMED4019', name='Bachelor of Veterinary Medicine and Surgery 4', school=veterinary,
                          level=4, credits=120)
    Module.objects.create(id='VETMED5055', name='Quality Improvement in Veterinary Practice', school=veterinary,
                          level=5, credits=20)
    Module.objects.create(id='VETMED5042', name='BVMS5 Professional Phase', school=veterinary, level=5, credits=180)
    Module.objects.create(id='VETMED2022', name='Bachelor of Veterinary Medicine and Surgery 2', school=veterinary,
                          level=2, credits=120)
    Module.objects.create(id='VETMED5043', name='BVMS5 Professional Phase', school=veterinary, level=5, credits=0)
    Module.objects.create(id='VETMED5058', name='Introduction to Veterinary Nursing Business Management',
                          school=veterinary, level=5, credits=20)
    Module.objects.create(id='VETMED5057', name='Teaching and Assessment in Veterinary Education', school=veterinary,
                          level=5, credits=20)
    Module.objects.create(id='VETMED4021', name='Bachelor of Veterinary Medicine and Surgery 4', school=veterinary,
                          level=4, credits=0)
    Module.objects.create(id='VETMED1030', name='VetStart Pathway', school=veterinary, level=1, credits=40)
    Module.objects.create(id='VETMED5060P', name='MSc Advanced Practice in Veterinary Nursing: Dissertation',
                          school=veterinary, level=5, credits=60)
    Module.objects.create(id='VETMED5056', name='Developing Evidence-Based Practice Through Reflection',
                          school=veterinary, level=5, credits=20)

    # School of Cancer Sciences (18 modules)
    Module.objects.create(id='BIOL5419', name='Cancer Drug Discovery and Development', school=cancer, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5340', name='Core Skills in Cancer Research', school=cancer, level=5, credits=10)
    Module.objects.create(id='BIOL5417', name='Cancer Immunology and Immunotherapy', school=cancer, level=5, credits=10)
    Module.objects.create(id='BIOL5400', name='Project Design and Data Analysis in Cancer Research', school=cancer,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5317P', name='MSc Bioscience Research Project (Cancer Research & Precision Oncology)',
                          school=cancer, level=5, credits=60)
    Module.objects.create(id='BIOL5418', name='Precision Oncology', school=cancer, level=5, credits=10)
    Module.objects.create(id='BIOL5380', name='The Cancer Microenvironment and Biomarkers', school=cancer, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4023', name='Cancer 4B option', school=cancer, level=4, credits=20)
    Module.objects.create(id='BIOL5339', name='Cancer Evolution', school=cancer, level=5, credits=20)
    Module.objects.create(id='BIOL5341', name='Hallmarks of Cancer', school=cancer, level=5, credits=20)
    Module.objects.create(id='BIOL5338', name='Cancer Research Distinguished Seminar Series', school=cancer, level=5,
                          credits=10)
    Module.objects.create(id='MED5599', name='Research Methods for Palliative Care', school=cancer, level=5, credits=20)
    Module.objects.create(id='MED5597', name='Clinical Leadership and Effectiveness', school=cancer, level=5,
                          credits=20)
    Module.objects.create(id='MED5598P', name='Palliative Care Dissertation', school=cancer, level=5, credits=60)
    Module.objects.create(id='MED5600', name='Holistic Management in Palliative Care', school=cancer, level=5,
                          credits=20)
    Module.objects.create(id='MED5601', name='Symptom Control', school=cancer, level=5, credits=20)
    Module.objects.create(id='MED5602', name='Themes in Palliative Care', school=cancer, level=5, credits=20)
    Module.objects.create(id='MED5596', name='Advanced Communication and Ethics', school=cancer, level=5, credits=20)

    # School of Cardiovascular and Metabolic (75 modules)
    Module.objects.create(id='BIOL4268', name='Functional Foods 4D option', school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL4273', name='Monitoring Sports Specific Performance 4Y option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4305', name='Physiological Disorders: Mechanisms and Treatment Challenges 4Y Option',
                          school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL4108', name='Sport and Exercise Science 3B', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4032', name='CNS Neurotransmitters and Drug Development 4Y option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4190', name='Bio-Imaging in the Life Sciences 4D option', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4036', name='Nutrition in Health & Disease Prevention 4Y option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4026', name='Advanced Exercise Physiology 4C option', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4249P', name='Life Sciences Internship Honours Project', school=cardio, level=4,
                          credits=40)
    Module.objects.create(id='BIOL4228', name='Human Biology and Physiology 3A', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4182', name='Core Skills in Pharmacology (Drug Discovery & Development) 4X core',
                          school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL4247P', name='Life Sciences Dissertation Honours Project', school=cardio, level=4,
                          credits=40)
    Module.objects.create(id='BIOL4225', name='Current Topics in Human Biology and Physiology 4X core', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4289', name='Cancer Immunopharmacology 4B option', school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL4043', name='Sports and Exercise Nutrition 4B option', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4097', name='Physical Activity and Public Health 4Y option', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4107', name='Sport and Exercise Science 3A', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4236', name='Pharmacology 3A', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4214', name='Performance Enhancing Techniques 4D option', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4284', name='Personalised Medicine & Clinical Trials 4C option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4098', name='Cardiometabolic Health & Physical Activity 4B option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4025', name='Cardiovascular Science 4A option', school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL5374P', name='Life Sciences Internship MSci Project', school=cardio, level=5,
                          credits=40)
    Module.objects.create(id='BIOL4307', name='Essential Skills for Working in Sport and Exercise 4A Option',
                          school=cardio, level=4, credits=20)
    Module.objects.create(id='BIOL5288P', name='Life Sciences Dissertation MSci Project', school=cardio, level=5,
                          credits=40)
    Module.objects.create(id='BIOL5343', name='Assessment of Vascular Function', school=cardio, level=5, credits=10)
    Module.objects.create(id='BIOL5261', name='Bio-Imaging for Research Scientists', school=cardio, level=5, credits=20)
    Module.objects.create(id='BIOL4237', name='Pharmacology 3B', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4024', name='Cardiovascular Pharmacology and Therapeutics 4A option', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4229', name='Human Biology and Physiology 3B', school=cardio, level=4, credits=60)
    Module.objects.create(id='BIOL4215', name='Physiological Determinants of Performance 4X core', school=cardio,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4267', name='Energy Balance (Impact of Lifestyle) 4X core', school=cardio, level=4,
                          credits=20)
    Module.objects.create(id='BIOL2043', name='Human Biological Sciences 2', school=cardio, level=2, credits=30)
    Module.objects.create(id='MED5344',
                          name='Physical Activity for Health: From Research to Public Health Interventions',
                          school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5666', name='Technology and Analytics in Sport and Exercise', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5539', name='Clinical and Research Laboratory Skills', school=cardio, level=5,
                          credits=10)
    Module.objects.create(id='MED5352', name='Cellular and Molecular Exercise Physiology', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5366', name='Applied Statistics for Clinical and Translational research',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5667', name='Technology and Analytics in Sport and Exercise', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5361', name='Factors Influencing Performance', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5544', name='Imaging in cardiovascular diseases: techniques and applications',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5343', name='Physical Activity and Health: Epidemiology, Mechanisms and Interventions',
                          school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5470', name='Nutritional Aids in Sport and Exercise', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5353', name='Physical Activity and Health: Biological Mechanisms', school=cardio,
                          level=5, credits=20)
    Module.objects.create(id='MED5368P', name='Research Dissertation', school=cardio, level=5, credits=60)
    Module.objects.create(id='MED5383',
                          name='Topics In Therapeutics - General topics, Cardiovascular and Diabetes Drugs',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5574', name='Lifestyle intervention in Cardiometabolic disease', school=cardio,
                          level=5, credits=10)
    Module.objects.create(id='MED5212P', name='MSc Sport and Exercise Science & Medicine - Dissertation', school=cardio,
                          level=5, credits=60)
    Module.objects.create(id='MED5336', name='Clinical Trials : Principles and Methods', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5381',
                          name='Pharmacogenomics & Molecular Medicine - Fundamentals of Molecular Medicine',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5105P', name='Clinical Pharmacology Dissertation', school=cardio, level=5, credits=60)
    Module.objects.create(id='MED5340', name='Exercise Prescription', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5382', name='Applied Pharmacogenomics & Molecular Medicine', school=cardio, level=5,
                          credits=10)
    Module.objects.create(id='MED5543', name='Epidemiology, outcomes and therapy of heart failure', school=cardio,
                          level=5, credits=10)
    Module.objects.create(id='MED5469', name='Nutritional Aids in Sport and Exercise', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5349', name='Sports Injuries: Prevention and Rehabilitation', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5339', name='Sports Injuries for Doctors and Physiotherapists', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5348', name='Factors Influencing Performance', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5362', name='Sports Injuries: Scientific Basis of Prevention and Rehabilitation',
                          school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5356', name='Medical Statistics', school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5360',
                          name='Physical Activity and Health: Public Health, Policy and Behavioural Change',
                          school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5350', name='Working with Elite Athletes', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5346', name='Physiological & Exercise Testing - Aerobic Fitness and Physical Activity',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5538', name='Evidence-Based Biomedical Research Methods and Statistics', school=cardio,
                          level=5, credits=20)
    Module.objects.create(id='MED5345', name='Human physiological & metabolic assessment', school=cardio, level=5,
                          credits=10)
    Module.objects.create(id='MED5542', name='Basic Science of Cardiovascular Disease: tissue cells and signalling',
                          school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5384', name='Topics in Therapeutics - Commonly used drugs', school=cardio, level=5,
                          credits=10)
    Module.objects.create(id='MED5363', name='Working with Elite Athletes', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5508P', name='MSc Sport and Exercise Science & Medicine - Dissertation', school=cardio,
                          level=5, credits=60)
    Module.objects.create(id='MED5111P', name='Cv Sciences Dissertation', school=cardio, level=5, credits=60)
    Module.objects.create(id='MED5668', name='Evidence-Based Biomedical Research Methods and Statistics', school=cardio,
                          level=5, credits=20)
    Module.objects.create(id='MED5347', name='Physiological & Exercise Testing - Strength, power and intensity domains',
                          school=cardio, level=5, credits=10)
    Module.objects.create(id='MED5355', name='Exercise Prescription', school=cardio, level=5, credits=20)
    Module.objects.create(id='MED5354', name='Sports Injuries for Doctors & Physiotherapists', school=cardio, level=5,
                          credits=20)
    Module.objects.create(id='MED5385', name='Clinical Aspects of CVD: patients and populations', school=cardio,
                          level=5, credits=20)

    # School of Chemistry (98 modules)
    Module.objects.create(id='CHEM5078', name='Biomolecular Interactions', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM5071', name='Frontiers of Catalysis', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM2001', name='Chemistry 2X', school=chemistry, level=2, credits=30)
    Module.objects.create(id='CHEM4011', name='Medicinal Chemistry 4H', school=chemistry, level=4, credits=20)
    Module.objects.create(id='CHEM5023', name='Physical Chemistry 4M (B)', school=chemistry, level=5, credits=15)
    Module.objects.create(id='CHEM5020', name='Medicinal Chemistry 4M', school=chemistry, level=5, credits=15)
    Module.objects.create(id='CHEM2005', name='Chemistry 2X (Half Course)', school=chemistry, level=2, credits=15)
    Module.objects.create(id='CHEM4014', name='Physical Chemistry 4H', school=chemistry, level=4, credits=20)
    Module.objects.create(id='CHEM5047', name='Organic Chemistry 5M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4024', name='Chemical Physics MSci: Work Placement Year', school=chemistry, level=4,
                          credits=120)
    Module.objects.create(id='CHEM5068', name='Catalyst Activation and Deactivation', school=chemistry, level=5,
                          credits=10)
    Module.objects.create(id='CHEM5126', name='Practical skills: Testing', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM5043P', name='Chemistry Project 4M for Chemical Physics non-WP', school=chemistry,
                          level=5, credits=60)
    Module.objects.create(id='CHEM5123P', name='Chemical Biology Research Project', school=chemistry, level=5,
                          credits=60)
    Module.objects.create(id='CHEM5021', name='Organic Chemistry 4M', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM4017P', name='Advanced Research Project (Visiting)(Sem 2)', school=chemistry, level=4,
                          credits=60)
    Module.objects.create(id='CHEM5079', name='Biopolymer Chemistry and Synthesis', school=chemistry, level=5,
                          credits=10)
    Module.objects.create(id='CHEM5051', name='Frontiers of Chemistry 5M', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM2017', name='Chemistry 2Y single', school=chemistry, level=2, credits=30)
    Module.objects.create(id='CHEM5070', name='Catalyst structure and function from bulk to surface.', school=chemistry,
                          level=5, credits=10)
    Module.objects.create(id='CHEM3012', name='Organic Chemistry 3', school=chemistry, level=3, credits=40)
    Module.objects.create(id='CHEM4040', name='Summer research project (Chemistry)', school=chemistry, level=4,
                          credits=24)
    Module.objects.create(id='CHEM5080', name='Chemical Research Skills', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM5006', name='Chemistry Problems 4M (B)', school=chemistry, level=5, credits=15)
    Module.objects.create(id='CHEM4013', name='Organic Chemistry 4H (Half)', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM5058', name='Surface Chemistry: Structure and Reactivity 4M', school=chemistry,
                          level=5, credits=10)
    Module.objects.create(id='CHEM4048', name='Materials Chemistry Project 4H', school=chemistry, level=4, credits=40)
    Module.objects.create(id='CHEM5076', name='Chemistry Special Topics 5M', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM3014', name='Physical Chemistry 3', school=chemistry, level=3, credits=40)
    Module.objects.create(id='CHEM5054', name='Materials Characterisation 4M', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4028', name='Chemistry With Medicinal Chemistry MSci:Work Placement Year',
                          school=chemistry, level=4, credits=120)
    Module.objects.create(id='CHEM5007', name='Chemistry Problems 4M (C)', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4016P', name='Advanced Research Project (Visiting)(Sem 1)', school=chemistry, level=4,
                          credits=60)
    Module.objects.create(id='CHEM5048', name='Physical Chemistry 4M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM3027', name='Organic Chemistry for Chemical Studies', school=chemistry, level=3,
                          credits=20)
    Module.objects.create(id='CHEM4010', name='Inorganic Chemistry 4H (Half)', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM5005', name='Chemistry Problems 4M (A)', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM4025', name='Chemistry MSci: Work Placement Year', school=chemistry, level=4,
                          credits=120)
    Module.objects.create(id='CHEM2016', name='Chemistry 2X single', school=chemistry, level=2, credits=30)
    Module.objects.create(id='CHEM4015', name='Physical Chemistry 4H (Half)', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM2007', name='Organic Chemistry I for Visiting Students', school=chemistry, level=2,
                          credits=20)
    Module.objects.create(id='CHEM4001', name='Chemistry Special Topics 4H', school=chemistry, level=4, credits=20)
    Module.objects.create(id='CHEM4002', name='Chemistry Special Topics 4H Half', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM5050', name='Research Skills', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM3011', name='Inorganic Chemistry 3 (Half)', school=chemistry, level=3, credits=20)
    Module.objects.create(id='CHEM3025', name='Chemical Studies Project', school=chemistry, level=3, credits=20)
    Module.objects.create(id='CHEM5049', name='Physical Chemistry 5M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4044', name='Materials Chemistry MSci: Work Placement Year', school=chemistry,
                          level=4, credits=120)
    Module.objects.create(id='CHEM5052', name='Advanced Materials Characterisation 5M', school=chemistry, level=5,
                          credits=20)
    Module.objects.create(id='CHEM5074', name='Preparation of Catalytic Materials', school=chemistry, level=5,
                          credits=10)
    Module.objects.create(id='CHEM5008P', name='Chemistry Project for MSc', school=chemistry, level=5, credits=60)
    Module.objects.create(id='CHEM2002', name='Chemistry 2Y', school=chemistry, level=2, credits=30)
    Module.objects.create(id='CHEM5046', name='Organic Chemistry 4M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM1004', name='Chemistry 1 (Half Course)', school=chemistry, level=1, credits=20)
    Module.objects.create(id='CHEM5127P', name='Materials Chemistry Project 4M', school=chemistry, level=5, credits=40)
    Module.objects.create(id='CHEM4003P', name='Chemistry Project 4H', school=chemistry, level=4, credits=40)
    Module.objects.create(id='CHEM5016', name='Frontiers Of Chemistry 3M', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM5019', name='Inorganic Chemistry 4M (C)', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM3026', name='Inorganic Chemistry for Chemical Studies', school=chemistry, level=3,
                          credits=20)
    Module.objects.create(id='CHEM4042', name='Materials Characterisation 4H', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM5073', name='Industrial Catalysis Project', school=chemistry, level=5, credits=60)
    Module.objects.create(id='CHEM5124', name='Practical skills: Deactivation', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM3015', name='Physical Chemistry 3 (Half)', school=chemistry, level=3, credits=20)
    Module.objects.create(id='CHEM5060', name='Chemistry of the f-Block 4M', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM5077', name='Bioconjugation Chemistry', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM1002', name='Science Fundamentals-1X', school=chemistry, level=1, credits=20)
    Module.objects.create(id='CHEM1003', name='Science Fundamentals-1Y', school=chemistry, level=1, credits=20)
    Module.objects.create(id='CHEM5055', name='Nanostructured Materials 4M', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4047', name='Summer Research Project (Chemistry)', school=chemistry, level=4,
                          credits=25)
    Module.objects.create(id='CHEM3013', name='Organic Chemistry 3 (Half)', school=chemistry, level=3, credits=20)
    Module.objects.create(id='CHEM5125', name='Practical skills: Preparation and Characterisation', school=chemistry,
                          level=5, credits=20)
    Module.objects.create(id='CHEM4009', name='Inorganic Chemistry 4H', school=chemistry, level=4, credits=20)
    Module.objects.create(id='CHEM3010', name='Inorganic Chemistry 3', school=chemistry, level=3, credits=40)
    Module.objects.create(id='CHEM2015', name='Organic chemistry II for visiting students', school=chemistry, level=2,
                          credits=20)
    Module.objects.create(id='CHEM5045', name='Inorganic Chemistry 5M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM5010P', name='Chemistry Project 5M', school=chemistry, level=5, credits=30)
    Module.objects.create(id='CHEM5009P', name='Chemistry Project 4M (A)', school=chemistry, level=5, credits=40)
    Module.objects.create(id='CHEM5003', name='Chemistry Special Topics 4M (A)', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM4045', name='Nanostructured Materials 4H', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM4029', name='Chemistry With Medicinal Chemistry MSci: European Placement Year',
                          school=chemistry, level=4, credits=120)
    Module.objects.create(id='CHEM1001', name='Chemistry 1', school=chemistry, level=1, credits=40)
    Module.objects.create(id='CHEM3028', name='Physical Chemistry for Chemical Studies', school=chemistry, level=3,
                          credits=20)
    Module.objects.create(id='CHEM5018', name='Inorganic Chemistry 4M (B)', school=chemistry, level=5, credits=15)
    Module.objects.create(id='CHEM5069', name='Catalyst testing and industrial process development.', school=chemistry,
                          level=5, credits=10)
    Module.objects.create(id='CHEM5059', name='Chemical Thermodynamics and Statistical Mechanics 4M', school=chemistry,
                          level=5, credits=10)
    Module.objects.create(id='CHEM5053', name='Functional Materials 4M', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM5044', name='Inorganic Chemistry 4M (half) for Chemistry & Mathematics',
                          school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4041', name='Functional Materials 4H', school=chemistry, level=4, credits=10)
    Module.objects.create(id='CHEM4012', name='Organic Chemistry 4H', school=chemistry, level=4, credits=20)
    Module.objects.create(id='CHEM5081', name='The Chemical Biology Toolkit', school=chemistry, level=5, credits=10)
    Module.objects.create(id='CHEM4026', name='Chemistry With European Placement MSci: European Placement Year',
                          school=chemistry, level=4, credits=120)
    Module.objects.create(id='CHEM1010', name='General Chemistry I for Visiting Students', school=chemistry, level=1,
                          credits=20)
    Module.objects.create(id='CHEM5017', name='Inorganic Chemistry 4M (A)', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM5022', name='Physical Chemistry 4M (A)', school=chemistry, level=5, credits=20)
    Module.objects.create(id='CHEM2006', name='Chemistry 2Y (Half Course)', school=chemistry, level=2, credits=15)
    Module.objects.create(id='CHEM5057', name='Polymers and Organic Materials 4M', school=chemistry, level=5,
                          credits=10)
    Module.objects.create(id='CHEM5042', name='Using Chemical Structure Databases in Drug Discovery', school=chemistry,
                          level=5, credits=10)
    Module.objects.create(id='CHEM5004', name='Chemistry Special Topics 4M (B)', school=chemistry, level=5, credits=10)

    # School of Computing Science (135 modules)
    Module.objects.create(id='COMPSCI1028',
                          name='Foundation Mathematics for Computing Science and Software Engineering 1',
                          school=computing, level=1, credits=0)
    Module.objects.create(id='COMPSCI2024', name='Networks and Operating Systems Essentials 2', school=computing,
                          level=2, credits=10)
    Module.objects.create(id='COMPSCI5101', name='Software Engineering Full Year Placement Review', school=computing,
                          level=5, credits=10)
    Module.objects.create(id='COMPSCI4093P', name='Workplace Project Supplement', school=computing, level=4, credits=30)
    Module.objects.create(id='COMPSCI4012', name='Networked Systems (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5063', name='CyberSecurity Fundamentals for MSc (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4079', name='Software Engineering Full Year Industrial Placement H',
                          school=computing, level=4, credits=120)
    Module.objects.create(id='COMPSCI2008', name='Object-Oriented Software Engineering 2', school=computing, level=2,
                          credits=10)
    Module.objects.create(id='COMPSCI5115', name='Software Product Release Engineering (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI3004', name='Team Project 3', school=computing, level=3, credits=30)
    Module.objects.create(id='COMPSCI1023', name='Web Application Systems', school=computing, level=1, credits=10)
    Module.objects.create(id='COMPSCI4066', name='Computer Vision Methods and Applications (H)', school=computing,
                          level=4, credits=10)
    Module.objects.create(id='COMPSCI2025', name='Advanced Professional Software Engineering', school=computing,
                          level=2, credits=10)
    Module.objects.create(id='COMPSCI1024', name='Workplace Assessment Year 1', school=computing, level=1, credits=20)
    Module.objects.create(id='COMPSCI1020', name='How to Learn a New Language', school=computing, level=1, credits=30)
    Module.objects.create(id='COMPSCI4024P', name='Individual Project (H) (Combined)', school=computing, level=4,
                          credits=20)
    Module.objects.create(id='COMPSCI5077', name='Enterprise Cyber Security (M)', school=computing, level=5, credits=15)
    Module.objects.create(id='COMPSCI4081', name='Systems Programming (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI2001', name='Introduction to Object Oriented Programming', school=computing,
                          level=2, credits=10)
    Module.objects.create(id='COMPSCI4043', name='Systems And Networks', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5084', name='Distributed and Parallel Technologies (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI1021', name='Practical Algorithms', school=computing, level=2, credits=20)
    Module.objects.create(id='COMPSCI5111', name='Human Computer Interaction (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5073P', name='MSci Research Proposal and Project', school=computing, level=5,
                          credits=80)
    Module.objects.create(id='COMPSCI4094', name='Coaching Software Teams (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4087', name='Startup Growth Engineering (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5072P', name='MSci Research Proposal and Project (Half)', school=computing,
                          level=5, credits=40)
    Module.objects.create(id='COMPSCI5057', name='Human Computer Interaction Design and Evaluation (M)',
                          school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI1006', name='Computing Science 1F - Computing Fundamentals', school=computing,
                          level=1, credits=10)
    Module.objects.create(id='COMPSCI5092', name='Research and Professional Skills (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4100', name='Computing Science Education Theory and Practice (H)',
                          school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5113', name='Coaching Software Teams (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5093', name='Secured Software Engineering (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5085', name='Deep Learning (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4011', name='Operating Systems (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI3012', name='Professional Issues in the Workplace', school=computing, level=3,
                          credits=10)
    Module.objects.create(id='COMPSCI5104', name='Secured Software Engineering for MSc (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5002', name='Programming for AI', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4105', name='Quantum Computing H', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5060', name='Human-Centred Security (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4089', name='Advanced Systems Programming (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4009', name='Algorithmics I (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5018P', name='MSc Project for Information Technology +', school=computing, level=5,
                          credits=60)
    Module.objects.create(id='COMPSCI2028', name='Data Science Fundamentals', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI4013', name='Database Systems (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5106', name='Text as Data for MSc', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5012', name='Internet Technology (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5094', name='Conversational Interfaces (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5107', name='Web Science for MSc', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5082P', name='MSci (Sandwich Year) Software Engineering Individual Project',
                          school=computing, level=5, credits=40)
    Module.objects.create(id='COMPSCI5098P', name='MSc Project for Computing Science (SOCIAL)', school=computing,
                          level=5, credits=60)
    Module.objects.create(id='COMPSCI5080', name='Cyber Systems Forensics (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI2029', name='Data Storage and Retrieval', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI5059', name='Software Engineering (M)', school=computing, level=5, credits=15)
    Module.objects.create(id='COMPSCI1017', name='Computing Science 1PX (Alternate Route)', school=computing, level=1,
                          credits=10)
    Module.objects.create(id='COMPSCI1027', name='Introduction to Programming', school=computing, level=1, credits=0)
    Module.objects.create(id='COMPSCI2030', name='Systems Programming', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI5117', name='Extended Reality Interaction (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4085P', name='Workplace Assessment Year 4', school=computing, level=4, credits=60)
    Module.objects.create(id='COMPSCI5074', name='MSc IT+ Team Project (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4106', name='Cloud Systems (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4062', name='Cyber Security Fundamentals (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5118', name='Cloud Systems (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI2021', name='Web Application Development 2', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI5103', name='Deep Learning for MSc (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI2033', name='Workplace Assessment Year 2', school=computing, level=2, credits=40)
    Module.objects.create(id='COMPSCI5096', name='Text as Data - An Introduction to Document Analytics (M)',
                          school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI2027', name='Computer Architecture and Network Systems', school=computing, level=2,
                          credits=20)
    Module.objects.create(id='COMPSCI4061', name='Machine Learning (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5119', name='Secure Systems Programming in Rust (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4084', name='Programming and Systems Development (H)', school=computing, level=4,
                          credits=20)
    Module.objects.create(id='COMPSCI5112', name='Mobile Human-Computer Interaction for MSc', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4082', name='Distributed and Parallel Technologies (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4101', name='Patient Centred Health-Technologies', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5120', name='Principles of Cybersecurity (M)', school=computing, level=5,
                          credits=15)
    Module.objects.create(id='COMPSCI4102', name='Software Product Release Engineering (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI1016', name='Computing Science - 1CT Introduction to Computational Thinking',
                          school=computing, level=1, credits=20)
    Module.objects.create(id='COMPSCI5076', name='Databases and Data Analytics (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5095', name='Computational Social Intelligence (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5087', name='Artificial Intelligence (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5004', name='Algorithms And Data Structures (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4069', name='Information Retrieval (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4038', name='Professional Skills and Issues (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5079', name='Cryptography and Secure Development (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5100', name='Machine Learning & Artificial Intelligence for Data Scientists (M)',
                          school=computing, level=5, credits=15)
    Module.objects.create(id='COMPSCI4064', name='Big Data: Systems, Programming, and Management (H)', school=computing,
                          level=4, credits=10)
    Module.objects.create(id='COMPSCI4021', name='Functional Programming (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4003', name='Algorithmics II (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI2026', name='Algorithmics', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI1026', name='Spatial Skills Training 1', school=computing, level=1, credits=0)
    Module.objects.create(id='COMPSCI4047', name='Team Project (H)', school=computing, level=4, credits=30)
    Module.objects.create(id='COMPSCI1001', name='Computing Science 1P (Standard Route)', school=computing, level=1,
                          credits=20)
    Module.objects.create(id='COMPSCI4023', name='Human-Computer Interaction (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4039', name='Programming', school=computing, level=4, credits=20)
    Module.objects.create(id='COMPSCI4014', name='Human-centred Systems Design and Evaluation (H)', school=computing,
                          level=4, credits=10)
    Module.objects.create(id='COMPSCI4016', name='Programming Languages (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5086P', name='MSc Project for Computing Science+', school=computing, level=5,
                          credits=60)
    Module.objects.create(id='COMPSCI5088', name='Big Data: Systems, Programming, and Management (M)', school=computing,
                          level=5, credits=10)
    Module.objects.create(id='COMPSCI1005', name='Computing Science 1P (Half Course)', school=computing, level=1,
                          credits=10)
    Module.objects.create(id='COMPSCI5003', name='Project Research Readings In Computing Science (M)', school=computing,
                          level=5, credits=10)
    Module.objects.create(id='COMPSCI2031', name='User Interaction', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI5011', name='Information Retrieval (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4007', name='Computer Architecture (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4025P', name='Individual Project (H) (Single)', school=computing, level=4,
                          credits=40)
    Module.objects.create(id='COMPSCI4076', name='Robotics Foundations (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI1019', name='Foundations of Professional Software Engineering', school=computing,
                          level=1, credits=30)
    Module.objects.create(id='COMPSCI5099', name='Information Visualisation (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4044', name='Team Project ESE (H)', school=computing, level=4, credits=30)
    Module.objects.create(id='COMPSCI1031', name='Object Oriented Design', school=computing, level=1, credits=10)
    Module.objects.create(id='COMPSCI4046', name='Software Engineering Summer Placement (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4070', name='Team Project Minor (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI3011', name='Workplace Assessment Year 3', school=computing, level=3, credits=60)
    Module.objects.create(id='COMPSCI5006', name='Constraint Programming (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI5078', name='Web Science (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI4072', name='Theory of Computation (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5083', name='Advanced Systems Programming (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI5116', name='Computational Game Theory (M)', school=computing, level=5, credits=10)
    Module.objects.create(id='COMPSCI2007', name='Algorithms & Data Structures 2', school=computing, level=2,
                          credits=10)
    Module.objects.create(id='COMPSCI2003', name='Algorithmic Foundations 2', school=computing, level=2, credits=10)
    Module.objects.create(id='COMPSCI4080', name='Computational Social Intelligence (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5089', name='Introduction to Data Science and Systems (M)', school=computing,
                          level=5, credits=15)
    Module.objects.create(id='COMPSCI5025', name='Research Methods And Techniques (M) for MSci', school=computing,
                          level=5, credits=10)
    Module.objects.create(id='COMPSCI4091', name='Advanced Networked Systems (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4004', name='Artificial Intelligence (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4073', name='Data Fundamentals (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI4068', name='Mobile Human-Computer Interaction (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI5110', name='Emerging Topics in Cyber Security (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI4077', name='Web Science (H)', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5015', name='Mobile Human-Computer Interaction (M)', school=computing, level=5,
                          credits=10)
    Module.objects.create(id='COMPSCI1018', name='Computing Science - 1S Systems', school=computing, level=1,
                          credits=10)
    Module.objects.create(id='COMPSCI4015', name='Professional Software Development (H)', school=computing, level=4,
                          credits=10)
    Module.objects.create(id='COMPSCI4074', name='Text as Data - An Introduction to Document Analytics (H)',
                          school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5123', name='Trustworthy Systems: Verification and Synthesis', school=computing,
                          level=5, credits=10)
    Module.objects.create(id='COMPSCI4107P', name='Data Product Engineering H', school=computing, level=4, credits=10)
    Module.objects.create(id='COMPSCI5014', name='Machine Learning (M)', school=computing, level=5, credits=10)

    # School of Critical Studies (373 modules)
    Module.objects.create(id='COMMS5011', name='Cultures of Globalisation', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='COMMS5002P', name='Global Communications Individual Project', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='COMMS5007', name='Histories of Communication', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='COMMS5012', name='Intimate and Embodied Communications', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='COMMS5005', name='Communicating Health, Illness and Disease', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='COMMS5003', name='Research Methods and Strategies for Communication',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='COMMS5006',
                          name='Communication and Constructed Languages: from Esperanto to Elvish to AI',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='COMMS5008', name='Media Ecologies', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='COMMS5009', name='Policy Communications', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='COMMS5004', name='Communicating Culture: Arts and Media Infrastructures',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='COMMS5001', name='Communications & Media: Theory and Concepts', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='COMMS5010', name='Digital Memory', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5057', name='Reading Writing Death & Dying DL', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT5043', name='The Genre-Bending Art of Essaying', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT5058', name='Crime Fiction', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5036', name='Creative Writing: Craft And Experimentation 2', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT5035', name='Creative Writing: Craft And Experimentation 1', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT1001', name='Creative Writing Summer School', school=critical_studies, level=1,
                          credits=15)
    Module.objects.create(id='CRWRT5049',
                          name='Creative Writing: Poetry Intervenes Now: Diverse Queer Strategies of Making',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5022', name='Creative Writing: Craft and Experimentation 1 (DL)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5053', name='Creative Writing Workshop 2 (DLearning)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT5037P', name='Creative Writing Portfolio (PGT)', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='CRWRT5031', name='Creative Writing Fiction Workshop (cross-discipline)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5048',
                          name='Creative Writing: Of the Personal: Emotions and the Self in Creative Non-Fiction',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5047P', name='Crime Fiction', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5024', name='Creative Writing: Editing and Publication 1 (DL)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT1002', name='Writing the City Summer School', school=critical_studies, level=1,
                          credits=12)
    Module.objects.create(id='CRWRT5051',
                          name='Writing the City: Urban Places and Spaces in Creative Practice (Online Distance Learning)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5052', name='Creative Writing Workshop 1 (DLearning)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT5025', name='Creative Writing: Editing and Publication 2 (DL)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5050',
                          name='Creative Writing: Poetry Intervenes Now: Diverse Queer Strategies of Making',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5039', name='Creative Writing: Editing And Publication 2', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT5038', name='Creative Writing: Editing And Publication 1', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='CRWRT5040P', name='Creative Writing Portfolio (PGT) (DLearning)', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='CRWRT5023', name='Creative Writing: Craft and Experimentation 2 (DL)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='CRWRT5044P', name='Reading & Writing Death & Dying', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT5056', name='Reading Writing Death & Dying', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT5055', name='Creative Writing Workshop 2', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT1005', name='Writing the City (Online Distance Learning)', school=critical_studies,
                          level=1, credits=12)
    Module.objects.create(id='CRWRT5054', name='Creative Writing Workshop 1', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='CRWRT5045P', name='Reading & Writing Death & Dying DL', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4032', name='Corpus Linguistics', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5133', name='Research Training Course 1: Introduction to Research',
                          school=critical_studies, level=5, credits=10)
    Module.objects.create(id='ENGLANG5108', name='Semantics of English (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4067', name='Bad Language: From Taboo to Prescriptivism', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG5128', name='Approaches to Scots in Speech and Text', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG4050', name='Discourse in Professional Contexts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG4049', name='Phonetics 2: Advanced Concepts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG4042', name='Medieval Literature: Other Worlds', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG5117', name='Applying Linguistics in Social and Professional Life',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5094', name='Corpus Linguistics (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4041', name='Medieval Multitudes: Exploring Middle English Texts',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG4044', name='Name Studies', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5131', name='Corpora: Advanced Methods (CAM)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5092', name='Experimental Design and Data Analysis', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5135', name='Qualitative Sociolinguistics', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5104', name='Methods in Sociolinguistics (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4052', name='Semantics of English', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5109', name='Introduction to Psycholinguistics (PGT)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5103', name='Methods in Phonetics (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4046', name='Old English Language', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5081', name='Onomastics', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5121', name='Systemic Functional Linguistics and its Applications',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG4051', name='Reading the Past: From Script to Print', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG5110', name='Topics in Phonetics', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5137', name='The Psycholinguistics of Bilingualism', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5093P', name='Speech, Language & Sociolinguistics Dissertation',
                          school=critical_studies, level=5, credits=60)
    Module.objects.create(id='ENGLANG3001', name='Medieval Multitudes: Exploring Middle English Texts (Non Honours)',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='ENGLANG3002', name='Name Studies Non Honours', school=critical_studies, level=3,
                          credits=20)
    Module.objects.create(id='ENGLANG2004', name='ENGLISH LANGUAGE & LINGUISTICS 2A: Language, People, and Culture',
                          school=critical_studies, level=2, credits=20)
    Module.objects.create(id='ENGLANG4066', name='Dictionaries and Thesauruses', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG5126', name='Forensic Linguistics', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG1001', name='ENGLISH LANGUAGE & LINGUISTICS 1A: Language, Meaning, and Power',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='ENGLANG4037', name='History of English', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5097', name='History of English (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5134', name='Research Training Course 2: Dissertation Preparation',
                          school=critical_studies, level=5, credits=10)
    Module.objects.create(id='ENGLANG4036', name='Editing Historical English Texts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG1003', name='ENGLISH LANGUAGE & LINGUISTICS 1B: Language, Society, and Change',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='ENGLANG4059', name='Introduction to Psycholinguistics', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG4055', name='Reading with Style', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG3003', name='Medieval Literature: Other Worlds Non-Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='ENGLANG4047', name='Old Icelandic Language', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG4068', name='Pragmatics: Language use in context', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG4038', name='History of Scots', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5122', name='Social and Individual Variables in Language Learning and Teaching',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5107', name='Phonetics: Advanced Concepts (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5105', name='Old English Language (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5106', name='Old Icelandic Language (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4034P', name='Dissertation in English Language (40 credits)',
                          school=critical_studies, level=4, credits=40)
    Module.objects.create(id='ENGLANG5138', name='Speech Perception: Brain & Behaviour', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5100', name='Quantitative Sociolinguistics', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5040', name='Early Modern Manuscripts for Research', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG4060', name='The Language of Laws', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG4063', name='Experimental Design and Data Analysis', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG5114P', name='Applied Linguistics Dissertation', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='ENGLANG4069', name='Language and Identities', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG5095', name='Editing Historical EnglishTexts (PGT)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5101', name='Medieval Multitudes: Exploring Middle English Texts (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5129', name='Multilingualism: Individuals, Institutions and Society',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5111', name='Topics in Sociolinguistics', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG2005', name='ENGLISH LANGUAGE & LINGUISTICS 2B: Language, Mind, and Expression',
                          school=critical_studies, level=2, credits=20)
    Module.objects.create(id='ENGLANG4065P',
                          name='Applied Dissertation with Placement in English Language and Linguistics',
                          school=critical_studies, level=4, credits=40)
    Module.objects.create(id='ENGLANG4058P', name='Dissertation in English Language (20 credits)',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG4035',
                          name='Heroes, Outlaws, and Outsiders: Old English and Old Icelandic Literature in Translation',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5099', name='Introduction to Phonetics (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG4033', name='Culture and English Language Teaching', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG4043', name='Methods in Sociolinguistic Variation', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLANG4048', name='Phonetics 1: Introductory Concepts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG4031', name='Contemporary Issues in Semantics', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLANG5123',
                          name='Language and the Global Campus: Linguistic Issues in the Internationalisation of Higher Education',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG5130', name='Contemporary Issues in Semantics (PGT)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5098', name='Introduction to Older Scots (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLANG5084P', name='MSc DISSERTATION IN ENGLISH LANGUAGE & LINGUISTICS',
                          school=critical_studies, level=5, credits=60)
    Module.objects.create(id='ENGLANG5124', name='Critical Approaches to Language and Communication',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLANG4053', name='Sociolinguistics', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLANG5102', name='Medieval English Literature 2 (PGT)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLANG5136', name='Love, Death, and Dragons: Medievalism and Fantasy',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT3005', name='Irish and Scottish Literature post 1900 Non-Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='ENGLIT5094', name='Victorian 2: Readers, Writers, Publishers', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT5111', name='Canadian Literature (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4131', name='Dragged off the Street: Queer Players on the Renaissance Stage',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5100', name='Early Modern Mythmaking', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4087', name='Literature 1660-1780', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5031', name='Virginia Woolf Writes Modernity', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4120', name='Creative Writing Hybrid Forms', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4119', name='Creative Writing Fiction', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4127', name='Canadian Literature', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4123P', name='Medical Humanities Dissertation 40 credits', school=critical_studies,
                          level=4, credits=40)
    Module.objects.create(id='ENGLIT5122', name='The Material Lives of Texts', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4096', name='Literature and Medicine', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5013', name='Embodiments: Literature And Medicine in the Nineteenth Century',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5132',
                          name='Race, Ecology, Sound: Black Studies and the Environment from the Plantation to the Metaverse',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4100', name='Radical Theory: Culture and Critique since 1968',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5124', name='Realism and Fantasy in Victorian Literature (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4089', name='Literature 1830-1914', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT2001', name='English Literature 2A: Writing Ecologies', school=critical_studies,
                          level=2, credits=20)
    Module.objects.create(id='ENGLIT5087P', name='Fantasy Dissertation', school=critical_studies, level=5, credits=60)
    Module.objects.create(id='ENGLIT4109', name='The Contemporary Novel: Transatlantic Crosscurrents',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5113', name='Contemporary Realisms', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5128', name='Narratives of Estrangement: Travel and Travel Writing, 1750-1980',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5086', name='Fantasy 1: 1780-1950', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5130',
                          name='The Tomorrow People: Speculative Bodies and Minds in Contemporary Culture',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5093', name='Victorian 1: Writing the Times', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4054P', name='Medical Humanities Dissertation', school=critical_studies, level=4,
                          credits=30)
    Module.objects.create(id='ENGLIT4110', name='The Fantastic History of the Twentieth Century',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT1012',
                          name='Fantastic Texts and Where to Find Them: Approaching Fantasy Literature (Summer School)',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='ENGLIT4091', name='Literature 1945-present', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5047P', name='Modernities Dissertation', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='ENGLIT5129', name='World-building', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5103', name='Alternative Continuities: Scottish literature, c.1400-1625',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4095', name='James Joyce', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4083', name='American Literature 1 (1836-1929)', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4094', name='Power and Resistance: Contemporary Irish and Scottish Literature',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4116', name='Core Course 2: The Words on the Page', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT4133P', name='Applied Dissertation with Placement in English Literature',
                          school=critical_studies, level=4, credits=40)
    Module.objects.create(id='ENGLIT4141', name='Fantastika Now: Cultures of Contemporary Genre Fiction',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5021', name='Neovictorianism', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4118P', name='Creative Writing Dissertation', school=critical_studies, level=4,
                          credits=40)
    Module.objects.create(id='ENGLIT4139', name='Women and the Writing of Violence', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4140',
                          name='Global Anglophone Literature: Colonialism, Capitalism, and the Infrastructural Imaginary',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5102', name='Seventeenth-Century Women\'s Writing', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT5133',
                          name='Race, Ecology, Sound: Black Studies and the Environment from the Plantation to the Metaverse (DL)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5115', name='Modern American Literature 1', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT5012', name='Decadence And The Modern', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4128', name='Fantasies of Energy', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4136', name='An Introduction to Medical and Health Humanities',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4114',
                          name='Writing the English Revolution: Literature, Politics and Religion from Milton to Marvell',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4101', name='Realism and Fantasy in Victorian Literature', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT4137',
                          name='A Periodical History of the Fantastic: Science Fiction and Fantasy in Magazines, 1880-Present',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4104', name='Romantic Ecologies', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5121', name='Futures: Unbundling the Now', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT2002', name='English Literature 2B: Writing the Body', school=critical_studies,
                          level=2, credits=20)
    Module.objects.create(id='ENGLIT5017P', name='Mlitt In Victorian Literature: Dissertation', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='ENGLIT5135P', name='English Literature Dissertation', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='ENGLIT4084', name='American Literature 2 (1930 to present)', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT5126', name='Raw Material: Literature, Empires, Commodities (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5098', name='Romantic Worlds 1: Encountering Environments', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT4125', name='Literature and Collecting', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4129', name='Poetry Mothers: Queer Poems, Queer Poetics', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT5095', name='English Literature Dissertation', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='ENGLIT5107P', name='Dissertation Early Modern Literature', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='ENGLIT5072', name='Modernities 2: 1945 to the present', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4142', name='Slavery, Créolité & Caribbean Textual Cultures',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5020', name='Modernities I:1880-1945', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4090', name='Literature 1890-1945', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4092', name='British Children\'s Literature', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT5024', name='The American Counterculture, 1945-75', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT5078', name='The Mind of the Contemporary American Novel', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT4102', name='Religion, Politics and Philosophy in Early Modern English Literature',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4098', name='Modernism and the Politics of Gender', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT5110P', name='Romantic Worlds Dissertation', school=critical_studies, level=5,
                          credits=60)
    Module.objects.create(id='ENGLIT4130', name='Raw Material: Literature, Empire, Commodities',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4107', name='Shakespeare and his Contemporaries: Playing with History',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5123',
                          name='Religion, Politics and Philosophy in Early Modern English Literature (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4108', name='Shakespearean Forms from Sonnet to Tragedy', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='ENGLIT4117P', name='English Literature Dissertation', school=critical_studies, level=4,
                          credits=40)
    Module.objects.create(id='ENGLIT5104', name='The Bleeding Edge: Contemporary narratives of illness and medicine',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4111', name='US Fictions of the Great Depression', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4099', name='Postcolonialism: Writing & Theory', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT5118', name='Children\'s Fantasy Literature', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4134', name='Futures: Unbundling the Now', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT5117P', name='Modern American Literature Dissertation', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='ENGLIT5076',
                          name='F. Scott Fitzgerald, Edith Wharton and Dialogues of American Literary Modernism',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5075', name='American Fiction of the 1930s', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT4121', name='Creative Writing Poetry', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT4138',
                          name='Fugitivity/Insurgency: African American Radicalism from 19th Century to the Present',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5026', name='Modern Everyday', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT1011', name='English Literature 1A: Poetry & Poetics', school=critical_studies,
                          level=1, credits=20)
    Module.objects.create(id='ENGLIT5116', name='Modern American Literature 2', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT5119', name='Victorian Literature Beyond the Human', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT4088', name='Literature 1780-1840', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5096', name='Fantasy Across Media', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4086', name='Literature 1510-1660: Rethinking the Renaissance',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='ENGLIT5101', name='English Literature Research Training Course', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT5131', name='Psychoanalysis and Empire', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT5001', name='African Modernities: Colonialism and Postcolonialism in the Novel',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT5085', name='Fantasy 2: 1950 to the present', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT1010', name='English Literature 1B: Critical Skill-Making: The Study of the Novel',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='ENGLIT4085', name='Core Course 1: Literary Theory', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4106', name='Science Fiction 1945-present', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT5109', name='Romantic Worlds 2: Selves and Societies', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT5125', name='Postcolonialism: Writing and Theory (PGT)', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='ENGLIT4105', name='Romanticism and Revolution', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT5114', name='Fantasies of Energy (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='ENGLIT5134', name='Slavery, Créolité & Caribbean Textual Cultures',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='ENGLIT4113', name='Victorian Popular Fiction', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='ENGLIT4115', name='Core Course 1: Author, Reader, World', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='SCOTLIT4029', name='Textual Editing: Scottish Texts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='SCOTLIT5017', name='Independent Study in Scottish and Celtic Studies',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='SCOTLIT4034', name='Modern Scottish Poetry', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4037', name='Scottish Fiction under Late Capitalism', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='SCOTLIT1013', name='Scottish Literature 1A: The Fantastic and the Real',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='SCOTLIT1016', name='Exploring Scotland: Culture, History, and People (Summer School)',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='SCOTLIT2002', name='Scottish Literature 2B: Early Scottish Literature & Language',
                          school=critical_studies, level=2, credits=20)
    Module.objects.create(id='SCOTLIT2001', name='Scottish Literature 2A: Early Scottish Literature & Language',
                          school=critical_studies, level=2, credits=20)
    Module.objects.create(id='SCOTLIT4036', name='Scottish Writers', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4039',
                          name='The Long Seventeenth Century: Scottish Literature\'s Final Frontier (1583-1706)',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4033', name='Memorialising Scottish Culture and Literature',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT1017', name='Cultural Heritage Skills for Business', school=critical_studies,
                          level=1, credits=10)
    Module.objects.create(id='SCOTLIT4024', name='Alternative Renaissances', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='SCOTLIT4038P', name='Applied Dissertation with Placement in Scottish Literature',
                          school=critical_studies, level=4, credits=40)
    Module.objects.create(id='SCOTLIT4030', name='Robert Burns', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4026P', name='Dissertation in Scottish Literature', school=critical_studies,
                          level=4, credits=40)
    Module.objects.create(id='SCOTLIT4013', name='The Scottish Enlightenment: Ideas and Influences',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT1014', name='Robert Burns (Online Distance Learning)', school=critical_studies,
                          level=1, credits=20)
    Module.objects.create(id='SCOTLIT4006', name='The Scottish Enlightenment: Ideas And Influences',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4027', name='Popular Literary Enlightenment, 1710 - 1790', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='SCOTLIT4023', name='Scottish Literature: Theory and Criticism', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='SCOTLIT4025', name='Contemporary Scottish Literature', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='SCOTLIT4035', name='Scottish Journeys', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4031',
                          name='From the Beginnings to the Early Modern in Older Scots Literature (1375-1501)',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT4040', name='The Short Story in Scotland: Tradition & Innovation',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='SCOTLIT1012', name='Scottish Literature 1B: Stories We Tell Ourselves',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS2004', name='TRS 2: Mysticism And Spirituality', school=critical_studies, level=2,
                          credits=20)
    Module.objects.create(id='TRS4102', name='Studies in Early Church History and Theology', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS3030', name='Wisdom Literature Non Honours', school=critical_studies, level=3,
                          credits=20)
    Module.objects.create(id='TRS3035', name='Modern Judaism: Aspects of Life and Literature Non Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS4119P', name='Applied Dissertation with Placement in Theology and Religious Studies',
                          school=critical_studies, level=4, credits=40)
    Module.objects.create(id='TRS5125', name='Biblical Manuscripts Directed Study', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS5056P', name='Theology and Religious Studies Dissertation', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='TRS5101', name='Christianity in Scotland since the Reformation', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS4065', name='Introductory New Testament Greek for Honours', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS4069', name='New Testament Themes and Topics with Greek', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS1037', name='Listening in Mission', school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS5093', name='Women and Gender in the Bible and the Ancient World (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS1031E', name='Managing Difficult Church Change', school=critical_studies, level=1,
                          credits=10)
    Module.objects.create(id='TRS4099', name='Political Theology', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4086P', name='Dissertation', school=critical_studies, level=4, credits=40)
    Module.objects.create(id='TRS4093', name='Sufism', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4096', name='Doctrine of God', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5122', name='Political Islam', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS5111', name='Case Studies in Religion and Global Challenges', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS4121', name='Scribal Culture in the Ancient World', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4104', name='The Church in Scotland since 1500', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4101', name='Roots of Sectarianism', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4067', name='New Testament Texts with Greek', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS1009', name='Religions in Asia', school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS4074', name='Wisdom Literature', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS1025', name='The Search For Meaning: Judaism, Christianity & Islam',
                          school=critical_studies, level=1, credits=15)
    Module.objects.create(id='TRS1028', name='A Comprehensive Introduction to Malayalam Grammar',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS3031', name='Pastoral Theology Non Honours', school=critical_studies, level=3,
                          credits=20)
    Module.objects.create(id='TRS5067', name='Religion, Theology and Culture Directed Study (Semester 1)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS3028', name='New Testament Texts Non Honours', school=critical_studies, level=3,
                          credits=20)
    Module.objects.create(id='TRS2002', name='TRS 2: Christian Traditions and Transformations', school=critical_studies,
                          level=2, credits=20)
    Module.objects.create(id='TRS4094', name='Understanding Muhammad', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5104', name='Creative Ministry', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS4081', name='Theology through Creative Writing', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4117', name='South Asian Epic Traditions', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4097', name='Jesus Christ since 1900', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5110', name='Research Training and Approaches to Studying Religions',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS4072', name='Old Testament / Tanakh Texts with Hebrew', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS3038', name='Studies in the History and Theology of the Reformation Non Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS4058', name='Existentialism: Atheism, Reason, and Faith', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS1029E', name='Worship and Contemporary Visual Arts', school=critical_studies, level=1,
                          credits=10)
    Module.objects.create(id='TRS4061', name='Introductory Classical Hebrew for Honours', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS5107', name='Religious practice in Japan (PGT)', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS1003', name='Worship & Liturgy 1', school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS4108', name='Muslims in Multicultural Britain', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4087', name='Holocaust Narratives and the Ethics of Representation',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4076', name='Christianity and Bioethics', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5116', name='Interpretive Approaches to Ancient Texts', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS3026', name='Genesis Non Honours', school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS5109', name='Studies in the History and Theology of the Reformation (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS1032E',
                          name='Introduction to Ministry & Mission in Digital Culture (Online Distance Learning)',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS1038', name='Eldership & Local Church Leaders in a Changing Context',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS1005', name='TRS 1 : Classical Hebrew Language', school=critical_studies, level=1,
                          credits=20)
    Module.objects.create(id='TRS4089', name='Modern Judaism: Aspects of Life and Literature', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS2021', name='TRS: Religion, Culture, and Controversy', school=critical_studies,
                          level=2, credits=20)
    Module.objects.create(id='TRS4116', name='Religious practice in Japan', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS2023', name='Preaching in Church Contexts', school=critical_studies, level=2,
                          credits=10)
    Module.objects.create(id='TRS5117', name='Ancient Language Directed Study', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS5126', name='Scribal Culture in the Ancient World', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS1026', name='History of Christianity in Scotland', school=critical_studies, level=1,
                          credits=15)
    Module.objects.create(id='TRS5103', name='Bible, Doctrine and Freedom of Interpretation', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS1034E', name='Creative Writing as Spiritual Reflection: Models, Methods and Practice',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS5106', name='Resourcing Congregational Ministry', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS1033E', name='Intoduction to Biblical Hebrew', school=critical_studies, level=1,
                          credits=10)
    Module.objects.create(id='TRS5090', name='Jewish Literature in the Graeco-Roman World (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS4075', name='Wisdom Literature Honours with Hebrew', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4090', name='Reading Islam', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS1007', name='TRS 1: The God Question: Exploring Christianity', school=critical_studies,
                          level=1, credits=20)
    Module.objects.create(id='TRS2008', name='Worship & Liturgy 2', school=critical_studies, level=2, credits=20)
    Module.objects.create(id='TRS4091', name='Religion in Modern Iran', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5099P', name='Church History and Theology Dissertation', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='TRS1040', name='History and Theology of Christian Worship', school=critical_studies,
                          level=1, credits=10)
    Module.objects.create(id='TRS4095', name='Issues in Contemporary Catholicism', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4062', name='Genesis', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5068', name='Religion, Theology and Culture Directed Study (Semester 2)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS3034', name='Holocaust Narratives and the Ethics of Representation Non Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS5119', name='Beginning Classical Hebrew for Postgraduates', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS5120', name='Religions, Cultures, and Environmental Crises', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS1036', name='Engaging the Bible', school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS4103', name='Studies in the History and Theology of the Reformation',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4109', name='Jewish Literature in the Graeco-Roman World', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS4118', name='Theology of Thomas Aquinas', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS1027', name='Religion and Spirituality in Scotland', school=critical_studies, level=1,
                          credits=15)
    Module.objects.create(id='TRS4066', name='New Testament Texts', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS4063', name='Genesis with Hebrew', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS1008', name='TRS 1: The Search For Meaning: Judaism, Christianity & Islam',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS4068', name='New Testament Themes and Topics', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS1041', name='Designing and Leading Christian Worship (Multiformat)',
                          school=critical_studies, level=1, credits=10)
    Module.objects.create(id='TRS4098', name='John Calvin and his Theology', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS5112P', name='Religion and Global Challenges Dissertation', school=critical_studies,
                          level=5, credits=60)
    Module.objects.create(id='TRS3029', name='Old Testament / Tanakh Texts Non Honours', school=critical_studies,
                          level=3, credits=20)
    Module.objects.create(id='TRS5091', name='History of Christianity in Africa', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS5124', name='Beginning Koine Greek for Postgraduates', school=critical_studies,
                          level=5, credits=20)
    Module.objects.create(id='TRS5092', name='Nature and Practice of Church History 1 (including Research Training)',
                          school=critical_studies, level=5, credits=40)
    Module.objects.create(id='TRS5108', name='Studies in Early Church History and Theology (PGT)',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS2022', name='Liturgy and Prayer in Church Worship', school=critical_studies, level=2,
                          credits=10)
    Module.objects.create(id='TRS5115', name='Bible in Material and Digital Culture', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS5031', name='Research Training - Theology and Religious Studies',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS5113', name='Leading in Church Change', school=critical_studies, level=5, credits=10)
    Module.objects.create(id='TRS4071', name='Old Testament / Tanakh Texts', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS5127', name='Literature, Culture and the New Sacred', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS4113', name='Religion and Trade in Premodern Asia', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS3040', name='Worship, Liturgy and Preaching Non-Honours', school=critical_studies,
                          level=3, credits=20)
    Module.objects.create(id='TRS3036', name='Sufism Non Honours', school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS4115', name='Law, Religion and the Rights of the Child', school=critical_studies,
                          level=4, credits=20)
    Module.objects.create(id='TRS4112', name='Women and Gender in the Bible and the Ancient World',
                          school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS3025', name='Bible, Literature and Culture Non Honours', school=critical_studies,
                          level=3, credits=20)
    Module.objects.create(id='TRS5123', name='Migration, Displacement and Religious Identities',
                          school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS1035', name='Women and Gender in the Bible and Contemporary Society (Summer School)',
                          school=critical_studies, level=1, credits=15)
    Module.objects.create(id='TRS3037', name='Studies in Early Church History and Theology Non Honours',
                          school=critical_studies, level=3, credits=20)
    Module.objects.create(id='TRS5105', name='Homiletics and Biblical Hermeneutics', school=critical_studies, level=5,
                          credits=20)
    Module.objects.create(id='TRS4082', name='Worship, Liturgy and Preaching', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS1006', name='TRS 1: Creation To Apocalypse: Introduction To The Bible',
                          school=critical_studies, level=1, credits=20)
    Module.objects.create(id='TRS1030E', name='Designing and Leading Christian Worship', school=critical_studies,
                          level=1, credits=10)
    Module.objects.create(id='TRS4079', name='Pastoral Theology', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS5077', name='Religion and Violence', school=critical_studies, level=5, credits=20)
    Module.objects.create(id='TRS4060', name='Bible, Literature and Culture', school=critical_studies, level=4,
                          credits=20)
    Module.objects.create(id='TRS4073', name='The Historical Jesus', school=critical_studies, level=4, credits=20)
    Module.objects.create(id='TRS2005', name='TRS 2: Texts and Cultures of the Bible', school=critical_studies, level=2,
                          credits=20)
    Module.objects.create(id='TRS5098', name='Nature and Practice of Church History 2', school=critical_studies,
                          level=5, credits=20)

    # School of Culture and Creative Arts (310 modules)
    Module.objects.create(id='CULTIND5004', name='Cultural Institutions', school=art, level=5, credits=20)
    Module.objects.create(id='CULTIND4007', name='Creative Arts and Industries Study Abroad', school=art, level=4,
                          credits=120)
    Module.objects.create(id='CULTIND4003P', name='Dissertation in Creative Arts and Industries (40 Credits)',
                          school=art, level=4, credits=40)
    Module.objects.create(id='CULTIND1002', name='Introduction to Creative Practice', school=art, level=1, credits=20)
    Module.objects.create(id='CULTIND4012P',
                          name='Practice Research Dissertation in Creative Arts and Industries (20 Credits)',
                          school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND5011', name='Research Methods 1 (CCPR)', school=art, level=5, credits=10)
    Module.objects.create(id='CULTIND5008', name='Media Economics', school=art, level=5, credits=30)
    Module.objects.create(id='CULTIND5012', name='Research Methods 2 (CCPR)', school=art, level=5, credits=10)
    Module.objects.create(id='CULTIND5007', name='Issues In Audience Management', school=art, level=5, credits=20)
    Module.objects.create(id='CULTIND5003', name='Cultural Cities and Creative Regions', school=art, level=5,
                          credits=20)
    Module.objects.create(id='CULTIND5002', name='Issues in Audience Management (MCS)', school=art, level=5, credits=20)
    Module.objects.create(id='CULTIND5009P', name='Media Management Dissertation', school=art, level=5, credits=60)
    Module.objects.create(id='CULTIND4009', name='Cultural Work Alternatives - Co-operation and Collaboration',
                          school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND5001',
                          name='Creative Lives and Cultural Industries (Creative Industries and Cultural Policy - Core 2)',
                          school=art, level=5, credits=30)
    Module.objects.create(id='CULTIND1001', name='Introduction to Creative Industries', school=art, level=1, credits=20)
    Module.objects.create(id='CULTIND5005', name='Research Methods in Creative Industries and Cultural Policy',
                          school=art, level=5, credits=20)
    Module.objects.create(id='CULTIND2002', name='Cultural Analysis and Creative Practice', school=art, level=2,
                          credits=20)
    Module.objects.create(id='CULTIND2001', name='Creative Labour', school=art, level=2, credits=20)
    Module.objects.create(id='CULTIND5010', name='Media & Cultural Policy', school=art, level=5, credits=30)
    Module.objects.create(id='CULTIND5013P', name='Creative Industries and Cultural Policy Dissertation', school=art,
                          level=5, credits=60)
    Module.objects.create(id='CULTIND5006', name='Creative Industries and Cultural Policy - Core 1', school=art,
                          level=5, credits=30)
    Module.objects.create(id='CULTIND4008', name='Creative Worlds', school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND4004P', name='Dissertation in Creative Arts and Industries (20 Credits)',
                          school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND4010', name='Cultures of Revolution', school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND4011', name='Making Culture Happen', school=art, level=4, credits=20)
    Module.objects.create(id='CULTIND4006P',
                          name='Practice Research Dissertation in Creative Arts and Industries (40 Credits)',
                          school=art, level=4, credits=40)
    Module.objects.create(id='FTV4112P',
                          name='Applied Dissertation in Community and Collaborative Practice (GMAC Partnership)',
                          school=art, level=4, credits=40)
    Module.objects.create(id='FTV1010', name='Screen Histories', school=art, level=1, credits=20)
    Module.objects.create(id='FTV5058', name='The Material of Film Curation', school=art, level=5, credits=30)
    Module.objects.create(id='FTV4030', name='Documentary Film And Television', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4103', name='Working in the UK Screen Industries', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5048', name='Practical Workshop 1: Project Preparation', school=art, level=5,
                          credits=40)
    Module.objects.create(id='FTV4100', name='Screens and Machines', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4102', name='Race on Screen', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4052', name='Radical Film And Television', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4111', name='Children\'s TV and Media', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4087', name='Introduction to Contemporary African Cinemas', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV5068', name='Research Methods and Dissertation Preparation', school=art, level=5,
                          credits=30)
    Module.objects.create(id='FTV5075P', name='Media Culture & Society Group Project (FTV)', school=art, level=5,
                          credits=60)
    Module.objects.create(id='FTV5046P', name='Practice Led Dissertation', school=art, level=5, credits=60)
    Module.objects.create(id='FTV4003', name='Cinematic Journeys', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4085', name='Japanese Cinema after WWII', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4106', name='Making History', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4089', name='Audiovisual Film and Television Criticism', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV4006P', name='FTV Dissertation (Long Version)', school=art, level=4, credits=40)
    Module.objects.create(id='FTV4094', name='Film Tourism', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4070', name='Television Drama', school=art, level=4, credits=20)
    Module.objects.create(id='FTV1011', name='Screen Analysis', school=art, level=1, credits=20)
    Module.objects.create(id='FTV4062', name='Screenwriting', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4116', name='Thinking Through Filmmaking', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4107', name='Screening Disability', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5061', name='Advanced Topics in Television Studies', school=art, level=5, credits=20)
    Module.objects.create(id='FTV4059', name='Screen Performance', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4004', name='Film Analysis', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4105', name='Film Archives: Theory and Practice', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4005P', name='FTV Dissertation (Short Version)', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5049', name='Experimental Art and Media', school=art, level=5, credits=20)
    Module.objects.create(id='FTV4018', name='American Independent Cinema', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4088', name='South Korean Cinema', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5069', name='History of Film and Television Studies', school=art, level=5, credits=30)
    Module.objects.create(id='FTV4084', name='Iranian Cinema', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4013', name='Television Analysis', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4073', name='Television, Memory And The Archive', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5071', name='Festivals (MCS)', school=art, level=5, credits=20)
    Module.objects.create(id='FTV5018P', name='FTV Postgraduate Dissertation', school=art, level=5, credits=60)
    Module.objects.create(id='FTV4123', name='Introduction to Latin American Cinema', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4036', name='Film & Television Technology', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5060', name='Advanced Topics in Film Studies', school=art, level=5, credits=20)
    Module.objects.create(id='FTV4120', name='Media and Mental Health', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4049', name='Melodrama & Film Noir: Issues Of Genre Creation', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV4083', name='Screen Production for Senior Honours FTV', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV2010', name='Screen Industries', school=art, level=2, credits=20)
    Module.objects.create(id='FTV4072', name='Television Sitcom', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4001', name='Animation', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4121', name='Romantic Comedy', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4096', name='Screen Production for Junior Honours FTV', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV5059', name='The Practice of Film Curation', school=art, level=5, credits=30)
    Module.objects.create(id='FTV4122', name='Representations of the Past in Film and Television', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV4099', name='New Media Arts: Theory and Practice', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5073', name='Television Drama (MCS)', school=art, level=5, credits=20)
    Module.objects.create(id='FTV4076', name='Critical Practice: Film and Cosmopolitanism', school=art, level=4,
                          credits=20)
    Module.objects.create(id='FTV4114', name='Queer Film and Television', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4008', name='Media And Cultural Policy', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5050', name='Festivals', school=art, level=5, credits=20)
    Module.objects.create(id='FTV5072', name='History of Film and Television Studies (MCS)', school=art, level=5,
                          credits=20)
    Module.objects.create(id='FTV4044', name='Hollywood In The 1930s', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4115', name='Thinking Through Creative Practices', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4118', name='Images of \'Gypsies\' on Screen', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5057', name='Creative Practice: Film Curation', school=art, level=5, credits=20)
    Module.objects.create(id='FTV4101', name='Experimental Cinema', school=art, level=4, credits=20)
    Module.objects.create(id='FTV4117', name='Feminist Film Theory', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5047', name='Practical Workshop 2: Pilot project', school=art, level=5, credits=40)
    Module.objects.create(id='FTV4110', name='Women Filmmakers', school=art, level=4, credits=20)
    Module.objects.create(id='FTV5074', name='Working in the Screen Industries (MCS)', school=art, level=5, credits=20)
    Module.objects.create(id='FTV2001', name='Screen Experiences', school=art, level=2, credits=20)
    Module.objects.create(id='FTV4109', name='Academic Filmmaking', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5126', name='Provenance and Restitution', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5055', name='Research Management', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5105', name='Research Methods and Skills', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5048', name='Textile Conservation Placement', school=art, level=5, credits=60)
    Module.objects.create(id='HISTART4088', name='Dada and Surrealism (20 Credits)', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5166', name='Art and Place', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5146', name='Principles and Practice: Conservation Projects - Book and Paper',
                          school=art, level=5, credits=40)
    Module.objects.create(id='HISTART5072', name='Work Placement', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5112', name='Masters of the Venetian Renaissance: Titian, Tintoretto, Veronese',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5165', name='The Global Avant-Garde', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4061', name='Art, Tradition and Identity in Venice 1350-1797', school=art, level=4,
                          credits=40)
    Module.objects.create(id='HISTART5111', name='The Palace as Portrait', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART2005', name='History Of Art 2B', school=art, level=2, credits=20)
    Module.objects.create(id='HISTART5101', name='Landscape art and the geography of eighteenth-century Britain',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5018P', name='Dissertation', school=art, level=5, credits=60)
    Module.objects.create(id='HISTART4060', name='Leonardo, Michelangelo, Raphael', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5051', name='Principles And Practice: Conservation Projects', school=art, level=5,
                          credits=40)
    Module.objects.create(id='HISTART4035', name='PHOTOGRAPHY AND MODERNISM', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART2004', name='History Of Art 2A', school=art, level=2, credits=20)
    Module.objects.create(id='HISTART4078', name='Printmaking in Britain c.1780-1914: contexts, processes, markets',
                          school=art, level=4, credits=40)
    Module.objects.create(id='HISTART5041', name='Material Cultures', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5167', name='Book and Paper Conservation Placement', school=art, level=5,
                          credits=60)
    Module.objects.create(id='HISTART4004', name='Architecture, Landscape Design and the Regency Imagination',
                          school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4031', name='Methodology Of Art History', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5053', name='Principles And Practice: Developing Skills', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART5116', name='Curatorial Practice 1', school=art, level=5, credits=40)
    Module.objects.create(id='HISTART1002', name='History of Art 1A', school=art, level=1, credits=20)
    Module.objects.create(id='HISTART5149P',
                          name='Dissertation for Book and Archival Materials Conservation & Paper Conservation',
                          school=art, level=5, credits=60)
    Module.objects.create(id='HISTART5124', name='Object Biography', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4091', name='Rethinking Italian Renaissance Art', school=art, level=4, credits=40)
    Module.objects.create(id='HISTART5097', name='Deconstructing the Artefact', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4044', name='Women, Art and Audience 1830-1914', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4070', name='Art in Eighteenth Century Britain', school=art, level=4, credits=40)
    Module.objects.create(id='HISTART5050', name='Principles And Practice: Advanced Skills', school=art, level=5,
                          credits=40)
    Module.objects.create(id='HISTART5164', name='Cross-Cultural Artistic Encounters in the Mediterranean, 1200-1700',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5077', name='Testimonies On Artists\' Practice: Documentary And Visual Sources',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5049', name='Preventive Conservation', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4084', name='Past Futures: Time and Temporality in Contemporary Art', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART4042', name='The Dawn of Modernism in Central Europe', school=art, level=4,
                          credits=40)
    Module.objects.create(id='HISTART5140P',
                          name='Dissertation. Managing Art & Cultural Heritage in Global Markets (MAGMa)', school=art,
                          level=5, credits=60)
    Module.objects.create(id='HISTART4039',
                          name='Symbolism and Secession: Aspects of Symbolism and the Vienna Secession', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART5022', name='Framing Dress and Textile Histories', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART1003', name='History of Art 1B', school=art, level=1, credits=20)
    Module.objects.create(id='HISTART4092', name='The Pre-Raphaelites: Medieval Dreams in the Age of Steam', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART5151', name='Testimonies on Practice: Book and Paper', school=art, level=5,
                          credits=10)
    Module.objects.create(id='HISTART5104', name='Victorian Visions: Dress and Textiles, c.1837-1901', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART4017P', name='Dissertation (History Of Art-Joint Hons)', school=art, level=4,
                          credits=20)
    Module.objects.create(id='HISTART4067', name='Historical Dress in Film & TV', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4079',
                          name='Publishing the Avant-Garde: a history of artists\' books and magazines from 1900 to 1970',
                          school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5052', name='Principles And Practice: Core Skills', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART4006', name='ART AND POLITICS IN WEIMAR GERMANY (1918-1933)', school=art, level=4,
                          credits=40)
    Module.objects.create(id='HISTART4011', name='Artists And The Art Market In Late 19th Century Britain', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART4086', name='The Art of Exploration', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4081', name='The Worlds of Hieronymus Bosch, Enemy Painter', school=art, level=4,
                          credits=20)
    Module.objects.create(id='HISTART4063', name='Forgeries, Attributions and the Art Market', school=art, level=4,
                          credits=40)
    Module.objects.create(id='HISTART5070', name='Understanding Textiles: Technology', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4046', name='Georgian Landscapes', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4058', name='Methodology of Art History with Placement', school=art, level=4,
                          credits=20)
    Module.objects.create(id='HISTART5114', name='From Gothic to Renaissance in Northern Europe', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART4082', name='Setting the Scene', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4018P', name='Dissertation (History Of Art-Single Hons)', school=art, level=4,
                          credits=40)
    Module.objects.create(id='HISTART5134', name='Ethics in Textile Conservation Practice', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART4001', name='Albrecht Durer: From Germany to Italy and Back Again', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART5004', name='Art, Embodiment, Transgression', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5110', name='Death and the Art of Dying in the Renaissance North', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART5128', name='Renaissance Dress and Textiles: Materials and Meaning', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART5130', name='Shaping Modern Artefacts: Material Form and Function', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART4040', name='The Apocalypse, Antichrist And The End Of Time In Medieval Art',
                          school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4085', name='Murillo: Art and Culture in Seventeenth-Century Spain', school=art,
                          level=4, credits=20)
    Module.objects.create(id='HISTART5160', name='Book and archival Materials: Placement', school=art, level=5,
                          credits=60)
    Module.objects.create(id='HISTART5158', name='Understanding Book and Paper: Materials, Making and Meaning',
                          school=art, level=5, credits=30)
    Module.objects.create(id='HISTART5122',
                          name='Making Time: performing and thinking temporalities in the creative arts', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART5040', name='Applying Dress and Textile Histories', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART5123', name='Cultures of Collecting - Collecting Cultures', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART5150',
                          name='Principles and Practice: Core Skills in Books and Archival Materials Conservation',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4032', name='Monsters, Women And Jews: Medieval Art And Identity', school=art,
                          level=4, credits=40)
    Module.objects.create(id='HISTART4068', name='Discourses in Cultural Property', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4036', name='Portfolio', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5142',
                          name='Interdisciplinary Research Methods & Approaches. Managing Art & Cultural Heritage in Global Markets',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5037', name='Independent Study', school=art, level=5, credits=20)
    Module.objects.create(id='HISTART4090', name='Portraiture in Spain 1550-1620', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4055', name='ARCHITECTURE IN MODERNITY 1900-1950', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4009', name='Art in America 1945-The Present', school=art, level=4, credits=40)
    Module.objects.create(id='HISTART4089', name='Early Modern Ecologies 1300-1600', school=art, level=4, credits=20)
    Module.objects.create(id='HISTART4056', name='The Renaissance Palace', school=art, level=4, credits=40)
    Module.objects.create(id='HISTART5129', name='Impressionism: Innovation and Invention 1874-1926', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART4021', name='Early Impressionism', school=art, level=4, credits=40)
    Module.objects.create(id='HISTART5093', name='Art in the Making: Modern & Avant-Garde Techniques', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART5094', name='Art in the Making: Historical Techniques', school=art, level=5,
                          credits=20)
    Module.objects.create(id='HISTART5064', name='The Authentic Art Work: Interpretation, Conservation, Presentation.',
                          school=art, level=5, credits=20)
    Module.objects.create(id='HISTART5153',
                          name='Principles and Practice: Developing Skills in Book and Paper Conservation', school=art,
                          level=5, credits=20)
    Module.objects.create(id='HISTART5143', name='Principles and Practice: Advanced Skills Book and Paper', school=art,
                          level=5, credits=40)
    Module.objects.create(id='HISTART4071',
                          name='Polychrome Sculpture and Painting in Golden Age Spain: The Quest for Reality',
                          school=art, level=4, credits=20)
    Module.objects.create(id='HISTART5131', name='Ethics for Artefacts: Modern Materials', school=art, level=5,
                          credits=20)
    Module.objects.create(id='MUSIC4068', name='Composition Advanced 40', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC4059', name='Genders (20)', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4096', name='Historiography and Criticism', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4105', name='The Jazz Performer (Hons)', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC5024', name='Music Research Seminar (B)', school=art, level=5, credits=10)
    Module.objects.create(id='MUSIC5060', name='Introduction to Musicology', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5059', name='Sound Art in Dialogue', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC2027', name='Experimental Music Practice', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC2024', name='Musical Techniques, Foundation Semester One', school=art, level=2,
                          credits=10)
    Module.objects.create(id='MUSIC4011', name='Introduction to Composition for Honours', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC4102', name='Music in History, Culture and Society 2', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC4077', name='Notation', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4090', name='Performance 3', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC5094', name='Music Cities', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC4106', name='Popular Music History', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC2006', name='Musical Techniques, Foundation (MA/BEng/MEng)', school=art, level=2,
                          credits=20)
    Module.objects.create(id='MUSIC4029', name='Performance 2 (Hons)', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4020', name='Musical Techniques, Intermediate (MA/BEng/MEng Hons)', school=art,
                          level=4, credits=20)
    Module.objects.create(id='MUSIC2002', name='Analysis: Formalist Approaches', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC2005', name='Introduction to Composition', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC4081', name='Popular Music Politics', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4104', name='The Jazz Composer (Hons)', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC5077', name='Genders', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5095', name='Popular Music History', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5075', name='Popular Music Politics', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC2025', name='Musical Techniques, Foundation Semester Two', school=art, level=2,
                          credits=10)
    Module.objects.create(id='MUSIC5092', name='Creative Sound Recording', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5015P', name='Music Industries Dissertation', school=art, level=5, credits=60)
    Module.objects.create(id='MUSIC5089', name='Popular Music Research', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC2009', name='Performance Level 2 (Intermediate)', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC5061', name='Current Issues in Musicology', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC2030', name='The Jazz Performer (Pre-Hons)', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC4095P', name='Applied Dissertation in Music', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC5081P', name='Dissertation in Musicology', school=art, level=5, credits=60)
    Module.objects.create(id='MUSIC4085', name='Sonic Arts: Interactive Audiovisual Media', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC5057', name='Sonic Arts Portfolio', school=art, level=5, credits=60)
    Module.objects.create(id='MUSIC5093P', name='Creative Sound & Media Portfolio', school=art, level=5, credits=60)
    Module.objects.create(id='MUSIC5023', name='Music Research Seminar (A)', school=art, level=5, credits=10)
    Module.objects.create(id='MUSIC1020', name='Listening in Culture', school=art, level=1, credits=20)
    Module.objects.create(id='MUSIC2022', name='Sonic Arts: Interacting with Sound (BEng/MEng)', school=art, level=2,
                          credits=20)
    Module.objects.create(id='MUSIC5052', name='Thinking Through Sound and Media', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC1023', name='Introduction to Creative Practice in Music', school=art, level=1,
                          credits=40)
    Module.objects.create(id='MUSIC5056', name='Creative Sound & Media Performance', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC4080', name='Performance Practice', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4083', name='Sonic Arts: Individual Creative Project', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC4087', name='Sonic Arts: Sound for Narrative Film', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC2029', name='The Jazz Composer (Pre-Hons)', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC5058', name='Sound Shaping and Design', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5006', name='Musicology', school=art, level=5, credits=40)
    Module.objects.create(id='MUSIC4076P', name='Music General Paper', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC2007', name='Musical Techniques, Intermediate', school=art, level=2, credits=20)
    Module.objects.create(id='MUSIC4079', name='Performance 4 (40)', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC4084', name='Sonic Arts: Interacting with Sound (MA/BMus/BEng/MEng Hons)',
                          school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4001', name='Aesthetics And Philosophy Of Music (MA/BEng/MEng/BMus Hons)',
                          school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC2023', name='Sonic Arts: Interacting with Sound (MA/BMus)', school=art, level=2,
                          credits=20)
    Module.objects.create(id='MUSIC4103', name='Composition Higher (40 Credits)', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC1002', name='Musical Techniques, Foundation (BMus)', school=art, level=1, credits=20)
    Module.objects.create(id='MUSIC1021', name='Listening through Analysis', school=art, level=1, credits=20)
    Module.objects.create(id='MUSIC4101', name='Music in History, Culture and Society 1', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC4071P', name='Dissertation in Music', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC4060', name='Genders (30)', school=art, level=4, credits=30)
    Module.objects.create(id='MUSIC4100', name='Song, Singing and Vocality', school=art, level=4, credits=40)
    Module.objects.create(id='MUSIC4073', name='Film Music', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC4002', name='Analysis: Formalist Approaches (Honours)', school=art, level=4,
                          credits=20)
    Module.objects.create(id='MUSIC4072', name='Experimental Music Practice', school=art, level=4, credits=20)
    Module.objects.create(id='MUSIC2001', name='Aesthetics And Philosophy Of Music (APM)', school=art, level=2,
                          credits=20)
    Module.objects.create(id='MUSIC5053', name='Audiovisual Composition', school=art, level=5, credits=20)
    Module.objects.create(id='MUSIC5062', name='Research Skills and Digital Musicology', school=art, level=5,
                          credits=20)
    Module.objects.create(id='MUSIC5096', name='The Global Music Industries', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4092', name='Digital Art and Performance (30 Credits)', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE2003', name='Theatre Studies 2B: Thinking Through Theatre Making', school=art,
                          level=2, credits=20)
    Module.objects.create(id='THEATRE4003', name='Autobiography And Performance', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5004', name='Theatre Studies PGT Work Placement', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4008', name='Modern German Theatre', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5032', name='Theatre Archive Placement', school=art, level=5, credits=40)
    Module.objects.create(id='THEATRE4100', name='Issues in Victorian and Edwardian Theatre', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE5040', name='Scottish Theatre: Place, Politics, and Practices', school=art,
                          level=5, credits=20)
    Module.objects.create(id='THEATRE4093', name='Digital Art and Performance (20 Credits)', school=art, level=4,
                          credits=20)
    Module.objects.create(id='THEATRE4009', name='Performance Theory and Analysis', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5039', name='21st Century Theatre in Britain: New Writing in Context', school=art,
                          level=5, credits=20)
    Module.objects.create(id='THEATRE4089', name='Making Theatre for Philosophers', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5042', name='Digital Art and Performance (20 Credits)', school=art, level=5,
                          credits=20)
    Module.objects.create(id='THEATRE4096', name='Postcolonial Encounters', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4012P', name='Theatre Studies Dissertation', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5001', name='Debating Dramaturgy', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4087', name='Advanced Theatre Making', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4036', name='Live Art: Histories, Theories & Practices', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE4079', name='Interwar Cultures', school=art, level=4, credits=20)
    Module.objects.create(id='THEATRE5028', name='Contemporary Dramaturgical Practices', school=art, level=5,
                          credits=20)
    Module.objects.create(id='THEATRE5007', name='Playwriting 2', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4082', name='Applied Theatre and Social Arts', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4030', name='Documentary Drama', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4083', name='Shaping Futures: Theatre and Cultural Policy', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE4097', name='Theatre in Scotland', school=art, level=4, credits=12)
    Module.objects.create(id='THEATRE4076', name='Queer Exceptions', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4011', name='Space, Place And Performance', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4101', name='Interwar Cultures', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4081', name='Arts Criticism (30 credits)', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4016', name='Writing For Performance', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5034', name='Queer Exceptions', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE1002', name='Theatre Studies 1: Theatre And Society', school=art, level=1,
                          credits=20)
    Module.objects.create(id='THEATRE4080', name='Arts Criticism', school=art, level=4, credits=10)
    Module.objects.create(id='THEATRE4073', name='Practising Location: Space, Place and Landscape', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE5005P', name='Individual Research Project (Dramaturgy)', school=art, level=5,
                          credits=60)
    Module.objects.create(id='THEATRE5041', name='Applied Theatre: Contextual Practices and Critical Pedagogies',
                          school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE5006', name='Playwriting 1', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4090', name='21st Century Theatre in Britain: New Writing in Context', school=art,
                          level=4, credits=30)
    Module.objects.create(id='THEATRE4085', name='Performing Character', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4014', name='Theatre Studies Single Honours Group Project', school=art, level=4,
                          credits=30)
    Module.objects.create(id='THEATRE5009', name='Research Methods', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4006', name='Devising', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE2001', name='Theatre Studies 2A: Thinking Through Theatre Histories', school=art,
                          level=2, credits=20)
    Module.objects.create(id='THEATRE4071', name='The Activist Stage', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE4086', name='Setting the Scene', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5029', name='Contemporary Devising Practices', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE5038', name='Professional Practice', school=art, level=5, credits=20)
    Module.objects.create(id='THEATRE4015', name='Theatre Studies Work Placement', school=art, level=4, credits=30)
    Module.objects.create(id='THEATRE5030', name='Independent Practice', school=art, level=5, credits=40)
    Module.objects.create(id='THEATRE5033P', name='Practice as Research Project', school=art, level=5, credits=60)
    Module.objects.create(id='THEATRE1001', name='Theatre Studies 1: Reading The Stage', school=art, level=1,
                          credits=20)

    # School of Education (272 modules)
    Module.objects.create(id='ADED5077', name='International Issues in Adult Education (IMAESC)', school=education,
                          level=5, credits=10)
    Module.objects.create(id='EDUC51007',
                          name='Local and Global Theories and Perspectives on Learning in Diverse Contexts',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC5401P', name='Dissertation', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC1095', name='Access to a Career Programme (Online Module)', school=education, level=1,
                          credits=15)
    Module.objects.create(id='EDUC5406', name='Adult Learning for Transformation', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC4091', name='Catholic Teachers\' Certificate PGDE Edinburgh', school=education,
                          level=4, credits=0)
    Module.objects.create(id='EDUC5349', name='Developing Literacies: An Inclusive Perspective', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC51025P', name='Master Dissertation (GLOBED)', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC4104', name='RE (Catholic) Specialism Part 2', school=education, level=4, credits=40)
    Module.objects.create(id='EDUC1033', name='Theology in Education 1', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC51084', name='Dynamics and Dilemmas of Ethical Leadership', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC3094', name='MEduc 3 School Experience', school=education, level=3, credits=10)
    Module.objects.create(id='EDUC3107P', name='Educational Elective 3', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC5835', name='Applied Qualitative Methods (PGT Conv)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC2060', name='Theology In Education 2', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC2095', name='Critical Understanding of Power in Communities', school=education,
                          level=2, credits=20)
    Module.objects.create(id='EDUC5862P', name='Educational Enquiry 4', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC51101', name='New Media for Children and Young Adults CLMC 2023-2024',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC3013', name='Multi-Professional Collaboration In Children\'s Services',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC2107', name='Technology Craft 2', school=education, level=2, credits=10)
    Module.objects.create(id='EDUC1064', name='Engagement Strategies for Community Development', school=education,
                          level=1, credits=20)
    Module.objects.create(id='EDUC3096', name='Children in Society', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC51026', name='International Issues in Adult Education (distance)', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC3097', name='Discourses on Childhood Practice', school=education, level=3, credits=40)
    Module.objects.create(id='EDUC1013', name='Fundamentals Of Education 1B', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC51017',
                          name='Contemporary Research Theory and Methods in Social and Pedagogical Contexts',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC4110P', name='Education and Society 4: Education for a Sustainable Global Future',
                          school=education, level=4, credits=30)
    Module.objects.create(id='EDUC51080', name='Developing as a Middle Leader', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC3087', name='School Experience 3', school=education, level=3, credits=10)
    Module.objects.create(id='EDUC4088', name='Applied Theatre and Social Arts', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC3073P',
                          name='Education in Practice 3: The Primary School as a Site of Teacher Learning',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC2104', name='Engineering 2', school=education, level=2, credits=10)
    Module.objects.create(id='EDUC3088', name='Technology Craft 3', school=education, level=3, credits=10)
    Module.objects.create(id='EDUC5954', name='Cognitive Psychology (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC5910', name='Equity, Social Justice and Change', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC4084P', name='Educational Elective 4', school=education, level=4, credits=30)
    Module.objects.create(id='EDUC51095P', name='IM Dissertation', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC51011', name='Psychology of Adult Learning (IMAESC)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5924', name='Placement - International Master in Adult Education for Social Change',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC3104', name='Curriculum Enquiry 3 Semester Abroad', school=education, level=3,
                          credits=15)
    Module.objects.create(id='EDUC51061', name='International actors and global education policies', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5409', name='International Issues In Adult And Continuing Education',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5404', name='The Impact of Drug and Alcohol Misuse on Children and Families',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51000', name='Modern Educational Thinking', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1090', name='Top-Up programme', school=education, level=1, credits=10)
    Module.objects.create(id='EDUC3084P', name='Education in Practice 3: Study Abroad students', school=education,
                          level=3, credits=10)
    Module.objects.create(id='EDUC5943', name='Curriculum, Assessment and Pedagogy: Understanding Learners',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51068', name='Key Themes in Early Childhood Education and Care', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC51088', name='Leading strategic change in school', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC2118', name='Eportfolios enhancing the professional dialectic', school=education,
                          level=2, credits=30)
    Module.objects.create(id='EDUC5376', name='Professional Enquiry And Decision Making', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC1021', name='Pedagogy And Development In Religious Education', school=education,
                          level=1, credits=15)
    Module.objects.create(id='EDUC3081', name='Introduction to Research for Community Development', school=education,
                          level=3, credits=20)
    Module.objects.create(id='EDUC51065', name='Education in Museums and Heritage: Critical Enquiry', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5346', name='Children\'s Literature And Literacies: Critical Enquiry',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51018', name='Education in Practice 5', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC2121', name='Professional Values for Leadership in Childhood Practice',
                          school=education, level=2, credits=30)
    Module.objects.create(id='EDUC51104P', name='Dissertation (Education)', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC5379', name='Reframing Language, Literature And Literacies For 21St Century Life',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51054', name='Language Learning for Young Multilingual Learners', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC51012', name='Recognising Built Capacity: Career and Impact Pathways',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC1089', name='Academic and Professional Practice for Working in Communities',
                          school=education, level=1, credits=20)
    Module.objects.create(id='EDUC3090P', name='Education in Practice 3: Assessment, Pedagogy and Professionalism',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC5912', name='Higher Education as a Field of Research, Policy and Practice',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5016', name='Applied Catholic Theology (PG)', school=education, level=5, credits=0)
    Module.objects.create(id='EDUC3092P',
                          name='Education & Society L9: The child, education and the global environment',
                          school=education, level=3, credits=30)
    Module.objects.create(id='EDUC5961', name='Applied Qualitative Methods (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC3098', name='Leading Practice', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC4101', name='Technology, Engineering and Society', school=education, level=4,
                          credits=20)
    Module.objects.create(id='EDUC2102', name='Design 2', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC51064', name='Access and Inclusion (International Masters)', school=education,
                          level=5, credits=10)
    Module.objects.create(id='EDUC51037', name='Becoming a Teacher: Connecting, Challenging and Changing',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC1098',
                          name='University of Glasgow Widening Participation Summer School (Academic Skills Module Blended Learning)',
                          school=education, level=1, credits=15)
    Module.objects.create(id='EDUC5356', name='Highly Able Learners, Raising Attainment & Achievement',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5946', name='Theorising Community Practice', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51001', name='Contemporary Themes in Education Policy', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC5049', name='Critical Reflection In Professional Learning And Practice',
                          school=education, level=5, credits=45)
    Module.objects.create(id='EDUC51031', name='Educational Leadership and Management at System Level',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC2096', name='Key Issues and Debates in Childhood Practice A', school=education,
                          level=2, credits=20)
    Module.objects.create(id='EDUC51089',
                          name='Responding to Adversity in Communities: Sex, Drugs, and (Vegan) Sausage Rolls',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1112P', name='Curriculum Enquiry 1B', school=education, level=1, credits=15)
    Module.objects.create(id='EDUC3080', name='Social Justice and Contemporary Issues', school=education, level=3,
                          credits=20)
    Module.objects.create(id='EDUC51097', name='Psychology of Environmental Sustainability', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5412', name='Practice Placement', school=education, level=5, credits=40)
    Module.objects.create(id='EDUC2062', name='Advanced Community Development Practice', school=education, level=2,
                          credits=40)
    Module.objects.create(id='EDUC2119', name='Key Issues in Childhood Practice', school=education, level=2, credits=30)
    Module.objects.create(id='EDUC4109P', name='Curriculum Enquiry 4', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC2054', name='Self-Evaluation And Quality Management', school=education, level=2,
                          credits=20)
    Module.objects.create(id='EDUC51027', name='MEduc Professional Enquiry And Decision Making', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC5423', name='Research Project', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC51067', name='The Museum as a Source for Learning (International Masters)',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51019', name='The Psychology of Adult Learning (online learning)', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC1103', name='Graphics 1', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC3009', name='Leadership, Management And Professional Values', school=education,
                          level=3, credits=20)
    Module.objects.create(id='EDUC51049', name='Sustainable Development and Education', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC51051', name='TESOL Curriculum', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5073', name='Education Policy', school=education, level=5, credits=45)
    Module.objects.create(id='EDUC5909', name='Education and Public Policy', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5908', name='Education Policy in Action', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1012', name='Fundamentals Of Education 1A', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC1097',
                          name='University of Glasgow Widening Participation Summer School (Academic Subject 2)',
                          school=education, level=1, credits=20)
    Module.objects.create(id='EDUC5814P', name='Dissertation for Childhood Practice', school=education, level=5,
                          credits=60)
    Module.objects.create(id='EDUC5840', name='Educational Psychology (PGT Conv)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC51072', name='Education, Race, Racism and Social Justice in a Global Society',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1086', name='CREDL: Aspects of Theological Education 2', school=education, level=1,
                          credits=15)
    Module.objects.create(id='EDUC1106', name='Technology Craft 1', school=education, level=1, credits=10)
    Module.objects.create(id='EDUC3078P', name='Educational Elective 3', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC51003P', name='Dissertation CLMC', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC5999', name='Education Policy and the Politics of Education', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5082', name='Professional Enquiry', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC51038', name='Research and Enquiry-Led Learning and Teaching', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC1102', name='Engineering 1', school=education, level=1, credits=10)
    Module.objects.create(id='EDUC51069', name='Perspectives On Youth And Young Adulthood (ES)', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC51074', name='Comparative Education', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5850', name='Leading Professional Learning', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC3020',
                          name='Professional Enquiry: Sustaining And Communicating Improvements In Practice',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC4113', name='Community, Arts and Media', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC5853', name='Designing and Planning a Practitioner Enquiry', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5410', name='Introduction To Educational And Social Research', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5424', name='Adult Learning Placement', school=education, level=5, credits=40)
    Module.objects.create(id='EDUC51024', name='Advanced Policy Enquiry', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5128', name='Curriculum, Pedagogies and Practice in The Primary', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC5877P', name='Educational Leadership: Dissertation', school=education, level=5,
                          credits=60)
    Module.objects.create(id='EDUC1083', name='What\'s the point of Education? Constructing an Educational Mindset',
                          school=education, level=1, credits=20)
    Module.objects.create(id='EDUC51070', name='Working with Young People: Education and Learning for Change (ES)',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1094', name='Access to a Career Programme (Top-Up Programme)', school=education,
                          level=1, credits=15)
    Module.objects.create(id='EDUC5321', name='The Learner And The Curriculum (DLS)', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC5930', name='Museums, Education and Curriculum Development Online', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC4100', name='Learning and Teaching in Secondary Technology', school=education,
                          level=4, credits=30)
    Module.objects.create(id='EDUC5960', name='Individual Differences (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC5156', name='Modern Educational Thought', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC4114', name='Practices for Sustainability in Community Development', school=education,
                          level=4, credits=20)
    Module.objects.create(id='EDUC2103', name='Electronics 2', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC2120', name='Leading Skills for Childhood Practice', school=education, level=2,
                          credits=30)
    Module.objects.create(id='EDUC5953',
                          name='Shaping professional identity and practice: using critical reflection in the transition to headship',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1066', name='Community Development Practice', school=education, level=1, credits=40)
    Module.objects.create(id='EDUC2106', name='School Experience 2', school=education, level=2, credits=10)
    Module.objects.create(id='EDUC51032', name='Contemporary Perspectives On Children And Childhoods', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC51075', name='Language and Intercultural Education for a Globalised World',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1093', name='Reach (Access to the High Demand Professions)', school=education,
                          level=1, credits=10)
    Module.objects.create(id='EDUC51087', name='Leading Change for Improvement', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC5863P', name='Education and Society 5: Social Justice and Education',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC5900P', name='Major Dissertation (TESOL)', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC4102', name='School Experience 4', school=education, level=4, credits=10)
    Module.objects.create(id='EDUC5824', name='Classroom Processes in TESOL: introduction to teaching and learning',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51094', name='Contemporary Issues in TESOL', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC3105P', name='Educational Elective 3_ Study Abroad', school=education, level=3,
                          credits=10)
    Module.objects.create(id='EDUC4108P', name='Education in Practice 4: Making Learning Happen', school=education,
                          level=4, credits=20)
    Module.objects.create(id='EDUC4097', name='Design 3', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC2117P', name='Education in Practice 2B: Educational Philosophies and Pedagogy',
                          school=education, level=2, credits=15)
    Module.objects.create(id='EDUC51078', name='Equity, Diversity and Inclusion', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC3029', name='School Experience 3', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC5342', name='Practitioner Enquiry; Developing Inclusive Pedagogy', school=education,
                          level=5, credits=40)
    Module.objects.create(id='EDUC5905', name='The Museum as a Source for Learning', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC4086', name='Approaches and Applied Research Methods (BACD4) Honours',
                          school=education, level=4, credits=40)
    Module.objects.create(id='EDUC5053', name='Leadership for 21st Century Learning', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC51102', name='Literature and Picturebooks for Early Years (0-8)', school=education,
                          level=5, credits=10)
    Module.objects.create(id='EDUC5934', name='Principles and Practices of Research', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC2105', name='Graphics 2', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC5405', name='Advanced Educational Research', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51053P', name='Challenge-based dissertation', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC5414', name='The Psychology Of Adult Learning', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC2114', name='MEduc 2 School Experience', school=education, level=2, credits=10)
    Module.objects.create(id='EDUC5386', name='Texts For Diversity: Children\'s Literature for a Diverse World',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC2091', name='What if...? Questioning Education', school=education, level=2,
                          credits=20)
    Module.objects.create(id='EDUC5955', name='Human Development (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC5903', name='Access and Inclusion', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC51008', name='Approaches to Inclusive Learning: Psychology, Knowledge and Curriculum',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC51034', name='Practitioner Enquiry And Decision-Making', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC5952', name='Pursuing equity and excellence in practice', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC5904', name='Museums, Education and Curriculum Development', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC5942', name='Curriculum, Assessment and Pedagogy: International Perspectives',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5823', name='Developing Professional Practice in TESOL', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC5387', name='Evolving Concept Of Inclusive Education', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC3091', name='Curriculum Enquiry 3', school=education, level=3, credits=30)
    Module.objects.create(id='EDUC5839', name='Dissertation (PGT Conv)', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC2113P',
                          name='Education & Society L8: The social and spatia dynamics of childhood education',
                          school=education, level=2, credits=20)
    Module.objects.create(id='EDUC1004', name='Catholic Teachers Certificate (UG)', school=education, level=1,
                          credits=0)
    Module.objects.create(id='EDUC5925P', name='Dissertation', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC1096',
                          name='University of Glasgow Widening Participation Summer School (Academic Subject 1)',
                          school=education, level=1, credits=20)
    Module.objects.create(id='EDUC51077', name='Educational Change for Collaborative Improvement', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5838', name='Cognitive Psychology (PGT Conv)', school=education, level=5, credits=10)
    Module.objects.create(id='EDUC5870', name='Clinical Health Psychology (PGT Conv)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC1065', name='Understanding Society , Community and Ideology', school=education,
                          level=1, credits=20)
    Module.objects.create(id='EDUC51010', name='Introduction to Adult Education for Social Change', school=education,
                          level=5, credits=10)
    Module.objects.create(id='EDUC51086P', name='Developing as an Agent of Change', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC2101', name='Education in Practice (Secondary) 2', school=education, level=2,
                          credits=30)
    Module.objects.create(id='EDUC4094', name='Community Development Responses to exclusion and marginalisation',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC51076', name='Fundamentals of Formal Education', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC3021', name='Professional Enquiry: Taking Action And Making An Intervention',
                          school=education, level=3, credits=20)
    Module.objects.create(id='EDUC5290', name='Identities, Relationships and Behaviours in Education', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5408', name='Collective Learning and Action for Social Justice', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5843', name='Individual Differences (PGT Conv)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC2111P', name='Curriculum Enquiry 2A', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC1100', name='Design 1', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC3045', name='Technology Craft Workshops T3', school=education, level=3, credits=10)
    Module.objects.create(id='EDUC4090', name='Catholic Teachers\' Certificate PGDE Strathclyde', school=education,
                          level=4, credits=0)
    Module.objects.create(id='EDUC5933', name='Education Dissertation', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC51090', name='Ethics and Research in Communities', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC1032', name='Theological Education And Personal Development', school=education,
                          level=1, credits=15)
    Module.objects.create(id='EDUC3034', name='Social And Cultural Concepts Of Childhood', school=education, level=3,
                          credits=20)
    Module.objects.create(id='EDUC2112P', name='Curriculum Enquiry 2B', school=education, level=2, credits=20)
    Module.objects.create(id='EDUC5249', name='Policy Enquiry And Decision-Making', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC4087', name='Research Project (BACD4) Honours', school=education, level=4, credits=40)
    Module.objects.create(id='EDUC5937', name='Dynamics and Dilemmas of Ethical Leadership', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC51009',
                          name='Teaching and learning practice for youth, community, and adult contexts',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC51063', name='Trauma and mental wellbeing in young people', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5846', name='Which English? Language Teaching And Sociolinguistics', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5923', name='Children\'s Literature for a Diverse World', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5415', name='Working with Young People: Education and Learning for Change',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC2097', name='Key Issues and Debates in Childhood Practice B', school=education,
                          level=2, credits=40)
    Module.objects.create(id='EDUC5333', name='Working Collaboratively: Teacher Leadership 2', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5944', name='Professional and Ethical Practice in Leading Community Organisations',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1101', name='Electronics 1', school=education, level=1, credits=20)
    Module.objects.create(id='EDUC5384', name='Texts For Children and Young People', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC51020', name='Education for All: Inclusive Special Education', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5876P', name='Education in Practice 5', school=education, level=5, credits=30)
    Module.objects.create(id='EDUC5842', name='Developmental Psychology (PGT Conv)', school=education, level=5,
                          credits=10)
    Module.objects.create(id='EDUC5845', name='Course Design And Practice in TESOL', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC51073', name='Vocational Education and Training for Development', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC3106', name='Curriculum Enquiry 3 Semester 2 Abroad', school=education, level=3,
                          credits=20)
    Module.objects.create(id='EDUC51071', name='Great Thinkers on Education', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5849', name='Language Proficiency, Assessment And Feedback', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC1113P', name='Education in Practice 1B: Theories of Child Development',
                          school=education, level=1, credits=15)
    Module.objects.create(id='EDUC51081', name='Developing as a strategic leader in school', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC5935', name='Research Application', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1109P', name='Education in Practice 1A: Learning and Values', school=education,
                          level=1, credits=15)
    Module.objects.create(id='EDUC5285', name='Seminars In Contemporary Issues', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5407', name='Community-Based Group Work', school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51050', name='Teaching English as an International Language', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC2116P', name='Education in Practice 2A: Learning through Curriculum',
                          school=education, level=2, credits=15)
    Module.objects.create(id='EDUC1105', name='Education in Practice (Secondary) 1', school=education, level=1,
                          credits=30)
    Module.objects.create(id='EDUC4098', name='Engineering 3', school=education, level=4, credits=10)
    Module.objects.create(id='EDUC2077', name='Popular Education: Theory and Practice', school=education, level=2,
                          credits=20)
    Module.objects.create(id='EDUC1056', name='Introduction to Community Development', school=education, level=1,
                          credits=20)
    Module.objects.create(id='EDUC3086', name='Education in Practice (Secondary) 3', school=education, level=3,
                          credits=30)
    Module.objects.create(id='EDUC1104', name='School Experience 1', school=education, level=1, credits=10)
    Module.objects.create(id='EDUC5945P', name='Practitioner Research Project', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC5962', name='Clinical Health Psychology (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC5428', name='Youth Work: Working with Young People for Positive Change',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1111P', name='Curriculum Enquiry 1A', school=education, level=1, credits=15)
    Module.objects.create(id='EDUC5858', name='International and Comparative Education', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC51033', name='Leadership, values and vision (with Practice Placement)',
                          school=education, level=5, credits=30)
    Module.objects.create(id='EDUC3049', name='Community Development Placement', school=education, level=3, credits=40)
    Module.objects.create(id='EDUC5959', name='Economics for Education and Public Policy', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC1085', name='CREDL: Aspects of Theological Education 1', school=education, level=1,
                          credits=15)
    Module.objects.create(id='EDUC4096', name='Education in Practice (Secondary) 4', school=education, level=4,
                          credits=30)
    Module.objects.create(id='EDUC5848', name='Language Learning And Applications To The Classroom', school=education,
                          level=5, credits=20)
    Module.objects.create(id='EDUC5378P', name='Professional Practice: Dissertation', school=education, level=5,
                          credits=60)
    Module.objects.create(id='EDUC51021', name='Working together to create inclusive learning environments',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC5964', name='Educational Psychology (Conversion) (Online Distance Learning)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC4112', name='MEduc 4 School Experience', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC5129', name='Curriculum, Pedagogies and Practice in The Secondary', school=education,
                          level=5, credits=30)
    Module.objects.create(id='EDUC3052', name='Space, Place and Community', school=education, level=3, credits=20)
    Module.objects.create(id='EDUC51052P',
                          name='Exploring, Designing and Practicing Post Colonial Narratives in Education',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC51066', name='Museums, Education and Curriculum Development (International Masters)',
                          school=education, level=5, credits=10)
    Module.objects.create(id='EDUC51035', name='Pedagogy, practice and leadership', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC3005', name='Educational Research', school=education, level=3, credits=10)
    Module.objects.create(id='EDUC5142P', name='Major Dissertation (Education)', school=education, level=5, credits=60)
    Module.objects.create(id='EDUC4095', name='Philosophy of Design and Technology Education', school=education,
                          level=4, credits=20)
    Module.objects.create(id='EDUC2078', name='Challenge,Change and Action for Social Change', school=education,
                          level=2, credits=20)
    Module.objects.create(id='EDUC2098',
                          name='Connecting Local and Global contexts in Community Development (study trip)',
                          school=education, level=2, credits=20)
    Module.objects.create(id='EDUC51083', name='Doing and Using Research for Practice', school=education, level=5,
                          credits=30)
    Module.objects.create(id='EDUC5911', name='Education and International Development', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC3099', name='Leading in Intergrated Children\'s Services', school=education, level=3,
                          credits=20)
    Module.objects.create(id='EDUC5359', name='Inclusive Classrooms, Inclusive Pedagogies', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC4099', name='Graphics 3', school=education, level=4, credits=20)
    Module.objects.create(id='EDUC51062', name='Internationalisation of Education', school=education, level=5,
                          credits=20)
    Module.objects.create(id='EDUC5847', name='Descriptions Of Language And Applications To The Classroom',
                          school=education, level=5, credits=20)
    Module.objects.create(id='EDUC1099',
                          name='University of Glasgow Widening Participation Summer School (Academic Skills Module Online Only)',
                          school=education, level=1, credits=15)
    Module.objects.create(id='EDUC4014', name='PGDE School Experience', school=education, level=4, credits=30)
    Module.objects.create(id='PHIL3010', name='Philosophy Of Religion', school=education, level=3, credits=20)

    # School of Engineering (383 modules)
    Module.objects.create(id='ENG4026', name='Architecture C4', school=engineering, level=4, credits=30)
    Module.objects.create(id='ENG4153', name='Mechatronic Team Project 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5291', name='Signal Processing of Biosignatures M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG3082', name='Construction Management 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4085', name='Business Planning and Management for Engineers', school=engineering,
                          level=4, credits=20)
    Module.objects.create(id='ENG2053', name='Thermodynamics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4098', name='Microelectronics in Consumer Products 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5325', name='Robotics Team Design Project M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG3027', name='Engineering Career Skills 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG1063', name='Engineering Mathematics 1', school=engineering, level=1, credits=40)
    Module.objects.create(id='ENG5031', name='Fault Detection, Isolation And Recovery', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG4173', name='Renewable and Sustainable Energy 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG4181', name='Biophysics of Cells and Systems 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5264', name='Aerospace Design Project M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4196', name='Rotorcraft Aeromechanics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5092', name='VLSI Design M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5174', name='Nanofabrication', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5026', name='Design Special Topic 5', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5029', name='Electrical Energy Systems M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG3043', name='Real Time Computer Systems 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3053', name='Thermodynamics of Energy Systems 3', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='ENG2026', name='Electronic Devices 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4188', name='Geotechnical Design Project 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4203', name='Appraisal of Existing Structures', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG4184', name='Navigation Systems 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5048', name='Industrial Aerodynamics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4206', name='Spacecraft Systems 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5027', name='Digital Signal Processing', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG3030', name='Fluid Mechanics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5275', name='Reclamation of Contaminated Land 5', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG3039', name='Dynamics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3046', name='Structural Design 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5062', name='Navigation Systems M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4066P', name='Final Year Project ESE4', school=engineering, level=4, credits=40)
    Module.objects.create(id='ENG3017', name='Mechanical Design 3', school=engineering, level=3, credits=20)
    Module.objects.create(id='ENG5224', name='Advanced Concrete Performance M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4172', name='Team Project EE4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5311', name='Fundamentals of Manufacturing and CAD', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG3049', name='Team Design Project EE3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5274', name='Adv. Structural Analysis & Earthquake Engineering 5', school=engineering,
                          level=5, credits=10)
    Module.objects.create(id='ENG5314', name='Control Systems Analysis and Design M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG4099', name='Quantum Electronic Devices 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG3062', name='Aircraft Structural Analysis and Design 3', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='ENG3015', name='Control 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4187', name='Power Electronics and Drives 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5096', name='Advanced Manufacture', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG2083', name='Introductory Programming 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4202', name='Engineering Optimisation', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4104', name='Power Systems 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG3034', name='Instrumentation and Data Systems 3', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='ENG5297', name='Insights to Industry', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4200', name='Introduction to Artificial Intelligence and Machine Learning 4',
                          school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG2077', name='Engineering Skills 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4185', name='Radar and Electro-Optic Systems 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG4183', name='Transportation Engineering 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG2078', name='Environmental Processes 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5263', name='Aeroelasticity and Aeroacoustics 5', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5321', name='Entrepreneurship in Biomedical Engineering', school=engineering, level=5,
                          credits=20)
    Module.objects.create(id='ENG5091', name='Physics of Fluids M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5338', name='Introduction to Artificial Intelligence and Machine Learning M',
                          school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5302', name='Ultrasound Technology and Applications', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5059P', name='MSc Project', school=engineering, level=5, credits=60)
    Module.objects.create(id='ENG4042', name='Control 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5052', name='Materials Engineering', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4110P', name='Individual Project 4', school=engineering, level=4, credits=30)
    Module.objects.create(id='ENG5278', name='Advanced Aerothermodynamics 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5326', name='Robotics M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5313', name='Aerospace Propulsion M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5227', name='Structures under Extreme Loads M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5273', name='Conceptual Design Project M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG4152', name='Environmental Biotechnology 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG3014', name='Communication Systems 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4036', name='Biosensors and Diagnostics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG3001', name='Aerodynamics and Fluid Mechanics 3', school=engineering, level=3,
                          credits=20)
    Module.objects.create(id='ENG4079', name='Industrial Aerodynamics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG2004', name='Analogue Electronics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4025', name='Finite Element Analysis 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG1022', name='Electronic Engineering 1Y', school=engineering, level=1, credits=20)
    Module.objects.create(id='ENG1003', name='Analogue Electronics 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG3059', name='Aircraft Performance 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4193', name='Ultrasound Technology and Applications 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5009', name='Advanced Control 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2087', name='Engineering in Biology 2', school=engineering, level=2, credits=20)
    Module.objects.create(id='ENG5012', name='Aerospace Systems Team Design Project M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5220', name='Real Time Embedded Programming', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5293', name='Water and Environment Design', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5277', name='Architecture C5', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG4102', name='Physics Of Fluids 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG3080', name='Environmental Process Engineering 3', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='ENG1033', name='Materials 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG3023', name='Electromagnetic Compatiblity 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3085', name='Engineering Hydraulics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5043', name='Integrated Engineering Design', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG4113', name='Rehabilitation Engineering 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4100', name='Microwaves & Optical Transmission Systems 4', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='ENG2071', name='Structural Design Project 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5292', name='Power Electronics and Drives M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5066', name='Optical Communications', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5330', name='Advanced Steel and Concrete Design M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG2079', name='Civil Engineering Skills 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5285', name='Advanced Imaging and Therapy M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4088', name='Lasers and Electro-Optic Systems 4', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='ENG5308', name='Biophysics of Cells and Systems M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5055', name='Micro & Nano Technology', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5276', name='Advanced Manufacture 5', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG1015', name='Design and Manufacture 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG3071', name='Mechatronic Team Project 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5280', name='Turbulent Flows 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG1027', name='Environmental Engineering 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG5250', name='Energy Conversion Systems M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3091', name='Advanced Programming and Software Engineering 3', school=engineering,
                          level=3, credits=10)
    Module.objects.create(id='ENG3007', name='Architecture C3', school=engineering, level=3, credits=30)
    Module.objects.create(id='ENG2088', name='Optical Engineering 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5319', name='Ultrasonic Engineering Technology and Applications', school=engineering,
                          level=5, credits=10)
    Module.objects.create(id='ENG5341', name='Aircraft Development 5', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5261', name='Quantum Electronic Devices M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG4195', name='Control Systems Analysis and Design 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG2090', name='Engineering Study Abroad (UESTC) 2', school=engineering, level=2,
                          credits=60)
    Module.objects.create(id='ENG2016', name='Mechanical Design 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4004', name='Materials Engineering 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5041P', name='Individual Project 5', school=engineering, level=5, credits=60)
    Module.objects.create(id='ENG2081', name='Mechanics of Structures 2A', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4013', name='Aerospace Design Project 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5322', name='Engineering Skills M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2008', name='Architecture C2', school=engineering, level=2, credits=20)
    Module.objects.create(id='ENG5332', name='Waste Heat and Power-to-X', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5328', name='Ultrasonic Engineering Case Study', school=engineering, level=5,
                          credits=20)
    Module.objects.create(id='ENG2031', name='Engineering Electromagnetics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG1061', name='Civil Engineering 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG3036', name='Simulation of Engineering Systems 3', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='ENG5014', name='Aircraft Handling Qualities and Control 5', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG3037', name='Mechanics of Solids 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG2039', name='Materials 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5334', name='Quantum Materials M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2012', name='Biomedical Engineering Skills 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG2085', name='Fluid Mechanics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG2042', name='Mathematics AE2X', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG3086', name='Transport Engineering 3: Urban Streets and Highways', school=engineering,
                          level=3, credits=10)
    Module.objects.create(id='ENG2011', name='Biomaterials 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4205', name='Introduction to Battery Technology', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5288', name='Biosensors and Diagnostics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG1021', name='Electronic Engineering 1X', school=engineering, level=1, credits=20)
    Module.objects.create(id='ENG5336', name='Digital Communications M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG3041', name='Power Engineering 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4053', name='Digital Signal Processing 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG4118', name='Robotics 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5144', name='Introduction to Research In Nanoscience and Nanotechnology',
                          school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4194', name='Aerospace Propulsion 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4189', name='Bioethics for Biomedical Engineering 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG2047', name='Soil Mechanics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG3075', name='Structural Design Project 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG1071', name='Biomolecular Processes in Bioengineering 1', school=engineering, level=1,
                          credits=10)
    Module.objects.create(id='ENG2080', name='Geology and Surveying for Civil Engineers 2', school=engineering, level=2,
                          credits=10)
    Module.objects.create(id='ENG4191', name='Signal Processing of Biosignatures 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5072', name='Radar and Electro-Optic Systems M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5324', name='Research Methods and Practice Group Project M', school=engineering,
                          level=5, credits=20)
    Module.objects.create(id='ENG5017', name='Autonomous Vehicle Guidance Systems M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG2084', name='Dynamics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG2023', name='Electrical Circuits 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG2048', name='Structural Design 2', school=engineering, level=2, credits=20)
    Module.objects.create(id='ENG3060', name='Flight Mechanics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3073', name='Geotechnical Engineering 3', school=engineering, level=3, credits=20)
    Module.objects.create(id='ENG5019', name='Composite Airframe Structures', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5294', name='Finite Element Analysis M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5090', name='Vibration', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG3081', name='Aircraft Structural Mechanics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4067', name='Flight Dynamics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG1016', name='Mechanical Design 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG5303', name='Advanced Thermal Engineering 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3038', name='Microscopy and Optics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4192', name='Hydraulics and Hydrology 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG1008', name='Architecture C1', school=engineering, level=1, credits=20)
    Module.objects.create(id='ENG5337', name='Advanced Artificial Intelligence and Machine Learning 5',
                          school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5316', name='Advanced Ultrasonics', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4072', name='Rock Mechanics and Engineering 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG1002', name='Aerospace Engineering 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG1064', name='Microelectronic Systems 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG4023', name='Aircraft Vibration and Aeroelasticity 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG4014', name='Aerospace Design Project 4M', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5329P', name='MSc Project (Chinese Campus)', school=engineering, level=5, credits=60)
    Module.objects.create(id='ENG5300', name='Materials Engineering 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5281', name='Energy in Biological Systems M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5022', name='Control M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG1062', name='Dynamics 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG4012', name='Aerospace Systems Design Project 4', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='ENG5088', name='Structures in Action M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2086', name='Engineering Mathematics 2', school=engineering, level=2, credits=20)
    Module.objects.create(id='ENG4179', name='Thermal Engineering 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5076', name='Simulation Of Aerospace Systems', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2045', name='Power Electronics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5013', name='Flight Dynamics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4052', name='Digital Communication 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG3092', name='Mechanical Engineering Skills 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4037', name='Computational Fluid Dynamics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4094', name='Mechanics of Solids 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5282', name='Scaffolds and Tissues M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3042', name='Propulsion & Turbomachinery 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG4138', name='VLSI Design 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG5287', name='Biomechanics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3047', name='Structural Mechanics 3', school=engineering, level=3, credits=20)
    Module.objects.create(id='ENG3090', name='Biomedical Engineering Skills 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3025', name='Electronic Devices 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG1031', name='Introduction To Biomedical Engineering 1', school=engineering, level=1,
                          credits=10)
    Module.objects.create(id='ENG3084', name='Biomechanics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5049', name='Lasers', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG5318', name='Materials for Acoustics and Applications', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5289', name='Microscopy and Optics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG2015', name='Design and Manufacture 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5082', name='Space Flight Dynamics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4186', name='Mechanical Design 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG2082', name='Mechanics of Structures 2B', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG1065', name='Statics 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG3011', name='Biological Fluid Mechanics 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5312', name='Introduction to Advanced Manufacturing', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG5056', name='Microwave and Millimetre Wave Circuit Design', school=engineering,
                          level=5, credits=20)
    Module.objects.create(id='ENG3076', name='Civil Design Projects 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG2029', name='Embedded Processors 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG3024', name='Electronic Circuit Design 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG2037', name='Aerodynamics & Aircraft Performance 2', school=engineering, level=2,
                          credits=10)
    Module.objects.create(id='ENG5286', name='Biological Fluid Mechanics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3006', name='Aircraft Design 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5265', name='Rotorcraft Aeromechanics M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5284', name='Advanced Soil Mechanics 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4001', name='Acoustics and Audio Technology 4', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='ENG4050', name='Civil Design Project 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG4074', name='High Speed Aerodynamics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG1026', name='Engineering Skills 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG5283', name='Civil Design Project M', school=engineering, level=5, credits=20)
    Module.objects.create(id='ENG4175', name='Autonomous Vehicle Guidance Systems 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG4121', name='Space Flight Dynamics 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5299', name='Dynamics 5', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG5290', name='Rehabilitation Engineering M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG3005', name='Aerospace Team Design Project 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG2025', name='Electronic Design Project 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG1066', name='Thermodynamics 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='ENG2020', name='Digital Electronics 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG4070', name='Geotechnical Engineering 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG4201', name='Public Engagement and Teaching in Engineering 4', school=engineering,
                          level=4, credits=10)
    Module.objects.create(id='ENG2002', name='Aerospace Design Project 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='ENG5307', name='Computational and Experimental Fluid Dynamics 5', school=engineering,
                          level=5, credits=10)
    Module.objects.create(id='ENG4122', name='Structural Analysis 4', school=engineering, level=4, credits=10)
    Module.objects.create(id='ENG5342', name='Mission Design & Development M', school=engineering, level=5, credits=10)
    Module.objects.create(id='ENG4124', name='Advanced Steel and Concrete Design 4', school=engineering, level=4,
                          credits=10)
    Module.objects.create(id='ENG5053', name='Mechanics Of Solids And Structures', school=engineering, level=5,
                          credits=20)
    Module.objects.create(id='ENG4137', name='Vibration 4', school=engineering, level=4, credits=20)
    Module.objects.create(id='ENG3026', name='Electronic System Design 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG5044', name='Integrated Systems Design Project M', school=engineering, level=5,
                          credits=10)
    Module.objects.create(id='ENG3032', name='Heat Transfer 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='ENG3035', name='Design and Manufacture 3', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN3022', name='Professional Software Development', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='UESTCHN1008', name='Physics I (UESTC)', school=engineering, level=1, credits=14)
    Module.objects.create(id='UESTCHN4011', name='Microwave Integrated Circuits', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN4023', name='Operating Systems', school=engineering, level=4, credits=10)
    Module.objects.create(id='UESTCHN1012', name='English for Academic and General Purposes (UESTC)',
                          school=engineering, level=1, credits=40)
    Module.objects.create(id='UESTCHN2010', name='Semiconductor Physics (UESTC)', school=engineering, level=2,
                          credits=18)
    Module.objects.create(id='UESTCHN2011', name='Signals and Systems (UESTC)', school=engineering, level=2, credits=20)
    Module.objects.create(id='UESTCHN3014', name='Power Electronics', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN2012', name='Computing Fundamentals', school=engineering, level=2, credits=10)
    Module.objects.create(id='UESTCHN4019', name='Digital Image Processing and Application (UESTC)', school=engineering,
                          level=4, credits=20)
    Module.objects.create(id='UESTCHN2001', name='Application and Design of Digital Logic (UESTC)', school=engineering,
                          level=2, credits=16)
    Module.objects.create(id='UESTCHN2005', name='English Communication and Engineering Career Skills',
                          school=engineering, level=2, credits=20)
    Module.objects.create(id='UESTCHN2015', name='Networks and Operating Systems Essentials 2', school=engineering,
                          level=2, credits=10)
    Module.objects.create(id='UESTCHN1002', name='Calculus I (UESTC)', school=engineering, level=1, credits=20)
    Module.objects.create(id='UESTCHN2014', name='Introduction to Object Oriented Programming', school=engineering,
                          level=2, credits=10)
    Module.objects.create(id='UESTCHN4005', name='Digital Signal Processing (UESTC)', school=engineering, level=4,
                          credits=16)
    Module.objects.create(id='UESTCHN4001', name='Advanced Digital Communication', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN3009', name='Electronic System Design', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN3023', name='Systems Programming', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN4021', name='Cloud Systems', school=engineering, level=4, credits=10)
    Module.objects.create(id='UESTCHN3019', name='Algorithms & Data Structures 2', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='UESTCHN2016', name='Object-Oriented Software Engineering 2', school=engineering, level=2,
                          credits=10)
    Module.objects.create(id='UESTCHN1011', name='English for Engineering Studies B (UESTC)', school=engineering,
                          level=1, credits=20)
    Module.objects.create(id='UESTCHN2007', name='Physical Experiment II (UESTC)', school=engineering, level=2,
                          credits=6)
    Module.objects.create(id='UESTCHN3004', name='Communication Circuit Design', school=engineering, level=3,
                          credits=20)
    Module.objects.create(id='UESTCHN3011', name='Engineering and the Law', school=engineering, level=3, credits=15)
    Module.objects.create(id='UESTCHN4012', name='Mobile Communications (UESTC)', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN4008P', name='Individual Project', school=engineering, level=4, credits=32)
    Module.objects.create(id='UESTCHN4010', name='Microelectronic Packaging Technology (UESTC)', school=engineering,
                          level=4, credits=10)
    Module.objects.create(id='UESTCHN4017', name='Wireless Sensor Networks', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN1007', name='Physical Experiment I (UESTC)', school=engineering, level=1,
                          credits=6)
    Module.objects.create(id='UESTCHN2003', name='Communication Networks (UESTC)', school=engineering, level=2,
                          credits=16)
    Module.objects.create(id='UESTCHN3002', name='Artificial Intelligence & Machine Learning', school=engineering,
                          level=3, credits=10)
    Module.objects.create(id='UESTCHN3020', name='Artificial Intelligence', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN1006', name='Microelectronic Systems', school=engineering, level=1, credits=10)
    Module.objects.create(id='UESTCHN3012', name='Engineering Project Management and Finance (UESTC)',
                          school=engineering, level=3, credits=15)
    Module.objects.create(id='UESTCHN1005', name='Introductory Programming', school=engineering, level=1, credits=10)
    Module.objects.create(id='UESTCHN3016', name='Stochastic Signal Analysis (UESTC)', school=engineering, level=3,
                          credits=8)
    Module.objects.create(id='UESTCHN4009', name='Information Security', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN4014', name='Real Time Computing Systems and Architecture', school=engineering,
                          level=4, credits=20)
    Module.objects.create(id='UESTCHN1001', name='Linear Algebra and Space Analytic Geometry I (UESTC)',
                          school=engineering, level=1, credits=14)
    Module.objects.create(id='UESTCHN4007', name='Electromagnetic Field and Microwave Technology (UESTC)',
                          school=engineering, level=4, credits=16)
    Module.objects.create(id='UESTCHN3005', name='Communication Principles and Systems', school=engineering, level=3,
                          credits=16)
    Module.objects.create(id='UESTCHN1010', name='English for Engineering Studies A (UESTC)', school=engineering,
                          level=1, credits=30)
    Module.objects.create(id='UESTCHN4022', name='Cybersecurity Fundamentals', school=engineering, level=4, credits=10)
    Module.objects.create(id='UESTCHN2009', name='Probability Theory and Mathematical Statistics (UESTC)',
                          school=engineering, level=2, credits=14)
    Module.objects.create(id='UESTCHN4016', name='Wireless & Optical Transmission Systems', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN2008', name='Physics II (UESTC)', school=engineering, level=2, credits=14)
    Module.objects.create(id='UESTCHN3001', name='Application and Design of Digital Logic 3 (UESTC)',
                          school=engineering, level=3, credits=18)
    Module.objects.create(id='UESTCHN3015', name='Signals and Systems (UESTC)', school=engineering, level=3, credits=20)
    Module.objects.create(id='UESTCHN1013', name='Computing Science 1', school=engineering, level=1, credits=10)
    Module.objects.create(id='UESTCHN3013', name='Micro & Nano Technology', school=engineering, level=3, credits=16)
    Module.objects.create(id='UESTCHN3018', name='Team Design Project and Skills (UESTC only)', school=engineering,
                          level=3, credits=10)
    Module.objects.create(id='UESTCHN4003', name='Design of Integrated Circuits', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN1003', name='Calculus II (UESTC)', school=engineering, level=1, credits=20)
    Module.objects.create(id='UESTCHN2002', name='Circuit Analysis and Design', school=engineering, level=2, credits=18)
    Module.objects.create(id='UESTCHN3021', name='Data Fundamentals', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN2006', name='Fundamentals of Analogue Circuits (UESTC)', school=engineering,
                          level=2, credits=18)
    Module.objects.create(id='UESTCHN4004', name='Design of Photonic Integrated Circuits', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTCHN4006', name='Digital Communication', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN4018P', name='Individual Project (UESTC only)', school=engineering, level=4,
                          credits=32)
    Module.objects.create(id='UESTCHN3003', name='Comprehensive Experiment of Modern Electronic Technology (UESTC)',
                          school=engineering, level=3, credits=8)
    Module.objects.create(id='UESTCHN4002', name='Control Engineering', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN3010', name='Elements of Information Theory (UESTC)', school=engineering, level=3,
                          credits=8)
    Module.objects.create(id='UESTCHN3008', name='Electronic Devices', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN4013', name='Power Semiconductor Device and Integration Technology (UESTC)',
                          school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN3017', name='Team Design Project and Skills', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='UESTCHN4015', name='VLSI Design', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTCHN3007', name='Dynamics and Control', school=engineering, level=3, credits=12)
    Module.objects.create(id='UESTCHN3006', name='Digital Circuit Design', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTCHN2013', name='Computing Science 2', school=engineering, level=2, credits=10)
    Module.objects.create(id='UESTCHN2004', name='Embedded Processors', school=engineering, level=2, credits=10)
    Module.objects.create(id='UESTC3030', name='Engineering and the Law', school=engineering, level=3, credits=15)
    Module.objects.create(id='UESTC4037', name='Microwave Integrated Circuits', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC4017', name='Mobile Communications (UESTC)', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC2018', name='Communication Networks (UESTC)', school=engineering, level=2,
                          credits=16)
    Module.objects.create(id='UESTC3031', name='Engineering Project Management and Finance (UESTC)', school=engineering,
                          level=3, credits=15)
    Module.objects.create(id='UESTC4020', name='Wireless Sensor Networks', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC3018', name='Communication Principles and Systems', school=engineering, level=3,
                          credits=16)
    Module.objects.create(id='UESTC1008', name='Microelectronic Systems', school=engineering, level=1, credits=10)
    Module.objects.create(id='UESTC3007', name='Signals and Systems (UESTC)', school=engineering, level=3, credits=20)
    Module.objects.create(id='UESTC4021P', name='Individual Project (UESTC only)', school=engineering, level=4,
                          credits=32)
    Module.objects.create(id='UESTC1006', name='Physical Experiment I (UESTC)', school=engineering, level=1, credits=6)
    Module.objects.create(id='UESTC1002', name='Calculus I (UESTC)', school=engineering, level=1, credits=20)
    Module.objects.create(id='UESTC4033', name='Design of Integrated Circuits', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC2019', name='Solid State Lighting (G)', school=engineering, level=2, credits=10)
    Module.objects.create(id='UESTC2005', name='Fundamentals of Analogue Circuits (UESTC)', school=engineering, level=2,
                          credits=18)
    Module.objects.create(id='UESTC3010', name='Team Design Project and Skills', school=engineering, level=3,
                          credits=10)
    Module.objects.create(id='UESTC2012', name='Probability Theory and Mathematical Statistics (UESTC)',
                          school=engineering, level=2, credits=14)
    Module.objects.create(id='UESTC1033', name='English for Academic and General Purposes (UESTC)', school=engineering,
                          level=1, credits=40)
    Module.objects.create(id='UESTC4035', name='Digital Image Processing and Application (UESTC)', school=engineering,
                          level=4, credits=20)
    Module.objects.create(id='UESTC2026', name='Signals and Systems (UESTC)', school=engineering, level=2, credits=20)
    Module.objects.create(id='UESTC3024', name='Stochastic Signal Analysis (UESTC)', school=engineering, level=3,
                          credits=8)
    Module.objects.create(id='UESTC3029', name='Communication Circuit Design', school=engineering, level=3, credits=20)
    Module.objects.create(id='UESTC2010', name='Physics II (UESTC)', school=engineering, level=2, credits=14)
    Module.objects.create(id='UESTC3001', name='Dynamics and Control', school=engineering, level=3, credits=12)
    Module.objects.create(id='UESTC2004', name='Embedded Processors', school=engineering, level=2, credits=10)
    Module.objects.create(id='UESTC1018', name='English for Engineering Studies A (UESTC)', school=engineering, level=1,
                          credits=30)
    Module.objects.create(id='UESTC4019', name='Real Time Computing Systems and Architecture', school=engineering,
                          level=4, credits=20)
    Module.objects.create(id='UESTC2022', name='Circuit Analysis and Design', school=engineering, level=2, credits=18)
    Module.objects.create(id='UESTC3035', name='Comprehensive Experiment of Modern Electronic Technology (UESTC)',
                          school=engineering, level=3, credits=8)
    Module.objects.create(id='UESTC3003', name='Electronic System Design', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTC3027', name='Team Design Project and Skills (UESTC only)', school=engineering,
                          level=3, credits=10)
    Module.objects.create(id='UESTC4005', name='Digital Signal Processing (UESTC)', school=engineering, level=4,
                          credits=16)
    Module.objects.create(id='UESTC4006P', name='Individual Project', school=engineering, level=4, credits=32)
    Module.objects.create(id='UESTC2025', name='Inventions and Innovations of Scotland', school=engineering, level=2,
                          credits=10)
    Module.objects.create(id='UESTC2001', name='Application and Design of Digital Logic (UESTC)', school=engineering,
                          level=2, credits=16)
    Module.objects.create(id='UESTC1003', name='Calculus II (UESTC)', school=engineering, level=1, credits=20)
    Module.objects.create(id='UESTC4002', name='Electromagnetic Field and Microwave Technology (UESTC)',
                          school=engineering, level=4, credits=16)
    Module.objects.create(id='UESTC1027', name='English for Academic and General Purposes (UESTC)', school=engineering,
                          level=1, credits=30)
    Module.objects.create(id='UESTC3021', name='Elements of Information Theory (UESTC)', school=engineering, level=3,
                          credits=8)
    Module.objects.create(id='UESTC1009', name='Physics I (UESTC)', school=engineering, level=1, credits=14)
    Module.objects.create(id='UESTC2028', name='Semiconductor Physics (UESTC)', school=engineering, level=2, credits=18)
    Module.objects.create(id='UESTC2009', name='Physical Experiment II (UESTC)', school=engineering, level=2, credits=6)
    Module.objects.create(id='UESTC3032', name='Micro & Nano Technology', school=engineering, level=3, credits=16)
    Module.objects.create(id='UESTC4007', name='VLSI Design', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC4004', name='Digital Communication', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC4003', name='Control Engineering', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC1001', name='Linear Algebra and Space Analytic Geometry I (UESTC)',
                          school=engineering, level=1, credits=14)
    Module.objects.create(id='UESTC3028', name='Advanced Project Skills Summer School for Glasgow College UESTC',
                          school=engineering, level=3, credits=15)
    Module.objects.create(id='UESTC4028', name='Advanced Digital Communication', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTC1019', name='English for Engineering Studies B (UESTC)', school=engineering, level=1,
                          credits=20)
    Module.objects.create(id='UESTC3020', name='Digital Circuit Design', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTC3034', name='Application and Design of Digital Logic 3 (UESTC)', school=engineering,
                          level=3, credits=18)
    Module.objects.create(id='UESTC4034', name='Design of Photonic Integrated Circuits', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTC4032', name='Power Semiconductor Device and Integration Technology (UESTC)',
                          school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC4036', name='Information Security', school=engineering, level=4, credits=20)
    Module.objects.create(id='UESTC4024', name='Wireless & Optical Transmission Systems', school=engineering, level=4,
                          credits=20)
    Module.objects.create(id='UESTC1005', name='Introductory Programming', school=engineering, level=1, credits=10)
    Module.objects.create(id='UESTC2029', name='English Communication and Engineering Career Skills',
                          school=engineering, level=2, credits=20)
    Module.objects.create(id='UESTC3022', name='Power Electronics', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTC4031', name='Microelectronic Packaging Technology (UESTC)', school=engineering,
                          level=4, credits=10)
    Module.objects.create(id='UESTC3002', name='Electronic Devices', school=engineering, level=3, credits=10)
    Module.objects.create(id='UESTC3036', name='Artificial Intelligence & Machine Learning', school=engineering,
                          level=3, credits=10)

    # School of Geographical and Earth Sciences (112 modules)
    Module.objects.create(id='EARTH4096', name='Environmental Geoscience Skills', school=geography, level=4, credits=10)
    Module.objects.create(id='EARTH4093', name='Igneous and Metamorphic Geology', school=geography, level=4, credits=30)
    Module.objects.create(id='EARTH5015', name='Modelling of Landscape Evolution', school=geography, level=5,
                          credits=10)
    Module.objects.create(id='EARTH4088', name='Geo-Environmental Policy and Planning for Sustainable Futures',
                          school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH4086', name='Planetary Science', school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH5020', name='Exploring the Solar System', school=geography, level=5, credits=20)
    Module.objects.create(id='EARTH4090', name='Landscape Dynamics', school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH5022', name='Astrobiology', school=geography, level=5, credits=20)
    Module.objects.create(id='EARTH5016', name='Numerical Foundations of Geodynamics', school=geography, level=5,
                          credits=10)
    Module.objects.create(id='EARTH4080P', name='Independent Environmental Geoscience Dissertation', school=geography,
                          level=4, credits=30)
    Module.objects.create(id='EARTH2010', name='Earth Science 2A', school=geography, level=2, credits=30)
    Module.objects.create(id='EARTH4089', name='Hydrogeology', school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH5021', name='Applied Remote Sensing of Earth and Solar System Bodies',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='EARTH4092', name='Advanced Geological Skills', school=geography, level=4, credits=10)
    Module.objects.create(id='EARTH4084', name='Engineering Geology: Geotechnical and Environmental', school=geography,
                          level=4, credits=20)
    Module.objects.create(id='EARTH5014', name='Machine Learning Applications for Earth Systems Problems',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='EARTH1002', name='Earth Science 1B', school=geography, level=1, credits=20)
    Module.objects.create(id='EARTH4078', name='Geological Skills', school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH3010', name='The Geology of Scotland - Earth Science International Summer School',
                          school=geography, level=3, credits=20)
    Module.objects.create(id='EARTH5017', name='GES_Numerical Modelling of Solid Earth Dynamics', school=geography,
                          level=5, credits=10)
    Module.objects.create(id='EARTH4071', name='Sedimentary Systems and Deposits', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='EARTH5013', name='Analytical Methods in Geoscience', school=geography, level=5,
                          credits=20)
    Module.objects.create(id='EARTH5023', name='Mathmatical Foundations in the Planetary and Geological Sciences',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='EARTH4094', name='Orogens and Basins: Structure and Resources', school=geography, level=4,
                          credits=30)
    Module.objects.create(id='EARTH2012', name='Earth Science Study Abroad 2', school=geography, level=2, credits=120)
    Module.objects.create(id='EARTH4082', name='Geological Hazards', school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH5018', name='Introduction to Earth Science', school=geography, level=5, credits=10)
    Module.objects.create(id='EARTH5010P', name='Independent Geoscience Research Project', school=geography, level=5,
                          credits=60)
    Module.objects.create(id='EARTH4087', name='Environmental Aqueous Geochemistry', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='EARTH4079P', name='Independent Geology Dissertation', school=geography, level=4,
                          credits=30)
    Module.objects.create(id='EARTH1001', name='Earth Science 1A', school=geography, level=1, credits=20)
    Module.objects.create(id='EARTH4095', name='Advanced Environmental Geoscience Skills', school=geography, level=4,
                          credits=10)
    Module.objects.create(id='EARTH2011', name='Earth Science 2B', school=geography, level=2, credits=30)
    Module.objects.create(id='EARTH4083', name='Minerals, Metals and Materials for Sustainable Futures',
                          school=geography, level=4, credits=20)
    Module.objects.create(id='EARTH5019', name='Theoretical and Applied Climatology', school=geography, level=5,
                          credits=20)
    Module.objects.create(id='EARTH4074', name='Climates: Past and Future', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG4141', name='Polar Environments', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5127', name='Systems Thinking for Climate Change and Sustainble Decision Making',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG4134',
                          name='Global Challenges: Inequalities, Injusticies and Building Hopeful Futures',
                          school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG4013', name='Geographic Thought', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG4090', name='Environmental Hazards', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG2001', name='Geography 2', school=geography, level=2, credits=60)
    Module.objects.create(id='GEOG5015', name='Web and Mobile Mapping', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG1015', name='Introduction to Climate Change and Sustainability', school=geography,
                          level=1, credits=10)
    Module.objects.create(id='GEOG5130P', name='GES Masters Research Project', school=geography, level=5, credits=60)
    Module.objects.create(id='GEOG5026', name='Visualisation & Map Use', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5099', name='Applied Land Surveying', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG1001', name='Geography 1: Living in a Changing World', school=geography, level=1,
                          credits=40)
    Module.objects.create(id='GEOG5023', name='Land Surveying II', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5121', name='Research Design,Ethics and Impact', school=geography, level=5,
                          credits=20)
    Module.objects.create(id='GEOG4091', name='Exploration: Histories, Cultures, Politics', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='GEOG4133', name='Black Geographies', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG5115', name='Managing Sustainable Water Environments: Policy and Practice',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG4083', name='Geographies of the body', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG4052P', name='Dissertation (Geography)', school=geography, level=4, credits=30)
    Module.objects.create(id='GEOG4117', name='Geography Beyond the Academy', school=geography, level=4, credits=30)
    Module.objects.create(id='GEOG4113', name='Population Geographies A:Past and Present', school=geography, level=4,
                          credits=10)
    Module.objects.create(id='GEOG4130', name='Geographical Education: Pedagogy and Practice', school=geography,
                          level=4, credits=10)
    Module.objects.create(id='GEOG4095', name='Urban Geographies: Cities, Ecologies, Politics', school=geography,
                          level=4, credits=20)
    Module.objects.create(id='GEOG5097P', name='Geospatial Science Work Placement', school=geography, level=5,
                          credits=60)
    Module.objects.create(id='GEOG5013', name='Geospatial Data Infrastructures and Land Administration',
                          school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5114', name='Monitoring Water Environments', school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG4137', name='Geographies of the Emotions', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5056', name='Remote Sensing of the Environment', school=geography, level=5,
                          credits=10)
    Module.objects.create(id='GEOG5117', name='Modelling Water Environments', school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG4114', name='Population Geographies B:Space, Sex and Death', school=geography,
                          level=4, credits=10)
    Module.objects.create(id='GEOG4101', name='Biogeography of Europe', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG4132', name='Political Geology: An Introduction', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='GEOG4025', name='Research Skills', school=geography, level=4, credits=30)
    Module.objects.create(id='GEOG5014', name='Hydrographic Survey', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5018', name='Principles of Cartographic Design & Production', school=geography,
                          level=5, credits=10)
    Module.objects.create(id='GEOG4097', name='Geographies of Solidarity and Internationalism', school=geography,
                          level=4, credits=20)
    Module.objects.create(id='GEOG4139', name='The (Geo)Politics of Infectious Disease', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='GEOG4015', name='Geographical Techniques', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5006', name='Directed Studies in Geomatics', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG2015', name='Geography 2 Residential Field Class', school=geography, level=2,
                          credits=0)
    Module.objects.create(id='GEOG4129', name='Decolonising Geography: Spaces of Colonialism and Anti-Colonialism',
                          school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5126', name='Climate and Carbon Literacy', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG4057', name='Managing River Catchments', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5123', name='Academic and Professional Skills for GES PGT', school=geography, level=5,
                          credits=10)
    Module.objects.create(id='GEOG5019', name='Principles of GIS', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG4136', name='Coastal and Climate Change: Science, Risk, Vulnerability and Adaptation',
                          school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG5025', name='Topographic Modelling and Landscape Monitoring', school=geography,
                          level=5, credits=10)
    Module.objects.create(id='GEOG3010', name='Research Skills DD', school=geography, level=3, credits=30)
    Module.objects.create(id='GEOG5008', name='Geospatial Fundamentals', school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG5020', name='Land Surveying I', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5022', name='Researching Human Geography: Design, Methods and Ethics',
                          school=geography, level=5, credits=40)
    Module.objects.create(id='GEOG5102', name='Applied GIS', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5120', name='Global Challenges', school=geography, level=5, credits=40)
    Module.objects.create(id='GEOG1007', name='Geography 1: Living In A Changing World (Half Course)', school=geography,
                          level=1, credits=20)
    Module.objects.create(id='GEOG4135', name='Urban Landscapes', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5131P', name='GES MSc Project', school=geography, level=5, credits=60)
    Module.objects.create(id='GEOG5080', name='Conceptualising Human Geography 2: Geographical Engagements',
                          school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG4103', name='Earth Futures: Thinking and Planning for the Anthropocene',
                          school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5133', name='Global Challenges 1: Living in a Changing Climate', school=geography,
                          level=5, credits=20)
    Module.objects.create(id='GEOG4123', name='Human Mobility in a Changing Climate', school=geography, level=4,
                          credits=20)
    Module.objects.create(id='GEOG4115', name='Oceanography', school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG4112', name='GIS B:Theory & Practice', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG2016', name='Geography 2 (Half Course)', school=geography, level=2, credits=30)
    Module.objects.create(id='GEOG4124', name='Glacial Landsystems', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5116', name='Ecology and Restoration of Water Environments', school=geography,
                          level=5, credits=10)
    Module.objects.create(id='GEOG4019', name='Joint Student Research Skills', school=geography, level=4, credits=30)
    Module.objects.create(id='GEOG4089', name='HISTORICAL GEOGRAPHIES OF CARE, CONFLICT AND CONFINEMENT',
                          school=geography, level=4, credits=20)
    Module.objects.create(id='GEOG5004', name='Conceptualising Human Geography 1: Space, Politics, Ecologies',
                          school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG4111', name='GIS A:Applied Spatial Analysis', school=geography, level=4, credits=10)
    Module.objects.create(id='GEOG5007', name='Engineering Survey', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5128', name='Introduction to GIS', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5132', name='GES_Spatial Data Analytics', school=geography, level=5, credits=10)
    Module.objects.create(id='GEOG5119', name='Graduate Futures Work Placement', school=geography, level=5, credits=20)
    Module.objects.create(id='GEOG5134', name='Global Challenges 2: Human-environment Lifecyles', school=geography,
                          level=5, credits=20)
    Module.objects.create(id='GEOG5122', name='Introduction to Statistics for Environmental Analysis', school=geography,
                          level=5, credits=10)
    Module.objects.create(id='GEOG5012', name='GNSS and Geodesy', school=geography, level=5, credits=10)

    # School of Health and Wellbeing (115 modules)
    Module.objects.create(id='BIOL5449', name='Complex Disease Genomics: linking genome to phenome', school=health,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5457', name='The Role of a Clinical Trials Unit in Trial Design and Deliver',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5173', name='Professional Issues And Research Design In Clinical Neuropsychology',
                          school=health, level=5, credits=15)
    Module.objects.create(id='MED5653', name='Introduction to Epidemiology and Statistics', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED6034', name='Advanced Clinical Practice II', school=health, level=6, credits=40)
    Module.objects.create(id='MED5082', name='Research Methods', school=health, level=5, credits=20)
    Module.objects.create(id='MED5272', name='Research Methods (Qualitative, Quantitative and Health Economics)',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5159', name='Neurosciences For Clinical Neuropsychology', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5070P', name='Project', school=health, level=5, credits=60)
    Module.objects.create(id='MED5611', name='Substance Use, Health, and Society', school=health, level=5, credits=20)
    Module.objects.create(id='MED6037', name='Service Evaluation and Quality Improvement', school=health, level=6,
                          credits=10)
    Module.objects.create(id='MED5432', name='Health Promotion: Principles and Practice', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5632', name='Substance Use in the Contemporary World', school=health, level=5,
                          credits=10)
    Module.objects.create(id='MED6007', name='Research Practice II', school=health, level=6, credits=80)
    Module.objects.create(id='MED5657', name='Infant Mental Health Intervention Training', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5587', name='Themes in Global Mental Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5664', name='Systems Around the Infant', school=health, level=5, credits=20)
    Module.objects.create(id='MED5011', name='Communicable Diseases', school=health, level=5, credits=20)
    Module.objects.create(id='MED5468', name='Research Methods', school=health, level=5, credits=20)
    Module.objects.create(id='MED5449', name='Mental Health Promotion across the Life-span', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5654', name='Implementing Positive Behaviour Support Using Practice Leadership',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED6024', name='Service Evaluation and Quality Improvement', school=health, level=6,
                          credits=10)
    Module.objects.create(id='MED5688', name='Understanding Infant Mental Health and Development (January)',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5642', name='Understanding Infant Mental Health and Development', school=health,
                          level=5, credits=10)
    Module.objects.create(id='MED5634', name='Complex Care Needs & Positive Behaviour Support', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5546P', name='Clinical Neuropsychology Research Dissertation', school=health, level=5,
                          credits=60)
    Module.objects.create(id='MED5659', name='Exploring Infant Mental Health and Development', school=health, level=5,
                          credits=10)
    Module.objects.create(id='MED5019', name='Planetary Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5641', name='Choice experiments for health economics, HTA and one health',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5133', name='Epilepsy, Seizure And Sleep Disorders And Clinical Neuropsychology',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5615', name='Introduction to Health Economics and Health Technology Assessment',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5660', name='Reflective Practice', school=health, level=5, credits=10)
    Module.objects.create(id='MED5499', name='Research Methods in Health & Wellbeing', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5374',
                          name='Maximising the Value of Clinical Trial Data: Analysis for Economic Evaluation and Modelling',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5377', name='Health Technology Assessment in a global context', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5027', name='Introduction To Epidemiology', school=health, level=5, credits=20)
    Module.objects.create(id='MED6031', name='Research Practice I', school=health, level=6, credits=45)
    Module.objects.create(id='MED5595', name='Understanding & Assessing Challenging Behaviour', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5433', name='Introduction to Epidemiology', school=health, level=5, credits=20)
    Module.objects.create(id='MED5268', name='Cultural, Social and Biological Determinants of Mental Health',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5479P', name='Master of Public Health Research Project', school=health, level=5,
                          credits=60)
    Module.objects.create(id='MED6030', name='Research Design And Statistics', school=health, level=6, credits=15)
    Module.objects.create(id='MED5092', name='Acquired Brain Injury And Clinical Neuropsychology', school=health,
                          level=5, credits=15)
    Module.objects.create(id='MED5371',
                          name='Understanding Evidence for the Real World:Critical Appraisal for Healthcare',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5275', name='HTA: policy and principles', school=health, level=5, credits=20)
    Module.objects.create(id='MED5269P', name='Global Mental Health Dissertation', school=health, level=5, credits=60)
    Module.objects.create(id='MED5545P', name='Clinical Neuropsychology Practice', school=health, level=5, credits=60)
    Module.objects.create(id='MED5674P', name='Infant Mental Health Dissertation', school=health, level=5, credits=60)
    Module.objects.create(id='MED5661', name='Infant Observation', school=health, level=5, credits=10)
    Module.objects.create(id='MED5040', name='Managing Healthcare Organisations', school=health, level=5, credits=20)
    Module.objects.create(id='MED6021', name='DClinPsy: Advanced Professional Practice I', school=health, level=6,
                          credits=10)
    Module.objects.create(id='MED5663', name='Fundamentals of Infant Mental Health and Development', school=health,
                          level=5, credits=10)
    Module.objects.create(id='MED5673', name='Infant Mental Health and Neurodevelopment in Practice', school=health,
                          level=5, credits=20)
    Module.objects.create(id='MED5201', name='Stroke and Clinical Neuropsychology', school=health, level=5, credits=20)
    Module.objects.create(id='MED5126', name='Degenerative Conditions and Clinical Neuropsychology', school=health,
                          level=5, credits=15)
    Module.objects.create(id='MED5068', name='Principles of Public Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED6033', name='DClinPsy:Foundation Clinical Practice II', school=health, level=6,
                          credits=50)
    Module.objects.create(id='MED5685', name='Sexual Health and Wellbeing', school=health, level=5, credits=20)
    Module.objects.create(id='MED5450', name='Mental Health and Disability: International Law and Policy',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5434', name='Principles of Public Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5378', name='Real-world data in health care decision making', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5022', name='Globalisation And Public Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED1021',
                          name='Global Public Health in Action: Tackling Health Inequalities and Advancing Wellbeing',
                          school=health, level=1, credits=20)
    Module.objects.create(id='MED6025', name='Foundation Clinical Practice I', school=health, level=5, credits=45)
    Module.objects.create(id='MED5445', name='Cultural, Social and Biological Determinants of Mental Health',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5652', name='Introduction to Epidemiology and Statistics', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5636P', name='Positive Behaviour Support Practice', school=health, level=5, credits=60)
    Module.objects.create(id='MED5675P', name='Infant Mental Health Practice', school=health, level=5, credits=60)
    Module.objects.create(id='MED6029', name='Psychology And The Law', school=health, level=6, credits=10)
    Module.objects.create(id='MED5628', name='Decision Analytic Modelling and Early Health Technology Assessment',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5277P', name='Health Technology Assessment: Research Project', school=health, level=5,
                          credits=60)
    Module.objects.create(id='MED5683', name='Research Methods in Health Economics and HTA', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5633', name='Advanced Positive Behaviour Support Strategies', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED6026', name='Foundation Knowledge, Understanding And Skills', school=health, level=6,
                          credits=45)
    Module.objects.create(id='MED5635', name='Implementing Positive Behaviour Support in Systems', school=health,
                          level=5, credits=20)
    Module.objects.create(id='MED6036', name='Service Evaluation and Quality Improvement (APL)', school=health, level=6,
                          credits=10)
    Module.objects.create(id='MED6022', name='Advanced Professional Practice II', school=health, level=6, credits=10)
    Module.objects.create(id='MED5677', name='Geography of Health and Health Inequalities', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5519', name='Advanced Statistics', school=health, level=5, credits=20)
    Module.objects.create(id='MED5436', name='Qualitative Research Methods for Public Health', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5163', name='Paediatric Neurological Conditions And Clinical Neuropsychology',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5054', name='Oral Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5447',
                          name='Access to Mental Health Care in the Global Context: Innovation, Equity and Enterprise',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5446P', name='Global Mental Health Dissertation', school=health, level=5, credits=60)
    Module.objects.create(id='MED5680', name='Planetary Health ODL', school=health, level=5, credits=20)
    Module.objects.create(id='MED1020', name='Making Sense of Problem Substance Use in Scotland (C4L)', school=health,
                          level=1, credits=10)
    Module.objects.create(id='MED5442', name='Noncommunicable Disease and Multimorbidity in Primary Care',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED6020', name='Advanced Clinical Practice I', school=health, level=6, credits=40)
    Module.objects.create(id='MED5334P', name='Master of Public Health Research Project', school=health, level=5,
                          credits=60)
    Module.objects.create(id='MED5024', name='Health Promotion: Principles and Practice', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED6028', name='Learning Disability Theory And Practice', school=health, level=6,
                          credits=50)
    Module.objects.create(id='MED5266', name='Mental Health and Disability: International Law and Policy',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5594', name='Monitoring & Evaluating Positive Behaviour Support Plans', school=health,
                          level=5, credits=20)
    Module.objects.create(id='MED5665', name='Research Methods', school=health, level=5, credits=20)
    Module.objects.create(id='MED5525', name='Evaluation Design', school=health, level=5, credits=20)
    Module.objects.create(id='MED5431', name='Globalisation and Public Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5648',
                          name='Behaviour Change for Health and Wellbeing: Translating Theory into Practice',
                          school=health, level=5, credits=10)
    Module.objects.create(id='MED5271', name='Mental Health Promotion Across the Life-span', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5023', name='Health Economics for HTA online', school=health, level=5, credits=20)
    Module.objects.create(id='MED5220', name='Context and Perspectives in Clinical Neuropsychology', school=health,
                          level=5, credits=15)
    Module.objects.create(id='MED5616', name='Impact of Trauma on Mental Health', school=health, level=5, credits=10)
    Module.objects.create(id='MED5021', name='Advanced Statistics', school=health, level=5, credits=20)
    Module.objects.create(id='MED5593', name='Developing & Implementing Positive Behaviour Support Plans',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5523', name='Advanced Epidemiology', school=health, level=5, credits=20)
    Module.objects.create(id='MED5591', name='Advanced Epidemiology', school=health, level=5, credits=20)
    Module.objects.create(id='MED5029', name='Introduction To Statistical Methods', school=health, level=5, credits=20)
    Module.objects.create(id='MED5372',
                          name='Statistical methods for Health Technology Assessment and Evidence Based Medicine',
                          school=health, level=5, credits=20)
    Module.objects.create(id='MED5658', name='Clinical Skills in Infant Mental Health', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED5380', name='Survival analysis for Health Technology Assessment', school=health,
                          level=5, credits=10)
    Module.objects.create(id='MED5077', name='Qualitative Research Methods', school=health, level=5, credits=20)
    Module.objects.create(id='MED5522', name='Social Determinants of Health', school=health, level=5, credits=20)
    Module.objects.create(id='MED5678', name='Geography of Health and Health Inequalities', school=health, level=5,
                          credits=20)
    Module.objects.create(id='MED6027', name='Foundations Of Clinical Psychology', school=health, level=6, credits=30)
    Module.objects.create(id='MED5586', name='Themes in Global Mental Health', school=health, level=5, credits=20)
    Module.objects.create(id='SPS5039', name='Fundamentals of Evaluation', school=health, level=5, credits=20)

    # School of Humanities (546 modules)
    Module.objects.create(id='ARCH5042', name='The Process of Artefact Studies', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH4083', name='Pottery Skills: understanding Archaeology\'s most common material',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH5118', name='Landscape and Environment in Gaelic Scotland', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='ARCH4071', name='Contemporary and future archaeologies', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='ARCH4080', name='People in a Changing World', school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH5016', name='Modern Warfare: 19th and 20th Century Warfare', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='ARCH5007P', name='Archaeology Dissertation', school=humanities, level=5, credits=60)
    Module.objects.create(id='ARCH5098', name='Cloth and Clothing', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5020', name='Independent Study Project', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5106', name='Landscape Archaeologies', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5101',
                          name='Feasting like the Ancients: An Inter-Disciplinary Approach to Early Food and Drink',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH4063', name='Cloth and Clothing', school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH5035', name='Research Report', school=humanities, level=5, credits=30)
    Module.objects.create(id='ARCH4067', name='Practical Heritage Experience (Senior Honours)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='ARCH5009', name='British Battlefields: Analysis and Cultural Resource Management',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5125P', name='Archaeology Applied Dissertation', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='ARCH4048', name='Viking Movements', school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH5115', name='Reassembling the Artefacts', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH2011', name='Archaeology 2B:Theory and Practice', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='ARCH5123', name='Pottery Skills: understanding Archaeology\'s most common material',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5109', name='Contemporary and future archaeologies', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='ARCH5124', name='Decolonising the Heritage of Slavery and Colonialism', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='ARCH5107', name='Archaeological Digital Imaging', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5048P', name='Work Placement', school=humanities, level=5, credits=30)
    Module.objects.create(id='ARCH4001P', name='Archaeology Dissertation (Joint Hons)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='ARCH4070', name='Archaeology, Games and Interactive Media', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='ARCH4065', name='Reflexive Archaeological Practice', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='ARCH4002P', name='Archaeology Dissertation (Single Hons)', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='ARCH3001', name='Archaeological Studies 3', school=humanities, level=3, credits=80)
    Module.objects.create(id='ARCH2004', name='Archaeology 2A: 20 Things that Changed the World', school=humanities,
                          level=2, credits=20)
    Module.objects.create(id='ARCH5018', name='Geographical Information Systems in Archaeology', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='ARCH5090', name='Student Exhibition Design', school=humanities, level=5, credits=30)
    Module.objects.create(id='ARCH5038', name='The Art of War: Concepts and Theories', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='ARCH4074', name='Being Human in Ancient Egypt and Mesopotamia', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='ARCH1001', name='Archaeology 1A: The Archaeology of Scotland', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='ARCH5119', name='Heritage Material Science', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH4082', name='Landscape and Environment in Gaelic Scotland', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='ARCH5117', name='Environmental Archaeology; plants, animals and people',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH4060', name='Advanced Heritage Project', school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH3002', name='Archaeology 3 (Arts)', school=humanities, level=3, credits=60)
    Module.objects.create(id='ARCH4014', name='Settlement and Society in Scandinavian Scotland', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='ARCH4061', name='Environmental Archaeology; Plants, Animals and People',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH5086', name='Research and Professional Skills', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='ARCH4019', name='Theory & Interpretation in Archaeology', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='ARCH1002', name='Archaeology 1B: Archaeology in the Modern World', school=humanities,
                          level=1, credits=20)
    Module.objects.create(id='ARCH4077', name='Assembling the Artefacts', school=humanities, level=4, credits=20)
    Module.objects.create(id='ARCH4026', name='Geographical Information Systems in Archaeology', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='ARCH5108', name='Kingdoms and societies in northern Britain AD 400-800 Masters',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH5104', name='Archaeology, Games and Interactive Medi', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='ARCH5025', name='Material Culture in Context', school=humanities, level=5, credits=20)
    Module.objects.create(id='ARCH4018', name='Kingdoms and societies in northern Britain AD 400-800',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CELTCIV5031', name='Cultural Memory Studies and Medieval Irish Literature (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV4046P', name='Dissertation (Celtic) Joint Honours', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CELTCIV5030', name='Skills and Scholarship in Celtic Studies', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CELTCIV4045P', name='Applied Dissertation with Placement in Celtic', school=humanities,
                          level=4, credits=40)
    Module.objects.create(id='CELTCIV5003', name='Advanced Medieval Welsh 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV5025', name='Celtic Place-Names of Scotland', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CELTCIV2002', name='Celtic Civilisation 2B', school=humanities, level=2, credits=20)
    Module.objects.create(id='CELTCIV5012', name='Special Option 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV5026', name='Critical Issues in Early Gaelic Literature', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CELTCIV4016', name='Celtic Place-Names Of Scotland', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CELTCIV5006P', name='Dissertation (Celtic Studies)', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='CELTCIV5034',
                          name='Literacy in Celtic Culture and Society: an Interdisciplinary Approach (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV5033', name='Medieval Welsh Literature In Translation (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CELTCIV4009', name='Advanced Early Gaelic Texts', school=humanities, level=4, credits=20)
    Module.objects.create(id='CELTCIV5032', name='Medieval Ireland, 800-1100: sources and debates', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CELTCIV4006', name='Introduction To Early Gaelic (Old And Middle Irish)',
                          school=humanities, level=4, credits=40)
    Module.objects.create(id='CELTCIV1002', name='Celtic Civilisation 1B', school=humanities, level=1, credits=20)
    Module.objects.create(id='CELTCIV4042', name='Medieval Ireland 800 - 1100', school=humanities, level=4, credits=20)
    Module.objects.create(id='CELTCIV4027', name='Medieval Welsh Literature In Translation', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CELTCIV4025', name='Introduction To Medieval Welsh', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='CELTCIV4034', name='The Finn Cycle', school=humanities, level=4, credits=20)
    Module.objects.create(id='CELTCIV4007', name='Literacy In Medieval Celtic Societies', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CELTCIV5027', name='Finn in Gaelic Literature', school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV4019', name='Early Gaelic Literature In Translation', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CELTCIV5008', name='Introduction To Early Gaelic (Old And Middle Irish)',
                          school=humanities, level=5, credits=40)
    Module.objects.create(id='CELTCIV5001', name='Advanced Early Gaelic 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV2001', name='Celtic Civilisation 2A', school=humanities, level=2, credits=20)
    Module.objects.create(id='CELTCIV1001', name='Celtic Civilisation 1A', school=humanities, level=1, credits=20)
    Module.objects.create(id='CELTCIV5014', name='Themes and Debates in Celtic Studies', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CELTCIV4005', name='Early Gaelic Poetry', school=humanities, level=4, credits=20)
    Module.objects.create(id='CELTCIV4047P', name='Dissertation (Celtic) Single Honours', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='CELTCIV5013', name='Special Option 2', school=humanities, level=5, credits=20)
    Module.objects.create(id='CELTCIV5009', name='Introduction To Medieval Welsh', school=humanities, level=5,
                          credits=40)
    Module.objects.create(id='CLASSIC5128', name='Women and Power? The extraordinary women of the ancient world (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5066', name='Approaching the Ancient World through Text', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC4055', name='Core Travel for Classics (Senior Honours)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='CLASSIC5112', name='The Novel in Antiquity (PGT)', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5059', name='Ancient Drama', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4093', name='Intermediate Ancient Egyptian Hieroglyphs for Honours',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5090', name='Cleopatra: Life and Legend', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4006', name='Rhetoric At Rome', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4085',
                          name='Imperium Indivisum?: The Collapse of the West Roman Empire in the fifth century AD',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4001', name='Athenian Democracy: Model Or Mob-Rule?', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5119', name='The Histories of Trans People (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC4100', name='Religions of Rome (CLASSIC, Hons)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5087', name='Ancient Medicine', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5124', name='Greek Letters and Letter-Writers: Friendship, Philosophy, Forgery',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4097', name='Greek Letters and Letter-Writers: Friendship, Philosophy, Forgery',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5110', name='Love and War: poetry at the end of the Roman Republic (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5084', name='Lyric poems and their performance in ancient Greece (PG)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5116',
                          name='Imperium Indivisum?: The Collapse of the West Roman Empire in the Fifth Century AD (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4077P', name='Dissertation (Ancient History)', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='CLASSIC5092', name='Roman Art', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC2001',
                          name='Classical Civilisation 2A: Identities, Ideology and the Hellenistic World',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='CLASSIC5129', name='Women, Witches and Witchcraft in Antiquity (PG)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC4056', name='The Invention of History: Herodotus, Thucydides, Xenophon',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5098', name='The Roman Historical Imagination for Postgraduates',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5093', name='Greek Art', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC2011', name='Classical Civilisation 2B: Empire and Identity (DL)',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='CLASSIC5091', name='Impairment and Disability in the Ancient World', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC5094', name='Basic ancient Egyptian hieroglyphs for postgraduates',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5063', name='Explorations in the Classical Tradition', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC5130', name='Independent study project Classics/Ancient Cultures',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5127', name='Religions of Rome (CLASSIC, PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC1002', name='Classical Civilisation 1B: Augustan Rome: From Republic to Empire',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='CLASSIC5107', name='The Art of Divergence in Ancient Egypt (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC5108',
                          name='From the Gracchi to Sulla: the sources and the history 133-70 BC (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4047P', name='Dissertation (Classics)', school=humanities, level=4, credits=40)
    Module.objects.create(id='CLASSIC5102', name='Myths, Fictions, and Histories of Alexander the Great (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4083', name='The Material World in Greek Religious Thought and Practice',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5069', name='Ancient Technology in Context', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC4092', name='The Art of Divergence in Ancient Egypt (Hons)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='CLASSIC4081', name='Ancient Warfare', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5104',
                          name='Reasons to be Cheerful: Theorising Comedy with Aristophanes and Menander (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4062', name='From the Gracchi to Sulla: the sources and the history 133-70 BC',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4007', name='ROMAN ART', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4013', name='Gender And Sexuality In Ancient Rome', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5097', name='Homer and his Readers for Postgraduates', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC5096', name='Athenian Democracy: Model or Mob Rule (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC4010',
                          name='The Roman Stage: A History Of Roman Drama From The Republic To The Empire',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5109', name='Intermediate Ancient Egyptian hieroglyphs (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='CLASSIC5118', name='Rome in Transition 49-27 BC (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC4091', name='Stargazing: Astronomy, Astrology and Meteorology in Antiquity',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5065', name='Approaching the Ancient World through Material Culture',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4038', name='Rome In Transition, 49-27 BC', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC1001', name='Classical Civilisation 1A: Myth and Politics in Classical Athens',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='CLASSIC4089', name='Basic ancient Egyptian hieroglyphs for Honours', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='CLASSIC2010',
                          name='Classical Civilisation 2A: Identities, Ideology and the Hellenistic World (DL)',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='CLASSIC2002', name='Classical Civilisation 2B: Empire and Identity', school=humanities,
                          level=2, credits=20)
    Module.objects.create(id='CLASSIC4101', name='Women and Power? The extraordinary women of the ancient world',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5126', name='Basic Ancient Egyptian Hieroglyphs (DL)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC4070', name='Ancient Medicine', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5078', name='Ancient Warfare (PG)', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4005',
                          name='Reasons To Be Cheerful: Theorising Comedy With Aristophanes And Menander',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4075', name='Religion in Ancient Greece', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5086', name='The Invention of History: Herodotus, Thucydides, Xenophon (PG)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4094', name='Love and War: poetry at the end of the Roman Republic',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4071', name='Ancient Technology in Context', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC4098', name='The Histories of Trans People (UG)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5080', name='Religion in Ancient Greece (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC4072', name='Cleopatra: Life and Legend (Hons)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5095',
                          name='Heroes and heretics: a cultural archaeology of kingship in 18th dynasty Egypt',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4102', name='Women, Witches and Withcraft in Antiquity', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='CLASSIC4049', name='Greek Art', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5081',
                          name='The Material world in Greek Religious Thought and Practice (for postgraduates)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4082', name='The Later Roman Empire, 270-400 AD', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5125', name='Roman Mobilities', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5082', name='The Other Greeks: Sparta, Crete, Thessaly (for postgraduates)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5077', name='Theories and Methods for Ancient History and Classics',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4060', name='Lyric poems and their performance in ancient Greece',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC4024', name='Homer And His Readers', school=humanities, level=4, credits=20)
    Module.objects.create(id='CLASSIC5046P', name='Dissertation (Classics)', school=humanities, level=5, credits=60)
    Module.objects.create(id='CLASSIC5079', name='The Later Roman Empire, 270-400 AD (PG)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='CLASSIC5088', name='Rhetoric at Rome (PG)', school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC4045', name='The Roman Historical Imagination', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='CLASSIC5114', name='Greek Letters and Letter-Writers: Friendship, Philosophy, Forgery',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='CLASSIC5100', name='Stargazing: Astronomy, Astrology and Meteorology in Antiquity',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='GAELIC4051', name='Gaelic Identity from the Middle Ages to the Present',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC4004', name='Gaelic (Beginners) for Honours Students', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='GAELIC3011', name='Bogadh sa Ghàidhlig - Leughadh is Sgrìobhadh', school=humanities,
                          level=3, credits=40)
    Module.objects.create(id='GAELIC4006', name='Gaelic (Intermediate) for Honours Students', school=humanities,
                          level=4, credits=40)
    Module.objects.create(id='GAELIC1003', name='Gaelic 1 (Beginners)', school=humanities, level=1, credits=40)
    Module.objects.create(id='GAELIC4010', name='Introduction To Modern Irish', school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC2013', name='Bogadh sa Ghàidhlig - Coimhearsnachd na Gàidhlig (Half course)',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='GAELIC4050',
                          name='Innse Gall, Ulaidh agus Rìgh Seumas VI. Tuineachadh agus Sìobhaltas, c.1541-1639',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC4011', name='Sgilean Canain 3', school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC1018', name='Cert HE Bogadh sa Ghàidhlig - Èisteachd is Labhairt',
                          school=humanities, level=1, credits=40)
    Module.objects.create(id='GAELIC5001', name='Gaelic (AB Initio)', school=humanities, level=5, credits=40)
    Module.objects.create(id='GAELIC5034P', name='MRanns an Gàidhlig (Gaelic 90)', school=humanities, level=5,
                          credits=90)
    Module.objects.create(id='GAELIC3013', name='Bogadh sa Ghàidhlig - Èisteachd is Labhairt', school=humanities,
                          level=3, credits=40)
    Module.objects.create(id='GAELIC1004', name='Gaelic 1 Beginners (Half Course)', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='GAELIC4048P', name='Dissertation (Gaelic) Single Honours', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='GAELIC2001', name='Gaelic 2 (Advanced)', school=humanities, level=2, credits=40)
    Module.objects.create(id='GAELIC1001', name='Gaelic 1 (Advanced)', school=humanities, level=1, credits=40)
    Module.objects.create(id='GAELIC4012', name='Sgilean Canain 4', school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC1006', name='Gaelic 1 Intermediate (Half Course)', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='GAELIC1016', name='Cert HE Bogadh sa Ghàidhlig - Leughadh is Sgrìobhadh (Half course)',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='GAELIC1015', name='Cert HE Bogadh sa Ghàidhlig - Leughadh is Sgrìobhadh',
                          school=humanities, level=1, credits=40)
    Module.objects.create(id='GAELIC1002', name='Gaelic 1 Advanced (Half Course)', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='GAELIC4047P', name='Dissertation (Gaelic) Joint Honours', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GAELIC1005', name='Gaelic 1 (Intermediate)', school=humanities, level=1, credits=40)
    Module.objects.create(id='GAELIC3014', name='Bogadh sa Ghàidhlig - Coimhearsnachd na Gàidhlig', school=humanities,
                          level=3, credits=40)
    Module.objects.create(id='GAELIC4041', name='The Folklore of Gaelic Scotland', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GAELIC4043', name='Guth nan Eilthireach: Litreachas Gàidhlig anns an t-Saoghal Ùr',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC1017', name='Cert HE Bogadh sa Ghàidhlig - Èisteachd is Labhairt (half course)',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='GAELIC4052', name='Ainmean-Àite o Bheul-Aithris', school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC4046P', name='Applied Dissertation with Placement in Gaelic', school=humanities,
                          level=4, credits=40)
    Module.objects.create(id='GAELIC5003', name='Gaidhlig Adhartach', school=humanities, level=5, credits=40)
    Module.objects.create(id='GAELIC2012', name='Cert HE Bogadh sa Ghàidhlig - Coimhearsnachd na Gàidhlig',
                          school=humanities, level=2, credits=40)
    Module.objects.create(id='GAELIC4045', name='An Dealbh-Chluich agus a\' Ghàidhlig bho 1790', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GAELIC5002', name='Gaelic (Intermediate)', school=humanities, level=5, credits=40)
    Module.objects.create(id='GAELIC2002', name='Gaelic 2 Advanced (Half Course)', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='GAELIC2004', name='Gaelic 2 Intermediate (Half Course)', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='GAELIC3015', name='Bogadh sa Ghàidhlig - Coimhearsnachd na Gàidhlig (Half course)',
                          school=humanities, level=3, credits=20)
    Module.objects.create(id='GAELIC2003', name='Gaelic 2 (Intermediate)', school=humanities, level=2, credits=40)
    Module.objects.create(id='GAELIC3001', name='Gaelic 3', school=humanities, level=3, credits=60)
    Module.objects.create(id='GAELIC3012', name='Bogadh sa Ghàidhlig - Èisteachd is Labhairt (half course)',
                          school=humanities, level=3, credits=20)
    Module.objects.create(id='GAELIC4001', name='An 19Mh Linn Tro Shuilean Nan Gaidheal', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GAELIC4002', name='Bardachd Cogaidh 1930-1950', school=humanities, level=4, credits=20)
    Module.objects.create(id='GAELIC3010', name='Bogadh sa Ghàidhlig - Leughadh is Sgrìobhadh (Half course)',
                          school=humanities, level=3, credits=20)
    Module.objects.create(id='GAELIC4042', name='Seinn sa Ghàidhlig / Gaelic Song in Performance', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GREEK4022P', name='Dissertation (Greek)', school=humanities, level=4, credits=40)
    Module.objects.create(id='GREEK3001', name='Advanced Greek', school=humanities, level=3, credits=40)
    Module.objects.create(id='GREEK2002', name='Greek 2B: Intermediate Greek 2', school=humanities, level=2, credits=20)
    Module.objects.create(id='GREEK5010', name='Greek Tragedy (Linguistic Pathway)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK4012', name='Greek Lyric, Elegiac, And Iambic Poetry', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GREEK4023', name='Greek Epigraphy', school=humanities, level=4, credits=20)
    Module.objects.create(id='GREEK5007', name='Further Topic In Greek 2', school=humanities, level=5, credits=20)
    Module.objects.create(id='GREEK4033', name='The Roman Historical Imagination: Greek Sources', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GREEK5001', name='Intermediate Greek for Postgraduates 1', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK4001', name='Intermediate Greek for Honours 1', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GREEK5002', name='Intermediate Greek for Postgraduate 2', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK5004', name='Basic Greek For Postgraduates 2', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK4026', name='Athenian Democracy: Model or Mob-rule? (Greek)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GREEK5009', name='Greek Comedy (Linguistic Pathway)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK1002', name='Greek 1B: Basic Greek 2', school=humanities, level=1, credits=20)
    Module.objects.create(id='GREEK2001', name='Greek 2A:Intermediate Greek 1', school=humanities, level=2, credits=20)
    Module.objects.create(id='GREEK4009', name='Greek Unprepared Translation (Senior Honours)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GREEK4002', name='Intermediate Greek for Honours 2', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GREEK4031', name='Literature in Fragments (Greek)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='GREEK4027', name='The Invention of History: Herodotus, Thucydides, Xenophon in Greek',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='GREEK5025', name='Greek Letters and Letter-writers (Greek) (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='GREEK5026', name='Hellenistic Poets in Greek (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK5006', name='Further Topic In Greek 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='GREEK4024', name='Ancient Technology in Context (Linguistic Pathway)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='GREEK4003', name='Basic Greek For Honours 1', school=humanities, level=4, credits=20)
    Module.objects.create(id='GREEK4025', name='Homer & his Readers - Greek', school=humanities, level=4, credits=20)
    Module.objects.create(id='GREEK1001', name='Greek 1A: Basic Greek 1', school=humanities, level=1, credits=20)
    Module.objects.create(id='GREEK4029', name='Reasons to be Cheerful: Greek Comedy with Aristophanes and Menander',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='GREEK5003', name='Basic Greek For Postgraduates 1', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='GREEK5020', name='Interpreting Greek Tragedy (for Postgraduates)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='GREEK4004', name='Basic Greek For Honours 2', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5190', name='Resistance to Slavery from 1700 to 1900 (DL)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST5165', name='Games and Gaming History', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5185', name='Enchanting Modernity: Gender, Sexuality and Esotericism (DL)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4016', name='Patriarchy, Sex and Gender in Early Modern Europe', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST1025', name='Introduction to Scottish Culture Semester 2', school=humanities, level=1,
                          credits=10)
    Module.objects.create(id='HIST5153', name='Commodity Histories in the Global South, 1500-2000', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST5203', name='In the Museum of Man: Empire, Race and Anthropology, 1850-1970 (PG)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5177', name='Enchanting Modernity: Gender, Sexuality and Esotericism',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5184', name='Making a Living: Work, Gender and Society 1700-1850 (DL)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4033', name='The Norman Conquest 1066-1100', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4279',
                          name='Imperial States: Race, War, and Expansion in American History, 1860s-1920s',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5167',
                          name='A \'New Form of Slavery\'?: Indentured Labour in Post-Slavery Caribbean Societies, c. 1836-1917',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4278',
                          name='From the Space Race to Star Wars: US Conflict and Cooperation in Orbit, 1945-2019',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4214',
                          name='People of plenty: The politics of consumption in the United States since 1890',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4277', name='Islands at War in the 20th Century: Invaders, Occupiers and Liberators:',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5193', name='Approaches to Queer and Trans Histories', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4310', name='A Special Relationship? Britain and the United States since c. 1900',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4295',
                          name='Empire in the city: the British empire and the making of urban space in Glasgow, 1707-2014',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST3016', name='Scottish Popular Culture 1500-1800 (non-Honours)', school=humanities,
                          level=3, credits=20)
    Module.objects.create(id='HIST5197', name='Gender History Applied', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4319', name='Material Histories of Modern Scotland', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST4284', name='Rwanda: Peace, Conflict and the Politics of History', school=humanities,
                          level=4, credits=60)
    Module.objects.create(id='HIST5069', name='War Studies Core Course: Battles, Conflicts and their Legacies',
                          school=humanities, level=5, credits=60)
    Module.objects.create(id='HIST4303', name='Global Histories of Children and Childhood', school=humanities, level=4,
                          credits=60)
    Module.objects.create(id='HIST4316', name='Black Communities in the Diaspora (1605-2025)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST4261',
                          name='Czechoslovakia: A case study of a country in Europe through the history of film',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5192', name='Byzantium and the Rise of Islam', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST1028', name='Summer Research Project in History B', school=humanities, level=1,
                          credits=25)
    Module.objects.create(id='HIST5154',
                          name='The Medievalists: the Middle Ages in 20th century Eastern and Central Europe',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4280', name='Becoming an Historian', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5123', name='Scottish Radicalism 1848-1950', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5158', name='The Global History of Inequalities', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4019', name='REBELLION, TREASON AND POLITICAL OPPOSITION - 1066-1352',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4250',
                          name='Century of the refugee: refugees & statelessness in the long twentieth century, c.1900-present (SS)',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST4300', name='Myths of Africa: Africa and Africans in Global History',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5200', name='The Global History of Inequalities (DL)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5008', name='Gender, Politics And Power', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5161', name='Qualitative Approaches to the Study of Political Violence',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4299', name='The Age of Justinian in the Mediterranean', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST4288',
                          name='From Scrolls to Screens: the Materiality of Manuscripts in the 21st Century',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4268', name='History through film and literature: Crisis situations',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4246',
                          name='The Medievalists: the Middle Ages in 20th century Eastern and Central Europe',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4304', name='The Political Worlds of Women in Nineteenth-Century Britain',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4281P', name='Applied Dissertation with Placement in History', school=humanities,
                          level=4, credits=40)
    Module.objects.create(id='HIST5181', name='Reparations Now I (DL)', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4266', name='Urban Lives: Gender, Culture and Society in the Eighteenth-Century Town',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5162', name='Reparations Now (Part One)', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST2016', name='History 2A: The Social and Cultural History of Europe, 1500-2000',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='HIST4226', name='Society and Religion in the Medieval Crusader States', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST4311', name='British LGBTQ+ History', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5174P', name='Dissertation. Reparatory Justice.', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='HIST4301', name='Animals and History, c. 1300 - c. 1600', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST5206', name='Reparatory Justice Project', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4312', name='Women And Feminist Movements In Europe C 1789-1980', school=humanities,
                          level=4, credits=60)
    Module.objects.create(id='HIST5207', name='Scottish Popular Culture 1500-1800 (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4207', name='The Transatlantic Slave Trade and the Development of Plantation Slavery',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST5107', name='Gender, Culture and Text', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5152', name='Global History through Local Archives', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5136', name='Plantation and Civility in the Hebrides and in Ulster, c1541-1639',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST2017', name='Scotland and the World (Summer School)', school=humanities, level=2,
                          credits=10)
    Module.objects.create(id='HIST4293', name='The First World War, 1911-1923 (SS)', school=humanities, level=4,
                          credits=60)
    Module.objects.create(id='HIST4305', name='Memory Studies: Introduction to an Interdisciplinary Field',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5198', name='Oral History Theory and Methods (DL)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5132', name='Women and Power in Renaissance Italy', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5205', name='Memory Studies: An Interdisciplinary Field (PGT)', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST4241', name='The Mongols and the West, c.1200 - c.1500', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST1022', name='Introduction to Scottish Culture Semester 1', school=humanities, level=1,
                          credits=10)
    Module.objects.create(id='HIST5191', name='Qualitative Approaches to the Study of Political Violence (DL)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4204',
                          name='Punishment, Internment and Containment: The History and Archaeology of Prisons and Camps',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5159', name='The Global Cold War, 1947-2008', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5151', name='Exploring Global History', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4022', name='Soviet/Russian Concepts of National Security from 1917 to Today',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5208',
                          name='Empire in the city: the British empire and the making of urban space in Glasgow, 1707-2014 (PGT)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4262', name='A Global History of Giving: from Begging to Basic Income',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5204', name='Gender, Politics And Power (DL)', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4258', name='The Making of Britain? Scotland and Ireland, 1707-c.1815',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5012', name='Issues, Ideologies And Institutions Of Modern Scotland',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5201', name='Games and Gaming (MCS)', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST2015', name='History2B: An Introduction to Global History', school=humanities,
                          level=2, credits=20)
    Module.objects.create(id='HIST4089', name='Oral History Theory and Methods (Hons)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST4298', name='American Freedom: Civil Rights Movements in the \'20th Century\'',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4005', name='Demanding The Impossible: European Societies In The 1960s',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST4082P', name='History Dissertation', school=humanities, level=4, credits=40)
    Module.objects.create(id='HIST4247', name='Plantation and Civility in the Hebrides and in Ulster, c1541-1639',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST1008',
                          name='History 1A: Scotland\'s Millennium: Kingdom, Union and Nation c 1000-2014',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='HIST4124', name='Scottish Popular Culture 1500-1800 (Honours)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST5209P', name='MCS Independent Research Project (HIST)', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='HIST4211', name='France, 1789-1914: Nation, Revolution and Empire (HIST 4211) - Honours.',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5039P', name='Dissertation (MSc in War Studies)', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='HIST5142', name='Medieval Palaeography: An Introduction to Reading Medieval Documents',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5146', name='Resistance to Slavery from 1700 to 1900', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4318', name='Historical Archaeology of the Black Atlantic', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST5155', name='The World of the Crusades: Critical Approaches to Medieval Sources',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5147', name='Working with Manuscripts as Historians', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4292', name='The Rise of Nineteenth Century Socialism', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST4314', name='Global Environmental Histories of Empire', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST5202', name='Gender History Applied (MCS)', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5055', name='Special Topic In History', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4308', name='Byzantium and the Rise of Islam', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5210', name='Slavery and Forced Migration in Global Perspective (DL)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5172', name='Making a Living: Work, Gender and Society 1700-1850', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST1020',
                          name='History 1B: A Medieval Mosaic: Europe and Its Neighbours in the Middle Ages, c.400-1500',
                          school=humanities, level=1, credits=20)
    Module.objects.create(id='HIST5171', name='Personal Testimony for Historians: theory, method, practice',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4227', name='The Radical Fringes of Interwar Europe, 1918-1936', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST5194', name='Approaches to Queer and Trans Histories (Distance Learning)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4289', name='Surviving and Resisting Enslavement in the British Caribbean',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST5180', name='Reproductive rights and justice: Historical perspectives',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5183', name='Women and Power in Renaissance Italy (DL)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST4287',
                          name='The Making of the Spanish Empire: Indigenous American, African, Asian and European perspectives',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST4206', name='Scottish Radicalism and Scottish Society, 1790-1945 (SS)',
                          school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST4320', name='Race in Scotland\'s History', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5140', name='Military Scotland in the Age of Proto-globalization, c.1600-c.1800',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5179', name='How Wars End', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4044', name='Anarchy & Society:The Reign Of Stephen', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='HIST4149', name='The Highland Clearances', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST4186', name='Modern Britain at War: From Rorke\'s Drift to Port Stanley',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST2018', name='Scotland and the World (Summer School)', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='HIST4275', name='What\'s in a Cup? The Global History of Coffee', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='HIST1027', name='Summer Research Project in History A', school=humanities, level=1,
                          credits=24)
    Module.objects.create(id='HIST5038P', name='Dissertation (MSc History)', school=humanities, level=5, credits=60)
    Module.objects.create(id='HIST5088', name='Battles, Conflicts and their Legacies', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5021', name='The American Way Of War', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5196', name='Gender History Concepts', school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST4243', name='Race and Slavery in the Eighteenth Century British Atlantic World',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5118', name='Crusading Warfare in the Eastern Mediterranean, 1096-1291',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5195',
                          name='A \'New Form of Slavery\'?: Indentured Labour in Post-Slavery Caribbean Societies, c. 1836-1917 (DL)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='HIST5164', name='Slavery and Forced Migration in Global Perspective', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST4210', name='European Politics, 1860-1914', school=humanities, level=4, credits=20)
    Module.objects.create(id='HIST5138', name='Intelligence Analysis & Policy Making', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5175', name='Oral History Theory and Methods (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='HIST5156', name='Doing History: Sources and Skills for Historians', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='HIST4263', name='Genocide in the Modern World', school=humanities, level=4, credits=60)
    Module.objects.create(id='HIST5170', name='Gender History Applied (DL)', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4019', name='AI for the Arts and Humanities (B)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST2002', name='Digital Media and Information Studies 2B', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='INFOST1001', name='Digital Media and Information Studies 1A', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='INFOST4006', name='Document Encoding', school=humanities, level=4, credits=20)
    Module.objects.create(id='INFOST4007', name='Enterprise, Creativity and Citizenship Online', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='INFOST4004', name='Digital Creativity', school=humanities, level=4, credits=20)
    Module.objects.create(id='INFOST5010', name='Description, Cataloguing and Navigation', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5015', name='Digital Cultural Heritage', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST1002', name='Digital Media and Information Studies 1B', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='INFOST4017P', name='Dissertation in Digital Media and Information Studies',
                          school=humanities, level=4, credits=40)
    Module.objects.create(id='INFOST5025', name='Empire and its Legacies in Memory Institutions', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST5013', name='Evaluating Library, Archive and Museum Services', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST5031', name='History of Information Communication Technology (MCS)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4020P', name='Dissertation by Individual Project', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='INFOST5032', name='Introduction to Digital Humanities (MCS)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST4001', name='2D Digitisation: Theory & Practice (Hons)', school=humanities, level=4,
                          credits=40)
    Module.objects.create(id='INFOST5026', name='Records and Evidence', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5017', name='Introduction to Museology', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4013', name='Music Curation and Analytics', school=humanities, level=4, credits=20)
    Module.objects.create(id='INFOST5042', name='Digital Humanities Skills and Methods', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST4008', name='Digital Cultural Heritage', school=humanities, level=4, credits=20)
    Module.objects.create(id='INFOST4005', name='Digital Media and Information Studies Study Abroad', school=humanities,
                          level=4, credits=120)
    Module.objects.create(id='INFOST5039P', name='MCS Independent Research Project (INFOST)', school=humanities,
                          level=5, credits=60)
    Module.objects.create(id='INFOST5029', name='An Introduction to Information Management', school=humanities, level=5,
                          credits=10)
    Module.objects.create(id='INFOST5009', name='Curating the Sciences', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5016', name='Introduction to Digital Curation', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5038P', name='Library and Information Studies Dissertation', school=humanities,
                          level=5, credits=60)
    Module.objects.create(id='INFOST5008', name='Curating Lively Practices', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5036', name='Special Collections and Digital Scholarship', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST4016P', name='DMIS Joint Honours Dissertation', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST5011', name='Document Encoding', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4009', name='History of Information Communication Technology', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='INFOST4010', name='Introduction to Digital Humanities', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST4003', name='Data Analysis, Visualisation and Communication', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='INFOST4015P',
                          name='Applied Dissertation with Placement in Digital Media & Information Studies',
                          school=humanities, level=4, credits=40)
    Module.objects.create(id='INFOST5005', name='Archives & Records Theory', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4011', name='Multimedia Analysis & Design (A)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST5030', name='Enterprise, Creativity and Citizenship Online (MCS)',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST4014', name='Records, Accountability, and Society', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST5037', name='Research Design and Methods in Information Studies', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST5006', name='Professional Issues in Archives and Records', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST4012', name='Multimedia Analysis & Design (B)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST2001', name='Digital Media and Information Studies 2A', school=humanities, level=2,
                          credits=20)
    Module.objects.create(id='INFOST5023', name='Museum Skills and Professional Practice', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5001P', name='Archives, Records, & Information Management and Dissertation',
                          school=humanities, level=5, credits=60)
    Module.objects.create(id='INFOST5022', name='Learning and Engagement in Cultural Heritage', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST5034', name='Information and Society', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5040', name='Critical Approaches to Digital Humanities', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5014', name='Exhibition Development (The Hunterian)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5003P', name='Museum Studies Dissertation', school=humanities, level=5, credits=60)
    Module.objects.create(id='INFOST5024', name='Museum Studies Work Placement', school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5041P', name='Applied Dissertation Digital Humanities', school=humanities, level=5,
                          credits=60)
    Module.objects.create(id='INFOST5012', name='Early Modern Palaeography', school=humanities, level=5, credits=5)
    Module.objects.create(id='INFOST5033', name='Digital Cultural Heritage (MCS)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST5019', name='Law, Information Governance and Collections', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST5043', name='Project Design and Management in Digital Humanities',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='INFOST5004', name='2D Digitisation: Theory & Practice (PGT)', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='INFOST4018', name='AI for the Arts and Humanities (A)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='INFOST5035', name='Libraries and Information Services Management', school=humanities,
                          level=5, credits=20)
    Module.objects.create(id='INFOST2003', name='Digital Media and Information Studies 2A - Online Version',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='INFOST4002', name='Books as New Media', school=humanities, level=4, credits=20)
    Module.objects.create(id='INFOST2004', name='Digital Media and Information Studies 2B - Online Version',
                          school=humanities, level=2, credits=20)
    Module.objects.create(id='INFOST5021', name='Managing and Using Collections', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='LATIN1001', name='Latin 1A: Basic Latin 1', school=humanities, level=1, credits=20)
    Module.objects.create(id='LATIN4001', name='Intermediate Latin for Honours 1', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='LATIN2002', name='Latin 2B: Intermediate Latin 2', school=humanities, level=2, credits=20)
    Module.objects.create(id='LATIN1002', name='Latin 1B: Basic Latin 2', school=humanities, level=1, credits=20)
    Module.objects.create(id='LATIN4003', name='Basic Latin For Honours 1', school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN5010', name='Further Topic In Latin 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='LATIN4029', name='Stargazing: Astronomy, Astrology and Meteorology in Antiquity',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN5008P', name='Latin Manuscripts (Project)', school=humanities, level=5, credits=20)
    Module.objects.create(id='LATIN4028', name='Roman Warfare', school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN4031',
                          name='The Roman Stage: A History of Roman Drama from the Republic to the Empire (Latin)',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN5003', name='Basic Latin For Postgraduates 1', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='LATIN4002', name='Intermediate Latin for Honours 2', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='LATIN5007', name='Latin Manuscripts (Core)', school=humanities, level=5, credits=20)
    Module.objects.create(id='LATIN4030',
                          name='Imperium Indivisum?: The Collapse of the West Roman Empire in the fifth century AD (Latin)',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN4036', name='Religions of Rome (LATIN, Hons)', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='LATIN5011', name='Further Topic In Latin 2', school=humanities, level=5, credits=20)
    Module.objects.create(id='LATIN4035', name='Rhetoric at Rome (Latin)', school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN4033', name='Love and War: Latin poetry at the end of the Republic',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN3001', name='Advanced Latin', school=humanities, level=3, credits=40)
    Module.objects.create(id='LATIN4005', name='Latin Unprepared Translation (Senior Honours)', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='LATIN5004', name='Basic Latin For Postgraduates 2', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='LATIN5001', name='Intermediate Latin For Postgraduates 1', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='LATIN4022P', name='Dissertation (Latin)', school=humanities, level=4, credits=40)
    Module.objects.create(id='LATIN2001', name='Latin 2A: Intermediate Latin 1', school=humanities, level=2, credits=20)
    Module.objects.create(id='LATIN4004', name='Basic Latin For Honours 2', school=humanities, level=4, credits=20)
    Module.objects.create(id='LATIN5002', name='Intermediate Latin For Postgraduates 2', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='PHIL4071', name='Social Epistemology', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4074', name='Social Philosophy', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4066', name='Causation', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL3011', name='History of Modern Philosophy Non Honours', school=humanities, level=3,
                          credits=20)
    Module.objects.create(id='PHIL2011', name='Philosophy 2B: What is there?', school=humanities, level=2, credits=20)
    Module.objects.create(id='PHIL4016', name='History Of Western Philosophy', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL1010', name='Philosophy 1A: How Should I Think?', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='PHIL5065', name='Contemporary Ethics', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5115', name='Classical Indian Philosophy: Language, Knowledge, and Reality',
                          school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5105', name='Pain & Pleasure', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5072', name='Liberalism', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5068', name='Formal Logic', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4006P', name='Directed Individual Research/Dissertation (Semester 2)',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5113', name='Introduction to Analytic Philosophy B', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='PHIL3012', name='Moral Philosophy Non Honours', school=humanities, level=3, credits=20)
    Module.objects.create(id='PHIL4064', name='Philosophy of Law', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4029', name='Philosophy Of Mathematics', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4073', name='Philosophy of Science', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4063', name='Virtue Ethics', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4007P', name='Directed Individual Research/Dissertation (Semester 1)',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5008', name='Philosophy Of Language A', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5095', name='Philosophy Research Methods B', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4027', name='Philosophy Of Art', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4041', name='Senior Honours Reading Seminar', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5112', name='Introduction to Analytic Philosophy A', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='PHIL4022', name='Metaphysics', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5106', name='Philosophy of Law', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4030', name='Philosophy Of Mind', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5097', name='Feminist Philosophy', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4039', name='Political Philosophy', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4028', name='Philosophy Of Language', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5080', name='Political Philosophy', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4070', name='Classical Indian Philosophy: Language, Knowledge, and Reality',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4018', name='Mind and Knowledge in the Scottish Enlightenment', school=humanities,
                          level=4, credits=20)
    Module.objects.create(id='PHIL5090', name='Philosophy Of Perception', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4069', name='Dreams', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4054', name='Distributive Justice', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5075', name='Philosophy Of Art', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5073', name='Metaphysics', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5102', name='Virtue Epistemology PGT', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4044', name='Liberalism', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4004', name='Contemporary Ethics', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4014', name='Formal Logic', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5005', name='Moral Philosophy B', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4043', name='Wittgenstein', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL2010', name='Philosophy 2A: What am I?', school=humanities, level=2, credits=20)
    Module.objects.create(id='PHIL5074', name='Moral Philosophy', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5116', name='Philosophy of Science', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4034', name='Philosophy Of Religion', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5114', name='Distributive Justice (PGT)', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5067', name='Epistemology', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5011', name='Philosophy Of Perception B', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5092', name='Epistemology B', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5001P', name='Philosophy Dissertation', school=humanities, level=5, credits=60)
    Module.objects.create(id='PHIL4011', name='Epistemology', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4060', name='Pain and Pleasure', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4059', name='Moral Epistemology', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4067',
                          name='Consciousness: Brains, Artificial Intelligence, and Subjective Experience',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5010', name='Philosophy Of Perception A', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4019', name='Virtue Epistemology', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL3013', name='Philosophy of Mind Non Honours', school=humanities, level=3, credits=20)
    Module.objects.create(id='PHIL4075', name='Doing Philosophy', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4031', name='Philosophy Of Perception', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5096', name='Philosophy Research Methods C', school=humanities, level=5, credits=10)
    Module.objects.create(id='PHIL4042', name='Senior Honours Reading Seminar', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5111', name='Dreams PGT', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5076', name='Philosophy Of Language', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4017', name='History of Moral and Political Philosophy', school=humanities, level=4,
                          credits=20)
    Module.objects.create(id='PHIL4065', name='Marxism and Anarchism', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL3014', name='Political Philosophy Non Honours', school=humanities, level=3,
                          credits=20)
    Module.objects.create(id='PHIL4068', name='Inquiry, Science, and Democracy: The Philosophy of Susan Stebbing',
                          school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL4061', name='Gender and Race', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL1011', name='Philosophy 1B: How Should I Live?', school=humanities, level=1,
                          credits=20)
    Module.objects.create(id='PHIL5070', name='History Of Moral And Political Philosophy', school=humanities, level=5,
                          credits=20)
    Module.objects.create(id='PHIL5099', name='Gender and Race', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5078', name='Philosophy Of Mind', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4024', name='Moral Philosophy', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5094', name='Philosophy Research Methods A', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL5069', name='History Of Modern Philosophy 1', school=humanities, level=5, credits=20)
    Module.objects.create(id='PHIL4072', name='The Philosophy of A.I.', school=humanities, level=4, credits=20)
    Module.objects.create(id='PHIL5108', name='Causation', school=humanities, level=5, credits=20)

    # School of Infection and Immunity (44 modules)
    Module.objects.create(id='BIOL4248P', name='Life Sciences Outreach Honours Project', school=infection, level=4,
                          credits=40)
    Module.objects.create(id='BIOL5366', name='Designing a Research Project: Infection Biology', school=infection,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5232', name='Work Placement Year in Life Sciences', school=infection, level=5,
                          credits=120)
    Module.objects.create(id='BIOL4057', name='Immunology 3B', school=infection, level=4, credits=60)
    Module.objects.create(id='BIOL4185', name='Fundamental Topics in Molecular Immunology 4Y option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4033', name='Core Skills in Microbiology 4X core', school=infection, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5319P', name='MSc Bioscience Research Project (Infection Biology)', school=infection,
                          level=5, credits=60)
    Module.objects.create(id='BIOL5173P', name='MSc Bioinformatics Project', school=infection, level=5, credits=60)
    Module.objects.create(id='BIOL5314', name='Emerging viruses', school=infection, level=5, credits=10)
    Module.objects.create(id='BIOL5379', name='Data Exploration and Interpretation for Bioinformatics',
                          school=infection, level=5, credits=10)
    Module.objects.create(id='BIOL5365', name='Designing a Research Project: Immunology and Inflammatory Disease',
                          school=infection, level=5, credits=20)
    Module.objects.create(id='BIOL5354', name='Omic Data Analysis and Visualisation, using R, for Biologists',
                          school=infection, level=5, credits=10)
    Module.objects.create(id='BIOL4186', name='Immunological Basis of Inflammatory Disease 4D option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4093', name='Medical Microbiology 3B', school=infection, level=4, credits=60)
    Module.objects.create(id='BIOL2044', name='Microbiology and Immunology 2', school=infection, level=2, credits=30)
    Module.objects.create(id='BIOL5421', name='Further Omics, Statistics and Clinical data in R', school=infection,
                          level=5, credits=20)
    Module.objects.create(id='BIOL4061', name='Industrial and Environmental Microbiology 4Y option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4092', name='Medical Microbiology 3A', school=infection, level=4, credits=60)
    Module.objects.create(id='BIOL5299', name='Pathogen Polyomics', school=infection, level=5, credits=20)
    Module.objects.create(id='BIOL5197', name='Omic analyses for the biomedical sciences: from genomics to metabolomic',
                          school=infection, level=5, credits=20)
    Module.objects.create(id='BIOL4297', name='Bioinformatics and Data Analysis using R 4B option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4224', name='Medical Virology 4C option', school=infection, level=4, credits=20)
    Module.objects.create(id='BIOL2040', name='Contemporary Issues in Biology 2', school=infection, level=2, credits=30)
    Module.objects.create(id='BIOL5289P', name='Life Sciences Outreach MSci Project', school=infection, level=5,
                          credits=40)
    Module.objects.create(id='BIOL5237', name='Immunology and Inflammatory Disease: Basic, Translational and Clinical',
                          school=infection, level=5, credits=40)
    Module.objects.create(id='BIOL5381', name='Biological Computing in Python', school=infection, level=5, credits=10)
    Module.objects.create(id='BIOL4056', name='Immunology 3A', school=infection, level=4, credits=60)
    Module.objects.create(id='BIOL5291', name='Neuroinflammation in health and disease', school=infection, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5369', name='Research Skills for Immunology and Infection Biology', school=infection,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5318P', name='MSc Bioscience Research Project (Immunology & Inflammatory Disease)',
                          school=infection, level=5, credits=60)
    Module.objects.create(id='BIOL4184', name='Fundamental Topics in Immunology 4X core', school=infection, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4222', name='Grand Challenges in Medical Microbiology 4D option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4223', name='Emerging Viruses 4A option', school=infection, level=4, credits=20)
    Module.objects.create(id='BIOL4189', name='Immunology of Infection 4A option', school=infection, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4246P', name='Life Sciences Investigative Honours Project', school=infection, level=4,
                          credits=40)
    Module.objects.create(id='BIOL5463', name='Pandemic preparedness', school=infection, level=5, credits=20)
    Module.objects.create(id='BIOL5196', name='Host-pathogen interactions and immune responses to infection',
                          school=infection, level=5, credits=40)
    Module.objects.create(id='BIOL4295', name='Molecular and Cellular Microbiology 4Y option', school=infection,
                          level=4, credits=20)
    Module.objects.create(id='BIOL5465', name='Single Cell and Spatial Omics for Biologists', school=infection, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5238', name='Animal Models of Disease', school=infection, level=5, credits=10)
    Module.objects.create(id='BIOL5287P', name='Life Sciences Investigative MSci Project', school=infection, level=5,
                          credits=40)
    Module.objects.create(id='BIOL4292', name='Programming and Databases for Biologists', school=infection, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4030', name='Chemotherapy, Resistance and Parasite Control 4B option',
                          school=infection, level=4, credits=20)
    Module.objects.create(id='BIOL5177', name='RNA-seq and Next Generation Transcriptomics', school=infection, level=5,
                          credits=20)

    # School of Law (222 modules)
    Module.objects.create(id='LAW4157', name='Debates in Private Law Theory', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4016', name='Competition Law', school=law, level=4, credits=40)
    Module.objects.create(id='LAW4195', name='Equality Law and Society', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2047', name='Jurisprudence (FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4011P', name='Dissertation In Law', school=law, level=4, credits=40)
    Module.objects.create(id='LAW1003', name='Criminal Law And Evidence 1', school=law, level=1, credits=20)
    Module.objects.create(id='LAW5181', name='Financial Technology (FinTech) Regulation', school=law, level=5,
                          credits=10)
    Module.objects.create(id='LAW4182', name='Water Rights and Global Challenges', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4165', name='Legal Responses to Domestic and Honour Abuse', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW5054P', name='LLM Dissertation', school=law, level=5, credits=60)
    Module.objects.create(id='LAW5012', name='Conveyancing (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5204', name='Law and Sustainable Finance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4194', name='Death, Dying and the Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4047', name='Overseas Honours Option 1', school=law, level=4, credits=30)
    Module.objects.create(id='LAW2042', name='Business Organisations (FR)', school=law, level=2, credits=15)
    Module.objects.create(id='LAW4127', name='INTERNATIONAL FAMILY LAW', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4199', name='Legal Theory', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5026', name='Foundations Of International Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4189', name='Globalisation, Justice and Human Rights', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5007', name='Civil Litigation (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW2007', name='Jurisprudence', school=law, level=2, credits=20)
    Module.objects.create(id='LAW2053', name='Equity and Trusts (CL-FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4206', name='Social Security Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2037', name='EUROPEAN COMPARATIVE LAW PROJECT', school=law, level=2, credits=10)
    Module.objects.create(id='LAW4162', name='Citizens v The State', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4168', name='Criminal Justice Issues', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5028', name='FUNDAMENTALS OF INTERNATIONAL LAW', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2057', name='Jurisprudence (Common Law)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4197', name='Intellectual Property Law: Culture and Personality', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW1038', name='Obligations 1A (FR)', school=law, level=1, credits=15)
    Module.objects.create(id='LAW5040', name='International Trade Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2054', name='Foundations of Evidence Law (CL-FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4191', name='Adult Relationships and the Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4024', name='Human Reproduction And The Law', school=law, level=4, credits=40)
    Module.objects.create(id='LAW5183', name='Dispute Resolution II: The Practice of Investment Arbitration',
                          school=law, level=5, credits=15)
    Module.objects.create(id='LAW5037', name='International Competition Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5013', name='Copyright In The Digital Environment', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5209', name='National Human Rights Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2001', name='Business Organisations', school=law, level=2, credits=15)
    Module.objects.create(id='LAW4187', name='Law and Digital Creative Industries', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4167', name='Comparative Issues in Children\'s Rights', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4183', name='Healthcare Law', school=law, level=4, credits=40)
    Module.objects.create(id='LAW4218', name='Housing & Homelessness Law Clinic', school=law, level=4, credits=20)
    Module.objects.create(id='LAW1023', name='Constitutional Law 1', school=law, level=1, credits=30)
    Module.objects.create(id='LAW5200', name='International Law and International Politics', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW4180', name='Law and Sustainability in the Anthropocene', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW5130', name='International Law and International Security', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW4207', name='Visiting Students (Semester 1) Competition Law', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW5238', name='Regulating Artificial Intelligence in the Creative Economy', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW5074', name='Criminal Litigation (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW4154', name='Gender, Sexualities and Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2043', name='Commercial Law (FR)', school=law, level=2, credits=15)
    Module.objects.create(id='LAW4220', name='Law of the Sea', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4060', name='Courses Abroad (15)', school=law, level=4, credits=15)
    Module.objects.create(id='LAW2003', name='Environmental Law', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4004', name='Commercial Law (Honours)', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4059', name='Courses Abroad (10)', school=law, level=4, credits=10)
    Module.objects.create(id='LAW5177', name='Employment Law (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW2044', name='European Union Law (Common law - FR)', school=law, level=2, credits=10)
    Module.objects.create(id='LAW5031', name='Human Rights Law (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW4029', name='International Criminal Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5228', name='FinTech Law and Regulation', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4007', name='Constitutional Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4048', name='Overseas Honours Option 2', school=law, level=4, credits=30)
    Module.objects.create(id='LAW1027', name='Law of Contract', school=law, level=1, credits=20)
    Module.objects.create(id='LAW2002', name='Commercial Law', school=law, level=2, credits=15)
    Module.objects.create(id='LAW2058', name='Law and Government (Common Law)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW5240', name='Data and Artificial Intelligence in the Creative Economy', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW5033', name='Intellectual Property Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4038', name='Law, Justice And Morality', school=law, level=4, credits=40)
    Module.objects.create(id='LAW1045', name='Constitutional Law (Common Law)', school=law, level=1, credits=30)
    Module.objects.create(id='LAW4215', name='International Law and the Global Economy', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4169', name='Criminal Justice Process', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5002', name='Advanced Civil Litigation (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5046', name='International Merger Control', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4201', name='Property Theory and Rights', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4190', name='Law and Political Economy', school=law, level=4, credits=40)
    Module.objects.create(id='LAW2011', name='Property Law', school=law, level=2, credits=40)
    Module.objects.create(id='LAW5043', name='International Human Rights Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4034', name='Law and Social Theory', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4064', name='Courses Abroad (75)', school=law, level=4, credits=75)
    Module.objects.create(id='LAW5066', name='International Courts and Tribunals', school=law, level=5, credits=20)
    Module.objects.create(id='LAW1021', name='Obligations 1A', school=law, level=1, credits=15)
    Module.objects.create(id='LAW5069', name='United Nations Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5236', name='Law and Just Energy Transition', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5185P', name='Investment Law Dissertation (LLM)', school=law, level=5, credits=60)
    Module.objects.create(id='LAW2008', name='Jurisprudence 2 (Abroad)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4212', name='Visiting Students (Semester 1) Politics of Labour Law', school=law,
                          level=4, credits=20)
    Module.objects.create(id='LAW5151', name='Law and Cultural Institutions', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5063', name='Public Law (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW1035', name='Constitutional Law 1 (FR)', school=law, level=1, credits=30)
    Module.objects.create(id='LAW4198', name='Law and Genetics', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4153', name='Women, Law and Society', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5154', name='The Laws of Armed Conflict', school=law, level=5, credits=20)
    Module.objects.create(id='LAW1020', name='Introduction to Legal Study', school=law, level=1, credits=10)
    Module.objects.create(id='LAW1043', name='Law of Torts (CL-FR)', school=law, level=1, credits=20)
    Module.objects.create(id='LAW2018', name='Law Placement', school=law, level=2, credits=10)
    Module.objects.create(id='LAW4063', name='Courses Abroad (60)', school=law, level=4, credits=60)
    Module.objects.create(id='LAW1006', name='Public International Law', school=law, level=1, credits=20)
    Module.objects.create(id='LAW5178', name='Introduction to Legal Innovation and Technology (DPLP)', school=law,
                          level=5, credits=15)
    Module.objects.create(id='LAW4125', name='Property Law: History and Comparison', school=law, level=4, credits=20)
    Module.objects.create(id='LAW1039', name='Obligations 1B (FR)', school=law, level=1, credits=15)
    Module.objects.create(id='LAW1037', name='Family Law (FR)', school=law, level=1, credits=10)
    Module.objects.create(id='LAW1034', name='Constitutional Law 1 (Common Law - FR)', school=law, level=1, credits=30)
    Module.objects.create(id='LAW4178', name='Freedom of Speech', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5019', name='The Law of Secured Finance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4010', name='Criminal Law: Theory and Doctrine', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5237', name='Fundamentals of Environmental Justice', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4173', name='Comparative Legal History', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5201', name='Transnational Crime, Justice, and Security', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW4203', name='The Emma Ritch Law Clinic Project', school=law, level=4, credits=40)
    Module.objects.create(id='LAW1044', name='English Family Law', school=law, level=1, credits=20)
    Module.objects.create(id='LAW1007', name='Roman Law Of Property & Obligations 1', school=law, level=1, credits=20)
    Module.objects.create(id='LAW2039', name='Equity and Trusts', school=law, level=2, credits=20)
    Module.objects.create(id='LAW1042', name='Law of Contract (CL-FR)', school=law, level=1, credits=20)
    Module.objects.create(id='LAW2041', name='Business Organisations (Common Law) (FR)', school=law, level=2,
                          credits=15)
    Module.objects.create(id='LAW4129', name='Comparative Constitutional Rights', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5025', name='Family Law (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5208', name='Advanced Introduction to the European Convention on Human Rights',
                          school=law, level=5, credits=20)
    Module.objects.create(id='LAW4164', name='Contemporary Issues in European Human Rights Law', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4177', name='Criminal Responsibility', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2004', name='European Law 2 (Abroad)', school=law, level=2, credits=15)
    Module.objects.create(id='LAW5159', name='International Law and International Economic Governance', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW5197', name='Corporate Finance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW1026', name='Criminal Law of England and Wales', school=law, level=1, credits=20)
    Module.objects.create(id='LAW4174', name='Constitutionalism and the European Union', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4213', name='Visiting Students (Semester 1) Human Reproduction and the Law',
                          school=law, level=4, credits=20)
    Module.objects.create(id='LAW4221P', name='Cryptolaw', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4166', name='Children\'s Rights', school=law, level=4, credits=20)
    Module.objects.create(id='LAW1004', name='Family Law', school=law, level=1, credits=10)
    Module.objects.create(id='LAW4150', name='Comparative Human Rights: Law and Legitimacy', school=law, level=4,
                          credits=40)
    Module.objects.create(id='LAW5212', name='International Insolvency Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5052', name='Law Research Methods', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5170', name='Patents and Innovation', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2052', name='Foundations of Evidence Law', school=law, level=2, credits=20)
    Module.objects.create(id='LAW5191', name='Law and International Development (EM)', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4204', name='Human Rights Systems: Law and Legitimacy', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4061', name='Courses Abroad (30)', school=law, level=4, credits=30)
    Module.objects.create(id='LAW5017', name='Corporate(DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5015', name='Corporate Governance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4005', name='Company Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2055', name='Land Law (CL-FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4095', name='The Politics Of Labour Law', school=law, level=4, credits=40)
    Module.objects.create(id='LAW5044', name='International Investment Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5061', name='Private Client (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5213P', name='Collaborative LLM dissertation', school=law, level=5, credits=60)
    Module.objects.create(id='LAW5192', name='Foundations of International Law (EM)', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5196', name='Climate Change Law and Governance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2046', name='Jurisprudence (Common Law - FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4062', name='Courses Abroad (45)', school=law, level=4, credits=45)
    Module.objects.create(id='LAW2040', name='Commercial Law (Common Law)', school=law, level=2, credits=15)
    Module.objects.create(id='LAW2049', name='Law and Government (FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW1036', name='Criminal Law And Evidence 1 (FR)', school=law, level=1, credits=20)
    Module.objects.create(id='LAW4216', name='International Law and Armed Conflict', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5235', name='Global Constitutionalism: Rise, Decline, Resilience', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW4209',
                          name='Visiting Students (Semester 1) International Law and the Problems of Contemporary World Order',
                          school=law, level=4, credits=20)
    Module.objects.create(id='LAW1028', name='Common Law System and Method', school=law, level=1, credits=10)
    Module.objects.create(id='LAW2010', name='Law and Government', school=law, level=2, credits=20)
    Module.objects.create(id='LAW5132', name='International and Comparative Intellectual Property Law', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW2045', name='European Union Law (FR)', school=law, level=2, credits=10)
    Module.objects.create(id='LAW5035', name='International Human Rights Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4176', name='Courts and Judicial Power', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4051', name='United Nations Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5222', name='Commercial Insurance Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW1029', name='Law of Torts', school=law, level=1, credits=20)
    Module.objects.create(id='LAW4193', name='Cybercrime Investigations and Enforcement', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4205', name='Philosophy of Human Rights Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5039', name='Advanced Introduction to International Criminal Law', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW5173', name='Property Law for Real Estate Surveyors', school=law, level=5, credits=10)
    Module.objects.create(id='LAW5042', name='Banking Regulation', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2005', name='European Union Law', school=law, level=2, credits=10)
    Module.objects.create(id='LAW5011', name='Contemporary Issues In Intellectual Property Law', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW5182', name='Introduction to International Investment Law', school=law, level=5,
                          credits=30)
    Module.objects.create(id='LAW5206', name='Information Law and Policy', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5184', name='Investment Law: Current Trends and Challenges', school=law, level=5,
                          credits=15)
    Module.objects.create(id='LAW5234', name='Policy Challenge in Intellectual Property and Technology', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW2050', name='Property Law (FR)', school=law, level=2, credits=40)
    Module.objects.create(id='LAW5057P', name='MRes Dissertation (LAW)', school=law, level=5, credits=60)
    Module.objects.create(id='LAW4026', name='Immigration Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW1041', name='Criminal Law of England and Wales (CL-FR)', school=law, level=1,
                          credits=20)
    Module.objects.create(id='LAW1001', name='Business Law', school=law, level=1, credits=20)
    Module.objects.create(id='LAW3010', name='Law Summer School', school=law, level=3, credits=10)
    Module.objects.create(id='LAW5223', name='Competition, Innovation and Digital Markets', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW5047', name='International Sales and Finance', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5186', name='Advanced Introduction to International Criminal Law (EM)', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW5160', name='Trade Marks and Brands', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2031', name='Advanced International Law', school=law, level=2, credits=20)
    Module.objects.create(id='LAW2006', name='International Private Law Level 2', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4211', name='Visiting Students (Semester 1) Law, Justice and Morality', school=law,
                          level=4, credits=20)
    Module.objects.create(id='LAW5038', name='Advanced Competition Law and Society', school=law, level=5, credits=20)
    Module.objects.create(id='LAW5014', name='International Capital Markets Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2034', name='Continental Legal Culture', school=law, level=2, credits=10)
    Module.objects.create(id='LAW5068', name='Advanced Introduction to the Law of the United Nations', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW5162', name='Commercial Property', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5034', name='Intellectual Property Law And The Market', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW5227', name='Technology Regulation Maker Lab', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2014', name='Citizens Advice Bureau Placement', school=law, level=2, credits=10)
    Module.objects.create(id='LAW1022', name='Obligations 1B', school=law, level=1, credits=15)
    Module.objects.create(id='LAW4217', name='International Dispute Settlement', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4219', name='Lawyering for Social Change: Racial Justice Clinic', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4084', name='Law In The Roman World', school=law, level=4, credits=20)
    Module.objects.create(id='LAW5161', name='Commercial Contracts', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5239', name='Digital Creators, Artificial Intelligence and the Law', school=law,
                          level=5, credits=20)
    Module.objects.create(id='LAW4159', name='INTERNATIONAL COMMERCIAL ARBITRATION', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4172', name='Parenthood and the Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4171',
                          name='Moveable Property Law and Trusts: Concepts, Comparisons and Security Rights',
                          school=law, level=4, credits=20)
    Module.objects.create(id='LAW5071', name='Commercial Awareness (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW5229', name='Business Strategies and Competition Policy', school=law, level=5,
                          credits=20)
    Module.objects.create(id='LAW1011', name='Elements Of Law For Engineers 1', school=law, level=1, credits=10)
    Module.objects.create(id='LAW5004', name='Advanced Criminal Litigation (DPLP)', school=law, level=5, credits=15)
    Module.objects.create(id='LAW4155', name='Access to Justice in Theory and Practice', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW4208', name='Visiting Students (Semester 1) Healthcare Law', school=law, level=4,
                          credits=20)
    Module.objects.create(id='LAW2056', name='European Union Law (Common Law)', school=law, level=2, credits=10)
    Module.objects.create(id='LAW2038', name='Land Law', school=law, level=2, credits=20)
    Module.objects.create(id='LAW4163', name='Comparative Family Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW2048', name='Law and Government (Common Law - FR)', school=law, level=2, credits=20)
    Module.objects.create(id='LAW5226', name='Artificial Intelligence and Law', school=law, level=5, credits=20)
    Module.objects.create(id='LAW4188', name='EU Institutions and Policies', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4185', name='Conemporary Issues in Land Law', school=law, level=4, credits=20)
    Module.objects.create(id='LAW4210', name='Visiting Students (1st Semester) Law and Political Economy', school=law,
                          level=4, credits=20)
    Module.objects.create(id='LAW5188', name='International Courts and Tribunals (EM)', school=law, level=5, credits=20)
    Module.objects.create(id='LAW2009', name='Labour Law', school=law, level=2, credits=20)

    # School of Mathematics and Statistics (193 modules)
    Module.objects.create(id='MATHS2001', name='Mathematics 2A: Multivariable Calculus', school=maths, level=2,
                          credits=10)
    Module.objects.create(id='MATHS2025', name='Mathematics 2T: Topics in Discrete Mathematics', school=maths, level=2,
                          credits=10)
    Module.objects.create(id='MATHS1016', name='Mathematics 1G: Introduction to Algebra, Geometry & Networks',
                          school=maths, level=1, credits=20)
    Module.objects.create(id='MATHS5083', name='AGQ: Gravity', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS5080', name='5E: Measure Theory and Probability', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS3016', name='Mathematics 3U: Complex Methods', school=maths, level=3, credits=10)
    Module.objects.create(id='MATHS5075', name='5E: Numerical Methods', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5076', name='5E: Partial Differential Equations', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5095', name='AGQ: Conformal Field Theory', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS5050', name='5M: Magnetohydrodynamics', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5089', name='Interfaces in Algebra and Quantum Fields A', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS1017', name='Mathematics 1', school=maths, level=1, credits=40)
    Module.objects.create(id='MATHS4119P', name='Study Abroad Work Based Learning (UG Maths)', school=maths, level=4,
                          credits=60)
    Module.objects.create(id='MATHS4103', name='4H: Functional Analysis', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS5088', name='Interfaces in Algebra and Geometry B', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS4109', name='4H: Numerical Methods', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS2027', name='MATHEMATICS 2P: GRAPHS AND NETWORKS', school=maths, level=2, credits=10)
    Module.objects.create(id='MATHS4061P', name='Mathematics Project 4', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS4111', name='4H: Topics in Algebra', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS5082', name='AGQ: Algebraic Geometry', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS5051P', name='5M: MSci Project', school=maths, level=5, credits=40)
    Module.objects.create(id='MATHS1015', name='Mathematics 1C: Introduction to Calculus', school=maths, level=1,
                          credits=20)
    Module.objects.create(id='MATHS5087', name='Interfaces in Algebra and Geometry A', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS5040', name='5M: Advanced Functional Analysis (SMSTC)', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS2033', name='Mathematics 2D: Mathematical Methods and Modelling', school=maths,
                          level=2, credits=10)
    Module.objects.create(id='MATHS4114P', name='Ambassador Scheme In Mathematics', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS1018', name='Mathematics 1 (Half Course)', school=maths, level=1, credits=20)
    Module.objects.create(id='MATHS5053', name='5M: Solitons', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5084', name='AGQ: Differential Topology', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS5068', name='5E: Fluid Mechanics', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS5045', name='5M: Commutative Algebra and Algebraic Geometry', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS4076', name='3H: Methods in Complex Analysis', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS5071', name='5E: Galois Theory', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS5091', name='Interfaces in Geometry and Quantum Fields A', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS5093', name='Algebraic Number Theory', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5043', name='5M: Applied Mathematical Methods (SMSTC)', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS5030P', name='Mathematics MSc Projects', school=maths, level=5, credits=60)
    Module.objects.create(id='MATHS5070', name='5E: Further Complex Analysis', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS4102', name='4H: Fluid Mechanics', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS4107', name='4H: Mathematical Physics', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS5039', name='5M: Advanced Differential Geometry and Topology', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS5092', name='Interfaces in Geometry and Quantum Fields B', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS4101', name='4H: Differential Geometry', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS4100', name='4H: Continuum Mechanics and Elasticity', school=maths, level=4,
                          credits=20)
    Module.objects.create(id='MATHS3021', name='Mathematics 3R: Algebra', school=maths, level=3, credits=10)
    Module.objects.create(id='MATHS5073', name='5E: Mathematical Physics', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS4120', name='4H: Theoretical Foundations of Machine Learning and Deep Learning',
                          school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS5049', name='5M: Lie Groups, Lie Algebras and their Representations', school=maths,
                          level=5, credits=20)
    Module.objects.create(id='MATHS4072', name='3H: Algebra', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS3019', name='Mathematics 3S: Mathematical Methods', school=maths, level=3,
                          credits=20)
    Module.objects.create(id='MATHS5047', name='5M: Fourier Analysis', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS2004', name='Mathematics 2B: Linear Algebra', school=maths, level=2, credits=10)
    Module.objects.create(id='MATHS3022', name='Mathematics 3T: Analysis', school=maths, level=3, credits=10)
    Module.objects.create(id='MATHS4108', name='4H: Number Theory', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS4117', name='4H: Mathematical Finance', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS4078', name='3H: Mechanics of Rigid and Deformable Bodies', school=maths, level=4,
                          credits=20)
    Module.objects.create(id='MATHS4116', name='4H: Measure Theory and Probability', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS5069', name='5E: Functional Analysis', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5044', name='5M: Biological and Physiological Fluid Dynamics', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS2032', name='Mathematics 2C: Introduction To Real Analysis', school=maths, level=2,
                          credits=10)
    Module.objects.create(id='MATHS5042', name='5M: Advanced Numerical Methods', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS1021', name='Foundations of Mathematics', school=maths, level=1, credits=20)
    Module.objects.create(id='MATHS4105', name='4H: Galois Theory', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS4079', name='3H: Writing and Presenting Mathematics', school=maths, level=4,
                          credits=10)
    Module.objects.create(id='MATHS5077', name='5E: Topics in Algebra', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS2035', name='Mathematics 2F: Groups, Transformations and Symmetries', school=maths,
                          level=2, credits=10)
    Module.objects.create(id='MATHS5066', name='5E: Continuum Mechanics and Elasticity', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS4073', name='3H: Analysis of Differentiation and Integration', school=maths, level=4,
                          credits=10)
    Module.objects.create(id='MATHS3017', name='Mathematics 3V: Dynamical Systems', school=maths, level=3, credits=10)
    Module.objects.create(id='MATHS4106', name='4H: Mathematical Biology', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS2034', name='Mathematics 2E: Mechanics', school=maths, level=2, credits=10)
    Module.objects.create(id='MATHS5085', name='AGQ: Algebraic Topology', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS5065', name='5E: Algebraic and Geometric Topology', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS5094', name='AGQ: Representation Theory', school=maths, level=5, credits=15)
    Module.objects.create(id='MATHS4039P', name='Statistics/Mathematics Msci Combined Project', school=maths, level=5,
                          credits=40)
    Module.objects.create(id='MATHS5048', name='5M: Further Topics in Group Theory', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS4112', name='4H: Algebraic and Geometric Topology', school=maths, level=4,
                          credits=20)
    Module.objects.create(id='MATHS5096', name='5E: Theoretical Foundations of Machine Learning and Deep Learning',
                          school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS4009P', name='Computing Science/Mathematics MSci Combined Project', school=maths,
                          level=5, credits=40)
    Module.objects.create(id='MATHS4074', name='3H: Dynamical Systems', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS4077', name='3H: Metric Space and Basic Topology', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS5046', name='5M: Elasticity', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5079', name='5M: Category Theory', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5074', name='5E: Number Theory', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS5067', name='5E: Differential Geometry', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5038', name='5M: Advanced algebraic and geometric topology', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS3018', name='Mathematics 3W: Writing and Presenting Mathematics', school=maths,
                          level=3, credits=10)
    Module.objects.create(id='MATHS4110', name='4H: Partial Differential Equations', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS4104', name='4H: Further Complex Analysis', school=maths, level=4, credits=10)
    Module.objects.create(id='MATHS5052', name='5M: Operator Algebras', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5072', name='5E: Mathematical Biology', school=maths, level=5, credits=20)
    Module.objects.create(id='MATHS5090', name='Interfaces in Algebra and Quantum Fields B', school=maths, level=5,
                          credits=15)
    Module.objects.create(id='MATHS4075', name='3H: Mathematical Methods', school=maths, level=4, credits=20)
    Module.objects.create(id='MATHS5081', name='5E: Mathematical Finance', school=maths, level=5, credits=10)
    Module.objects.create(id='MATHS3020', name='Mathematics 3Q: Mechanics', school=maths, level=3, credits=10)
    Module.objects.create(id='MATHS5041', name='5M: Advanced Methods in Differential Equations', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='MATHS5054', name='5M: Classical Field Theory', school=maths, level=5, credits=20)
    Module.objects.create(id='STATS2006', name='Statistics 2Y: Statistical Methods, Models and Computing 2',
                          school=maths, level=2, credits=10)
    Module.objects.create(id='STATS4070', name='Statistical Models (Bologna)', school=maths, level=4, credits=16)
    Module.objects.create(id='STATS5080', name='Data Management and Analytics using SAS (ODL)', school=maths, level=5,
                          credits=10)
    Module.objects.create(id='STATS5065', name='Research Practice (PhD with integrated study)', school=maths, level=5,
                          credits=20)
    Module.objects.create(id='STATS5013', name='Advanced Bayesian Methods (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5019', name='Generalised Linear Models (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5064P', name='Statistics Research Project 5 - Combined', school=maths, level=5,
                          credits=40)
    Module.objects.create(id='STATS5091P', name='Advanced Statistics Project and Dissertation', school=maths, level=5,
                          credits=60)
    Module.objects.create(id='STATS5095', name='Data Science Foundations (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5029P', name='Statistics Project and Dissertation', school=maths, level=5,
                          credits=60)
    Module.objects.create(id='STATS5063P', name='Statistics Research Project 5', school=maths, level=5, credits=80)
    Module.objects.create(id='STATS4052', name='Data Analysis', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS3023', name='Mathematics II (Bologna)', school=maths, level=3, credits=12)
    Module.objects.create(id='STATS4043', name='Generalised Linear Models', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4069', name='Multivariate Analysis (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS5011', name='Statistical Genetics (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS3011', name='Statistics 3A: Data Analysis', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS5056', name='Functional Data Analysis (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5074',
                          name='Data Mining and Machine Learning I: Supervised and Unsupervised Learning (ODL)',
                          school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5012', name='Spatial Statistics (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4037', name='Time Series', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5098', name='Advanced Predictive Models', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS3016', name='Statistics 3L: Linear Models', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS4046', name='Multivariate Methods', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS3024', name='Probability II (Bologna)', school=maths, level=3, credits=12)
    Module.objects.create(id='STATS3014', name='Statistics 3G: Generalised Linear Models', school=maths, level=3,
                          credits=10)
    Module.objects.create(id='STATS5076', name='Predictive Modelling (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5055P', name='Statistics Project WP (Level M)', school=maths, level=5, credits=20)
    Module.objects.create(id='STATS5022', name='Principles of Probability and Statistics (Level M)', school=maths,
                          level=5, credits=10)
    Module.objects.create(id='STATS5084', name='Uncertainty Assessment and Bayesian Computation (ODL)', school=maths,
                          level=5, credits=10)
    Module.objects.create(id='STATS5082', name='Data Programming in Python (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5025', name='Regression Models (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4040', name='Flexible Regression', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS3012', name='Statistics 3B: Biostatistics', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS3015', name='Statistics 3I: Inference', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS4066', name='Biostatistics (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS5054', name='Linear Mixed Models (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4015', name='Linear Models 3', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4072', name='Time Series (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS4024', name='Stochastic Processes', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5099', name='Data Mining and Machine Learning', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5094', name='Probability and Sampling Fundamentals (ODL)', school=maths, level=5,
                          credits=10)
    Module.objects.create(id='STATS5051', name='Advanced Data Analysis (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS3018', name='Statistics 3T: Time Series', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS4038', name='Advanced Bayesian Methods', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5103', name='Introduction to statistical programming in R and Python', school=maths,
                          level=5, credits=20)
    Module.objects.create(id='STATS4075', name='Spatial Statistics', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4009', name='Environmental and Ecological Statistics', school=maths, level=4,
                          credits=10)
    Module.objects.create(id='STATS5093P', name='Data Analytics Project (ODL)', school=maths, level=5, credits=60)
    Module.objects.create(id='STATS5052', name='Flexible Regression (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS1003', name='Statistics 1Z: Data Modelling in Action', school=maths, level=1,
                          credits=20)
    Module.objects.create(id='STATS4061P', name='Statistics Work Placement Year', school=maths, level=4, credits=120)
    Module.objects.create(id='STATS5014', name='Bayesian Statistics (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS1002', name='Statistics 1Y: Introduction to Statistics: Learning from Data',
                          school=maths, level=1, credits=20)
    Module.objects.create(id='STATS5030', name='Time Series (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS3017', name='Statistics 3R: R Programming', school=maths, level=3, credits=10)
    Module.objects.create(id='STATS5079', name='Data Analytics in Business and Industry (ODL)', school=maths, level=5,
                          credits=10)
    Module.objects.create(id='STATS5031', name='Environmental and Ecological Statistics (Level M)', school=maths,
                          level=5, credits=10)
    Module.objects.create(id='STATS4012', name='Inference 3', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5024', name='Probability (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5096', name='Sampling Fundamentals (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4067', name='Econometrics (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS4071', name='Survey Sampling (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS4045', name='Linear Mixed Models', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5026', name='Stochastic Processes (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4074', name='Statistical Genetics', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4006', name='Biostatistics', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5021', name='Multivariate Methods (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5075', name='Learning from Data - Data Science Foundations (ODL)', school=maths,
                          level=5, credits=10)
    Module.objects.create(id='STATS5028', name='Statistical Inference (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4048', name='Professional Skills', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4041', name='Bayesian Statistics', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5016', name='Big Data Analytics (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4044', name='R Programming', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5097', name='Statistical Computing (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS2005', name='Statistics 2X: Probability II', school=maths, level=2, credits=10)
    Module.objects.create(id='STATS5015', name='Biostatistics (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5073', name='Advanced Predictive Models (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4021P', name='Statistics Project 4 (Combined)', school=maths, level=4, credits=20)
    Module.objects.create(id='STATS4065', name='Analysis of Data (Bologna)', school=maths, level=4, credits=8)
    Module.objects.create(id='STATS5083', name='Large-Scale Computing for Data Analytics (ODL)', school=maths, level=5,
                          credits=10)
    Module.objects.create(id='STATS3013', name='Statsitics 3D: Design of Experiments', school=maths, level=3,
                          credits=10)
    Module.objects.create(id='STATS4008', name='Design of Experiments', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5081',
                          name='Data Mining and Machine Learning II: Big Data and Unstructured Data (ODL)',
                          school=maths, level=5, credits=10)
    Module.objects.create(id='STATS5085', name='Data Analysis Skills (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS4073', name='Functional Data Analysis', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS4039', name='Advanced Data Analysis', school=maths, level=4, credits=10)
    Module.objects.create(id='STATS5017', name='Design of Experiments (Level M)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS2003', name='Statistics 2S: Statistical Methods, Models and Computing 1',
                          school=maths, level=2, credits=10)
    Module.objects.create(id='STATS3002', name='Statistics For Biomedical Engineering 3', school=maths, level=3,
                          credits=10)
    Module.objects.create(id='STATS5078', name='R Programming (ODL)', school=maths, level=5, credits=10)
    Module.objects.create(id='STATS2002', name='Statistics 2R: Probability', school=maths, level=2, credits=10)
    Module.objects.create(id='STATS4068', name='Inference (Bologna)', school=maths, level=4, credits=12)
    Module.objects.create(id='STATS5090P', name='Statistics Project and Dissertation (with Placement)', school=maths,
                          level=5, credits=60)
    Module.objects.create(id='STATS4047', name='Principles of Probability and Statistics', school=maths, level=4,
                          credits=10)
    Module.objects.create(id='STATS4050P', name='Statistics Project', school=maths, level=4, credits=30)

    # School of Medicine Dentistry and Nursing (215 modules)
    Module.objects.create(id='BIOL5247', name='Introduction to Anatomy: Cells to Organs', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4231', name='Anatomy 3B with COIL', school=medicine, level=4, credits=60)
    Module.objects.create(id='BIOL4275', name='Anatomical Imaging Techniques 4C option', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5480', name='Clinically Applied Cardiovasular Anatomy and Physiology',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='BIOL5246', name='Structure and Function of the Human Body 2', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5353', name='Research Skills for Life Sciences', school=medicine, level=5, credits=10)
    Module.objects.create(id='BIOL2051', name='International Summer School Functional Anatomy', school=medicine,
                          level=2, credits=15)
    Module.objects.create(id='BIOL4270', name='Core Skills for Modern Anatomists 4X core', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4031', name='Clinical Applied Anatomy (Sem 2) 4D option', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4277', name='Forensic Osteology 4Y option', school=medicine, level=4, credits=20)
    Module.objects.create(id='BIOL4299', name='Diverse Anatomy 4Y option', school=medicine, level=4, credits=20)
    Module.objects.create(id='BIOL5248', name='Structure and Function of the Human Body 1', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4230', name='Anatomy 3A', school=medicine, level=4, credits=60)
    Module.objects.create(id='BIOL4117', name='Problems in Human Reproduction 4B option', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='DENT5096', name='Therapeutics and Diagnostics in Oral Sciences', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='DENT5094', name='Head & Neck Surgery and Oral Medicine', school=medicine, level=5,
                          credits=40)
    Module.objects.create(id='DENT5095', name='Oral Sciences Research Skills', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT1006', name='Biomolecular Science 1', school=medicine, level=1, credits=0)
    Module.objects.create(id='DENT5104', name='Tooth loss and strategies for tooth replacement', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='DENT1002', name='BDS1', school=medicine, level=1, credits=120)
    Module.objects.create(id='DENT3020', name='Dental Healthcare Systems', school=medicine, level=3, credits=20)
    Module.objects.create(id='DENT5083', name='Orofacial Infections', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5103', name='Advanced Endodontics', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5098', name='Biological Basis of Endodontic Disease', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='DENT5106P', name='Endodontology Project', school=medicine, level=5, credits=60)
    Module.objects.create(id='DENT5038', name='Temporomandibular Joint Diseases', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5107', name='Fundamentals of Oral Sciences', school=medicine, level=5, credits=10)
    Module.objects.create(id='DENT5074', name='Local Anaesthesia, General Anaesthesia and Sedation', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='DENT3002', name='BDS3', school=medicine, level=3, credits=120)
    Module.objects.create(id='DENT5004', name='BDS5', school=medicine, level=5, credits=120)
    Module.objects.create(id='DENT4022', name='Decontamination and Infection Control', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='DENT5099', name='Introduction to Oral Science Research Skills', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='DENT5070', name='Interdisciplinary Endodontics, Year 2', school=medicine, level=5,
                          credits=40)
    Module.objects.create(id='DENT5082', name='Oral Pathology', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5072',
                          name='Endodontics within the population and options for tooth replacement, Year 2',
                          school=medicine, level=5, credits=40)
    Module.objects.create(id='DENT3021', name='Statistics for Intercalating Dental Students', school=medicine, level=3,
                          credits=20)
    Module.objects.create(id='DENT5068', name='Biology of Endodontic Diseases', school=medicine, level=5, credits=40)
    Module.objects.create(id='DENT5075', name='Oral & Maxillofacial Surgery Research', school=medicine, level=5,
                          credits=100)
    Module.objects.create(id='DENT5073', name='Endodontics- Research', school=medicine, level=5, credits=100)
    Module.objects.create(id='DENT5077', name='Dentoalveolar Surgery', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5071', name='Management of endodontic problems and failure, Year 2', school=medicine,
                          level=5, credits=40)
    Module.objects.create(id='DENT4002', name='BDS4', school=medicine, level=4, credits=120)
    Module.objects.create(id='DENT5078', name='Dentofacial Deformities', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5069', name='Principles and practice of root canal treatment, Year 1',
                          school=medicine, level=5, credits=40)
    Module.objects.create(id='DENT2002', name='BDS2', school=medicine, level=2, credits=120)
    Module.objects.create(id='DENT5102', name='Endodontic Interfaces', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5100', name='Primary Root Canal Treatment', school=medicine, level=5, credits=20)
    Module.objects.create(id='DENT5101', name='Advanced Research Methods in Oral Sciences', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='DENT5076', name='Cleft and Craniofacial Deformities', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='DENT5062', name='Management of Partially Dentate Patients', school=medicine, level=5,
                          credits=40)
    Module.objects.create(id='DENT5080', name='Maxillofacial Trauma', school=medicine, level=5, credits=20)
    Module.objects.create(id='EDUC51030', name='Evidence-Based Teaching', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED2005', name='MBCHB2 Coursework', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED5331', name='SNP Assay Design and Validation', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5507', name='Paediatric Public and Social Health', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5330', name='Genetic Disease: from the Laboratory to the Clinic', school=medicine,
                          level=5, credits=60)
    Module.objects.create(id='MED3006', name='Student Selected Component 2 (MB3)', school=medicine, level=3, credits=0)
    Module.objects.create(id='MED5486P', name='Research Dissertation in Oral Sciences', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5329P', name='Medical Genetics Dissertation', school=medicine, level=5, credits=60)
    Module.objects.create(id='MED5388', name='Designing education research', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5365', name='Evidence-Based Research in Medicine', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED3008', name='MBChB Year 3 Written Examination', school=medicine, level=3, credits=0)
    Module.objects.create(id='MED5389', name='Evaluation of courses and curricula', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5562', name='Acute Kidney Injury', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5104', name='Clinical Nutrition Specialisation', school=medicine, level=5, credits=30)
    Module.objects.create(id='MED2003', name='Biochemistry', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED2009', name='Physology II', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED5128', name='Digestion, Absorption And Nutritional Metabolism', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='MED5398', name='Governance and ethics in education research', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED1008', name='Physiology I', school=medicine, level=1, credits=0)
    Module.objects.create(id='MED2004', name='MBChB 2nd Year', school=medicine, level=2, credits=120)
    Module.objects.create(id='MED4038',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Cardiovascular Studies',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5505', name='Paediatric Gastroenterology and Endocrinology', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED4012', name='Clinical Medicine', school=medicine, level=4, credits=120)
    Module.objects.create(id='MED4056', name='MBChB Year 4 Clinical Examination', school=medicine, level=4, credits=0)
    Module.objects.create(id='MED5656', name='Dietary And Nutritional Assessment with Diet Planning', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='MED5564', name='Clinical Governance and Quality Improvement', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED2006', name='MBCHB2 Written Paper (MB2)', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED5503', name='Cardiovascular and Respiratory Child Health', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5568', name='Nutrition in Critical Care', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED3004', name='MBChB Year 3', school=medicine, level=3, credits=120)
    Module.objects.create(id='MED5103P', name='Clinical Nutrition Research Dissertation', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED4058', name='BSc (Med Sci) Clinical Medicine - Emergency Medicine Specialist Course 4',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED4044',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Public Health',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5181P', name='Public Health Nutrition Research Dissertation', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5127', name='Dietary And Nutritional Assessment with Diet Planning', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='MED5332', name='Disease Screening in Populations', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED3005', name='MBChB Year 3 Clinical Examination', school=medicine, level=3, credits=0)
    Module.objects.create(id='MED5676P', name='MSc Health Services Management Project', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5649', name='Respiratory Failure', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5161', name='Obesity And Weight Management Specialisation', school=medicine, level=5,
                          credits=30)
    Module.objects.create(id='MED5160P', name='Obesity And Weight Management Research Dissertation', school=medicine,
                          level=5, credits=60)
    Module.objects.create(id='MED5407', name='Diagnostic Science in Action', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5504', name='Miscellaneous Paediatric Sub-Specialities', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED4057',
                          name='BSc(Med Sci) & BSc(Dent Sci) Clin.Med.Specialist Course Otolaryngology(ENT)/Head & Neck Surgery',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5171', name='Principles Of Pharmacology', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5650', name='Sepsis', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5395', name='Simulation in Health Professions Education', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED4046P', name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Research Project 4',
                          school=medicine, level=4, credits=40)
    Module.objects.create(id='MED5638',
                          name='Leading Care - Putting leadership into the health and social care context',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5484', name='Advanced Oral Science Research Skills', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED5392', name='Learning in Health Professions', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5129', name='Drug Disposition', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED4041',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Global health in primary care',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5495', name='Causes of multi-organ failure', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED4045',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Psychological Medicine',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5408', name='Medical and Research Ethics', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5506', name='Paediatric Neurology', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5390', name='Evidence in education research', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5397', name='Teaching in Health Professions', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5413', name='Translational Biomarkers', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5035', name='MBChB Year 5', school=medicine, level=5, credits=120)
    Module.objects.create(id='MED4054', name='Forensic Investigation', school=medicine, level=4, credits=30)
    Module.objects.create(id='MED4039', name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Core Course 4',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED3015', name='Critical Care Summer School', school=medicine, level=3, credits=10)
    Module.objects.create(id='MED5199', name='Sports And Exercise Nutrition Specialisation', school=medicine, level=5,
                          credits=30)
    Module.objects.create(id='MED3003', name='MBChB Year 3 Coursework', school=medicine, level=3, credits=0)
    Module.objects.create(id='MED2002', name='Behavioural Science In Med Pract', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED4005', name='Student Selected Component 4 (MB4)', school=medicine, level=4, credits=0)
    Module.objects.create(id='MED5034', name='MBChB Year 5 Written Examination', school=medicine, level=5, credits=0)
    Module.objects.create(id='MED1004', name='MBCHB1 Coursework', school=medicine, level=1, credits=0)
    Module.objects.create(id='MED4050', name='MBChB Year 4 Written Examination', school=medicine, level=4, credits=0)
    Module.objects.create(id='MED1017', name='Fundamental Skills in Medicine', school=medicine, level=1, credits=40)
    Module.objects.create(id='MED2010', name='Student Selected Component 1 (MB2)', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED5139', name='Food and Nutrient Requirements and Nutrition Through the Lifecycle',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5565', name='Gastrointestinal Emergencies', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED1016', name='Professional, Life, and Study Skills', school=medicine, level=1,
                          credits=25)
    Module.objects.create(id='MED5655', name='Nutrition Research Skills', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5592', name='Detecting Biomarkers for Precision Medicine Applications',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5485', name='Periodontitis and implications for systemic disease', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='MED5566', name='Leadership & Management in Critical Care', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5393', name='Managing the health professions curriculum', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5386', name='Assessment in Health Professions', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED4036',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Clinical Neuroscience',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5529', name='Introduction to Management and Leadership in Health Services',
                          school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5569', name='Research and Scientific Writing Skills', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5493P', name='Critical Care: Dissertation', school=medicine, level=5, credits=60)
    Module.objects.create(id='MED5180', name='Public Health and Eating Behaviour', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5561P', name='Critical Care, Leadership and Management dissertation', school=medicine,
                          level=5, credits=60)
    Module.objects.create(id='MED5488', name='Biomarkers for Precision Medicine (online)', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED5351', name='Evidence-based Research in Medicine', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED5428', name='Translational Research Approaches in Oral Sciences,', school=medicine,
                          level=5, credits=10)
    Module.objects.create(id='MED5165', name='Pharmaceutical Medicine', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5182', name='Public Health Nutrition Specialisation', school=medicine, level=5,
                          credits=30)
    Module.objects.create(id='MED1005', name='MBCHB1 Written Paper (MB1)', school=medicine, level=1, credits=0)
    Module.objects.create(id='MED5563P', name='Clinical Critical Care Dissertation', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED2008', name='Pharmacology', school=medicine, level=2, credits=0)
    Module.objects.create(id='MED5328', name='Case Investigations in Medical Genetics', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='MED5573P', name='Critical Care and Leadership Dissertation', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5394P', name='Research Dissertation in Health Professions Education', school=medicine,
                          level=5, credits=60)
    Module.objects.create(id='MED1006', name='Medical Ind Learning Exam (MB)', school=medicine, level=1, credits=0)
    Module.objects.create(id='MED4002', name='Clinical Incoming Elective (S2)', school=medicine, level=5, credits=0)
    Module.objects.create(id='MED5399P', name='Dissertation in Health Professions Education', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5681', name='Medications in Critical Care', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED4049',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Women and Children\'s Health',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5406', name='Quality Improvement in Health Care', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5387', name='Curriculum approaches and design', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5651P', name='Outreach and Engagement Project', school=medicine, level=5, credits=60)
    Module.objects.create(id='MED5492', name='Evidence-Based Quality Improvement', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED5391', name='Leadership in health professions education', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5567', name='Neurocritical Care', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED4042',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Inflammation Medicine',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5033', name='MBChB Year 5 Clinical Examination', school=medicine, level=5, credits=0)
    Module.objects.create(id='MED1003', name='MBChB 1st Year', school=medicine, level=1, credits=120)
    Module.objects.create(id='MED5198P', name='Sports And Exercise Nutrition Research Dissertation', school=medicine,
                          level=5, credits=60)
    Module.objects.create(id='MED4035',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clin. Med. Specialist Course 4: Critical Care &Perioperative Medicine',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED4004', name='MBChB Year 4', school=medicine, level=4, credits=120)
    Module.objects.create(id='MED4037',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Bench to Bedside Oncology',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED4047',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Sport & Exercise Medicine',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED4048',
                          name='BSc (Med Sci) & BSC (Dent Sci) Clinical Medicine Specialist Course 4: Statistics',
                          school=medicine, level=4, credits=20)
    Module.objects.create(id='MED5572', name='Trauma and Multi-Organ Failure', school=medicine, level=5, credits=10)
    Module.objects.create(id='MED5396', name='Teaching and assessment of clinical skills', school=medicine, level=5,
                          credits=10)
    Module.objects.create(id='MED5425', name='Clinical Genomics', school=medicine, level=5, credits=20)
    Module.objects.create(id='MED4043',
                          name='BSc (Med Sci) & BSc (Dent Sci) Clinical Medicine Specialist Course 4: Molecular Pathology',
                          school=medicine, level=4, credits=30)
    Module.objects.create(id='MED5530P', name='MSc Health Services Management Project', school=medicine, level=5,
                          credits=60)
    Module.objects.create(id='MED5671', name='Fundamentals of Management & Leadership in Healthcare Services',
                          school=medicine, level=5, credits=10)
    Module.objects.create(id='NURSING5063', name='Applying Research Approaches in Health Care', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='NURSING3064', name='Principles of Human Disease & Pharmacotherapy 3 (PHDP)',
                          school=medicine, level=3, credits=20)
    Module.objects.create(id='NURSING5045P', name='Managing Complex Lymphoedema', school=medicine, level=5, credits=40)
    Module.objects.create(id='NURSING5051', name='Leadership in Contemporary Health Care', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='NURSING3062', name='Final Practice Learning Experience 3', school=medicine, level=3,
                          credits=45)
    Module.objects.create(id='NURSING4032P', name='Dissertation 4H', school=medicine, level=4, credits=60)
    Module.objects.create(id='NURSING1012', name='Foundations for Nursing and Health 1', school=medicine, level=1,
                          credits=30)
    Module.objects.create(id='NURSING3028',
                          name='Principles Of Reconstructive Plastic Surgery And Burn Injury Care (Graduate Certificate)',
                          school=medicine, level=3, credits=20)
    Module.objects.create(id='NURSING3002', name='Burn Injury: Adults And Paediatrics (Graduate Certificate)',
                          school=medicine, level=3, credits=20)
    Module.objects.create(id='NURSING2014', name='Developing Knowledge for Nursing and Health 2', school=medicine,
                          level=2, credits=30)
    Module.objects.create(id='NURSING3041P', name='Lymphoedema: application of core skills & knowledge',
                          school=medicine, level=3, credits=20)
    Module.objects.create(id='NURSING4034', name='Policy in Health and Social Care', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='NURSING5012', name='Education For Professional Practice', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='NURSING3063', name='Practice Learning Experience 3', school=medicine, level=3, credits=50)
    Module.objects.create(id='NURSING5064', name='Global Health Challenges', school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING2013', name='Biomedical Life Sciences for Nursing 2', school=medicine, level=2,
                          credits=20)
    Module.objects.create(id='NURSING3065', name='Advancing Knowledge for Contemporary Nursing Practice 3 (AKCNP)',
                          school=medicine, level=3, credits=40)
    Module.objects.create(id='NURSING5027',
                          name='Professional Practice in Spiritual and Religious Care in Health and Social Care',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING3061', name='Appraising Research for Evidence Informed Practice 3 (AREIP)',
                          school=medicine, level=3, credits=10)
    Module.objects.create(id='NURSING5065P', name='Independent Project', school=medicine, level=5, credits=60)
    Module.objects.create(id='NURSING4021P', name='Managing Complex Lymphoedema', school=medicine, level=4, credits=40)
    Module.objects.create(id='NURSING5062', name='Informing Practice through the Evidence Base', school=medicine,
                          level=5, credits=20)
    Module.objects.create(id='NURSING3011', name='Clinical Consolidation Practice 3', school=medicine, level=3,
                          credits=45)
    Module.objects.create(id='NURSING2016', name='Research for Evidence Informed Practice 2', school=medicine, level=2,
                          credits=10)
    Module.objects.create(id='NURSING3040P', name='Lymphoedema: core skills & knowledge', school=medicine, level=3,
                          credits=40)
    Module.objects.create(id='NURSING5047', name='Acute and Critical Care', school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING1013', name='Practice Learning Experience 1', school=medicine, level=1, credits=60)
    Module.objects.create(id='NURSING3027',
                          name='Plastic And Reconstructive Surgery: Adults And Paediatrics (Graduate Certificate)',
                          school=medicine, level=3, credits=20)
    Module.objects.create(id='NURSING4033', name='Impact of The Environment on Global Health', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='NURSING3060', name='Advancing Clinical Skills 3 (ACS)', school=medicine, level=3,
                          credits=10)
    Module.objects.create(id='NURSING5058', name='Advanced Health and Social Care Practice (Distance Learning)',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING5049', name='Advanced Healthcare Practice', school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING5046P', name='Lymphoedema Advanced Practice', school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING2015', name='Practice Learning Experience 2', school=medicine, level=2, credits=75)
    Module.objects.create(id='NURSING4022P', name='Lymphoedema Specialist Practice', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='NURSING5066', name='Research Approaches in Health Care', school=medicine, level=5,
                          credits=20)
    Module.objects.create(id='NURSING4031', name='Concepts of Professionalism in Nursing', school=medicine, level=4,
                          credits=20)
    Module.objects.create(id='NURSING5029', name='Providing Spiritual and Religious Care in Health and Social Care',
                          school=medicine, level=5, credits=20)
    Module.objects.create(id='NURSING1011', name='Biomedical Life and Social Sciences 1', school=medicine, level=1,
                          credits=30)

    # School of Modern Languages and Cultures (460 modules)
    Module.objects.create(id='COMPLIT4026', name='Magical Narratives: Imagination, Fantasy and the Creation of Worlds',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4029', name='Holocaust Literature and Film', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4039', name='Migration and Displacement on Screen', school=language, level=4,
                          credits=20)
    Module.objects.create(id='COMPLIT4017', name='The Brothers Grimm and the European Fairy Tale', school=language,
                          level=4, credits=20)
    Module.objects.create(id='COMPLIT2012',
                          name='Comparative Literature 2B - Introduction to Literary Criticism and Theory',
                          school=language, level=2, credits=20)
    Module.objects.create(id='COMPLIT5035', name='Postcolonial Literature, Theory and Visual Culture', school=language,
                          level=5, credits=20)
    Module.objects.create(id='COMPLIT5036', name='Reading Workshop in Comparative Literature', school=language, level=5,
                          credits=20)
    Module.objects.create(id='COMPLIT4015', name='Writing Subjects', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT5037', name='Global Narratives of Crisis', school=language, level=5, credits=20)
    Module.objects.create(id='COMPLIT4036P', name='Applied Dissertation with Placement in Comparative Literature',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4044', name='Collecting, Archiving, Exhibiting: Museums and Storytelling',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT2002', name='Comparative Literature 2C - Frontiers (Exploring Identity)',
                          school=language, level=2, credits=20)
    Module.objects.create(id='COMPLIT4040', name='Writing Persia', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4033',
                          name='Transcultural Connections: \'Classic\' Texts and their Adaptations across Cultures',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4034', name='Bestsellers in the Pre-Industrial Age', school=language, level=4,
                          credits=20)
    Module.objects.create(id='COMPLIT1002', name='Comparative Literature 1B - Heroes (Heroic Women)', school=language,
                          level=1, credits=20)
    Module.objects.create(id='COMPLIT5038', name='Cervantes, Metafiction and Hollywood', school=language, level=5,
                          credits=20)
    Module.objects.create(id='COMPLIT5031', name='Comparative Literature in Practice', school=language, level=5,
                          credits=20)
    Module.objects.create(id='COMPLIT4002', name='Intercultural Readings', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT5039', name='Collections and Storytelling', school=language, level=5, credits=20)
    Module.objects.create(id='COMPLIT4046', name='Literary Prizes and Cultural Production', school=language, level=4,
                          credits=20)
    Module.objects.create(id='COMPLIT4028', name='Classic European Cinema East and West', school=language, level=4,
                          credits=20)
    Module.objects.create(id='COMPLIT4042', name='Dreaming about Science with Cervantes and Kepler', school=language,
                          level=4, credits=20)
    Module.objects.create(id='COMPLIT4037', name='Cervantes in Hollywood', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4031', name='Global Novels: how translated fiction becomes World Literature',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4027',
                          name='Narrating the City: Representation of Urban Space in Literature and Film',
                          school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT4043', name='Vampires and Vampirism: Intercultural Perspectives', school=language,
                          level=4, credits=20)
    Module.objects.create(id='COMPLIT4003', name='Theories Of Reading', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT2001', name='Comparative Literature 2A - Frontiers (Crossing Borders)',
                          school=language, level=2, credits=20)
    Module.objects.create(id='COMPLIT4032', name='Myths and Modern Imagination', school=language, level=4, credits=20)
    Module.objects.create(id='COMPLIT5030', name='An Introduction to Comparative Literature', school=language, level=5,
                          credits=20)
    Module.objects.create(id='COMPLIT4041', name='What is a human? Humans, Animals, Machines', school=language, level=4,
                          credits=20)
    Module.objects.create(id='COMPLIT1011', name='Comparative Literature 1C: Heroism across Time and Cultures',
                          school=language, level=1, credits=20)
    Module.objects.create(id='COMPLIT4030', name='The Everyday in Film, Photography and Literature', school=language,
                          level=4, credits=20)
    Module.objects.create(id='COMPLIT5032P', name='MLitt Comparative Literature Dissertation', school=language, level=5,
                          credits=60)
    Module.objects.create(id='COMPLIT4025', name='Postcolonial Literature, Thought and Visual Culture', school=language,
                          level=4, credits=20)
    Module.objects.create(id='COMPLIT1001', name='Comparative Literature 1A - Heroes (Heroic Men)', school=language,
                          level=1, credits=20)
    Module.objects.create(id='COMPLIT4001P', name='Comparative Literature Dissertation', school=language, level=4,
                          credits=20)
    Module.objects.create(id='CZECH1001', name='Czech 1', school=language, level=1, credits=40)
    Module.objects.create(id='CZECH2002', name='Czech 2 (Early Exit)', school=language, level=2, credits=20)
    Module.objects.create(id='CZECH5016', name='PG BEGINNER CZECH (EARLY EXIT)', school=language, level=5, credits=20)
    Module.objects.create(id='CZECH2001', name='Czech 2', school=language, level=2, credits=40)
    Module.objects.create(id='CZECH4008', name='Subsidiary Czech Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='CZECH4001', name='Czech Cinema', school=language, level=4, credits=20)
    Module.objects.create(id='CZECH4003', name='Czech, Polish And Russian Women\'s Writing In English Translation',
                          school=language, level=4, credits=20)
    Module.objects.create(id='CZECH1002', name='Czech 1 (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='CZECH5020', name='Czech Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='CZECH5022', name='English into Czech Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='CZECH5017', name='PG BEGINNER CZECH', school=language, level=5, credits=40)
    Module.objects.create(id='CZECH5019', name='Czech into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='CZECH4038', name='Advanced Subsidiary Czech', school=language, level=4, credits=20)
    Module.objects.create(id='CZECH4009', name='Subsidiary Czech Language (Intermediate)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='CZECH5021', name='English into Czech Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='CZECH3002', name='Czech Language 3', school=language, level=3, credits=30)
    Module.objects.create(id='CZECH4030',
                          name='Milan Kundera, a French writer? A study in intercultural literary discourse',
                          school=language, level=4, credits=20)
    Module.objects.create(id='CZECH5018', name='PG Intermediate Czech', school=language, level=5, credits=40)
    Module.objects.create(id='EAS1001',
                          name='EAP 1 - Academic English and Skills for International Undergraduates (Semester 1)',
                          school=language, level=1, credits=20)
    Module.objects.create(id='EAS3001', name='Speaking Arts and Humanities', school=language, level=3, credits=30)
    Module.objects.create(id='EAS5002', name='Advancing English for Business Students (Speaking)', school=language,
                          level=5, credits=10)
    Module.objects.create(id='EAS1004',
                          name='EAP 2 - Advanced Academic English and Skills for International Undergraduates - Semester 2',
                          school=language, level=1, credits=20)
    Module.objects.create(id='EAS5008', name='Advancing English for Social and Political Sciences', school=language,
                          level=5, credits=10)
    Module.objects.create(id='EAS5009', name='Practical Skills for Teaching English for Academic Purposes',
                          school=language, level=5, credits=20)
    Module.objects.create(id='EAS5007', name='Advancing English for Applied Linguistics', school=language, level=5,
                          credits=10)
    Module.objects.create(id='EAS5005', name='Teaching English for Academic Purposes', school=language, level=5,
                          credits=20)
    Module.objects.create(id='EAS4001', name='Teaching English to Speakers of Other Languages (Hons)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='EAS1002',
                          name='EAP 1 - Academic English and Skills for International Undergraduates (Semester 2)',
                          school=language, level=1, credits=20)
    Module.objects.create(id='EAS5003', name='Advancing English for Business Students - Writing', school=language,
                          level=5, credits=10)
    Module.objects.create(id='EAS3002', name='Writing Arts and Humanities', school=language, level=3, credits=30)
    Module.objects.create(id='EAS1005', name='EAP1 for Students in MVLS', school=language, level=1, credits=20)
    Module.objects.create(id='EAS5010', name='Research and Scholarship in English for Academic Purposes',
                          school=language, level=5, credits=20)
    Module.objects.create(id='EAS5004E', name='Teaching English for Academic Purposes Online', school=language, level=5,
                          credits=20)
    Module.objects.create(id='EAS1006', name='EAP 2 for Students in MVLS', school=language, level=1, credits=20)
    Module.objects.create(id='EAS1003',
                          name='EAP 2 - Advanced Academic English and Skills for International Undergraduates - Semester 1',
                          school=language, level=1, credits=20)
    Module.objects.create(id='FRENCH4108', name='Modern French Poetry and Poetics', school=language, level=4,
                          credits=20)
    Module.objects.create(id='FRENCH4100', name='France 1940-44: The Occupation and its Legacies', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH2013', name='FRENCH YEAR ABROAD STUDY', school=language, level=2, credits=120)
    Module.objects.create(id='FRENCH4079', name='French Song and Society: From Troubadours to Rap', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH4105', name='Writing the Visual: The Art of the Text', school=language, level=4,
                          credits=20)
    Module.objects.create(id='FRENCH4012', name='Modern French Thought', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH4082', name='French Honours Spoken Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='FRENCH5024', name='French Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='FRENCH4095', name='Consumption, Culture and Society in Modern France', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH4084', name='French Honours Spoken Language (year 1 exit)', school=language,
                          level=4, credits=10)
    Module.objects.create(id='FRENCH4109', name='Subsidiary French Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='FRENCH4098', name='Zombies and Terror: Representations of Haitian Dictatorship',
                          school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH5035', name='PG BEGINNER FRENCH', school=language, level=5, credits=40)
    Module.objects.create(id='FRENCH2012', name='FRENCH YEAR ABROAD ASSISTANTSHIP', school=language, level=2,
                          credits=120)
    Module.objects.create(id='FRENCH4090', name='Accountancy with Langs (French)', school=language, level=4, credits=30)
    Module.objects.create(id='FRENCH2011', name='French Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='FRENCH5038', name='English into French Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='FRENCH5039', name='English into French Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='FRENCH1010', name='French 1 Beginners (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='FRENCH4010', name='Language And Socio-Cultural Identity In Modern France',
                          school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH5033', name='PG Advanced French', school=language, level=5, credits=30)
    Module.objects.create(id='FRENCH4083', name='French Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='FRENCH4022', name='The European Emblem', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH5023', name='French to English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='FRENCH1004', name='French Culture 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='FRENCH1006', name='French Language 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='FRENCH4004', name='Court And Conflict In Medieval French Literature', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH3002', name='French 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='FRENCH4110P', name='Applied Dissertation with Placement in French', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH4006', name='French Cinema', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH2014', name='FRENCH YEAR ABROAD WORK PLACEMENT', school=language, level=2,
                          credits=120)
    Module.objects.create(id='FRENCH4085', name='French Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='FRENCH4104', name='Food and Culture in France', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH4007P', name='French Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH4015', name='Satire And Subversion In Medieval French Literature', school=language,
                          level=4, credits=20)
    Module.objects.create(id='FRENCH4089', name='French Honours Language for Law Students', school=language, level=4,
                          credits=60)
    Module.objects.create(id='FRENCH4086', name='French Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='FRENCH3001', name='French 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='FRENCH4027', name='Travel Writing', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH4002', name='Bande Dessinee', school=language, level=4, credits=20)
    Module.objects.create(id='FRENCH4097', name='The Twenty-First Century Novel in French', school=language, level=4,
                          credits=20)
    Module.objects.create(id='FRENCH5034', name='PG BEGINNER FRENCH (EARLY EXIT)', school=language, level=5, credits=20)
    Module.objects.create(id='FRENCH1005', name='French Language 1 (Beginners)', school=language, level=1, credits=40)
    Module.objects.create(id='FRENCH5036', name='PG Intermediate French', school=language, level=5, credits=20)
    Module.objects.create(id='FRENCH5037', name='PG Non-Beginner Elementary French', school=language, level=5,
                          credits=20)
    Module.objects.create(id='FRENCH2010', name='French Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='FRENCH4087', name='French Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='GERMAN5005', name='German Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='GERMAN2011', name='German Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='GERMAN4046', name='German Honours Spoken Language (year 1 exit)', school=language,
                          level=4, credits=10)
    Module.objects.create(id='GERMAN1003', name='German Language 1 (Beginners)', school=language, level=1, credits=40)
    Module.objects.create(id='GERMAN5014', name='English into German Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN4055', name='German Professional Communication', school=language, level=4,
                          credits=20)
    Module.objects.create(id='GERMAN4002P', name='German Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN5010', name='PG BEGINNER GERMAN', school=language, level=5, credits=40)
    Module.objects.create(id='GERMAN4051', name='Accountancy with Langs (German)', school=language, level=4, credits=30)
    Module.objects.create(id='GERMAN5001',
                          name='European Narratives of Illness. Medical and Literary Case Histories 1783-1933',
                          school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN5013', name='English into German Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN2012', name='GERMAN YEAR ABROAD ASSISTANTSHIP', school=language, level=2,
                          credits=120)
    Module.objects.create(id='GERMAN4054', name='European Political Thought: A View from Germany', school=language,
                          level=4, credits=20)
    Module.objects.create(id='GERMAN4048', name='German Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='GERMAN4057', name='Recent Women Writers in German', school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN4063', name='German Film: Expressionist and New German Cinema', school=language,
                          level=4, credits=20)
    Module.objects.create(id='GERMAN4049', name='German Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='GERMAN5011', name='PG Intermediate German', school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN1010', name='German 1 Beginners (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='GERMAN4003', name='German Junior Language Project', school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN3002', name='German 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='GERMAN4009', name='Re-Evaluations: German Literature And Thought 1880-1935',
                          school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN4004', name='German Liaison Interpreting', school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN5004', name='German into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN1002', name='German Culture 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='GERMAN4064',
                          name='Die Wende der Anderen [The Reunification of Others]-East German Perspectives on 1989/90(and beyond)',
                          school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN2013', name='GERMAN YEAR ABROAD STUDY', school=language, level=2, credits=120)
    Module.objects.create(id='GERMAN4050', name='German Honours Language for Law Students', school=language, level=4,
                          credits=60)
    Module.objects.create(id='GERMAN5008', name='PG Advanced German', school=language, level=5, credits=30)
    Module.objects.create(id='GERMAN5009', name='PG BEGINNER GERMAN (EARLY EXIT)', school=language, level=5, credits=20)
    Module.objects.create(id='GERMAN4062P', name='Applied Dissertation with Placement in German', school=language,
                          level=4, credits=20)
    Module.objects.create(id='GERMAN4044', name='German Honours Spoken Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='GERMAN5012', name='PG Non-Beginner Elementary German', school=language, level=5,
                          credits=20)
    Module.objects.create(id='GERMAN2010', name='German Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='GERMAN3001', name='German 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='GERMAN4061', name='Subsidiary German Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='GERMAN2015', name='GERMAN YEAR ABROAD WORK PLACEMENT', school=language, level=2,
                          credits=120)
    Module.objects.create(id='GERMAN4060', name='Brecht', school=language, level=4, credits=20)
    Module.objects.create(id='GERMAN1004', name='German Language 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='GERMAN4047', name='German Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='GERMAN4045', name='German Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4087', name='Spanish Spoken Language (Junior)', school=language, level=4, credits=0)
    Module.objects.create(id='HISP4113', name='Catalan Society', school=language, level=4, credits=20)
    Module.objects.create(id='HISP4019', name='Interpreting Skills In Spanish', school=language, level=4, credits=20)
    Module.objects.create(id='HISP4126', name='Humour and Horror in Early Modern Spain', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4121', name='Queer Subjectivities in Latin America', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4030', name='Women\'s Expressions Of Selfhood Across South America', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP1008', name='Spanish Language 1 (Beginners)', school=language, level=1, credits=40)
    Module.objects.create(id='HISP4107', name='Realism and Magic Realism in Latin America', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP1007', name='Spanish Culture 1 (Non-Beginners)', school=language, level=1, credits=20)
    Module.objects.create(id='HISP2011', name='Spanish Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='HISP4131', name='Thinking Revolution in Nineteenth-Century Spain', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP4079', name='Golden Age Iberia in Glasgow', school=language, level=4, credits=20)
    Module.objects.create(id='HISP1012', name='Spanish 1 Beginners (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='HISP4117P', name='Spanish Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='HISP4088', name='Spanish Honours Spoken Language (year 1 exit)', school=language, level=4,
                          credits=10)
    Module.objects.create(id='HISP4115', name='Medievalism and Orientalism in Hispanic America', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP4123', name='Subsidiary Spanish Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP5037', name='English into Spanish Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='HISP4125P', name='Applied Dissertation with Placement in Spanish', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP4105',
                          name='Representing Disappearance: Cultural Responses to the Argentine Dictatorship (1976-83)',
                          school=language, level=4, credits=20)
    Module.objects.create(id='HISP5014', name='Spanish Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='HISP5036', name='English into Spanish Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='HISP4127', name='Don Quixote against Reality', school=language, level=4, credits=20)
    Module.objects.create(id='HISP4114', name='Foundational Fictions: The Nineteenth Century', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4091', name='Spanish Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP4026', name='Power And Marginality In Latin America', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP5026', name='PG Intermediate Catalan', school=language, level=5, credits=20)
    Module.objects.create(id='HISP4118', name='Winter is Coming: The Middle Ages in the Modern World', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP2012', name='SPANISH YEAR ABROAD ASSISTANTSHIP', school=language, level=2,
                          credits=120)
    Module.objects.create(id='HISP5024', name='PG BEGINNER SPANISH (EARLY EXIT)', school=language, level=5, credits=20)
    Module.objects.create(id='HISP4093', name='Spanish Honours Language for Law Students', school=language, level=4,
                          credits=60)
    Module.objects.create(id='HISP4104', name='Cultural and Social Change in Contemporary Spain', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP4015P', name='Hispanic Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='HISP4023', name='Nonfiction Literature In Latin America', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP5020', name='PG Advanced Spanish', school=language, level=5, credits=30)
    Module.objects.create(id='HISP5021', name='PG BEGINNERS CATALAN', school=language, level=5, credits=20)
    Module.objects.create(id='HISP4095', name='Spanish Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP3003', name='Spanish 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='HISP4106', name='Images of Women in 20th century Hispanic Cultures', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP1009', name='Spanish Language 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='HISP4109', name='Representations of the Spanish Civil War', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4122', name='Sociolinguistics of the Spanish-speaking World', school=language,
                          level=4, credits=20)
    Module.objects.create(id='HISP5028', name='PG Intermediate Spanish', school=language, level=5, credits=20)
    Module.objects.create(id='HISP4132', name='Fashions Past: The Culture of Clothing in Nineteenth-Century Spain',
                          school=language, level=4, credits=20)
    Module.objects.create(id='HISP5032', name='English into Catalan Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='HISP4005', name='Catalan 1', school=language, level=4, credits=20)
    Module.objects.create(id='HISP2010', name='Spanish Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='HISP4133',
                          name='Literary New Worlds: Transatlantic Encounter and Exchange in the Hispanic Colonial Context',
                          school=language, level=4, credits=20)
    Module.objects.create(id='HISP4021', name='Mexico: Past, Present And Future', school=language, level=4, credits=20)
    Module.objects.create(id='HISP3002', name='Spanish 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='HISP5029', name='PG Non-Beginner Elementary Spanish', school=language, level=5,
                          credits=20)
    Module.objects.create(id='HISP4130', name='Languages and Community Engagement', school=language, level=4,
                          credits=20)
    Module.objects.create(id='HISP4089', name='Spanish Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='HISP5025', name='PG BEGINNER SPANISH', school=language, level=5, credits=40)
    Module.objects.create(id='HISP4096', name='Accountancy with Langs (Spanish)', school=language, level=4, credits=30)
    Module.objects.create(id='HISP4006', name='Catalan 2', school=language, level=4, credits=20)
    Module.objects.create(id='HISP2013', name='SPANISH YEAR ABROAD STUDY', school=language, level=2, credits=120)
    Module.objects.create(id='HISP4129', name='Tourism and Culture in Spain from the 1950s to the Present Day',
                          school=language, level=4, credits=20)
    Module.objects.create(id='HISP4090', name='Spanish Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='HISP5013', name='Spanish to English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='HISP4108', name='Contemporary Spanish Cinema', school=language, level=4, credits=20)
    Module.objects.create(id='HISP2023', name='SPANISH YEAR ABROAD WORK PLACEMENT', school=language, level=2,
                          credits=120)
    Module.objects.create(id='HISP5033', name='English into Catalan Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='HISP5031', name='Catalan Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='HISP5030', name='Catalan to English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='ITALIAN4049', name='Italian Honours Language for Law Students', school=language, level=4,
                          credits=60)
    Module.objects.create(id='ITALIAN3001', name='Italian 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='ITALIAN5004', name='Italian Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='ITALIAN4010', name='Modern Italian Poetry', school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN5008', name='PG BEGINNER ITALIAN (EARLY EXIT)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='ITALIAN5010', name='PG Intermediate Italian', school=language, level=5, credits=20)
    Module.objects.create(id='ITALIAN2012', name='ITALIAN YEAR ABROAD ASSISTANTSHIP', school=language, level=2,
                          credits=120)
    Module.objects.create(id='ITALIAN5011', name='PG Non-Beginner Elementary Italian', school=language, level=5,
                          credits=20)
    Module.objects.create(id='ITALIAN2014', name='ITALIAN YEAR ABROAD WORK PLACEMENT', school=language, level=2,
                          credits=120)
    Module.objects.create(id='ITALIAN4002P', name='Italian Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4057', name='Honour and Shame in Italian Culture: Emotions and Performance',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN5009', name='PG BEGINNER ITALIAN', school=language, level=5, credits=40)
    Module.objects.create(id='ITALIAN5013', name='English into Italian Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='ITALIAN4064', name='The Poetics of Self-Translation in Italian Literature',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4046', name='Italian Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='ITALIAN4065', name='Ecological Dialogues in Italian Literature and Cinema',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4044', name='Italian Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='ITALIAN4004', name='Italian Modernism: Svevo And Pirandello', school=language, level=4,
                          credits=20)
    Module.objects.create(id='ITALIAN4005', name='Italian Resistance To Fascism 1943-45', school=language, level=4,
                          credits=20)
    Module.objects.create(id='ITALIAN4043', name='Italian Honours Spoken Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='ITALIAN5003', name='Italian into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='ITALIAN4045', name='Italian Honours Spoken Language (year 1 exit)', school=language,
                          level=4, credits=10)
    Module.objects.create(id='ITALIAN2013', name='ITALIAN YEAR ABROAD STUDY', school=language, level=2, credits=120)
    Module.objects.create(id='ITALIAN1005', name='Italian Language 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='ITALIAN4061',
                          name='Feminist Encounters in Italy: Sexuality and the Body in 20th Century Women\'s Cultural Production',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4006', name='Italian Senior Honours Language Project: Contemporary Society',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN2010', name='Italian Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='ITALIAN1004', name='Italian Language 1 (Beginners)', school=language, level=1, credits=40)
    Module.objects.create(id='ITALIAN4050', name='Accountancy with Langs (Italian)', school=language, level=4,
                          credits=30)
    Module.objects.create(id='ITALIAN4062',
                          name='Multilingualism in Contemporary Italian Fiction and screen Adaptations',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN5012', name='English into Italian Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='ITALIAN4059', name='Subsidiary Italian Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='ITALIAN4047', name='Italian Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='ITALIAN1003', name='Italian Culture 1 (Non-Beginners)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='ITALIAN5007', name='PG Advanced Italian', school=language, level=5, credits=30)
    Module.objects.create(id='ITALIAN2011', name='Italian Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='ITALIAN4056',
                          name='Italian Cinema: Migration, Displacement and Exile in Films and Documentaries',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4003', name='Italian Junior Honours Language Project: Region And Culture',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN3002', name='Italian 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='ITALIAN1009', name='Italian 1 Beginners (Early Exit)', school=language, level=1,
                          credits=20)
    Module.objects.create(id='ITALIAN4048', name='Italian Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='ITALIAN4063',
                          name='Reading Italian Mountains: Naturecultural Landscapes Beyond the Postcard',
                          school=language, level=4, credits=20)
    Module.objects.create(id='ITALIAN4060P', name='Applied Dissertation with Placement in Italian', school=language,
                          level=4, credits=20)
    Module.objects.create(id='ITALIAN4012', name='Women In Modern Italy', school=language, level=4, credits=20)
    Module.objects.create(id='LIBARTS4002P', name='Liberal Arts Dissertation', school=language, level=4, credits=40)
    Module.objects.create(id='LIBARTS1001',
                          name='Liberal Arts 1A: Introduction to Public Humanities: Arts-Based Inquiry for Social Justice',
                          school=language, level=1, credits=20)
    Module.objects.create(id='LIBARTS2001',
                          name='Liberal Arts 2A: Beyond Borders and Boundaries: Exploring Roots and Routes in Human Mobilities',
                          school=language, level=2, credits=20)
    Module.objects.create(id='LIBARTS1002', name='Liberal Arts 1B: Intercultural Literacies (C4L)', school=language,
                          level=1, credits=20)
    Module.objects.create(id='LIBARTS4001',
                          name='Liberal Arts: Scottish and Global Environments: Past, Present, Future', school=language,
                          level=4, credits=20)
    Module.objects.create(id='LIBARTS2002', name='Liberal Arts 2B: Cultures and wellbeing', school=language, level=2,
                          credits=20)
    Module.objects.create(id='MFL2010', name='Medes German Stage 2', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1012', name='Japanese Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL2016', name='Medical SSC Stage 2:Spanish', school=language, level=2, credits=20)
    Module.objects.create(id='MFL2014', name='Medical SSC Stage 2:German', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1062', name='French Language for International Mobility 2 (Sem 1)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1052', name='Arabic Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1067', name='German Language for International Mobility 1 (Sem 2)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1058', name='Chinese Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1011', name='Japanese Language for International Mobility 1 (Sem 2)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1019', name='Italian Stage 1 for GSA', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1028', name='Portuguese Language for International Mobility 1', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1023', name='Medical SSC Stage 1:French', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1076', name='Spanish Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL2013', name='Medical SSC Stage 2:French', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1063', name='French Language for International Mobility 3 Semester 1', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1026', name='Medical SSC Stage 1:Spanish', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1075', name='Spanish Language for International Mobility 1 (Sem 2)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1074', name='Spanish Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1017', name='French Stage 1 for GSA', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1054', name='Arabic Language for International Mobility 3 Semester 2', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1010', name='Italian Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL2015', name='Medical SSC Stage 2:Italian', school=language, level=2, credits=20)
    Module.objects.create(id='MFL5004', name='French Language 2 for MGB (Master in Global Business)', school=language,
                          level=5, credits=10)
    Module.objects.create(id='MFL1055', name='Catalan Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1080', name='Spanish Language for International Mobility 4', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1072', name='Russian Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL2011', name='Medes Italian Stage 2', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1061', name='French Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1069', name='German Language for International Mobility 3 Semester 1', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1016', name='Japanese Language for International Mobility 4', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1079', name='Spanish Language for International Mobility 3 Semester 2',
                          school=language, level=1, credits=10)
    Module.objects.create(id='MFL1077', name='Spanish Language for International Mobility 2 (Sem 1)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1060', name='French Language for International Mobility 1 (Sem 2)', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1053', name='Arabic Language for International Mobility 3 Semester 1', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1021', name='Spanish Stage 1 for GSA', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1056', name='Catalan Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1015', name='Japanese Language for International Mobility 3 Semester 2',
                          school=language, level=1, credits=10)
    Module.objects.create(id='MFL1022', name='Medical SSC Stage 1: Chinese', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1064', name='French Language for International Mobility 3 Semester 2', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1057', name='Chinese Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1065', name='French Language for International Mobility 4', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1025', name='Medical SSC Stage 1:Italian', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1051', name='Arabic Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1027', name='Portuguese Language for International Mobility 1 (Sem 2)',
                          school=language, level=1, credits=10)
    Module.objects.create(id='MFL2012', name='Medes Spanish Stage 2', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1071', name='German Language for International Mobility 4', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL2009', name='Medes French Stage 2', school=language, level=2, credits=20)
    Module.objects.create(id='MFL1020', name='Portuguese Stage 1 for GSA', school=language, level=1, credits=20)
    Module.objects.create(id='MFL5003', name='Chinese Language 2 for MGB (Master in Global Business)', school=language,
                          level=5, credits=10)
    Module.objects.create(id='MFL1070', name='German Language for International Mobility 3 Semester 2', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1081', name='Ukrainian language for International Mobility 1', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1014', name='Japanese Language for International Mobility 3 Semester 1',
                          school=language, level=1, credits=10)
    Module.objects.create(id='MFL1013', name='Japanese Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1059', name='French Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1073', name='Russian Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1066', name='German Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1024', name='Medical SSC Stage 1:German', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1078', name='Spanish Language for International Mobility 3 Semester 1',
                          school=language, level=1, credits=10)
    Module.objects.create(id='MFL1029', name='Portuguese Language for International Mobility 2', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1018', name='German Stage 1 for GSA', school=language, level=1, credits=20)
    Module.objects.create(id='MFL1082', name='Ukrainian language for International Mobility 2', school=language,
                          level=1, credits=10)
    Module.objects.create(id='MFL1009', name='Italian Language for International Mobility 1', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MFL1068', name='German Language for International Mobility 2', school=language, level=1,
                          credits=10)
    Module.objects.create(id='MODLANG5024', name='Approaches to Translation and the Professional Environment (Nankai)',
                          school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG4005', name='Text/Image Cultures: Theory and Practice', school=language, level=4,
                          credits=20)
    Module.objects.create(id='MODLANG4012',
                          name='Translation Studies: An introduction to key topics in theory and practice',
                          school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG4015', name='Language Policy and Planning for European Minority Languages',
                          school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5032', name='Approaches to Translation and the Professional Environment',
                          school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5005', name='Marketing and Media Across Cultures', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG4007', name='Subsidiary Chinese (Mandarin) Language (Beginners)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='MODLANG5012', name='China and the West: Intellectuals and Knowledge dynamics',
                          school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5023', name='Translation of Literature and Culture 1 (Nankai)', school=language,
                          level=5, credits=20)
    Module.objects.create(id='MODLANG4016', name='Understanding Ukraine', school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5017', name='SMLC PGT Directed Study (Semester 2)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG1002', name='Chinese 1 (Mandarin)', school=language, level=1, credits=40)
    Module.objects.create(id='MODLANG5025', name='Translation Studies in Theory and Practice (Nankai)', school=language,
                          level=5, credits=20)
    Module.objects.create(id='MODLANG4011', name='Latin American Cinema', school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5001', name='English into Mandarin Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5010', name='PG Beginner Chinese Mandarin (Early Exit)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5034', name='Subtitling and Media Accessibility', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5009', name='Transnational Constructions of Gender', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG4014', name='Multilingualism in Context', school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5028P',
                          name='MSc Translation Studies: Translation and Professional Practice Dissertation (Glasgow-Nankai JGS)',
                          school=language, level=5, credits=60)
    Module.objects.create(id='MODLANG2002', name='Chinese 2 (Mandarin)', school=language, level=2, credits=40)
    Module.objects.create(id='MODLANG5040', name='Intercultural Communication', school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5006', name='Literary Translation Studies', school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5043', name='Practical Translation Workshop 2', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG4013', name='Censorship In Western Culture', school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5026', name='Research Methods and Skills in Translation Studies (Nankai)',
                          school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG5016', name='SMLC PGT Directed Study (Semester 1)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5044', name='Translation of Literature and Culture 2', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG4010', name='Subsidiary Chinese (Mandarin) Language (Intermediate)',
                          school=language, level=4, credits=20)
    Module.objects.create(id='MODLANG5011', name='PG Beginner Chinese (Mandarin)', school=language, level=5, credits=40)
    Module.objects.create(id='MODLANG5018', name='SMLC PGT Portfolio option (Semester 1)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5019', name='SMLC PGT Portfolio option (Semester 2)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5033P', name='MSc Translation and Intercultural Studies Dissertation',
                          school=language, level=5, credits=60)
    Module.objects.create(id='MODLANG5041', name='Introduction to Interpreting', school=language, level=5, credits=20)
    Module.objects.create(id='MODLANG1003', name='Chinese 1 (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='MODLANG5035', name='Translation Studies in Theory and Practice', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG5002', name='Mandarin Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='MODLANG5042', name='Practical Translation Workshop 1', school=language, level=5,
                          credits=20)
    Module.objects.create(id='MODLANG2004', name='Preparing for SMLC Residence Abroad', school=language, level=2,
                          credits=0)
    Module.objects.create(id='MODLANG5021', name='PG Intermediate Chinese (Mandarin)', school=language, level=5,
                          credits=40)
    Module.objects.create(id='MODLANG2001', name='Chinese 2 (Early Exit)', school=language, level=2, credits=20)
    Module.objects.create(id='NANKAI5025',
                          name='Translation Technology: Terminology Management and Subtitling (Nankai)',
                          school=language, level=5, credits=20)
    Module.objects.create(id='NANKAI5026', name='Mandarin Advanced Translation and Language Study 2 (Nankai)',
                          school=language, level=5, credits=20)
    Module.objects.create(id='NANKAI5005', name='Mandarin Advanced Translation and Language Study 1 (Nankai)',
                          school=language, level=5, credits=20)
    Module.objects.create(id='POLISH5018', name='PG BEGINNER POLISH (EARLY EXIT)', school=language, level=5, credits=20)
    Module.objects.create(id='POLISH5023', name='Polish for Social Scientists Beginners Semester 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='POLISH2002', name='Polish 2 (Early Exit)', school=language, level=2, credits=20)
    Module.objects.create(id='POLISH5019', name='PG BEGINNER POLISH', school=language, level=5, credits=40)
    Module.objects.create(id='POLISH5020', name='PG Intermediate Polish', school=language, level=5, credits=40)
    Module.objects.create(id='POLISH5016', name='Polish Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='POLISH4037', name='Advanced Subsidiary Polish', school=language, level=4, credits=20)
    Module.objects.create(id='POLISH1001', name='Polish 1', school=language, level=1, credits=40)
    Module.objects.create(id='POLISH1002', name='Polish 1 (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='POLISH2001', name='Polish 2', school=language, level=2, credits=40)
    Module.objects.create(id='POLISH3002', name='Polish Language 3', school=language, level=3, credits=30)
    Module.objects.create(id='POLISH4007', name='Subsidiary Polish Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='POLISH5024', name='Polish for Social Scientists Intermediate Semester 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='POLISH5015', name='Polish into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='POLISH4008', name='Subsidiary Polish Language (Intermediate)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='POLISH5021', name='English into Polish Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='POLISH5022', name='English into Polish Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='PORT5008', name='Portuguese Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='PORT4014', name='Portuguese Language Project', school=language, level=4, credits=20)
    Module.objects.create(id='PORT5007', name='Portuguese into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='PORT4011', name='Subsidiary Portuguese Language (Intermediate)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='PORT2001', name='Portuguese Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='PORT4009', name='Portuguese Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='PORT2002', name='Portuguese Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='PORT2003', name='PORTUGUESE YEAR ABROAD ASSISTANTSHIP', school=language, level=2,
                          credits=120)
    Module.objects.create(id='PORT5005', name='PG BEGINNER PORTUGUESE (EARLY EXIT)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='PORT4003', name='Portuguese Honours Language for Law Students', school=language, level=4,
                          credits=60)
    Module.objects.create(id='PORT1001', name='Portuguese 1 (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='PORT5006', name='PG Intermediate Portuguese', school=language, level=5, credits=20)
    Module.objects.create(id='PORT5004', name='PG BEGINNER PORTUGUESE', school=language, level=5, credits=40)
    Module.objects.create(id='PORT2004', name='PORTUGUESE YEAR ABROAD STUDY', school=language, level=2, credits=120)
    Module.objects.create(id='PORT4008', name='Portuguese Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='PORT1002', name='Portuguese Language 1 (Beginners)', school=language, level=1, credits=40)
    Module.objects.create(id='PORT5002', name='English into Portuguese Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='PORT4006', name='Portuguese Honours Spoken Language (year 1 exit)', school=language,
                          level=4, credits=10)
    Module.objects.create(id='PORT4007', name='Portuguese Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='PORT2005', name='PORTUGUESE YEAR ABROAD WORK PLACEMENT', school=language, level=2,
                          credits=120)
    Module.objects.create(id='PORT3002', name='Portuguese 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='PORT4001P', name='Applied Dissertation with Placement in Portuguese', school=language,
                          level=4, credits=20)
    Module.objects.create(id='PORT4005', name='Portuguese Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='PORT4002P', name='Portuguese Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='PORT5001', name='English into Portuguese Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='PORT3001', name='Portuguese 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='PORT5003', name='PG Advanced Portuguese', school=language, level=5, credits=30)
    Module.objects.create(id='PORT4004', name='Portuguese Honours Spoken Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='PORT4012', name='Space and Society in the Portuguese-Speaking World', school=language,
                          level=4, credits=20)
    Module.objects.create(id='PORT4010', name='Subsidiary Portuguese Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN4040', name='Brave New Worlds: Russian Culture in the Age of Revolution',
                          school=language, level=4, credits=20)
    Module.objects.create(id='RUSSIAN4034', name='Russian Honours Written Language (Senior)', school=language, level=4,
                          credits=40)
    Module.objects.create(id='RUSSIAN5022', name='PG BEGINNER RUSSIAN (EARLY EXIT)', school=language, level=5,
                          credits=20)
    Module.objects.create(id='RUSSIAN4002', name='Russian 20th Century Visual Culture', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN5026', name='English into Russian Advanced Translation and Language Study 2',
                          school=language, level=5, credits=20)
    Module.objects.create(id='RUSSIAN5017', name='Russian into English Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='RUSSIAN4041P', name='Applied Dissertation with Placement in Russian', school=language,
                          level=4, credits=20)
    Module.objects.create(id='RUSSIAN2012', name='Russian Language 2', school=language, level=2, credits=20)
    Module.objects.create(id='RUSSIAN4033', name='Russian Honours Written Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='RUSSIAN5018', name='Russian Advanced Translation and Language Study 2', school=language,
                          level=5, credits=20)
    Module.objects.create(id='RUSSIAN4008', name='The Russian Novel', school=language, level=4, credits=20)
    Module.objects.create(id='RUSSIAN5021', name='PG Advanced Russian', school=language, level=5, credits=30)
    Module.objects.create(id='RUSSIAN4035', name='Russian Honours Written Language (year 1 exit)', school=language,
                          level=4, credits=20)
    Module.objects.create(id='RUSSIAN1002', name='Russian 1 (Early Exit)', school=language, level=1, credits=20)
    Module.objects.create(id='RUSSIAN5025', name='English into Russian Advanced Translation and Language Study 1',
                          school=language, level=5, credits=20)
    Module.objects.create(id='RUSSIAN4004P', name='Russian Dissertation', school=language, level=4, credits=20)
    Module.objects.create(id='RUSSIAN4030', name='Russian Honours Spoken Language (Junior)', school=language, level=4,
                          credits=0)
    Module.objects.create(id='RUSSIAN5023', name='PG BEGINNER RUSSIAN', school=language, level=5, credits=40)
    Module.objects.create(id='RUSSIAN4042', name='Queerness in Russophone Cultures', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN4006', name='Subsidiary Russian Language (Beginners)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN3001', name='Russian 3 Language and Culture', school=language, level=3, credits=60)
    Module.objects.create(id='RUSSIAN1001', name='Russian 1', school=language, level=1, credits=40)
    Module.objects.create(id='RUSSIAN3002', name='Russian 3 Language', school=language, level=3, credits=30)
    Module.objects.create(id='RUSSIAN4007', name='Subsidiary Russian Language (Intermediate)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN4031', name='Russian Honours Spoken Language (Senior)', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN4032', name='Russian Honours Spoken Language (year 1 exit)', school=language,
                          level=4, credits=10)
    Module.objects.create(id='RUSSIAN2011', name='Russian Culture 2', school=language, level=2, credits=20)
    Module.objects.create(id='RUSSIAN4038', name='Russian Literature and State Power', school=language, level=4,
                          credits=20)
    Module.objects.create(id='RUSSIAN5024', name='PG Intermediate Russian', school=language, level=5, credits=20)
    Module.objects.create(id='RUSSIAN2010', name='RUSSIAN YEAR ABROAD STUDY', school=language, level=2, credits=120)

    # School of Molecular Biosciences (67 modules)
    Module.objects.create(id='BIOL5227', name='Biotechnology Applications', school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL4010', name='Biochemistry 3B', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL4191', name='Cell Compartmentalisation 4Y option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4281', name='Statistics for the Life Sciences (Sem 1) 4Y option', school=bioscience,
                          level=4, credits=20)
    Module.objects.create(id='BIOL4282', name='Statistics for the Life Sciences (Sem 2) 4E option', school=bioscience,
                          level=4, credits=20)
    Module.objects.create(id='BIOL1019', name='Biology 1C (Northeastern University)', school=bioscience, level=1,
                          credits=20)
    Module.objects.create(id='BIOL4124', name='Tissue and Cell Engineering 4Y option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5462', name='Industrial Biotechnology Industry Training', school=bioscience, level=5,
                          credits=40)
    Module.objects.create(id='BIOL4211', name='Current Topics in Genetics 4X core', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4074', name='Molecular & Cellular Biology 3A', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL5214', name='Molecular Laboratory Skills', school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL5336', name='Presentation skills in the biomedical sciences', school=bioscience,
                          level=5, credits=10)
    Module.objects.create(id='BIOL4291', name='ISS Short Research Project: Visit International Students (UCEAP)',
                          school=bioscience, level=4, credits=15)
    Module.objects.create(id='BIOL4055', name='Human Molecular Genetics 4Y option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4051', name='Genetics 3A', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL2042', name='Genes, Molecules & Cells 2', school=bioscience, level=2, credits=30)
    Module.objects.create(id='BIOL5151P', name='MRes Biomedical Sciences Project 2', school=bioscience, level=5,
                          credits=60)
    Module.objects.create(id='BIOL4027', name='Cell Signalling and Disease 4D option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4226', name='ISS Research Project: Visiting International Students',
                          school=bioscience, level=4, credits=24)
    Module.objects.create(id='BIOL4034', name='Core Skills in Molecular and Cellular Biology 4X core',
                          school=bioscience, level=4, credits=20)
    Module.objects.create(id='BIOL5220', name='Role of Insects in Food Security', school=bioscience, level=5,
                          credits=10)
    Module.objects.create(id='BIOL4259', name='Mitochondrial Biology 4C option', school=bioscience, level=4, credits=20)
    Module.objects.create(id='BIOL5266P', name='MSc Biomedical Sciences Project', school=bioscience, level=5,
                          credits=60)
    Module.objects.create(id='BIOL5217', name='Food Security Fundamentals - Crops', school=bioscience, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5150P', name='MRes Biomedical Sciences Project 1', school=bioscience, level=5,
                          credits=60)
    Module.objects.create(id='BIOL5332P', name='Stem Cell Engineering for Regenerative Medicine Project',
                          school=bioscience, level=5, credits=60)
    Module.objects.create(id='BIOL5382',
                          name='Foundations of Bioinformatics: an Introduction to Computational Biology and Omics Analysis',
                          school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL5230', name='Synthetic Biology: Concepts and Applications', school=bioscience,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5229', name='Molecular Research Skills', school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL5300', name='Identification of Disease-Causing Genetic Variants', school=bioscience,
                          level=5, credits=10)
    Module.objects.create(id='BIOL5213', name='Crop Biotechnology Applications', school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL5216', name='Food Security Fundamentals - Food of Animal Origin', school=bioscience,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5215P', name='Food Security Project', school=bioscience, level=5, credits=60)
    Module.objects.create(id='BIOL5145', name='Industrial and Environmental Microbiology', school=bioscience, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5383', name='Advanced Studies in Biomedical Sciences', school=bioscience, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4075', name='Molecular & Cellular Biology 3B', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL4110', name='Plant Biotechnology 4B option', school=bioscience, level=4, credits=20)
    Module.objects.create(id='BIOL5219', name='Plant Genetic Engineering', school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL5368',
                          name='Designing a Research Project: Stem Cells Engineering for Regenerative Medicine',
                          school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL5464', name='Introduction to Microbial Biotechnology', school=bioscience, level=5,
                          credits=10)
    Module.objects.create(id='BIOL5347',
                          name='Stem Cell Science and Engineering Microenvironments for Regenerative Medicine',
                          school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL4021', name='Current Topics in Biotechnology 4A option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL1018', name='Current Directions in Life Sciences (Online)', school=bioscience,
                          level=1, credits=20)
    Module.objects.create(id='BIOL5376', name='Genome Editing', school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL4052', name='Genetics 3B', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL5438', name='Biomaterials and immune regulation', school=bioscience, level=5,
                          credits=10)
    Module.objects.create(id='BIOL4009', name='Biochemistry 3A', school=bioscience, level=4, credits=60)
    Module.objects.create(id='BIOL4123', name='Stem Cells 4D option', school=bioscience, level=4, credits=20)
    Module.objects.create(id='BIOL1002', name='Biology 1B', school=bioscience, level=1, credits=20)
    Module.objects.create(id='BIOL4296', name='Genetics of Complex Traits and Disorders 4C option', school=bioscience,
                          level=4, credits=20)
    Module.objects.create(id='BIOL5305', name='Recombinant Protein Expression', school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL5461P', name='Biotechnology Policy Brief Project', school=bioscience, level=5,
                          credits=60)
    Module.objects.create(id='BIOL5149', name='Higher Skills in Biomedical Sciences', school=bioscience, level=5,
                          credits=20)
    Module.objects.create(id='BIOL5218', name='Introduction to Food Security', school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL4112', name='Plant Molecular Biology 4Y option', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5312', name='Plant Biotechnology', school=bioscience, level=5, credits=20)
    Module.objects.create(id='BIOL5200', name='Technology Transfer and Commercialisation of Bioscience Research',
                          school=bioscience, level=5, credits=10)
    Module.objects.create(id='BIOL4079', name='Molecular Basis of Cardiometabolic Disease 4B option', school=bioscience,
                          level=4, credits=20)
    Module.objects.create(id='BIOL5152', name='The Molecular Genetics of Disease', school=bioscience, level=5,
                          credits=30)
    Module.objects.create(id='BIOL5415', name='Biotechnology of Crops', school=bioscience, level=5, credits=30)
    Module.objects.create(id='BIOL4029', name='Central Approaches in Biochemistry 4X core', school=bioscience, level=4,
                          credits=20)
    Module.objects.create(id='BIOL5228P', name='Biotechnology Project', school=bioscience, level=5, credits=60)
    Module.objects.create(id='BIOL4125', name='Functional Genetics and Cellular Contexts in Model Organisms 4A option',
                          school=bioscience, level=4, credits=20)
    Module.objects.create(id='BIOL1001', name='Biology 1A', school=bioscience, level=1, credits=20)
    Module.objects.create(id='BIOL4290', name='ISS Research Project: Visit International Students (UCEAP)',
                          school=bioscience, level=4, credits=25)
    Module.objects.create(id='BIOL1017', name='ISS MVLS Pre-University Summer School (Life Sciences)',
                          school=bioscience, level=1, credits=10)
    Module.objects.create(id='BIOL2039', name='Fundamental Topics in Biology 2', school=bioscience, level=2, credits=30)

    # School of Physics and Astronomy (128 modules)
    Module.objects.create(id='ASTRO1001', name='Astronomy 1', school=physics, level=1, credits=40)
    Module.objects.create(id='ASTRO4003P', name='Astronomy Skills 1', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO1004', name='Exploring the Cosmos 1Y', school=physics, level=1, credits=20)
    Module.objects.create(id='ASTRO2002', name='Astronomy 2(Half)', school=physics, level=2, credits=15)
    Module.objects.create(id='ASTRO5001', name='General Relativity and Gravitation', school=physics, level=5,
                          credits=15)
    Module.objects.create(id='ASTRO4013', name='Astronomical Data Analysis', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO4011', name='Stellar Structure and Evolution', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO4006', name='Cosmology', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO4005', name='Heliophysics and Stellar Atmospheres', school=physics, level=4,
                          credits=15)
    Module.objects.create(id='ASTRO1002', name='Astronomy 1(Half)', school=physics, level=1, credits=20)
    Module.objects.create(id='ASTRO5003', name='Statistical Astronomy', school=physics, level=5, credits=15)
    Module.objects.create(id='ASTRO1010', name='Astronomy 1 for Faster Route', school=physics, level=1, credits=20)
    Module.objects.create(id='ASTRO4010', name='Instruments for Optical and Radio Astronomy', school=physics, level=4,
                          credits=15)
    Module.objects.create(id='ASTRO4004P', name='Astronomy Skills 2', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO5004', name='Plasma Theory and Diagnostics', school=physics, level=5, credits=15)
    Module.objects.create(id='ASTRO5002', name='Pulsars and Supernovae', school=physics, level=5, credits=15)
    Module.objects.create(id='ASTRO5011', name='Space Environments', school=physics, level=5, credits=10)
    Module.objects.create(id='ASTRO4008', name='Galaxies', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO2001', name='Astronomy 2', school=physics, level=2, credits=30)
    Module.objects.create(id='ASTRO4007', name='Exploring Planetary Systems', school=physics, level=4, credits=15)
    Module.objects.create(id='ASTRO4001P', name='Astronomy Laboratory 1', school=physics, level=4, credits=10)
    Module.objects.create(id='ASTRO4020P', name='Astronomy Project for 4M Students', school=physics, level=4,
                          credits=20)
    Module.objects.create(id='ASTRO1003', name='Exploring the Cosmos 1X', school=physics, level=1, credits=20)
    Module.objects.create(id='ASTRO5010', name='The Sun\'s Atmosphere', school=physics, level=5, credits=10)
    Module.objects.create(id='ASTRO4009', name='High Energy Astrophysics', school=physics, level=4, credits=15)
    Module.objects.create(id='PHYS5014', name='Relativistic Quantum Fields', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4011', name='Mathematical Methods 1', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5012', name='Problem Solving Workshop', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4056', name='Numerical Methods (December Exam)', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4034', name='Physics Education And Communication In Schools', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS5007', name='Groups And Symmetries', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5092P', name='MSc Project (Edinburgh)', school=physics, level=5, credits=60)
    Module.objects.create(id='PHYS4062', name='MSc SIS Edinburgh Course - Radio Frequency Engineering 4',
                          school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4031', name='Waves & Diffraction', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5001', name='Advanced Data Analysis For Physics And Astronomy', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS4002', name='Atomic Systems', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5085', name='MSc SIS Edinburgh Course - Analogue circuit design', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS5083', name='MSc SIS Edinburgh Course - Technology and Innovation Management',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5054', name='Relativistic Quantum Fields (December Exam)', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS4054', name='Circuits & Systems (December Exam)', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5002', name='Quantum and Atom Optics', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5004', name='Dynamics, Electrodynamics & Relativity', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS5075', name='MSc SIS Edinburgh Course - BioSensors and Instrumentation',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5035', name='Imaging and Detectors', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5038', name='Nuclear Power Reactors', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4069P', name='Applied Computing in Physics', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS1020', name='The Science of Musical Instruments and Acoustics', school=physics,
                          level=1, credits=20)
    Module.objects.create(id='PHYS5041', name='Nano and Atomic Scale Imaging 1', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5009P', name='Physics M Project', school=physics, level=5, credits=40)
    Module.objects.create(id='PHYS1001', name='Physics 1', school=physics, level=1, credits=40)
    Module.objects.create(id='PHYS4046', name='Summer research project', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS4014', name='Lasers & Non-Linear Optics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4013', name='Medical Imaging', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4057', name='Waves & Diffraction (December Exam)', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS1017', name='International Physics Summer School 2', school=physics, level=1,
                          credits=15)
    Module.objects.create(id='PHYS5056', name='Experimental Techniques in Quantum Optics', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS4067', name='Analytical Mechanics (Dec Exam)', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5095',
                          name='MSc SIS Edinburgh Course - Radio Frequency (RF) and Microwave Circuits and Systems',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4061', name='Honours Physics Laboratory (December Exam)', school=physics, level=4,
                          credits=20)
    Module.objects.create(id='PHYS4030', name='Thermal Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5063', name='Nuclear Power Reactors (December Exam)', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS4022P', name='Physics Project', school=physics, level=4, credits=30)
    Module.objects.create(id='PHYS4003', name='Circuits & Systems', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5051', name='Groups And Symmetries (December Exam)', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS4021P', name='Physics Group Project', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS2003', name='Physics 2T: Programming Under Linux', school=physics, level=2,
                          credits=10)
    Module.objects.create(id='PHYS4009', name='Honours Physics Laboratory', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS5057P',
                          name='Applications of Intelligent Sensing and Measurement (University of Edinburgh)',
                          school=physics, level=5, credits=20)
    Module.objects.create(id='PHYS4008', name='Honours Computational Physics Laboratory', school=physics, level=4,
                          credits=20)
    Module.objects.create(id='PHYS2001', name='Physics 2', school=physics, level=2, credits=60)
    Module.objects.create(id='PHYS1011', name='Science Skills', school=physics, level=1, credits=20)
    Module.objects.create(id='PHYS1002', name='Physics 1(Half)', school=physics, level=1, credits=20)
    Module.objects.create(id='PHYS1018',
                          name='International Physics Summer School for physical sciences and engineering 1',
                          school=physics, level=1, credits=15)
    Module.objects.create(id='PHYS4025', name='Quantum Mechanics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5021P', name='MSc Project', school=physics, level=5, credits=60)
    Module.objects.create(id='PHYS1025', name='Physics Skills for Faster Route', school=physics, level=1, credits=10)
    Module.objects.create(id='PHYS5082', name='MSc SIS Edinburgh Course - Research Project Preparation', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS1022', name='Summer Physics for Life Sciences 2', school=physics, level=1, credits=10)
    Module.objects.create(id='PHYS4015', name='Nuclear & Particle Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4060', name='Honours Computational Physics Laboratory (December Exam)',
                          school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS5005', name='Electromagnetic Theory 2', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4012', name='Mathematical Methods 2', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5074', name='MSc SIS Edinburgh Course - Applications of Sensor and Imaging Systems',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS1019',
                          name='International Physics Summer School for physical sciences and engineering 2',
                          school=physics, level=1, credits=15)
    Module.objects.create(id='PHYS1023', name='Summer Physics for Sciences and Engineering 1', school=physics, level=1,
                          credits=10)
    Module.objects.create(id='PHYS5042', name='Nano and Atomic Scale Imaging 2', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5044', name='Fundamentals of Sensing and Measurement', school=physics, level=5,
                          credits=20)
    Module.objects.create(id='PHYS4047', name='Energy And Environment (December Exam)', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS2002', name='Physics 2 (Half)', school=physics, level=2, credits=30)
    Module.objects.create(id='PHYS4053P', name='Physics 40-credit H-level Project', school=physics, level=4, credits=40)
    Module.objects.create(id='PHYS5094', name='Systems Engineering: Thinking and Practice (Edinburgh)', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS4017', name='Numerical Methods', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4016', name='Nuclear Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4066', name='Analytical Mechanics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4007', name='General Physics Workshop', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4023P', name='Physics Project', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS5081', name='MSc SIS Edinburgh Course - Physical Techniques in Action Level 11',
                          school=physics, level=5, credits=20)
    Module.objects.create(id='PHYS5006', name='Gravitational Wave Detection', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5078', name='MSc SIS Edinburgh Course - Innovation-driven Entrepreneurship',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4026', name='Quantum Theory', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4028', name='Solid State Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4052', name='Solid State Physics (December Exam)', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS1021', name='Summer Physics for Life Sciences 1', school=physics, level=1, credits=10)
    Module.objects.create(id='PHYS4029P', name='Theoretical Physics Group Project', school=physics, level=4, credits=20)
    Module.objects.create(id='PHYS4055', name='Mathematical Methods 1 (December Exam)', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS5093', name='MSc SIS Edinburgh Course - Sensors and Instrumentation', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS5016', name='Statistical Mechanics', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5036', name='Detection and Analysis of Ionising Radiation', school=physics, level=5,
                          credits=10)
    Module.objects.create(id='PHYS5079', name='MSc SIS Edinburgh Course - Lab-on-Chip Technologies', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS4006', name='Energy And Environment', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5077', name='MSc SIS Edinburgh Course - Chemistry of Functional Materials Level 11',
                          school=physics, level=5, credits=20)
    Module.objects.create(id='PHYS4049', name='Mathematical Methods 2 (December Exam)', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS4018', name='Particle Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4045', name='Peer to Peer Teaching and Learning in Physics', school=physics, level=4,
                          credits=10)
    Module.objects.create(id='PHYS4051', name='Quantum Theory (December Exam)', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5037', name='Environmental Radioactivity', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS4010', name='Magnetism & Superconductivity', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4068', name='Atomic Systems December Exam', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5047P', name='Physics Literature Project', school=physics, level=5, credits=20)
    Module.objects.create(id='PHYS5090', name='MSc SIS Edinburgh Course - Data Converter Design in Simulink 5',
                          school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS1016', name='International Physics Summer School 1', school=physics, level=1,
                          credits=15)
    Module.objects.create(id='PHYS4064', name='MSc SIS Edinburgh Course - Bio-Inspired Engineering', school=physics,
                          level=4, credits=10)
    Module.objects.create(id='PHYS1024', name='Summer Physics for Sciences and Engineering 2', school=physics, level=1,
                          credits=10)
    Module.objects.create(id='PHYS4027', name='Semiconductor Physics', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS4004', name='Electromagnetic Theory 1', school=physics, level=4, credits=10)
    Module.objects.create(id='PHYS5080', name='MSc SIS Edinburgh Course - Microfabrication Techniques', school=physics,
                          level=5, credits=10)
    Module.objects.create(id='PHYS5015', name='Research Skills', school=physics, level=5, credits=10)
    Module.objects.create(id='PHYS5039', name='Quantum Information', school=physics, level=5, credits=10)

    # School of Psychology and Neuroscience (100 modules)
    Module.objects.create(id='BIOL4266', name='Perspectives on Cognitive Neuroscience 4B option', school=psychology,
                          level=4, credits=20)
    Module.objects.create(id='BIOL5364', name='Designing a Research Project: Brain Sciences', school=psychology,
                          level=5, credits=20)
    Module.objects.create(id='BIOL4258', name='Contemporary Issues in Neuroscience 4X core', school=psychology, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4235', name='Neuroscience 3B', school=psychology, level=4, credits=60)
    Module.objects.create(id='BIOL4001', name='Neuronal Pathways Underlying Pain, Nociception and Itch 4A option',
                          school=psychology, level=4, credits=20)
    Module.objects.create(id='BIOL4234', name='Neuroscience 3A', school=psychology, level=4, credits=60)
    Module.objects.create(id='BIOL5282', name='Neuroscience: Animal Models of Disease and Function', school=psychology,
                          level=5, credits=20)
    Module.objects.create(id='BIOL5316P', name='MSc Bioscience Research Project (Brain Sciences)', school=psychology,
                          level=5, credits=60)
    Module.objects.create(id='BIOL4279', name='Neuromodulation & Synaptic Plasticity 4C option', school=psychology,
                          level=4, credits=20)
    Module.objects.create(id='BIOL5283', name='Fundamentals of Neuroscience Research', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='BIOL4038', name='Diseases of the Nervous System 4Y option', school=psychology, level=4,
                          credits=20)
    Module.objects.create(id='BIOL4306', name='Stress, behaviour and experimental design 4D option', school=psychology,
                          level=4, credits=20)
    Module.objects.create(id='PSYCH5028', name='Perception And Visual Cognition (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4006', name='Human Development 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5033', name='Social Psychology (PGT Conv)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH2010', name='Psychology 2A', school=psychology, level=2, credits=30)
    Module.objects.create(id='PSYCH4011', name='Professional Skills 3', school=psychology, level=4, credits=20)
    Module.objects.create(id='PSYCH5053', name='Psychology and Biology of Mental Health Conditions (PGT Conv)',
                          school=psychology, level=5, credits=20)
    Module.objects.create(id='PSYCH5056', name='Sleep and Circadian Timing (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH5018', name='Research Methods in Cognitive Science (PGT)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH5051', name='Neuropsychological Dissociations (PGT Conv)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH5020', name='Statistics & Research Design (PGT)', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='PSYCH5069', name='Neuroscience of Decision Making (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4098', name='Applied Data Visualisation 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4039', name='Individual Differences 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH1002', name='Psychology 1B', school=psychology, level=1, credits=20)
    Module.objects.create(id='PSYCH5107', name='Introduction to Neuroscience (PGT)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4066', name='From Visual Awareness to Free Will 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH5087', name='Social Psychology (PGT Conv ODL)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4002', name='Cognitive Psychology 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5042', name='Autism (PGT Conv)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH5025', name='Formal Models and Quantitative Methods for Psychology (PGT)',
                          school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH4104', name='Current Issues in Psychology 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4058', name='Quantitative Project 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5047', name='Cognitive Neuroscience Insights into Brain Plasticity (PGT Conv)',
                          school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH4091', name='Simulation Methods for Psychologists using R 4H', school=psychology,
                          level=4, credits=10)
    Module.objects.create(id='PSYCH5089', name='Research Methods 2 (PGT Conv)', school=psychology, level=5, credits=20)
    Module.objects.create(id='PSYCH4040', name='Sleep and Circadian Timing 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5022', name='Cognitive Brain Imaging Methods (PGT)', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='PSYCH5078', name='Conceptual and Historical Issues in Psychology (PGT Conv ODL)',
                          school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH4036', name='Social Psychology 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4034', name='Psychology and Biology of Mental Health Conditions 4H',
                          school=psychology, level=4, credits=20)
    Module.objects.create(id='PSYCH5029', name='Physiological Psychology (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4079', name='Summer Research Project', school=psychology, level=4, credits=24)
    Module.objects.create(id='PSYCH5090', name='Social Robotics (PGT)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH5103', name='Forensic Psychology (PGT Conv ODL)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4065', name='Physiological Psychology 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5099', name='Basics of fMRI in Cognitive Psychology (PGT Conv)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH5038P', name='Research Project (PGT)', school=psychology, level=5, credits=60)
    Module.objects.create(id='PSYCH4007P', name='Dissertation 4H', school=psychology, level=4, credits=30)
    Module.objects.create(id='PSYCH4031', name='Neuropsychological Dissociations 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH5017', name='Professional Skills (PGT)', school=psychology, level=5, credits=20)
    Module.objects.create(id='PSYCH4037', name='Statistical Models 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4064', name='Neuroscience of Decision Making 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH2011', name='Psychology 2B', school=psychology, level=2, credits=30)
    Module.objects.create(id='PSYCH5083', name='Dissertation (PGT Conv ODL)', school=psychology, level=5, credits=60)
    Module.objects.create(id='PSYCH5079', name='Physiological Psychology (PGT Conv ODL)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4088', name='Psychometrics 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4105', name='Science Communication and Dissemination 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH1012', name='Applied Data Skills (C4L)', school=psychology, level=1, credits=20)
    Module.objects.create(id='PSYCH5070', name='From Visual Awareness to Free Will (PGT Conv)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH5040', name='Psychology Dissertation (PGT Conv)', school=psychology, level=5,
                          credits=60)
    Module.objects.create(id='PSYCH5082', name='Current Issues In Psychology (PGT Conv ODL)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH5016', name='Introduction to MatLab Programming (PGT)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4018', name='Cognitive Neuroscience: Insights into Brain Plasticity 4H',
                          school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH1010', name='Introduction to Psychology', school=psychology, level=1, credits=10)
    Module.objects.create(id='PSYCH4008', name='Perception And Visual Cognition 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH4096', name='Qualitative Research Enquiry 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH5077', name='Data Skills for Reproducible Research (PGT)', school=psychology,
                          level=5, credits=20)
    Module.objects.create(id='PSYCH4023', name='Realtime fMRI 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5061', name='Cognitive Psychology (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH5094', name='From Visual Awareness to Free Will (PGT)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH5048', name='Forensic Psychology (PGT Conv)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH5109', name='Neural circuits and behaviour', school=psychology, level=5, credits=20)
    Module.objects.create(id='PSYCH5095', name='Health Neuroscience (PGT Conv)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH1001', name='Psychology 1A', school=psychology, level=1, credits=20)
    Module.objects.create(id='PSYCH5034', name='Current Issues In Psychology (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH5067', name='Human Development (PGT Conv)', school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH4080', name='Analysis of Psychometric Data 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH4094', name='Qualitative Project 3 ABROAD', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH4014', name='Autism 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5088', name='Research Methods 1 (PGT Conv)', school=psychology, level=5, credits=20)
    Module.objects.create(id='PSYCH4086', name='Social Robotics 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5086', name='Research Methods 2 (PGT Conv ODL)', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='PSYCH4097',
                          name='Service Learning: Supporting Schools with Effective Learning Strategies 4H',
                          school=psychology, level=4, credits=20)
    Module.objects.create(id='PSYCH4082', name='Health Neuroscience 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5021', name='Advanced Perception and Cognition (PGT)', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='PSYCH4057', name='Qualitative Project 3', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5080', name='Research Methods 1 (PGT Conv ODL)', school=psychology, level=5,
                          credits=20)
    Module.objects.create(id='PSYCH4100', name='Psychological Assessment 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5093', name='Theories of Counselling and Psychotherapy PGT (Conv)',
                          school=psychology, level=5, credits=10)
    Module.objects.create(id='PSYCH5030', name='Introduction to Professional Skills (PGT Conv)', school=psychology,
                          level=5, credits=10)
    Module.objects.create(id='PSYCH4085', name='Theories of Counselling and Psychotherapy 4H', school=psychology,
                          level=4, credits=10)
    Module.objects.create(id='PSYCH4090', name='Basics of fMRI in Cognitive Psychology 4H', school=psychology, level=4,
                          credits=10)
    Module.objects.create(id='PSYCH4099', name='Applied Psychology in Sport 4H', school=psychology, level=4, credits=10)
    Module.objects.create(id='PSYCH5049', name='Individual Differences (PGT Conv)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH2014',
                          name='Advanced Introduction to Individual Differences and Developmental Psychology',
                          school=psychology, level=2, credits=10)
    Module.objects.create(id='PSYCH5105', name='Virtual Reality in Psychology Research (PGT)', school=psychology,
                          level=5, credits=20)
    Module.objects.create(id='PSYCH5101', name='Transdisciplinary Team Science (PGT)', school=psychology, level=5,
                          credits=10)
    Module.objects.create(id='PSYCH4101', name='Quantitative Project 3 ABROAD', school=psychology, level=4, credits=10)

    # School of Social and Environmental Sustainability (122 modules)
    Module.objects.create(id='DUMF5098', name='Working in an inter-agency environment', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF2068', name='Modern Languages: Policy and Pedagogy', school=environmental, level=2,
                          credits=10)
    Module.objects.create(id='DUMF4040', name='Environmental Policy and Management', school=environmental, level=4,
                          credits=20)
    Module.objects.create(id='DUMF1013', name='Mathematics - Theory And Pedagogy 1', school=environmental, level=1,
                          credits=20)
    Module.objects.create(id='DUMF3089', name='STEM across the Primary Curriculum', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF5019', name='Tourism Sustainability And Climate Change', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF3023P', name='Dissertation 3', school=environmental, level=3, credits=60)
    Module.objects.create(id='DUMF3006', name='Curriculum And Assessment', school=environmental, level=3, credits=20)
    Module.objects.create(id='DUMF5173', name='Modelling social-ecological changes and risk', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF5106', name='Reflective Practice', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5139', name='Environmental Policy (Nankai)', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5165', name='Leading and Managing Change', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5125', name='Enhanced Practice Dissertation', school=environmental, level=5,
                          credits=60)
    Module.objects.create(id='DUMF2069', name='Child Development And Learning', school=environmental, level=2,
                          credits=20)
    Module.objects.create(id='DUMF3081P', name='Environmental Placement (International)', school=environmental, level=3,
                          credits=60)
    Module.objects.create(id='DUMF5080', name='Writing the Environment: Modern and Contemporary Nature Writing',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5110', name='PGDE with Teaching Qualification: School Experience',
                          school=environmental, level=5, credits=30)
    Module.objects.create(id='DUMF5145', name='Wildlife Tourism and Environmental Responsibility', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF5104', name='Work Placement', school=environmental, level=5, credits=60)
    Module.objects.create(id='DUMF1008', name='Introduction To Global Environmental Issues', school=environmental,
                          level=1, credits=20)
    Module.objects.create(id='DUMF2043', name='SIS study abroad credits L2 sem 1', school=environmental, level=2,
                          credits=60)
    Module.objects.create(id='DUMF3084', name='Aquatic Environment: Processes, Monitoring and Management',
                          school=environmental, level=3, credits=20)
    Module.objects.create(id='DUMF5166', name='Digital Transformation For Third Sector Leaders', school=environmental,
                          level=5, credits=10)
    Module.objects.create(id='DUMF1023', name='French For Beginners (i)', school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF5115', name='Principles of GIS for Environmental Science (Nankai)',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5127', name='The Continuum of Ageing and Dying', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5009', name='Heritage, Interpretation And Development', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5146', name='The Economics of Circular Tourism', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5008', name='Sustainable Heritage Management', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF3090', name='Research Methods For Education', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF5130', name='Public Health Approaches to the End of Life', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF5157', name='Cognitive Science, Learning and Pedagogy', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF3095', name='Building Sustainable Learning Settings', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF5100', name='Critical Thinking and Communication', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5162', name='Leadership for Sustainability and Innovation in Tourism',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5133P', name='Dissertation MSc End of Life Studies', school=environmental, level=5,
                          credits=60)
    Module.objects.create(id='DUMF5131', name='Cultural Representations of Death and Dying', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF3048', name='SIS study abroad credits L3 sem 2', school=environmental, level=3,
                          credits=60)
    Module.objects.create(id='DUMF1076', name='Introduction to Sustainable Development', school=environmental, level=1,
                          credits=20)
    Module.objects.create(id='DUMF5117P', name='Environmental Science Dissertation (Nankai JGS)', school=environmental,
                          level=5, credits=60)
    Module.objects.create(id='DUMF2071', name='Biodiversity, Ecology and Ecosystems', school=environmental, level=2,
                          credits=20)
    Module.objects.create(id='DUMF2044', name='SIS study abroad credits L2 sem 2', school=environmental, level=2,
                          credits=60)
    Module.objects.create(id='DUMF4024', name='Sociology of Education', school=environmental, level=4, credits=20)
    Module.objects.create(id='DUMF5012', name='Tourism and Heritage Dissertation', school=environmental, level=5,
                          credits=60)
    Module.objects.create(id='DUMF1016', name='Professional Practice in Education 1', school=environmental, level=1,
                          credits=20)
    Module.objects.create(id='DUMF1074', name='Energy, Waste and Pollution: Options for Sustainability',
                          school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF2012', name='Mathematics - Theory And Pedagogy 2', school=environmental, level=2,
                          credits=20)
    Module.objects.create(id='DUMF2074', name='Perspectives on the Environment', school=environmental, level=2,
                          credits=20)
    Module.objects.create(id='DUMF2078', name='Environmental Communication and Behaviour Change', school=environmental,
                          level=2, credits=10)
    Module.objects.create(id='DUMF3016', name='Professional Practice in Education 3', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF4043', name='Environmental Field Course', school=environmental, level=4, credits=20)
    Module.objects.create(id='DUMF3086P', name='Placement', school=environmental, level=3, credits=60)
    Module.objects.create(id='DUMF3088', name='Enhanced Mathematics', school=environmental, level=3, credits=20)
    Module.objects.create(id='DUMF3080P', name='Environmental Placement', school=environmental, level=3, credits=60)
    Module.objects.create(id='DUMF5140', name='Research Design and Methods (Nankai)', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5159', name='Language Development', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF3047', name='SIS study abroad credits L3 sem 1', school=environmental, level=3,
                          credits=60)
    Module.objects.create(id='DUMF2081', name='Political Economy of Globalisation and Development',
                          school=environmental, level=2, credits=20)
    Module.objects.create(id='DUMF5114', name='Environmental Remote Sensing (Nankai)', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5158', name='Fundamentals of Reading: Planning, Instruction, and Assessment',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF4021', name='Professionalism and Leadership in Education', school=environmental,
                          level=4, credits=20)
    Module.objects.create(id='DUMF5143', name='Sustainable Tourism', school=environmental, level=5, credits=10)
    Module.objects.create(id='DUMF2035', name='Professional Practice in Education 2', school=environmental, level=2,
                          credits=10)
    Module.objects.create(id='DUMF2073', name='SIS Study Abroad Credits L2 Full Year', school=environmental, level=2,
                          credits=120)
    Module.objects.create(id='DUMF1073', name='Water, Natural Hazards and Resilience', school=environmental, level=1,
                          credits=20)
    Module.objects.create(id='DUMF5129', name='Assisted Dying: Rhetorics and Reality', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5150', name='End of Life Challenges and Palliative Care', school=environmental,
                          level=5, credits=10)
    Module.objects.create(id='DUMF5161', name='Innovation and Technology in Sustainable Tourism', school=environmental,
                          level=5, credits=10)
    Module.objects.create(id='DUMF5096', name='Social Science Research Methods', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5108', name='Ecology, Environment and Conservation', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5121', name='Introduction to Environmental Impact Assessment (Nankai)',
                          school=environmental, level=5, credits=15)
    Module.objects.create(id='DUMF5060', name='Environmental Ethics and Behaviour Change', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF2011', name='Literacy 2', school=environmental, level=2, credits=20)
    Module.objects.create(id='DUMF5151P', name='Study Abroad (WBL) PGT', school=environmental, level=5, credits=60)
    Module.objects.create(id='DUMF5102', name='Tourism Marketing', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF3091', name='SIS Study Abroad Credits L3 Full Year', school=environmental, level=3,
                          credits=120)
    Module.objects.create(id='DUMF5135', name='Risk and Resilience of Land and Water', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF3033', name='Rural Tourism And Stewardship', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF1075', name='People, Power and Place', school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF1071', name='Discovering Scotland\'s Past', school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF4046P', name='Honours Action Research Project II', school=environmental, level=4,
                          credits=60)
    Module.objects.create(id='DUMF3096', name='Art, Ideas, and Communication', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF5174', name='Smart Tourism and Heritage', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5105P', name='Events Management', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF4008P', name='Environmental Stewardship Project', school=environmental, level=4,
                          credits=60)
    Module.objects.create(id='DUMF1064', name='Philosophy 1', school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF2080', name='Terrestrial Environment: Pollutants and Processes', school=environmental,
                          level=2, credits=20)
    Module.objects.create(id='DUMF5156', name='Taxonomy and population monitoring', school=environmental, level=5,
                          credits=40)
    Module.objects.create(id='DUMF4010P', name='Honours Dissertation - Primary Education', school=environmental,
                          level=4, credits=40)
    Module.objects.create(id='DUMF5034', name='A Cultural History Of Animals', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5075', name='Environmental Politics and Society', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF2079', name='Global Perspectives on Health and Human Development',
                          school=environmental, level=2, credits=20)
    Module.objects.create(id='DUMF5018', name='Tourism And Regional Development', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF5164', name='Perspectives on Power and Professional Practice', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF3087P', name='Placement (International)', school=environmental, level=3, credits=60)
    Module.objects.create(id='DUMF5079', name='Environmental Communication', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF2024', name='Research Methods For Environmental Scientists', school=environmental,
                          level=2, credits=20)
    Module.objects.create(id='DUMF5109', name='Professional Enquiry', school=environmental, level=5, credits=30)
    Module.objects.create(id='DUMF4044', name='Honours Action Research Project I', school=environmental, level=4,
                          credits=60)
    Module.objects.create(id='DUMF5116', name='Understanding Environmental Change (Nankai)', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF5128', name='Theory, Methods, and Ethics in End of Life Research',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5171', name='Integrated Coastal Ecosystem Dynamics', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF2075', name='Introduction to GIS', school=environmental, level=2, credits=20)
    Module.objects.create(id='DUMF5138', name='Principles of Environmental Risk and Management', school=environmental,
                          level=5, credits=20)
    Module.objects.create(id='DUMF5163', name='Evaluating Educational Change', school=environmental, level=5,
                          credits=20)
    Module.objects.create(id='DUMF4050', name='Professional Skills in Environmental Science', school=environmental,
                          level=4, credits=20)
    Module.objects.create(id='DUMF5126', name='Global Challenges and Dilemmas in End of Life Care',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF1072', name='Introduction to Rural Entrepreneurship', school=environmental, level=1,
                          credits=10)
    Module.objects.create(id='DUMF2072', name='Leadership and Teamworking', school=environmental, level=2, credits=20)
    Module.objects.create(id='DUMF5137', name='Research Methods in Environmental Risk and Management',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5160', name='The Science of Reading', school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5111', name='Understanding Learning And Teaching', school=environmental, level=5,
                          credits=30)
    Module.objects.create(id='DUMF3001', name='Applied Ecology & Conservation', school=environmental, level=3,
                          credits=20)
    Module.objects.create(id='DUMF2077', name='Politics and the Environment', school=environmental, level=2, credits=10)
    Module.objects.create(id='DUMF5078', name='Dissertation', school=environmental, level=5, credits=60)
    Module.objects.create(id='DUMF1043', name='Earth System Science', school=environmental, level=1, credits=20)
    Module.objects.create(id='DUMF3085', name='Inclusion and ASN: Concepts, Policy & Practice', school=environmental,
                          level=3, credits=20)
    Module.objects.create(id='DUMF5081', name='Reading the Environment: Old and New World Romanticisms',
                          school=environmental, level=5, credits=20)
    Module.objects.create(id='DUMF5112', name='Learning And Teaching In The Primary Curriculum', school=environmental,
                          level=5, credits=30)
    Module.objects.create(id='DUMF3007P', name='Dissertation 3', school=environmental, level=3, credits=60)
    Module.objects.create(id='DUMF4016', name='Professional Practice in Education 4', school=environmental, level=4,
                          credits=40)
    Module.objects.create(id='DUMF1012', name='Literacy 1', school=environmental, level=1, credits=20)

    # School of Social and Political Sciences (489 modules)
    Module.objects.create(id='CEES1015', name='CEES 1A: Central and Eastern Europe in the Age of Stalin',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='CEES5092', name='Colonialism in comparative perspective: Post-Soviet Eurasia',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5015P', name='MSc Dissertation Project (Russian and East European Studies)',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='CEES2010', name='CEES 2A: Post-communist Russia and the Former Soviet Union',
                          school=politics, level=2, credits=20)
    Module.objects.create(id='CEES5017P', name='MSc Social Science Research (Dissertation)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='CEES5055', name='Russian For Social Scientists (Intermediate)', school=politics, level=5,
                          credits=40)
    Module.objects.create(id='CEES4003',
                          name='The rise and fall of Communism in Central Europe 1945-89: a socio-economic perspective',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES2011', name='CEES 2B: Central and South-East Europe after Communism', school=politics,
                          level=2, credits=20)
    Module.objects.create(id='CEES5090', name='Designing your Security & Area Studies Research Proposal',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES4060', name='Social History and Cultural Politics', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='CEES5076', name='Russian for Social Scientists Intermediate Semester 2', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES4082', name='The International Politics of Post-Soviet Central Asia', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='CEES3012', name='The Russian Revolutions of 1917', school=politics, level=3, credits=20)
    Module.objects.create(id='CEES4041',
                          name='Perspectives on Security in Cold War Central and Eastern Europe (1945-1989)',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES5073', name='CEERES Methodologies Summer School', school=politics, level=5, credits=0)
    Module.objects.create(id='CEES5093',
                          name='Mandatory language course for Russian, East European and Eurasian Studies',
                          school=politics, level=5, credits=40)
    Module.objects.create(id='CEES5023', name='Statehood and Nationality in Russia, Central and Eastern Europe',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5016P', name='MSc Dissertation Project (Central & East European Studies)',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='CEES5062', name='Rethinking Central Asian Security', school=politics, level=5, credits=20)
    Module.objects.create(id='CEES3027', name='Quantitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='CEES4014',
                          name='Cultural Politics and Social Diversity in Contemporary Russia and Post-Socialist Europe',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES5063', name='Geopolitics of Central Europe (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='CEES4079', name='Russian Foreign Policy', school=politics, level=4, credits=20)
    Module.objects.create(id='CEES4094', name='Russian Politics and Society', school=politics, level=4, credits=20)
    Module.objects.create(id='CEES3030',
                          name='(De)constructing Yugoslavia: migrants, refugees, and diasporas 1918-2008 (level 3)',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='CEES4040',
                          name='Nationalism, State Consolidation and the Politics of Identity in Post-Communist Europe',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES5059', name='Russian Foreign Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='CEES4011', name='Post Soviet Russia: Renegotiating Global, National and Local Identities',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES5083', name='Yugoslavia and After: Themes and Controversies', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES4043', name='European Integration and Politics of Central & Eastern Europe',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES4097',
                          name='(De)constructing Yugoslavia: migrants, refugees, and diasporas 1918-2008',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES4016P', name='Dissertation', school=politics, level=4, credits=40)
    Module.objects.create(id='CEES5084', name='Russian Politics and Society', school=politics, level=5, credits=20)
    Module.objects.create(id='CEES4091',
                          name='War and Revolution: an International History of the Balkans 1804-2012, CEES honours',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES3028', name='Qualitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='CEES4074', name='Qualitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='CEES1016', name='CEES 1B: Communism and its Collapse', school=politics, level=1,
                          credits=20)
    Module.objects.create(id='CEES4099', name='Soviet Disunion: Nationalities Issues in the USSR', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='CEES4102', name='Warfare and Armed Conflict in the former Soviet Union', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='CEES4100', name='Energy, politics and society in Eurasia', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='CEES5078', name='The International Politics of Post-Soviet Central Asia [Nankai]',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5086', name='War-making and Peace-making in the former Soviet Union', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES5075', name='Russian for Social Scientists Beginners Semester 2', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES5061', name='The Geopolitics of Central Europe', school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5082', name='Russia, China, and international politics of Eurasia', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES4059', name='The Russian Revolutions Of 1917', school=politics, level=4, credits=20)
    Module.objects.create(id='CEES4073', name='Quantitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='CEES3033', name='Soviet Disunion: Nationalities Issues in the USSR (L3)', school=politics,
                          level=3, credits=20)
    Module.objects.create(id='CEES5065', name='Contemporary Challenges in Eastern Europe, Russia and Eurasia',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5088', name='Europe-Russia Relations since the Collapse of the USSR', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES5009', name='Hungarian For Social Scientists', school=politics, level=5, credits=40)
    Module.objects.create(id='CEES5077', name='CEERES International Master 3rd Mobility', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='CEES5094',
                          name='Mandatory language course for Russian, East European and Eurasian Studies Semester 2',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5041P', name='RCEES International Masters Dissertation', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='CEES3023', name='European integration and politics of Central & Eastern Europe',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='CEES4098', name='Russia, China, and international politics of Eurasia', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='CEES3029',
                          name='Perspectives on Security in Cold War Central and Eastern Europe (1945-1989)',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='CEES5060',
                          name='Media and Democratisation in Central and Eastern Europe and the Former Soviet Union',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='CEES5054', name='Russian For Social Scientists (Beginners)', school=politics, level=5,
                          credits=40)
    Module.objects.create(id='CEES5087', name='Energy, politics and society in Eurasia', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='CEES3010',
                          name='Nationalism, State Consolidation, Politics of Identity in Post-Communist Europe',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='CEES4101',
                          name='From Hope to Confrontation: Relations between Europe and Russia since the Collapse of the USSR',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='CEES5079', name='Russian for Social Scientists Advanced Semester 2', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='CEES5072P', name='Central and East European, Russian and Eurasian Studies Dissertation',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='CEES5080', name='Russian For Social Scientists (Advanced)', school=politics, level=5,
                          credits=40)
    Module.objects.create(id='ESH4079', name='Sexualities and Social Control, c.1885- c.1980', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4055', name='World War II: Economy and Society', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4086', name='Oral History for Social Scientists', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4088', name='The British Empire and India, 1757-1947', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH5069', name='Decolonisation & International Economic Relations', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='ESH4090', name='Themes and Debates in Economic and Social History', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='ESH4048', name='Families, society and the state in Britain, c. 1750 - 1914',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='ESH1002', name='Economic & Social History 1B: Themes in Globalisation, 1914-c2008',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='ESH4033', name='International Economic Relations since 1931', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4013', name='British Economic Policy 1945-51: The Labour Governments', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='ESH4011', name='Scotland Since 1914', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4077', name='Youth Culture, Deviance and Society', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4082', name='Cuba: Resilient Revolution', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH3003', name='Economic & Social History 3: Studies in Economic and Social History',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='ESH3001', name='Economic & Social History 3: Research Methods In Econ & Social History A',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='ESH4093', name='Black British History', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH1001',
                          name='Economic & Social History 1A: Economic and Social History in Global Contexts, ca. 1750-1914',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='ESH4029', name='Innovations in Western Medicine: Social Origins & Cultural Impacts',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4078', name='Latin America in the 20th century', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4002P', name='Dissertation', school=politics, level=4, credits=40)
    Module.objects.create(id='ESH2001', name='Economic & Social History 2A: Britain 1770-1914', school=politics,
                          level=2, credits=20)
    Module.objects.create(id='ESH4080', name='Science, Technology, and Medicine in the Modern Middle East',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4092', name='British Capitalism and its Discontents', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4006', name='Industry and Innovation: International Perspectives', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='ESH4074',
                          name='The Globalisation of Stuff: The Making, Trading, and Meaning of Everyday and Treasured Things',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='ESH5068', name='Inequalities in the Global Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='ESH4053', name='Work & Labour in Britain Since 1940', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4089', name='Colonialism, Capitalism and Environmental Movements since the 1960s',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='ESH4084', name='Money and Finance in United States\' Society, 1880-2020', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='ESH4076', name='Medicine & the State in Modern Britain', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH5071', name='Development and the Global South: African Experiences since 1945',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='ESH3002',
                          name='Economic & Social History 3: Research Methods in Economic and Social History B',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='ESH5060', name='Latin American Development from Independence to the Present',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='ESH5066', name='Corporate Social Responsibility in the Global Economy', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='ESH4010P', name='Researching Economic And Social History 2', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4087', name='Global South Asia', school=politics, level=4, credits=20)
    Module.objects.create(id='ESH5020', name='Studies In The History Of Medicine From 1850 To 2000', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='ESH5070', name='Sports in the Global Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='ESH2002', name='Economic & Social History 2B: Britain Since 1914', school=politics,
                          level=2, credits=20)
    Module.objects.create(id='ESH4009', name='Researching Economic And Social History 1', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4094', name='Money and Economy Making in African History', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='ESH4091', name='Motherhood and Maternity in 20th-Century Britain', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='MODLANG5022', name='Czech for Social Scientists Beginners Semester 2', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC4175', name='The Politics of Immigration', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4186', name='Texts and Contexts in the History of Political Thought',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5092', name='Regional Economic Integration and Organisations (REIO)',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC4156', name='Politics of the Middle East', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC3016', name='Scottish Politics', school=politics, level=3, credits=20)
    Module.objects.create(id='POLITIC5102', name='Social Justice Activism in the Information Age', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC4013', name='Latin American Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4176', name='International Relations Concepts', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5065', name='International Relations Theory', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5074', name='Humanitarian Intervention: Civilian or Sovereignty', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC5105', name='Global Development and Human Rights', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC3019', name='Qualitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='POLITIC4124', name='Chinese Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4160', name='International Political Economy', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4149', name='Authoritarianism: Concepts, Theories and Comparative Analysis',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4170', name='Post-colonial and De-colonial International Theory', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='POLITIC5079', name='International Relations and Development', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC5012', name='Political Institutions And Communication', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4015', name='Political Parties, Instituions and Society', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5078', name='International Relations Theory (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4187', name='Defying Dictators:Political Opposition in Authoritarian States',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4130', name='The European Union and International Relations', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='POLITIC5007', name='Human Rights And Global Politics', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4022', name='Scottish Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC2002', name='Politics 2B: Introduction to Comparative Politics', school=politics,
                          level=2, credits=20)
    Module.objects.create(id='POLITIC4131', name='Civil Society and Social Capital: Comparative Perspectives',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC3023', name='Feminist Perspectives on Politics', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='POLITIC5099', name='Globalisation: Challenges from the South', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4090', name='Comparative European Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5020', name='China\'s International Politics', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4158', name='US Foreign Policy', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC3024', name='Politics and Social Media', school=politics, level=3, credits=20)
    Module.objects.create(id='POLITIC4119', name='Politics and Social Media', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4189', name='Dissertation Preparation', school=politics, level=4, credits=0)
    Module.objects.create(id='POLITIC5014P', name='Postgraduate Dissertation (Politics)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='POLITIC4179', name='Politics and Popular Culture', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4172', name='Politics of Terror', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4010', name='Issues In International Relations', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC1001', name='Politics 1A: Introduction to Politics', school=politics, level=1,
                          credits=20)
    Module.objects.create(id='POLITIC5011', name='Media And Democracy', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC3020', name='Politics 3: Issues in British Politics', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='POLITIC4017P', name='Politics Dissertation', school=politics, level=4, credits=40)
    Module.objects.create(id='POLITIC4005', name='Government and Public Policy in the UK', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4184', name='The Psychology of Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5110', name='The Ethics of War and Peace', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC4192', name='African Politics in Global Perspective', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4188', name='Elections and Voters', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4161',
                          name='Protest Politics in a Post-Political Age: Reform, Resistance or Revolution?',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4154', name='Global Distributive Justice', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4020', name='Politics Of The European Union', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4004', name='Issues in Comparative Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5111', name='Global Social Movements', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5001', name='Conflict Analysis', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC4185', name='The Politics of Borders', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4164', name='China\'s International Relations', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5093', name='International Relations of the Middle East', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC5100', name='Media and Conflict in Divided Societies', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4182', name='Comparative Perspectives on Populism', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4033', name='Citizenship And Democracy', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4002', name='British Prime Ministers since 1945', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5108', name='Political Economy of the Media', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5084', name='Strategy, Defence and International Relations', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC2001', name='Politics 2A: History Of Political Thought', school=politics, level=2,
                          credits=20)
    Module.objects.create(id='POLITIC4102', name='Politics, Communication and Democracy', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4082', name='Gender and International Development', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4104', name='Feminist Perspectives on Politics', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4171', name='International Organizations', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4128', name='Social Movements', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4190', name='Challenges to Democracy', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4138', name='Qualitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5109', name='Research Design for Politics and International Relations',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5077', name='Comparative European Politics (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4183', name='Contemporary Challenges in Politics', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4122', name='Global Inequality and International Development', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='POLITIC1002', name='Politics 1B: Introduction to International Relations',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='POLITIC4155', name='Narratives of War and Conflict', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4140', name='War and International Security', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4103', name='International Political Communication', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4133', name='Radical Politics: Marx, Marxism and Anarchism', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='POLITIC5017', name='The Internet and Civil Society', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC4191', name='Good Government and its Corruption', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC5103', name='Climate, Energy and International Relations', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC5004',
                          name='Introduction to Human Rights Theories and Politics: A Critical Perspective',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5085', name='Gender, Race and International Relations', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC5081', name='International Organisations', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5086', name='Politics and Society in Southern Europe', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4147',
                          name='The Politics of Conflict and Insecurity: Narratives and Counter-narratives',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC3025', name='International Political Communication', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='POLITIC4137', name='Quantitative Methods in the Social Sciences', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='POLITIC4008', name='Human Rights In Global Perspective', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4168', name='Global Energy Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4123', name='Egalitarianism and its Critics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4162', name='Intergroup Conflict and Reconciliation', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4009', name='Issues In British Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5101', name='Political Economy of Conflict', school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5087', name='Southern Europe in International Affairs', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4019P', name='Politics Independent Research Paper', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4001', name='American Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5009', name='International Security and Strategic Studies', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='POLITIC3018', name='Quantitative Methods in the Social Sciences', school=politics,
                          level=3, credits=20)
    Module.objects.create(id='POLITIC4146', name='Comparative Public Opinion', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5069', name='International Security and International Relations', school=politics,
                          level=5, credits=30)
    Module.objects.create(id='POLITIC4007', name='Global Environmental Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC4159', name='Business and Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='POLITIC5107', name='Propaganda and Public Diplomacy: Authoritarian States',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='POLITIC5106', name='Communist Regimes and their Societies', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='POLITIC4153', name='Securitisation and the New Security Agenda', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='POLITIC4174', name='Visual Global Politics', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4037', name='Education For Citizenship', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4041', name='Work, Welfare and the Politics of Reform', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3014', name='Introduction to the Fundamentals of Transport Studies',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='PUBPOL4025', name='Quantitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL4029', name='Health and Health Inequalities - A Policy Context', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='PUBPOL4042', name='Youth, Policy and Welfare: Cross-Cultural Perspectives',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4026', name='Qualitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3015', name='Health and Health Inequalities - A Policy Context', school=politics,
                          level=3, credits=20)
    Module.objects.create(id='PUBPOL4001P', name='Dissertation', school=politics, level=4, credits=40)
    Module.objects.create(id='PUBPOL2010',
                          name='Social and Public Policy 2A: Perspectives on Public Policy - Conflicting Ideas and Changing Agendas',
                          school=politics, level=2, credits=20)
    Module.objects.create(id='PUBPOL4035', name='Utopias: Welfare Theory and Social Policies for a \'Good Society\'',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL1010', name='Social and Public Policy 1A: Foundations of Welfare', school=politics,
                          level=1, credits=20)
    Module.objects.create(id='PUBPOL4030', name='Housing: Policy, Welfare and Markets', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3016', name='Work, Welfare and the Politics of Reform', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='PUBPOL4043', name='Urban Economy', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4028', name='Disability And Society', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4038', name='Active Citizenship', school=politics, level=4, credits=40)
    Module.objects.create(id='PUBPOL4046', name='Environmental and Climate Justice', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3010', name='Quantitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='PUBPOL4045', name='Policy, Inclusive Economies, and Society', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3018', name='Making Public Policy in the Real World', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='PUBPOL2011', name='Social and Public Policy 2B: Policy, Politics and Power',
                          school=politics, level=2, credits=20)
    Module.objects.create(id='PUBPOL4044', name='Big Data, Policy & Power', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4048', name='Scotland\'s Policy Landscape', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL1011',
                          name='Social and Public Policy 1B: Understanding Glasgow in a Globalised World',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='PUBPOL3011', name='Qualitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='PUBPOL4040', name='Making Public Policy in the Real World', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='PUBPOL3017', name='Youth, Policy and Welfare: Cross-Cultural Perspectives',
                          school=politics, level=3, credits=20)
    Module.objects.create(id='PUBPOL4031', name='Ideological Concepts and Values', school=politics, level=4, credits=20)
    Module.objects.create(id='PUBPOL4034', name='Remaking Cities in a Global Age: Dilemmas of Urban Policy',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='RUSSIAN5029', name='Russian for Social Scientists Post- Intermediate Semester 2',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5024', name='Globalisation and the Nation State', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS1006', name='Nankai and Glasgow Joint Graduate School Summer School', school=politics,
                          level=1, credits=0)
    Module.objects.create(id='SPS5040P', name='GLOCAL Dissertation', school=politics, level=5, credits=60)
    Module.objects.create(id='SPS5030P', name='Global Migrations and Social Justice Dissertation /Project',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='SPS5025P', name='Independent Study and Work Placement Portfolio (Security)',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='SPS4011', name='Art and Science of Surveys: Designing Questions and Analysing Data',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5008', name='Media, War and Security', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS4006P', name='Social Inequality in Education', school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5070', name='Understanding Society: Critical Social Research 1', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='SPS5036', name='Introduction To Social Theory For Researchers', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5016', name='The Globalised Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5058P', name='MEDIA CULTURE & SOCIETY INDEPENDENT RESEARCH PROJECT', school=politics,
                          level=5, credits=60)
    Module.objects.create(id='SPS5007', name='Thematic Issues in Global Security', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5012', name='Labour and the Global Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5059P', name='MEDIA CULTURE & SOCIETY DISSERTATION', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SPS5061', name='Diversity of Entrepreneurships: Gender, SMEs, Immigrants and Ethnicities',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5062', name='Quantitative Data Analysis 2', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS4013', name='The John Smith Youth Poll Project', school=politics, level=4, credits=20)
    Module.objects.create(id='SPS1010',
                          name='Does Scotland need Human Rights? Mobilising for Change with Civil Society (C4L)',
                          school=politics, level=1, credits=10)
    Module.objects.create(id='SPS1009',
                          name='Intercultural Understanding and Emotional Resilience in Times of Uncertainty',
                          school=politics, level=1, credits=10)
    Module.objects.create(id='SPS5026', name='European and International Security Strategies', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5042', name='Qualitative Research Methods', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5041', name='Research Design', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5073', name='Working with Secondary Data: Data Project 1', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='SPS5019', name='Understanding Health Policy (10 credit)', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='SPS5034', name='Research Design', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5018', name='The Wealth of Nations', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS2001', name='QM2 - Analysing Your Social World', school=politics, level=2, credits=20)
    Module.objects.create(id='SPS5004', name='Business in the Global Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS1001', name='QM1 - Measuring Your Social World (C4L)', school=politics, level=1,
                          credits=20)
    Module.objects.create(id='SPS4005', name='Measurement and Scaling', school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5066', name='Designing your Global Economy Research Project', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5056',
                          name='Transformations in Media, Culture and Society 2: Contemporary Debates and Issues',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SPS4003', name='Research Design and Method Selection', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SPS4012',
                          name='Multilevel and Network Analysis in Social, Educational & Public Health Research',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SPS4009', name='Socialism: A global history', school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5037', name='Qualitative Research Methods', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5072', name='Working with Digital Data: Data Project 2', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='SPS5022', name='Improving Health and Society: Programme Development and Evaluation',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5010P', name='MSc Dissertation Project (Global Economy)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SPS4004',
                          name='Advanced Regression: Limited and Categorical Dependent Variable Regression',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5045', name='Business and Government in the Global Economy', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5001', name='Global Health in Social Context', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS3002', name='Scotland and the 2014 Independence Referendum (Summer School course)',
                          school=politics, level=3, credits=10)
    Module.objects.create(id='SPS5060', name='Themes in the Global Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5069', name='Business in Times of Global Instability', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS3009E', name='Data visualization - Graphics for Impact', school=politics, level=3,
                          credits=5)
    Module.objects.create(id='SPS5068',
                          name='Transformations in Media, Culture and Society 1: Theoretical, Empirical and Conceptual Approaches',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5013', name='Understanding Health Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5015', name='Technology Transfer in the Global Economy', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5038', name='Global Varieties of Capitalism', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5021', name='Globalisation Of International Banking And Finance', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='SPS4008', name='West European Relations with Central and East Europe from Détente to EU',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5067', name='Global Development, Taxation and Finance', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5006P', name='Global Security Dissertation', school=politics, level=5, credits=60)
    Module.objects.create(id='SPS5031P', name='Dissertation in International Relations (Nankai)', school=politics,
                          level=5, credits=60)
    Module.objects.create(id='SPS5043', name='Nankai and Glasgow Joint Graduate School Summer School', school=politics,
                          level=5, credits=0)
    Module.objects.create(id='SPS3004', name='Urban Economy', school=politics, level=3, credits=20)
    Module.objects.create(id='SPS5023', name='Methods of Social Research', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5071', name='Understanding Data: Critical Social Reseach 2', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5027P', name='Independent Study Portfolio (Security)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SPS5047', name='Innovation in the Middle East and North Africa', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS5020', name='Globalisation of the World Economy (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SPS4010', name='Longitudinal and Non-Linear Modelling for Social Scientists',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SPS5017', name='Health and Culture', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5033', name='Quantitative Data Analysis', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5057', name='MEDIA, CULTURE & MEMORY', school=politics, level=5, credits=20)
    Module.objects.create(id='SPS5029', name='Research Design and Methods (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO5127',
                          name='Equitable and Just Digital Society: Developing Interdisciplinary Skills and Knowledge',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5124', name='PGT Research Design in Practice', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4147', name='Critical Approaches to Cultural Production', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO4136',
                          name='Aftermath of Atrocity: Social Sciences Perspectives on Political Violence and Justice',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4056', name='General Paper In Sociology', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO2021', name='Sociology 2B', school=politics, level=2, credits=20)
    Module.objects.create(id='SOCIO4125', name='Gender and Migration', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5122', name='Media Research Methods', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5092', name='Writing News', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5090', name='Racial Justice and the City', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO3022', name='Qualitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='SOCIO4112',
                          name='\'Freedom Now\': a historical sociology of black liberation in the USA, 1954-80',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4040', name='Sociology Of Gender', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4113', name='Sociology of the City', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5084', name='Gender Relations (Contemporary Critical Approaches)', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='SOCIO5105P', name='Digital Society (MSc) - Independent Study Portfolio', school=politics,
                          level=5, credits=60)
    Module.objects.create(id='SOCIO5081', name='Producing News', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4129', name='Bureaucracy and Violence', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4060', name='Understanding And Explaining Crime', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO2020', name='Sociology 2A', school=politics, level=2, credits=20)
    Module.objects.create(id='SOCIO4069', name='Sociology of Health and Illness', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4140',
                          name='Youth and Young Adulthood in Contemporary Society: Cultures, Transitions and Inequalities',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4014', name='Global Civil Society And Human Rights', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO4131', name='Media in Africa', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5107', name='Journalism and Global Change 5', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5111', name='Violence, Victimisation, and Social Harm', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO5118', name='Rethinking Justice', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4118', name='The State, Institutions and Policy: a Political Sociology Approach',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5023', name='Religion In Society', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5088', name='A Public Social Science for Social Justice.', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO4141', name='Spatialities of Crime and Justice', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO5126', name='Global Borders & Border Crossings', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO4070', name='Punishment and Society', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5104', name='Digital Societies - The Living Lab', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO4003', name='Anthropology of Religion', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4047',
                          name='Contemporary Debates in Media Sociology: Audiences, Publics & Digital Media',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5001', name='Crime, Media And Popular Culture', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO3021', name='Quantitative Methods in the Social Sciences', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='SOCIO5080', name='Media, Communications and Journalism: Criticism and Theory',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO1010', name='Sociology 1B: Critical Research in Contemporary Societies',
                          school=politics, level=1, credits=20)
    Module.objects.create(id='SOCIO4095', name='Quantitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO5100', name='Diaspora: The Experience of Migration, Displacement and Difference',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO3020', name='Sociology 3: Social Theory (Non-Honours)', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='SOCIO5116', name='Criminal Justice and Injustice', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5019', name='Punishment and In/justice', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5091', name='Media and Journalism in the Global South', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO4023', name='Sexualities', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5021', name='Racism And Capitalist Modernity', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5106', name='Migration, Settlement and Belonging', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO5071P', name='MSc Dissertation Project (Sociology)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SOCIO4144',
                          name='Exploring the sociology of mental distress and neurodiversity: Where\'s your head at?',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4008P', name='Dissertation in Sociology', school=politics, level=4, credits=40)
    Module.objects.create(id='SOCIO4142', name='Criminology, climate change and the environment', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO4127', name='Ways of Living: Studying Different Worlds', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO5099P', name='MSc Dissertation Project (Global Health)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SOCIO4105', name='Class and the Making of Modern Britain', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO1009', name='Sociology 1A: Self and Society', school=politics, level=1, credits=20)
    Module.objects.create(id='SOCIO4097', name='Understanding Empire: Imperialism and the Modern World',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5115', name='Contemporary Issues in Policing', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5082', name='Researching Audiences and Media Representations', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='SOCIO4139', name='Leisure and Society', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4119', name='Pervasive Punishment: In/justice and penal control', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO4071', name='Global Health, Local Healing', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4057', name='Substantive Topics in the Sociology of Consumption', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO5093P', name='Media, Communications and International Journalism Project',
                          school=politics, level=5, credits=60)
    Module.objects.create(id='SOCIO4110', name='Youth, Gangs, and Globalisation', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4146', name='Embodiment and Inequalities: Bodies at the Margins', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO5025', name='Sexualities And Society', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4108', name='Migration, Settlement and Intimacy', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO4126', name='Sociology of Cognition: How Do We Know What We Know?', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO5112', name='Social Media, Disinformation and Democracy', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO5089', name='Global Migrations: Histories, Structures, Experiences.',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5075', name='Class and Stratification', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4099', name='Sociological Alternatives: Ways to Change the World', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO4091', name='Class and Everyday Life', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4037', name='Sociology Of Consumption: Historical And Theoretical Perspectives',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4107', name='Contemporary Migration in Global Perspective', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO4090', name='Social Theory (Hons)', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5073', name='Current Issues in Social Theory', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5070P', name='MSc Dissertation Project (Criminology)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='SOCIO5108', name='Sociology of Culture', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4134', name='Gender and Nationalism', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5032', name='Criminological Theory in Context', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4096', name='Qualitative Methods in the Social Sciences', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO5031', name='The Disabling Society', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4138', name='Sociology of Reproduction', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4130', name='Disabling worlds: Exploring disability in the global north and south',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4115', name='Defamiliarising the Familiar: The Sociology of Zygmunt Bauman',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4124', name='Crime, Violence, and Social Control in Africa', school=politics,
                          level=4, credits=20)
    Module.objects.create(id='SOCIO4004', name='Black Radical Social Thought', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4137', name='Sociology of Poetry', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5119', name='Gender diversity', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5117', name='Crime, Control and the City', school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4123', name='Ethno-Graphing Race and Racism', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5103', name='Digital Society-Theory and Substantive Issues', school=politics,
                          level=5, credits=20)
    Module.objects.create(id='SOCIO4122', name='Religions on the Move: Comparative Perspectives on Religion',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4121', name='Digital Society: Digital Technology, Inequality and Culture',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO5102', name='Practicing Research and Working with Data in the Digital Age',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5123',
                          name='Platform Praxis: Sociology of Culture, Practice, and Deviance in the Digital Age',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO4128', name='Prisons and beyond: The sociology of \'total\' institutions',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4046',
                          name='Sociology Of Media: Issues Of Production, Information Supply And Content',
                          school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4148', name='Sociology of Revolution', school=politics, level=4, credits=20)
    Module.objects.create(id='SOCIO4133', name='Glasgow: Capitalism, Class and Resistance', school=politics, level=4,
                          credits=20)
    Module.objects.create(id='SOCIO5121E',
                          name='Equitable and Just Digital Society: Developing Interdisciplinary Skills and Knowledge.',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='SOCIO5120', name='Contemporary Perspectives on Justice', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='SOCIO4145', name='Science, Technology and the Body', school=politics, level=4, credits=20)
    Module.objects.create(id='URBAN5100',
                          name='Real Estate Institutions and Markets (Glasgow-Nankai Joint Graduate School)',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5092', name='Understanding Housing Markets', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5086', name='Housing Contexts', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5093', name='Understanding Public Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5106', name='Reflective Practice in Housing', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5114', name='Principles and Applications of GIS (10 credits)', school=politics,
                          level=5, credits=10)
    Module.objects.create(id='URBAN5128', name='Private Rented Sector', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5048', name='Strategic Real Estate Management', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5140', name='The Wellbeing Economy', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5160', name='Advanced Topics for Urban Analytics', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5130', name='Management of Housing Businesses', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5148', name='Place Adaptation and Green Infrastructure', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5118', name='Urban Conservation', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5146', name='Inclusive Cities', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5039', name='Real Estate Markets', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5142', name='Researching Public Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5010', name='Designing Resilient Places', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5158', name='Planning Theory and Values', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5157', name='Planning Systems and Procedures', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5136', name='Migration Policy Making', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5040', name='Real Estate Valuation and Appraisal (20)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5145', name='Global Urban Challenges (10)', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5112', name='Community Empowerment and Engagement', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='SPS3003', name='Researching the City: Spatial Approaches', school=politics, level=3,
                          credits=20)
    Module.objects.create(id='URBAN5137', name='Co-creating Urban Futures: Citizen Participation in Local Governance',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5156', name='Integrative City Planning Lab', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5125', name='Big Data, AI & Urban Analytics', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5050', name='Design Governance', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5104', name='Global Cities (Nankai)', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5143', name='Contemporary Questions in Real Estate', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5103', name='Statistical Methods for Transport Planning', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5153', name='Sustainable Energy Landcapes', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5080P', name='MSc Dissertation Project (Urban Studies)', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='URBAN5154', name='Sustainable Real Estate Investment', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5102', name='Understanding Transport Choices', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5090', name='Global Urban Challenges', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5099',
                          name='City Planning Theory and Practice (Glasgow-Nankai Joint Graduate School)',
                          school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5083', name='Evidence, Evaluation and Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5131', name='International Housing Policy', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5147', name='International Residential Real Estate', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5155', name='Applied Built Environment Research', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5135', name='Researching Public Policy', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5095', name='Housing, Inequality and Society (10 credit)', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5026', name='International Real Estate Markets', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5151', name='Smart Cities and Infrastructure', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5152', name='Southern Urbanism', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5149', name='Planning for Just Transitions', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5123', name='Programming Tools for Urban Analytics', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5144', name='Digital Planning Systems and Tools', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5159', name='Real Estate Valuation and Appraisal (10)', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5097', name='Sustainable Housing Development (10 Credits)', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5046', name='Sustainable Spatial Strategies Lab', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5098', name='Urban Design and Development (Nankai)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5141', name='Homelessness: Problems, perceptions and policies', school=politics,
                          level=5, credits=10)
    Module.objects.create(id='URBAN5116', name='Sustainable Urban Futures (10)', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5105P', name='Dissertation in Urban & Regional Planning (Nankai)', school=politics,
                          level=5, credits=60)
    Module.objects.create(id='URBAN5124', name='Urban Analytics Group Project', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5101', name='Fundamentals of Transport Studies', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5129', name='Housing Policy Contrasts across a Devolved UK', school=politics,
                          level=5, credits=10)
    Module.objects.create(id='URBAN5087', name='Housing, Inequality and Society', school=politics, level=5, credits=20)
    Module.objects.create(id='URBAN5038', name='Real Estate Finance and Investment', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5111', name='Principles and Applications of GIS', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5037', name='Economics of Planning and Development Lab', school=politics, level=5,
                          credits=10)
    Module.objects.create(id='URBAN5027', name='Scottish Housing Law', school=politics, level=5, credits=10)
    Module.objects.create(id='URBAN5127', name='Quantitative Data Analysis (Semester 1)', school=politics, level=5,
                          credits=20)
    Module.objects.create(id='URBAN5150P', name='Real Estate and Planning Major Resarch Project', school=politics,
                          level=5, credits=60)
    Module.objects.create(id='URBAN5054P', name='Real Estate and Planning Dissertation', school=politics, level=5,
                          credits=60)
    Module.objects.create(id='URBAN5115', name='Development Appraisal for Real Estate Surveyors', school=politics,
                          level=5, credits=10)

    # Short Courses (356 modules)
    Module.objects.create(id='ADED12099', name='German in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11833', name='Get Ready for Norwegian Post Beginners A2', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11242', name='Learn to paint in a week', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11842', name='Get Ready for Swedish Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11844', name='Get Ready for Arabic Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11993', name='Glasgow\'s art collections: paintings', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED2070E', name='French upper intermediate B2', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED2067', name='Italian Language and Culture (Intermediate B2)', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED11427', name='A history of Italy', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2074', name='More German Language and Culture B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11841', name='Get Ready For Spanish Post-Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11740E', name='German beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11967E',
                          name='Light and shade: the architecture of 19th, 20th and 21st century Glasgow',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11407E', name='Access to Higher Education: Classical Studies', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED12007E', name='Introduction to short story writing: getting started',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11781', name='British Sign Language unit 3', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11987E', name='Introduction to art psychotherapy (online)', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11692', name='Printmaking: an introduction', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED3024E', name='Handwritten Egyptian: from cursive hieroglyphs to hieratic (online)',
                          school=short_courses, level=3, credits=20)
    Module.objects.create(id='ADED11416E', name='Access to Higher Education: Politics', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11477', name='Five famous Scots', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11880', name='Get Ready For Spanish Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12061E', name='The Irish Revolution: From Home Rule to Independence, 1885-1925',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12000E', name='The ancient Celtic world (online)', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11847', name='Get Ready for Gaelic Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED1616E', name='Understanding archaeology', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED1053E', name='Introduction to ancient Egypt 1B', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11742E', name='German improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11978', name='Mary Magdalene: her life and legacy', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11709E', name='Swedish improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11873', name='Get Ready for French Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11747E', name='Italian improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11824', name='Get Ready for Arabic Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11418E', name='Access to Higher Education: Scottish History', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED11732E', name='French post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11436', name='Secession and political independence in the 20th century',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11878', name='Get Ready for Portuguese Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11868', name='More Italian Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12093', name='Catalan in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11428', name='For King and Covenant', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED1005E', name='Ancient Egyptian temples', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12066', name='More Norwegian Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11711E', name='Arabic post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12053E', name='Five Artists: Portraiture', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11866', name='More French Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12022E', name='Feminist Philosophies: an introductory guide', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11812', name='More reading in Latin', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED1170E', name='Ancient Egyptian archaeology - people and places 1B',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2056', name='Spanish Language and Culture (Intermediate B2)', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED12013E', name='Introduction to Sociology', school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED2017E', name='Life and culture in ancient Egypt', school=short_courses, level=2,
                          credits=40)
    Module.objects.create(id='ADED11636', name='Wire jewellery: an introduction to techniques', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11611', name='El Greco to Goya: Spanish painting in focus', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED1020E', name='COSCA Counselling Skills', school=short_courses, level=2, credits=40)
    Module.objects.create(id='ADED11442', name='Introduction to art history', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11719E', name='Gaelic beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12052E', name='Five Artists: Landscapes', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11476', name='A history of Spain', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11694E', name='Classical Roman civilisation 1B', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11984E', name='Continental perspectives on truth: Nietzsche, Bergson and Deleuze',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11849', name='Get Ready For Italian Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12074', name='Italian in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11874', name='Get Ready For German Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11422', name='More Reading in Ancient Egyptian 2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11626E', name='Scotland in ten buildings', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11977', name='Walking the cemeteries and crematoria of Glasgow', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED1059E', name='Introduction to social psychology', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11845', name='Get Ready for Dutch Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11552',
                          name='The madwoman in the attic talks back: Kate Chopin, Virginia Woolf and Jean Rhys',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11467E', name='From antiquity to late Medieval art', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12005E', name='Introduction to novel writing: getting started', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11846', name='Get Ready for French Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11380', name='Working with trauma', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11516E', name='Archaeology of medieval and post medieval Scotland',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11240', name='Introduction to painting techniques', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11907E', name='Philosophy of the self', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11999E', name='Peoples of ancient and early medieval Scotland (online)',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11734E', name='French lower intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11743E', name='German lower intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11212', name='More reading in ancient Egyptian', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11469E', name='Northern Renaissance art', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED11548', name='Introduction to Landscape Painting', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11622', name='Studies in Latin literature in translation: exploring Roman culture',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11708E', name='Swedish post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11454E', name='Slavery in the Americas', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED9756E', name='Accelerated Level 5 Maths', school=short_courses, level=9, credits=15)
    Module.objects.create(id='ADED11848', name='Get Ready for German Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11425E', name='American politics in the 21st century', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12043E', name='Understanding Autism', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11478', name='Four poems by Kathleen Jamie', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11704E', name='Spanish intermediate B1+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11521E', name='Classical Roman civilisation 1A', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11372', name='Introducton to Fiction Writing', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11966E',
                          name='Introduction to Creative Writing: Poetry in response to online art, ekphrasis',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11484', name='Our fragile Earth', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11815', name='Neurocinematics and the psychology of film', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11741E', name='German post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11973E', name='An introduction to the British manor house', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED12063E', name='Five Artists: Myths and Legends', school=short_courses, level=1,
                          credits=5)
    Module.objects.create(id='ADED11334', name='Topics in Psychology', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2085E', name='Intermediate Creative Writing', school=short_courses, level=2,
                          credits=20)
    Module.objects.create(id='ADED12020E', name='Introduction to writing creative personal essays',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11881', name='Get Ready for Swedish Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11736E', name='Japanese beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11289E', name='Scotland after the Union 1707-1838', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED2061', name='French language and culture (Intermediate B2)', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED11789E', name='Introduction to R', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11420E', name='Access to Higher Education: Sociology', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED12071', name='Applied Sport and Exercise Psychology', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11816E', name='Access to Higher Education: Archaeology', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED11744E', name='German intermediate B1+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11348', name='Writing Fiction: One week course', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11520E', name='Ancient Egypt and the Bible', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11817E', name='Access to Higher Education: Geology', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11337', name='Starting Creative Writing', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11410E', name='Access to Higher Education: History of Art', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED11858', name='Get Ready for Swedish Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11230', name='Drawing and painting 1', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2065E', name='German upper intermediate B2', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED12017E', name='Reading classic short stories from the 19th Century',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12082', name='Spanish in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11863', name='More Spanish Intermediate B1+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11367E', name='Introduction to contemporary Scottish fiction', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11784', name='The artist: rebel, mystic and social conscience', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED1007E', name='Ancient Egyptian texts 1B', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2050E', name='Intermediate hieroglyphs', school=short_courses, level=2, credits=20)
    Module.objects.create(id='ADED11877', name='Get Ready for Norwegian Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11721E', name='Portuguese beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11720E', name='Gaelic post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11715E', name='Russian improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2075', name='More Italian Language and Culture B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11472', name='Great art collections 2', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11862', name='More Italian Intermediate B1+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED2052E',
                          name='Level 2 Politics: Nationalism, democracy and self-determination since the French Revolution',
                          school=short_courses, level=2, credits=20)
    Module.objects.create(id='ADED11258', name='Existentialism: Nietzsche and Sartre', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED3021E', name='Writing Fiction: Advanced Techniques', school=short_courses, level=3,
                          credits=40)
    Module.objects.create(id='ADED11728E', name='Norwegian beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11507', name='Walks around Glasgow, series 2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11988E', name='Art psychotherapy: practice and theory (online)', school=short_courses,
                          level=1, credits=40)
    Module.objects.create(id='ADED11571', name='The Earth\'s Resources', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11241', name='Istanbul - a short survey of its art and architecture',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11856', name='Get Ready for Russian Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12079', name='Polish in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11421E', name='Access to Higher Education: Theology and Religious Studies',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11834', name='Get Ready for Polish Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11713E', name='Russian beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11276', name='Road to war: the rise of Hitler and Appeasement 1918-1939',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11852', name='Get Ready for Modern Greek Improvers A2+', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11869', name='More Japanese Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12081', name='Russian in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11288E', name='Scotland 1567-1707', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12031E', name='Introduction to Psychology', school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11965E', name='Introduction to writing from real life, memoir and autofiction',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11404', name='An introduction to portrait drawing in a week', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11970E', name='The American presidency: the Biden administration',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11406E', name='Access to Higher Education: Chemistry', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11696E', name='Scotland into the modern age: 1837-1952', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11860', name='More French Intermediate B1+', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED12078', name='Norwegian in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED1091E', name='Scottish 19th century painting', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11390E', name='Constable to Cézanne: Painting in Britain and France 1800-1900',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11248', name='The art collectors and patrons of Glasgow', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12038E', name='Women artists in Europe c.1890 - c.2000', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11733E', name='French improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11971E', name='The Irish Revolution 1912-1925', school=short_courses, level=1,
                          credits=5)
    Module.objects.create(id='ADED11700E', name='Spanish beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12098', name='Gaelic in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11703E', name='Spanish lower intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED2040E', name='Coptic Language and Lives, Level 2', school=short_courses, level=2,
                          credits=40)
    Module.objects.create(id='ADED11901', name='Archaeology and art: exploring creativity through the past',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2079', name='More Italian Upper Intermediate B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11505', name='Magic in ancient Greece and Rome', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11409E', name='Access to Higher Education: English Literature', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED11429', name='A history of modern terrorism: \'the infernal machine\', 1800 onwards',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11473E', name='Scotland in the Middle Ages 1124 - 1371', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11830', name='Get Ready For Japanese Post-Beginners A2', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12033', name='General English beginners A1', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11568E', name='Twentieth century philosophy: the dawn of analysis',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12004E', name='Introduction to writing poetry', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED1069E', name='Literature of the Ancient Near East', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12092', name='Arabic in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED1006E', name='Ancient Egyptian texts 1A', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11831', name='Get Ready for Mandarin Post Beginners A2', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11714E', name='Russian post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2073', name='More French Language and Culture B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11745E', name='Italian beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11975E', name='An introduction to Evolutionary Psychology', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED11278', name='Scottish Rebels, Radicals and Revolutionaries 1780-1914',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2043E', name='The art of the ancient Near East', school=short_courses, level=2,
                          credits=40)
    Module.objects.create(id='ADED2071', name='More French Advanced C1', school=short_courses, level=2, credits=0)
    Module.objects.create(id='ADED2084E', name='Virtual reality in psychological research', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED11417E', name='Access to Higher Education: Psychology', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11383', name='Geology in the Field', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11236', name='Hepworth to Hockney: British art 1930s-1960s', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12095', name='Dutch in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12054E', name='Introductory Calculus for Science', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED12026E', name='Short introduction to writing flash fiction', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED11730E', name='Norwegian improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11818E', name='Cognitive psychology: an introduction', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12015E', name='Reading modern Gothic Horror writing', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11737E', name='Japanese post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11266', name='West End Lectures', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11717E', name='Dutch post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11619', name='Sylvia Plath and Ted Hughes: The poetry behind the myth',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11980E', name='The Scottish Gothic: fantastic and supernatural', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED1004E', name='Ancient Egyptian art', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11739E', name='Japanese lower intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12001E', name='The early medieval Celtic world (online)', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11829', name='Get Ready For Italian Post-Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11851', name='Get Ready for Mandarin Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11985E', name='Access to Higher Education: Business and Management',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11557', name='The Russian Revolution', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11960E', name='British Sign Language Unit 4 Conversation Class', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED11906E', name='Danish Beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12035', name='General English improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12067', name='More Russian Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED2068E', name='Italian advanced C1', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED11686', name='Geology and the landscape', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED12060E', name='Ireland through Union, Rebellion and Famine 1798-1885',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED1026E', name='Dutch 17th century painting', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED12024E', name='Forensic Psychology: an Introduction (International Summer School)',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11426E', name='Scotland under the early Stewart kings 1371-1603',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11724E', name='Mandarin beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11854', name='Get Ready for Polish Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11405E', name='Access to Higher Education: Biology', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11716E', name='Dutch beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11969E', name='Exploring Scotland\'s slavery past in 5 locations',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED2057E', name='General English upper intermediate B2', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED11231', name='Drawing and Painting 2', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11731E', name='French beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11726E', name='Modern Greek beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11701E', name='Spanish post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12023E',
                          name='How to be more rational: critical thinking, logic and reasoning (International Summer School)',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11828', name='Get Ready for German Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11780', name='British Sign Language unit 2', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11702E', name='Spanish improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11437', name='Walks around Glasgow 1', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11749E', name='Italian intermediate B1+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11825', name='Get Ready for Dutch Post-Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11270', name='A History of Greece', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2062E', name='French advanced C1', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED2059E', name='Spanish upper intermediate B2', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED12051E', name='Swedish Intermediate B1+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11707E', name='Swedish beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11567E',
                          name='Souls, minds and matter: An introduction to the philosophy of human nature',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12072E', name='Catalan Beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11879', name='Get Ready for Russian Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11474', name='18th century Scotland', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED12036', name='General English lower intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12003E', name='Introduction to writing fiction: novel and short story',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11243', name='Learn to draw in a week', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11415E', name='Access to Higher Education: Physics', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED12064E', name='Five Artists: Still Life', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED12065', name='General English Intermediate B1+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11839', name='Get Ready Portuguese Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11779', name='British Sign Language Unit 1', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED2058E', name='General English advanced C1', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED11850', name='Get Ready For Japanese Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11853', name='Get Ready for Norwegian Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11827', name='Get Ready for Gaelic Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12083', name='Swedish in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11514E', name='The history and mystery of psychogeography', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11239', name='Introduction to drawing techniques', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11998E', name='Celtic art and architecture (online)', school=short_courses, level=1,
                          credits=5)
    Module.objects.create(id='ADED12027E', name='Ways of Looking at Western Art (International Summer School)',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11981E', name='Scotland and Europe: historical literary dialogues',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11257', name='Environmental Ethics: right and wrong in the age of climate crisis',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11408E', name='Access to Higher Education: Economics', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED12062E', name='A History of Northern Ireland, 1921-1998', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11509', name='Poetic themes: an introduction to poetry in English',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11564', name='An art revolution in Europe', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2066E', name='Italian upper intermediate B2', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED12016E', name='Reading contemporary Gothic Horror writing', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED12096', name='Estonian in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11098E', name='Introduction to creative writing: the novel', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED2088E', name='Intermediate life writing, memoir and autofiction',
                          school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED12080', name='Portuguese in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12040E', name='Short Introduction to Writing Crime Fiction', school=short_courses,
                          level=1, credits=5)
    Module.objects.create(id='ADED12070E', name='Estonian Beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12097', name='French in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED2049E', name='Caravaggio to Velázquez: Baroque art in southern Europe',
                          school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED11515E', name='Archaeology of prehistoric and Roman Scotland', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED11794E',
                          name='How to be more rational: an introduction to logic and systematic reasoning',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12041E', name='Short Introduction to Writing Historical Fiction',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED12057E', name='Reconstruction and the birth of Jim Crow America, 1865-1877',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED2072', name='More Spanish Advanced C1', school=short_courses, level=2, credits=0)
    Module.objects.create(id='ADED11974E', name='Women artists in Europe c.1400-c.1890', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11861', name='More German Intermediate B1+', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11785', name='British design from the Great Exhibition to the Festival of Britain',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11989E', name='Continental perspectives on truth: Nietzsche, Bergson and Deleuze',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11566E',
                          name='Morality, nature and beauty: An introduction to the philosophy of value',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11887', name='Forensic Psychology: an introduction', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12042E', name='Understanding ADHD', school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11386E', name='Creative drawing and painting: developing skills and techniques',
                          school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED2076', name='More Spanish Language and Culture B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11448E', name='Child development: an introduction', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED12037', name='Walking Glasgow\'s Libraries', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11840', name='Get Ready for Russian Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11413E', name='Access to Higher Education: Medieval European History',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED12049E', name='Norwegian Lower Intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11712E', name='Arabic improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11832', name='Get Ready for Modern Greek Post Beginners A2', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11244', name='Milan and Mantua - a short survey of their art and architecture',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED12068', name='More Swedish Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12077', name='Modern Greek in 5 weeks: an introduction', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12002E',
                          name='Introduction to writing creative non-fiction: from memoir to personal essay',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED12012E', name='Introduction to Politics', school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED12094', name='Danish in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11738E', name='Japanese improvers A2+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11777E', name='Polish beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED12075', name='Japanese in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11843', name='Get Ready for Turkish Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12019E', name='Reading contemporary short stories from the 21st Century',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED12034', name='General English post beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11875', name='Get Ready For Italian Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12006E', name='Introduction to novel writing: keeping going', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED2078', name='More German Upper Intermediate B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED2086E', name='Intermediate short story writing', school=short_courses, level=2,
                          credits=10)
    Module.objects.create(id='ADED11419E', name='Access to Higher Education: Social and Economic History',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED11414E', name='Access to Higher Education: Philosophy', school=short_courses, level=1,
                          credits=20)
    Module.objects.create(id='ADED11857', name='Get Ready For Spanish Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11699E', name='The 1989 European revolutions', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11326', name='Introducing Geology', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11876', name='Get Ready For Japanese Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED12069', name='More Swedish Intermediate B1+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11452', name='Creative writing: workshop', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11826', name='Get REady for French Post Beginners A2', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11455E', name='A history of the western seaboard of Scotland', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED2063', name='French Language and Culture (Intermediate B2)', school=short_courses,
                          level=2, credits=0)
    Module.objects.create(id='ADED11368E', name='Introduction to the short story', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11746E', name='Italian post-beginners A2', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11748E', name='Italian lower intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED1057E',
                          name='What is consciousness? An introduction to the philosophy of mind and cognitive science',
                          school=short_courses, level=1, credits=20)
    Module.objects.create(id='ADED2087E', name='Intermediate novel writing:getting to the end', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED2089E', name='Art of the 20th Century', school=short_courses, level=2, credits=10)
    Module.objects.create(id='ADED11786', name='The Hunterian Art Gallery collection', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11735E', name='French intermediate B1+', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11870', name='More Spanish Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11627', name='Palaces of industry: Explore Glasgow\'s industrial architecture',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED11979', name='Exploring the Dead Sea Scrolls', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11855', name='Get Ready for Portuguese Improvers A2+', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12010E', name='Hitler\'s lightning war: the Battle for France, 1940',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11412E', name='Access to Higher Education: Mathematics', school=short_courses,
                          level=1, credits=20)
    Module.objects.create(id='ADED11612', name='Studies in ancient Egyptian literature in translation: life in letters',
                          school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED2077', name='More French Upper Intermediate B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED11710E', name='Arabic beginners A1', school=short_courses, level=1, credits=10)
    Module.objects.create(id='ADED11867', name='More German Lower Intermediate B1', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED12059E', name='Northern Ireland since the Peace Process, 1998 to present day',
                          school=short_courses, level=1, credits=5)
    Module.objects.create(id='ADED11690', name='Five Masters: 19th century', school=short_courses, level=1, credits=0)
    Module.objects.create(id='ADED12076', name='Mandarin in 5 weeks: an introduction', school=short_courses, level=1,
                          credits=0)
    Module.objects.create(id='ADED11982E', name='Scotland and Europe: modern literary dialogues', school=short_courses,
                          level=1, credits=10)
    Module.objects.create(id='ADED2080', name='More Spanish Upper Intermediate B2', school=short_courses, level=2,
                          credits=0)
    Module.objects.create(id='ADED2064', name='German Language and Culture (Intermediate B2)', school=short_courses,
                          level=2, credits=10)
    Module.objects.create(id='ADED12050E', name='Russian Lower Intermediate B1', school=short_courses, level=1,
                          credits=10)
    Module.objects.create(id='ADED11872', name='Get Ready For Arabic Lower Intermediate B1', school=short_courses,
                          level=1, credits=0)
    Module.objects.create(id='ADED11859', name='Get Ready for Turkish Improvers A2+', school=short_courses, level=1,
                          credits=0)

    # Student Learning Development (8 modules)
    Module.objects.create(id='EDUC1127', name='Introduction to Communicating as a Scientist',
                          school=student_learning_development, level=1, credits=10)
    Module.objects.create(id='EDUC1128', name='Introduction to Criticality', school=student_learning_development,
                          level=1, credits=5)
    Module.objects.create(id='EDUC1136', name='Writing Across Times, Topics and Theories: Rhetoric, Power and Science',
                          school=student_learning_development, level=1, credits=20)
    Module.objects.create(id='EDUC1116E', name='Rationality and Scientific Debates',
                          school=student_learning_development, level=1, credits=5)
    Module.objects.create(id='EDUC1130',
                          name='Theory for the Terrified: Understanding and Using Critical Theory in an Academic Context',
                          school=student_learning_development, level=1, credits=10)
    Module.objects.create(id='EDUC51056',
                          name='Investigating Academic Writing: A Linguistic Analysis of Academic Writing as a Genre',
                          school=student_learning_development, level=5, credits=10)
    Module.objects.create(id='EDUC1117', name='History of Argumentation', school=student_learning_development, level=1,
                          credits=5)
    Module.objects.create(id='EDUC1119', name='Understanding Academic Writing in Context',
                          school=student_learning_development, level=1, credits=5)

    print(f'Created {Module.objects.count()} modules')
    print('Creating admin/superuser account...')
    # tier 1 admin
    superuser = User.objects.create_superuser(
        username='admin',
        email='admin@gla.ac.uk',
        password='AdminPass123!',
        first_name='Database',
        last_name='Administrator',
    )


    # tier 2 moderator
    print('Creating moderator account...')
    mod1 = User.objects.create_user(
        username='moderator1',
        email='mod1@gla.ac.uk',
        password='ModPass123!',
        first_name='John',
        last_name='Moderator',
        role='moderator',
    )

    # tier 3 student
    print('Creating student account...')
    student1_user = User.objects.create_user(
        username='student1',
        email='student1@gla.ac.uk',
        password='StudentPass123!',
        first_name='Alice',
        last_name='Student',
        role='student',
    )

    student1 = Student.objects.create(
        user=student1_user,
        degree=degrees['G400'],
        graduation_year=2028,
        bio='Love coding and coffee!',
    )

    print("Done!")
    print(f"Schools: {School.objects.count()}")
    print(f"Degrees: {Degree.objects.count()}")
    print(f"Modules: {Module.objects.count()}")
    print(f"Accounts made: {User.objects.count()}")


if __name__ == '__main__':
    populate()