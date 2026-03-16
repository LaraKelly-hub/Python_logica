
# O código tem o intuito de realizar manipulação de lista e dicionario como uma forma de gerenciar os funcionários 
# e seus dados.


# clase para gerenciar registro de funcionários e seus dados pessoais
class Dados_pessoais():
    lista_funcionario=[]
    dicionario={}

    def __init__(self,nome:str,idade:int):
          self._nome=nome
          self._idade=idade
      

    def registro(self):
        if  isinstance(self._nome,str):
          self.__class__.lista_funcionario.append(self._nome)
          return 'Funcionario registrado com sucesso.'
        else:
           return 'A variavél deve ser do tipo string.'

    
    def exibir(self):
    #  Exibir lista de funcionários
     if self.lista_funcionario:
      return f'Funcionarios registrados: {(self.__class__.lista_funcionario)}'
     
     else:
        return 'Lista sem registro.'

    
    def registro_completo(self):
      #  Adiciona nome e idade ao dicionário
       self.__class__.dicionario[self._nome]=self._idade
       return self.__class__.dicionario
   



if __name__=='__main__':

 funcionario01=Dados_pessoais('Lara',20)
 funcionario01.registro()
 print(funcionario01.registro_completo())
 print(funcionario01.exibir())

 funcionario2=Dados_pessoais('Maycon', 56)
 funcionario2.registro()
 print(funcionario2.registro_completo())
 print(funcionario2.exibir())
 


    
