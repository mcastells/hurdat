import hurdat

storms = hurdat.listFromFile('HURDATHurricaneTracks.txt')

n = 3
print(f'{len(storms)} storms recorded. Last {n} storms:')
for storm in storms[-n:]:
    print(f'\n{storm.id = }')
    print(f'{storm.name = }')
    print(f'{storm.record_count = }')
    for record in storm.records:
        print(f'\n{record.datetime.strftime("%c") = }')
        print(f'{record.year = }, {record.month = }, {record.day = }, {record.hour = }')
        print(f'{record.lat = }, {record.lon = }')
        print(f'{record.minpressure = }, {record.maxwspeed = }')
        #etc...