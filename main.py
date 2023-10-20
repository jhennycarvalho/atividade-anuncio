class Anuncio:
    def __init__(self, Titulo, Valor, textoAnuncio, NomeDeContato, Tel1, Tel2, Imagem, Data, obsTel):
        self.Titulo = Titulo
        self.Valor = Valor
        self.textoAnuncio = textoAnuncio
        self.NomeDeContato = NomeDeContato
        self.Tel1 = Tel1
        self.Tel2 = Tel2
        self.Imagem = Imagem
        self.Data = Data
        self.obsTel = obsTel

    def TotalizaAnuncios(self):
        total_anuncios = 10

        print(f"Total de anúncios: {total_anuncios}")

        resposta = input("Deseja mais informações sobre os anúncios? (y/n): ")
        if resposta.lower() == 'y':
            print("Aqui se encontram todos os  anúncios.")
        else:
            print(" Movimentação encerrada.")


class Secao:
    def __init__(self, Nome):
        self.Nome = Nome
        self.anuncios = []

    def TotalizaAnuncios(self):
        total_anuncios = len(self.anuncios)

        print(f"Total de anúncios na seção {self.Nome}: {total_anuncios}")

        resposta = input("Deseja visualizar os anúncios? (s/n): ")
        if resposta.lower() == 's':
            for anuncio in self.anuncios:
                print(f"Titulo: {anuncio.Titulo}, Valor: {anuncio.Valor}")
        else:
            print("Operação encerrada.")

    def adicionarAnuncio(self, anuncio):
        self.anuncios.append(anuncio)


class TipoDeAnuncio:
    def __init__(self, NomeDoAnuncio, QtndDePalavras, ComImagem, IdTipoAnuncio):
        self.NomeDoAnuncio = NomeDoAnuncio
        self.QtndDePalavras = QtndDePalavras
        self.ComImagem = ComImagem
        self.IdTipoAnuncio = IdTipoAnuncio
        self.anuncios = []

    def incluirTipoAnuncio(self, TipoAnuncio):
        novo_tipo = input("Digite o novo tipo de anúncio: ")
        print(f"Novo tipo de anúncio '{novo_tipo}' incluído.")

    def alterarTipoAnuncio(self, IdAnuncio, TipoAnuncio):
        novo_tipo = input(f"Digite o novo tipo de anúncio para o ID {IdAnuncio}: ")
        print(f"Tipo de anúncio para o ID {IdAnuncio} alterado para '{novo_tipo}'.")

    def consultarTipoAnuncio(self, TipoAnuncio):
        tipo = input("Digite o tipo de anúncio que deseja consultar: ")
        print(f"Consultando informações sobre o tipo de anúncio '{tipo}'...")

        for anuncio in self.anuncios:
            if anuncio.NomeDoAnuncio == tipo:
                print(f"Titulo: {anuncio.Titulo}, Valor: {anuncio.Valor}")

    def excluirTipoAnuncio(self, IdTipoAnuncio):
        print(f"Excluindo tipo de anúncio com ID {IdTipoAnuncio}...")


class Cliente:
    def __init__(self, NomeDoCliente, TelDoCliente, EmailCliente, Contribuidor):
        self.NomeDoCliente = NomeDoCliente
        self.TelDoCliente = TelDoCliente
        self.EmailCliente = EmailCliente
        self.Contribuidor = Contribuidor

    def incluirCliente(self):
        novo_nome = input("Digite o nome do novo cliente: ")
        novo_telefone = input("Digite o telefone do novo cliente: ")
        novo_email = input("Digite o email do novo cliente: ")
        novo_contribuidor = input("O cliente é um contribuidor? (s/n): ").lower() == 's'

        novo_cliente = Cliente(novo_nome, novo_telefone, novo_email, novo_contribuidor)
        print(f"Novo cliente '{novo_nome}' incluído.")
        return novo_cliente


# Exemplo 
anuncio1 = Anuncio("Venda de apartamento", 200000, "Apartamento em ótima localização", "Maria", "987654321", "123456789", "apartamento.jpg", "2023-10-22", "Nenhuma observação")
anuncio2 = Anuncio("Aluguel de escritório", 1500, "Escritório com 100m²", "José", "123456789", "987654321", "escritorio.jpg", "2023-10-23", "Inclui estacionamento")

secao_imoveis = Secao("Imóveis")
secao_imoveis.adicionarAnuncio(anuncio1)
secao_imoveis.adicionarAnuncio(anuncio2)

tipo_anuncio_imoveis = TipoDeAnuncio("Imóveis", 60, True, 2)
tipo_anuncio_imoveis.anuncios.extend([anuncio1, anuncio2])

cliente3 = Cliente("Pedro", "777777777", "pedro@example.com", True)
cliente4 = Cliente("Joana", "888888888", "joana@example.com", False)
novo_cliente = cliente4.incluirCliente()
