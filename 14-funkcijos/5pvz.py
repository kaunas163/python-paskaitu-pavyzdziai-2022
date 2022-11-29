def pirma():
    print('pirmos funkcijos pradzia')
    print('pirmos funkcijos pabaiga')

def antra():
    print('antros funkcijos pradzia')
    pirma()
    print('antros funkcijos pabaiga')

pirma()
antra()