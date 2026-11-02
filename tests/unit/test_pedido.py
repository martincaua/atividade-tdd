
import pytest
from unittest.mock import MagicMock
from pedido.pedido import Item, Pedido
from pedido.pedido import Item, Pedido, contar_frete_gratis


# =============================================================
# EXEMPLO — teste pronto fornecido pela atividade
# =============================================================

def test_exemplo_quantidade_total(pedido_pequeno):
    # 1 café + 2 pães de queijo = 3 unidades
    assert pedido_pequeno.quantidade_total() == 3


# =============================================================
# PARTE 1 — Encontre os bugs
# Cada teste deve FALHAR no código original.
# Não altere src/pedido/pedido.py ainda.
# =============================================================

def test_subtotal_considera_quantidade():
    itens = [
        Item("Pão de queijo", 3.00, 2),
        Item("Café", 5.00, 1),
    ]
    pedido = Pedido("Cauã", itens)

    # 2 pães de queijo (R$ 6,00) + 1 café (R$ 5,00)
    assert pedido.subtotal() == 11.00


def test_frete_gratis_com_subtotal_exatamente_50():
    itens = [
        Item("Produto", 50.00, 1),
    ]
    pedido = Pedido("Cauã", itens)

    assert pedido.tem_frete_gratis() is True

def test_item_mais_barato_retorna_item_de_menor_preco():
    itens = [
        Item("Teclado", 100.00, 1),
        Item("Mouse", 50.00, 1),
        Item("Cabo", 15.00, 1),
    ]
    pedido = Pedido("Cauã", itens)

    assert pedido.item_mais_barato().nome == "Cabo"  

def test_total_com_desconto_subtrai_percentual():
    itens = [
        Item("Teclado", 100.00, 1),
    ]
    pedido = Pedido("Cauã", itens)

    assert pedido.total_com_desconto(10) == 90.00
# =============================================================
# PARTE 2 — Implemente com TDD
# Ciclo: teste → implementação → refatoração
# =============================================================

# Requisito 1 — contar_frete_gratis(pedidos) -> int
# Os testes serão adicionados antes da implementação.

def test_contar_frete_gratis_todos_com_frete_gratis():
    pedidos = [
        Pedido("Ana", [Item("Lanche", 60.00)]),
        Pedido("Bruno", [Item("Pizza", 50.00)]),
    ]

    assert contar_frete_gratis(pedidos) == 2


def test_contar_frete_gratis_nenhum_com_frete_gratis():
    pedidos = [
        Pedido("Ana", [Item("Café", 10.00)]),
        Pedido("Bruno", [Item("Suco", 20.00)]),
    ]

    assert contar_frete_gratis(pedidos) == 0


def test_contar_frete_gratis_lista_mista():
    pedidos = [
        Pedido("Ana", [Item("Lanche", 60.00)]),
        Pedido("Bruno", [Item("Café", 10.00)]),
        Pedido("Carla", [Item("Pizza", 50.00)]),
    ]

    assert contar_frete_gratis(pedidos) == 2


def test_contar_frete_gratis_lista_vazia():
    assert contar_frete_gratis([]) == 0

# Requisito 2 — situacao(unidades_indisponiveis) -> str
# Os testes serão adicionados antes da implementação.


# Requisito 3 — sugerir_frete_gratis(sms_service) -> None
# Utilizar MagicMock para simular o serviço de SMS.
# Os testes serão adicionados antes da implementação.
