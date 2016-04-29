from django.contrib.auth.models import User
from django.db import models


class StudentDetail(models.Model):
    '''
    It stores information about the Students of college.
    '''
    # List of courses
    BTECH = 'BTech'
    MCA = 'MCA'
    MBA = 'MBA'
    MTECH = 'MTech'
    OTHERS = 'OTHER'
    COURSE = (
        (BTECH, 'BTech'),
        (MCA, 'MCA'),
        (MBA, 'MBA'),
        (MTECH, 'MTech'),
        (OTHERS, 'Others'),
    )
    # List of branches
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    MT = 'MT'

    BRANCH = (
        ('AllBranches', 'None'),
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (EE, 'Electrical Engineering'),
        (ECE, 'Electronics and Communication Engineering'),
        (EEE, 'Electrical and Electronics Engineering'),
        (CE, 'Civil Engineering'),
        (IC, 'Instrumentation and Control Engineering'),
        (ME, 'Mechanical Engineering'),
        (MT, 'Manufacturing Technology'),
    )

    YEAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )


    SECTION = (
        ('AllSections', 'None'),
        ('CSE1','CSE1'),
        ('CSE2','CSE2'),
        ('IT1','IT1'),
        ('IT2','IT2'),
        ('ECE1','ECE1'),
        ('ECE2','ECE2'),
        ('EE1','EE1'),
        ('EE2','EE2'),
        ('CE1','CE1'),
        ('CE2','CE2'),
        ('ICE1','ICE1'),
        ('ICE2','ICE2'),
        ('MT1','MT1'),
        ('MT2','MT2'),
        ('ME1','ME1'),
        ('ME2','ME2'),
    )

    user = models.OneToOneField(User)
    course = models.CharField(max_length=5, choices=COURSE, default=None, null=True)
    branch = models.CharField(max_length=5, choices=BRANCH, default=None, null=True)
    year = models.PositiveIntegerField(null=True, blank=True, default=1)
    section = models.CharField(default=None, choices=SECTION, max_length=10, null=True)
    univ_roll_no = models.PositiveIntegerField(blank=True, null=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    display_to_others = models.BooleanField(default=True)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)
    # relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)

    def __unicode__(self):
        return self.user.username


class FacultyDetail(models.Model):
    '''
    It stores the information about the faculties/administration of college
    '''
    user = models.OneToOneField(User)
    designation = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    alternate_email = models.EmailField(max_length=254, blank=True, null=True)
    display_to_others = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)

    def __unicode__(self):
        return self.user.username

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name
