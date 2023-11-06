import subprocess


data = subprocess.check_output(['systeminfo']).decode('cp437').replace('\r', '').strip().split('\n')
sys_info = ['Hostname', 'Betriebssystemname', 'Betriebssystemversion', 'Betriebssystemhersteller',
            'Typ des Betriebssystembuilds', 'Registrierter Benutzer', 'Produkt-ID', 'Systemhersteller',
            'Systemmodell', 'Systemtyp', 'Prozessor(en)', 'BIOS-Version', 'Gesamter physischer Speicher',
            'Verfügbarer physischer Speicher']
sysinfo = {}
for item in data:
    key, value = item.split(':',1)
    for str in sys_info:
        if key == str:
            sysinfo[key] = value
print(sysinfo)