import hurdat

storms = hurdat.listFromFile('HURDATHurricaneTracks.txt')

n = 3
print(f'{len(storms)} storms recorded. Last {n} storms:')
for storm in storms[-n:]:
    print(f'\nstorm.id = {storm.id}')
    print(f'storm.name = {storm.name}')
    print(f'storm.record_count = {storm.record_count}')
    for record in storm.records:
        print(f'\nrecord.datetime.strftime("%c") = {record.datetime.strftime("%c")}')
        print(f'record.year = {record.year}, record.month = {record.month}, record.day = {record.day}, record.hour = {record.hour}')
        print(f'record.lat = {record.lat}, record.lon = {record.lon}')
        print(f'record.minpressure = {record.minpressure}, record.maxwspeed = {record.maxwspeed}')
        #etc...