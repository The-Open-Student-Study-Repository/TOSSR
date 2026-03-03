import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tossr.settings')
django.setup()

from accounts.models import User, Student
from modules.models import School, Degree, Module, StudentModule


def populate():
    print("Populating TOSSR...\n")
    """
    NOTE: I will intentionally leave out Computer Science and it's modules so that we can 
    use it for testing e.g. adding via admin panel.
    """
    # Clear existing
    User.objects.all().delete()
    School.objects.all().delete()

    # === SCHOOLS ===
    # computing = School.objects.create(name='School of Computing Science')
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
    # === DEGREES ===
    beng_aero_eng = Degree.objects.create(code='H415', degree_type='BEng', name='Aeronautical Engineering')
    beng_aero_eng.schools.add(engineering)

    meng_ese_eng = Degree.objects.create(code='HG66', degree_type='MEng', name='Electronic & Software Engineering ')
    meng_ese_eng.schools.add(engineering)

    bsc_acc_math = Degree.objects.create(code='NG4C', degree_type='BSc', name='Accounting & Mathematics')
    bsc_acc_math.schools.add(business, maths)

    bsc_math = Degree.objects.create(code='G100', degree_type='BSc', name='Mathematics')
    bsc_math.schools.add(maths)




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
        degree = bsc_math,
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