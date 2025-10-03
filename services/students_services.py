from models import *
from config import db

def add_student_service(body: dict) -> dict:

    """
    Adiciona um estudante ao banco de dados

    Args:
        body (dict): Dicionário com os campos 'nome' e 'nota'.
    Returns:
        dict: Um dicionário com os dados do estudante recem adicionado.
    Raises:
        ValueError: Caso algum dos campos não exista ou a nota seja inválida.
    """
    
    nome = body.get('nome')
    if not nome:
        return {"ERRO": "O campo 'nome' ou 'nota' está faltando."}, 400
    
    try:
        nota = float(body.get('nota'))
    except (ValueError, TypeError):
        return {"ERRO": "A nota deve ser um valor numérico."}, 400
    if not (0 <= nota <= 10):
        return {"ERRO": "A nota deve ser um número entre 0 e 10."}, 400

    try:
        novo_estudante = Student(
            nome = nome,
            nota = nota
        )

        db.session.add(novo_estudante)
        db.session.commit()

        mensagem = {
            "id": novo_estudante.id,
            "nome": novo_estudante.nome,
            "nota": novo_estudante.nota,
            "menssagem": "Estudante adicionado com sucesso."
        }
        return mensagem, 201
    
    except Exception as e:
        db.session.rollback()
        return {"ERRO": f"Um erro inesperado aconteceu: {e}"}, 500