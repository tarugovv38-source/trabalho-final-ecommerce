"""
Testes Unitários - API E-Commerce
Disciplina: Cloud Computing - UNIDAVI
Autor: Vitor Hugo Tavares
"""

import sys
import os

# Garante que o módulo api/app.py seja encontrado durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app


@pytest.fixture
def cliente():
    """Cria um cliente de teste para a API Flask."""
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


# ------------------------------------------------------------------
# Teste 1: GET /produtos retorna HTTP 200
# ------------------------------------------------------------------
def test_listar_produtos_retorna_200(cliente):
    """
    Verifica se a rota GET /produtos responde com status HTTP 200 (OK).
    É o teste mais básico: garante que a rota está acessível e funcional.
    """
    resposta = cliente.get("/produtos")
    assert resposta.status_code == 200


# ------------------------------------------------------------------
# Teste 2: Validação da estrutura do JSON retornado
# ------------------------------------------------------------------
def test_estrutura_json_produtos(cliente):
    """
    Verifica se o JSON retornado por GET /produtos contém os campos
    obrigatórios: 'total' e 'produtos', e se 'produtos' é uma lista
    com pelo menos 10 itens, cada um contendo os campos esperados.
    """
    resposta = cliente.get("/produtos")
    dados = resposta.get_json()

    # Verifica campos raiz
    assert "total" in dados
    assert "produtos" in dados
    assert isinstance(dados["produtos"], list)
    assert len(dados["produtos"]) >= 10

    # Verifica estrutura de cada produto
    campos_obrigatorios = {"id", "nome", "categoria", "preco", "estoque", "disponivel"}
    for produto in dados["produtos"]:
        for campo in campos_obrigatorios:
            assert campo in produto, f"Campo '{campo}' ausente no produto: {produto}"


# ------------------------------------------------------------------
# Teste 3: GET /produtos/{id} retorna HTTP 404 para ID inexistente
# ------------------------------------------------------------------
def test_produto_inexistente_retorna_404(cliente):
    """
    Verifica se a rota GET /produtos/{id} retorna HTTP 404 quando
    o ID informado não existe na base de dados.
    Usar id=9999 garante que nunca haverá conflito com dados reais.
    """
    resposta = cliente.get("/produtos/9999")
    assert resposta.status_code == 404


# ------------------------------------------------------------------
# Teste 4 (autoria própria): Verifica produtos disponíveis em estoque
# ------------------------------------------------------------------
def test_produtos_disponiveis_tem_estoque_positivo(cliente):
    """
    Teste de consistência de dados: verifica se todos os produtos
    marcados como 'disponivel: true' possuem estoque maior que zero.
    Isso garante integridade entre os campos 'disponivel' e 'estoque',
    simulando uma regra de negócio real de um e-commerce: um produto
    não pode estar disponível para compra se não há unidades em estoque.
    """
    resposta = cliente.get("/produtos")
    dados = resposta.get_json()

    for produto in dados["produtos"]:
        if produto["disponivel"]:
            assert produto["estoque"] > 0, (
                f"Produto '{produto['nome']}' está disponível mas tem estoque zero."
            )
