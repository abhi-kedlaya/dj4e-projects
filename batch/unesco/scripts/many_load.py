import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    
    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    count = 0;

    for row in reader:
#        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        nm = row[0]
        des = row[1]
        jst = row[2]
        yr = row[3]
        lon = row[4]
        lat = row[5]
        try:
            a = float(row[6])
        except:
            a = None

        s = Site(name=nm, year=yr, latitude=lat, longitude=lon , description=des, justification=jst , area_hectares=a, category=c, region=r, iso=i, state=s)
        #print(s)
        s.save()
