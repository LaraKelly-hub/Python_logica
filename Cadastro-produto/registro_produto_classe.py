dici = []

class CadastroProduto:

    @staticmethod
    def registra_pdt():

        quantidade = int(input("Quantos produtos deseja registrar? "))

        for n in range(quantidade):

            nome_produto = input("Nome do produto: ")

            try:
                preco = float(input("Preço do produto: "))
                quantidade_estoque = int(input("Quantidade em estoque: "))

            except ValueError:
                print("Informe dígitos numéricos!")
                continue

            produtos = {
                "Nome": nome_produto,
                "Preço": preco,
                "Estoque": quantidade_estoque
            }

            dici.append(produtos)

        total_estoque = 0

        print("\nProdutos cadastrados:")

        for produto in dici:
            print(produto["Nome"])
            total_estoque += produto["Preço"] * produto["Estoque"]

        produto_mais_caro = max(dici, key=lambda p: p["Preço"])

        print(f"\nProduto mais caro: {produto_mais_caro['Nome']}")
        print(f"\nValor total do estoque: {total_estoque:.2f} R$")


if __name__ == "__main__":
    CadastroProduto.registra_pdt()
