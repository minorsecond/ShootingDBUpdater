import models
from sqlalchemy.orm import sessionmaker
import requests
import csv

csv_url = "https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv"

Session = sessionmaker(bind=models.engine)
session = Session()

existing_data = session.query(models.Shooting.id).all()

id_list = []
for row in existing_data:
    id_list.append(int(row[0]))

added_counter = 0
with requests.Session() as s:
    row_counter = 0
    download = s.get(csv_url)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    csv_list = list(cr)
    for row in csv_list:
        if row_counter >= 1:
            id = int(row[0])
            if id not in id_list:

                if row[1] == '':
                    name = None
                else:
                    name = row[1]

                if row[2] == '':
                    date = None
                else:
                    date = row[2]

                if row[3] == '':
                    manner_of_death = None
                else:
                    manner_of_death = row[3]

                if row[4] == '':
                    armed = None
                else:
                    armed = row[4]

                if row[5] == '':
                    age = None
                else:
                    age = row[5]

                if row[6] == '':
                    gender = None
                else:
                    gender = row[6]

                if row[7] == '':
                    race = None
                else:
                    race = row[7]

                if row[8] == '':
                    city = None
                else:
                    city = row[8]

                if row[9] == '':
                    state = None
                else:
                    state = row[9]

                if row[10] == "True":
                    somi = True
                else:
                    somi = False

                if row[11] == '':
                    threat_level = None
                else:
                    threat_level = row[11]

                if row[12] == '':
                    flee = None
                else:
                    flee = row[12]

                if row[13] == "True":
                    bc = True
                else:
                    bc = False

                if row[14] == '':
                    lon = None
                else:
                    lon = row[14]

                if row[15] == '':
                    lat = None
                else:
                    lat = row[15]

                if row[16] == "True":
                    true_geocode = True
                else:
                    true_geocode = False

                # Create new DB row

                if lat and lon:
                    new_row = models.Shooting(
                        id=id,
                        name=name,
                        date=date,
                        manner_of_death=manner_of_death,
                        armed=armed,
                        age=age,
                        gender=gender,
                        race=race,
                        city=city,
                        state=state,
                        signs_of_mental_illness=somi,
                        threat_level=threat_level,
                        flee=flee,
                        body_camera=bc,
                        geom=f'SRID=4326;POINT({lon} {lat})',
                        is_geocoding_exact=true_geocode
                    )

                else:
                    new_row = models.Shooting(
                        id=id,
                        name=name,
                        date=date,
                        manner_of_death=manner_of_death,
                        armed=armed,
                        age=age,
                        gender=gender,
                        race=race,
                        city=city,
                        state=state,
                        signs_of_mental_illness=somi,
                        threat_level=threat_level,
                        flee=flee,
                        body_camera=bc,
                        is_geocoding_exact=true_geocode
                    )
                session.add(new_row)
                added_counter += 1
                row_counter += 1
        else:
            row_counter += 1

print(f"Added {added_counter} rows to DB")
session.commit()
session.close()
