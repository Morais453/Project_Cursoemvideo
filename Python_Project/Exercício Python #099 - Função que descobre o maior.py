def maior(*i):
    m = 0
    print('Valores passados...')
    for c in i:
        print(c, end=' ')

    if len(i) > 0:
        for k,v in enumerate(i):
            if k == 0 or v > m:
                m = v
    print(f'Foram informados {len(i)} valores ao todo\n'
          f'O maior valor informado foi {m}')
    
maior(10,40,2,4,0)

maior(0,1,2,3)

maior()