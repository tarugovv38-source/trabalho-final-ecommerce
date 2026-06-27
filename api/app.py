"""
API REST - Infraestrutura para Pequeno E-Commerce
Disciplina: Cloud Computing - UNIDAVI
Autor: Vitor Hugo tavares
"""

import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Caminho para o arquivo de dados externo
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "produtos.json")


def carregar_produtos():
    """Carrega os produtos a partir do arquivo JSON externo."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/status", methods=["GET"])
def status():
    """
    Rota de health check da API.
    Retorna informações básicas sobre o estado da aplicação.
    """
    return jsonify({
        "nome": "API E-Commerce UNIDAVI",
        "versao": "1.0.0",
        "status": "online"
    }), 200


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    """
    Retorna a lista completa de produtos disponíveis no e-commerce.
    Aceita o parâmetro opcional ?categoria= para filtrar por categoria.
    """
    try:
        produtos = carregar_produtos()
        categoria = request.args.get("categoria")

        if categoria:
            produtos = [p for p in produtos if p["categoria"].lower() == categoria.lower()]

        return jsonify({
            "total": len(produtos),
            "produtos": produtos
        }), 200
    except Exception as e:
        return jsonify({"erro": "Erro interno ao carregar produtos", "detalhe": str(e)}), 500


@app.route("/produtos/<int:produto_id>", methods=["GET"])
def buscar_produto(produto_id):
    """
    Retorna um produto específico pelo seu ID.
    Caso o produto não exista, retorna HTTP 404.
    """
    try:
        produtos = carregar_produtos()
        produto = next((p for p in produtos if p["id"] == produto_id), None)

        if produto is None:
            return jsonify({"erro": f"Produto com id {produto_id} não encontrado"}), 404

        return jsonify(produto), 200
    except Exception as e:
        return jsonify({"erro": "Erro interno ao buscar produto", "detalhe": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
