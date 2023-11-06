import subprocess
import platform

os = platform.system()
if os == 'Windows':
    subprocess.call(["systeminfo", ">", "temp.txt"], shell=True)
    sysinfo = []
    with open("temp.txt", encoding='ANSI') as file:
        for line in file:
            sysinfo.append(line.replace('\x81', 'ue').replace('\x84', 'ae').replace('\x94', 'oe').replace('\x9A', 'Ue'))
    file.close()

    with open('systeminformationen.tex', 'w') as file:
        file.write('\\documentclass[a4paper,12pt]{scrartcl}\n')
        file.write('\\usepackage[utf8]{inputenc}\n')
        file.write('\\usepackage[ngerman]{babel}\n')
        file.write('\\usepackage[T1]{fontenc}\n')
        file.write('\\title{Systeminformationen}\n')
        file.write('\\date{\\today}\n')
        file.write('\\begin{document}\n')
        file.write('\\maketitle\n')
        file.write('{\\raggedright\n')
        file.write(sysinfo[1] + '{}'.format(r'\\')) # Hostname
        file.write(sysinfo[2] + '{}'.format(r'\\')) # Betriebssystemname
        file.write(sysinfo[3] + '{}'.format(r'\\')) # Betriebssystemversion
        file.write(sysinfo[4] + '{}'.format(r'\\')) # Betriebssystemhersteller
        file.write(sysinfo[6] + '{}'.format(r'\\')) # Typ des Betriebssystembuilds
        file.write(sysinfo[7] + '{}'.format(r'\\')) # Registrierter Benutzer
        file.write(sysinfo[9] + '{}'.format(r'\\')) # Produkt-ID
        file.write(sysinfo[12] + '{}'.format(r'\\')) # Systemhersteller
        file.write(sysinfo[13] + '{}'.format(r'\\')) # Systemmodell
        file.write(sysinfo[14] + '{}'.format(r'\\')) # Systemtyp
        file.write(sysinfo[15] + '{}'.format(r'\\')) # Prozessoren
        file.write(sysinfo[17] + '{}'.format(r'\\')) # BIOS-Version
        file.write(sysinfo[24] + '{}'.format(r'\\')) # Gesamter physischer Speicher
        file.write(sysinfo[25] + '{}'.format(r'\\')) # Verfügbarer physischer Speicher
        file.write('}')
        file.write('\n\\end{document}')
    file.close()

    subprocess.call(["pdflatex", "systeminformationen.tex"], shell=True)
    subprocess.call(["systeminformationen.pdf"], shell=True)
elif os == 'Darwin':
    print('Noch nicht implementiert')