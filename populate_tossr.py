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
    computing = School.objects.create(name='School of Computing Science')
    psychology = School.objects.create(name='School of Psychology & Neuroscience')
    engineering = School.objects.create(name='James Watt School of Engineering')
    business = School.objects.create(name='Adam Smith Business School')
    cancer = School.objects.create(name='School of Cancer Sciences')
    veterinary = School.objects.create(name='School of Biodiversity, One Health & Veterinary Medicine')
    chemistry = School.objects.create(name='School of Chemistry')
    critical_studies = School.objects.create(name='School of Critical Studies')
    art = School.objects.create(name='School of Culture & Creative Arts')
    education = School.objects.create(name='School of Education')
    geography = School.objects.create(name='School of Geographical & Earth Sciences')
    health =School.objects.create(name='School of Health & Wellbeing')
    humanities = School.objects.create(name='School of Humanities | Sgoil nan Daonnachdan')
    infection = School.objects.create(name='School of Infection & Immunity')
    law = School.objects.create(name='School of Law')
    maths = School.objects.create(name='School of Mathematics & Statistics')
    medicine = School.objects.create(name='School of Medicine, Dentistry & Nursing')
    language = School.objects.create(name='School of Modern Languages & Cultures')
    bioscience = School.objects.create(name='School of Biosciences')
    physics = School.objects.create(name='School of Physics & Astronomy')
    environmental = School.objects.create(name='School of Social & Environmental Sustainability')
    politics = School.objects.create(name='School of Social & Political Sciences')
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



    # === MODULES ===
    maths1017 = Module.objects.create(
        id='MATHS1017', name='Mathematics 1',
        school=maths, level=1, credits=40
    )

    eng1021 = Module.objects.create(
        id='ENG1021', name='Electronic Engineering 1X',
        school=engineering, level=1, credits=20
    )

    accfin1003 = Module.objects.create(
        id='ACCFIN1003', name='Accounting',
        school=business, level=1, credits=20
    )

    eng1002 = Module.objects.create(
        id='ENG1002', name='Aerospace Engineering 1',
        school=engineering, level=1, credits=10
    )

    # === ADMIN ===
    User.objects.create_user(
        username='admin', password='admin123',
        first_name='John', last_name='Admin',
        email='admin@tossr.com',
        role='admin', is_staff=True, is_superuser=True
    )

    # === STUDENTS ===
    glasgow_student = Student.objects.create(
        user=User.objects.create_user(
            username='glasgow_student', password='test',
            first_name='Glasgow', last_name='Student',
            email='student@test.com',
            role='student'
        ),
        degree = degrees['N400'],
        graduation_year = 2030,
        bio='First year math student. test account'
    )
    StudentModule.objects.create(student=glasgow_student, module=maths1017)



    print("✅ Done!")
    print(f"Schools: {School.objects.count()}")
    print(f"Degrees: {Degree.objects.count()}")
    print(f"Modules: {Module.objects.count()}")
    print(f"Students: {Student.objects.count()}")


if __name__ == '__main__':
    populate()