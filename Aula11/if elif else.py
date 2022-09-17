"""
Condições IF, ELIF, ELSE
"""

variavel1: bool = bool(True)
variavel2: bool = bool(True)
variavel3: bool = bool(True)
variavel4: bool = bool(True)
variavel5: bool = bool(True)
variavel6: bool = bool(True)

if variavel1:
    print('Vamos seguir')
    if variavel2:
        print('Vamos seguir')
        if variavel3:
            print('Vamos seguir')
            if variavel4:
                print('Vamos seguir')
                if variavel5:
                    print('Vamos seguir')
                    if variavel6:
                        print('Vamos seguir')
                    else:
                        print('Tenta denovo')
                else:
                    print('Tenta denovo')
            else:
                print('Tenta denovo')
        else:
            print('Tenta denovo')
    else:
        print('Tenta denovo')
else:
    print('Tenta denovo')
