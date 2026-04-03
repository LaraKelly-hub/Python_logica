dici=[]

def registro_atendimento():
    #Lop para validar a entrada de dados
    while True:
     try:
      qnt=int(input('Deseja cadastra quantos atendimentos: '))

      if qnt <=0:
        print('Digite um número positivo.')
        continue
      
      else:
        break
     except ValueError:
       print('Informe um número!')

    # Lop para que o usúario informe a quantidade de atendimentos desejado
    for n in range(qnt):
      nome_cliente=input('Nome do cliente: ')
    
    # Lop while para validar os tipos de atendimentos, devermos ser vigorosos com os dados informados!
      while True:
       tipo=['Suporte','Reclamação','Dúvida']
       tipo_atendimento=input('O atendimento é Suporte, Reclamação ou Dúvida?  ')

       if tipo_atendimento.title() not in tipo:
         print('Informe um dos nossos serviços!')
         continue
       else:
         break
   
     


      while True:
        try:
          tempo_atendimento=int(input('Tempo de atendimento em minutos: '))
          if tempo_atendimento <=0:
            print('Informe um número inteiro!')
            continue

          else:
            break

        except ValueError:
          print('Você deve informe a quantidade de minutos em número! ')

      registro={
        'Nome': nome_cliente,
        'Tempo atendimento': tempo_atendimento,
        'Tipo atendimento': tipo_atendimento
      }
      
      dici.append(registro)
    
    # Cálculo da média
    soma=0
    for n in dici:
       soma+=n['Tempo atendimento']/len(dici)
       media=soma/len(dici)
    print(f'\nOs atendimentos levam {media:.0f} minutos em média. ')

    # Armazenamento de clientes com atendimento acima da média
    acima_media=[v['Nome'] for v in dici if v['Tempo atendimento'] > media ]
    print(f'Clientes com atendimento acima da média:\n{acima_media}')
    
    # Contagem automatizada
    contagem={}
    for item in dici:
      tipo_atnd=item['Tipo atendimento'].title()
      contagem[tipo_atnd] = contagem.get(tipo_atnd,0)+1
    
    print('\nQuantidade por atendimento')
    for tipo,quantidade in contagem.items():
      print(f'{tipo}: {quantidade}')


    maior=0
    nome=''
    for n in dici:
      if n['Tempo atendimento']>maior:
        maior=n['Tempo atendimento']
        nome=n['Nome']

    print(f'\nAtendimento mais demorado:\n{nome} - {maior} minutos')
  
   
  


registro_atendimento()
