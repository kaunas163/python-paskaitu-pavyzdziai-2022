paieskos_fraze = 'SlaPtas'

if paieskos_fraze == 'slaptas':
    print('radome, case sensitive')
elif paieskos_fraze.lower() == 'slaptas':
    print('radome, case insensitive')
elif paieskos_fraze.lower() != 'slaptas':
    print('neradome')
