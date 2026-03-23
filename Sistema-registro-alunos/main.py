# SISTEMA DE NOTAS

dicionario_notas = []

# Função para registrar alunos
def registra_notas():
  
  # Loop com exceções para validar dados
  while True:
    try:
      qnt_alunos = int(input('Informe a quantidade de alunos que deseja cadastrar: '))
      if qnt_alunos > 0:
        break
      else:
        print('Informe um número maior que 0.')
    
    except ValueError:
      print('Informe um número inteiro.')
       
  # Cadastro de alunos
  for n in range(qnt_alunos):
    nome = input('Nome do aluno(a): ')

    # Validação de notas 
    while True:
      try:
        nota1 = float(input('Primeira nota: '))
        nota2 = float(input('Segunda nota: '))

        if nota1 < 0 or nota2 < 0:
          print('As notas devem ser positivas!')
          continue
        
        break

      except ValueError:
        print('A nota deve ser numérica!')

    # Dicionário para armazenar os dados
    alunos = {
      'Nome': nome,
      'Nota 1': nota1,
      'Nota 2': nota2
    }
    
    dicionario_notas.append(alunos)
  
  # Todos os alunos registrados
  print('\nAlunos cadastrados e suas respectivas notas:')
  for aluno in dicionario_notas:
    print(f'{aluno["Nome"]} - {aluno["Nota 1"]}, {aluno["Nota 2"]}')
    
  # Aprovados
  print('\nAlunos Aprovados')
  for aluno in dicionario_notas:
    media = (aluno['Nota 1'] + aluno['Nota 2']) / 2
    if media >= 7:
      print(f'{aluno["Nome"]} com média: {media:.1f}')
  
  # Reprovados
  print('\nAlunos reprovados')
  for aluno in dicionario_notas:
    media = (aluno['Nota 1'] + aluno['Nota 2']) / 2
    if media < 7:
      print(f'{aluno["Nome"]} - média {media:.1f}')
    

registra_notas()
