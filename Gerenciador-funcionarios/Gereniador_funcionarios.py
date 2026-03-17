ici=[]
class Cadastro_produto():
   

    def registra_Pdt():
        
        quantidade=int(input("Quantos produtos desejar registra? "))
        
        
        for n in range(quantidade):
            nome_produto=input('Nome do produto: ')

            try:
                preco=float(input('Preço do produto: '))
                quantidade_estoque=int(input('Quantidade em estoque: '))

            except ValueError:
                print('Informe dígitos númericos!')
                continue

            produtos={
            'Nome': nome_produto,
            'Preço': preco,
            'Estoque': quantidade_estoque
            }

            dici.append(produtos)
 
        
        total_estoque=0
        print('\nProdutos cadastrados: ')

        for produto in dici:
         print(f'{produto["Nome"]}')
         
         total_estoque+=produto["Preço"] *produto["Estoque"]
         produto_mais_caro=max(dici,key= lambda p: p['Preço'])
         
         
        print(f"\nProduto mais caro:\n{produto_mais_caro['Nome']}")
        print(f'\nValor total do estoque: {total_estoque:.1f}R$')
    
      

if _name_ == "_main_":
    n1=Cadastro_produto
    n1.registra_Pdt()
