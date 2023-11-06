import subprocess
import platform

os = platform.system()
if os == 'Windows':
    data = subprocess.check_output(['systeminfo']).decode('cp437').replace('\r', '').strip().split('\n')
    # Falls andere Informationen benötigt werden, wanted_data erweitern oder kürzen
    wanted_data = ['Hostname', 'Betriebssystemname', 'Betriebssystemversion', 'Betriebssystemhersteller',
                'Typ des Betriebssystembuilds', 'Registrierter Benutzer', 'Produkt-ID', 'Systemhersteller',
                'Systemmodell', 'Systemtyp', 'Prozessor(en)', 'BIOS-Version', 'Gesamter physischer Speicher',
                'Verfügbarer physischer Speicher']
    sysinfo = {}
    # Wenn andere Informationen benötigt werden, muss auf Index von temp geachtet werden
    # Nicht jedes Element umfasst 2 Items
    for item in data:
        temp = item.split(':', 1)
        for val in wanted_data:
            if temp[0] == val:
                sysinfo[temp[0]] = temp[1]

    with open('systeminformationen.tex', 'w') as file:
        file.write('\\documentclass[a4paper,12pt,xcolor=dvipsnames]{scrartcl}\n') # A4 Format, Schriftgröße 12
        file.write('\\usepackage[utf8]{inputenc}\n')
        file.write('\\usepackage[ngerman]{babel}\n')
        file.write('\\usepackage[T1]{fontenc}\n') # Schriftart
        file.write('\\usepackage{tikz}\n')
        file.write('\\usepackage{xcolor}\n')
        file.write('\\usepackage{graphicx}\n') # Bilder einfügen
        file.write('\\usepackage{scrlayer-scrpage}\n')
        file.write('\\usepackage[doublespacing]{setspace}\n')
        file.write('\\newcommand{\\mybox}[1]{%\n') # Command für colored Box
        file.write('    \\tikz[baseline=(text.base)]\n')
        file.write('        {\\node [rounded corners,fill=cyan,draw=violet] (text) {#1};}%\n')
        file.write('}\n')
        #file.write('\\chead{\\includegraphics[scale=0.25]{image.jpg}\n') # SVLFG bei GoogleBilder 4 Reihe Nr2
        file.write('\\title{Systeminformationen}\n')
        file.write('\\date{\\today}\n')
        file.write('\\begin{document}\n')
        file.write('\\maketitle\n')
        file.write('\\raggedright\n')
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Hostname', sysinfo['Hostname'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Betriebssystemname', sysinfo['Betriebssystemname'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Betriebssystemversion', sysinfo['Betriebssystemversion'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Betriebssystemhersteller', sysinfo['Betriebssystemhersteller'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Typ des Betriebssystembuilds', sysinfo['Typ des Betriebssystembuilds'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Registrierter Benutzer', sysinfo['Registrierter Benutzer'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Produkt-ID', sysinfo['Produkt-ID'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Systemhersteller', sysinfo['Systemhersteller'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Systemmodell', sysinfo['Systemmodell'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Systemtyp', sysinfo['Systemtyp'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'Prozessor(en)', sysinfo['Prozessor(en)'], '}', r'\\'))
        file.write('\\mybox{}{}: {} {}{}\n'.format('{', 'BIOS-Version', sysinfo['BIOS-Version'], '}', r'\\'))
        file.write('\\mybox{}{}: {}{}\n'.format('{', 'Gesamter physischer Speicher', sysinfo['Gesamter physischer Speicher'], '}', r'\\'))
        file.write('\\mybox{}{}: {}{}\n'.format('{', 'Verfuegbarer physischer Speicher', sysinfo['Verfügbarer physischer Speicher'], '}'))
        file.write('\\end{document}')
    file.close()

    subprocess.call(["pdflatex", "systeminformationen.tex"], shell=True) # PDF erstellen
    subprocess.call(["systeminformationen.pdf"], shell=True) # PDF Öffnen
elif os == 'Darwin':
    print('Noch nicht implementiert')
