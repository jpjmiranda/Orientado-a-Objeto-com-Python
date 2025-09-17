from modelos.cardapio.item_cardapio import ItemCardapio 

class Prato(ItemCardapio):
    def __init__(self, nome, descricao, preco):
        super().__init__(nome, preco)
        self.descricao = descricao
