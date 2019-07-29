def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v=int(input9(mensagem))
            if v >= minimo and v<= maximo:
                return v
            else:
                print('Digite um valor entre %d e %d' % (minimo, maximo))
        except:
            print('Você deve digitar um número inteiro')            