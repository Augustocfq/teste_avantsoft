from models import *
from config import db

def add_student_service(body: dict) -> tuple:

    """
    Adiciona um estudante ao banco de dados

    Args:
        body (dict): Dicionário com os campos 'nome' e 'nota'.
    Returns:
        (tuple): Um dicionário com os dados do estudante recem adicionado e um código de status HTTP.
    Raises:
        ERRO: Caso algum dos campos não exista ou a nota seja inválida.
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
    
def get_students_service() -> tuple:
    """
    Retorna uma lista com todos os etudantes cadastrados

    Returns:
        (tuple): Uma lista de estudantes cadastrados e um código de status HTTP
    """
    try:
        estudantes = Student.query.all()
        
        lista_estudantes = []
        for estudante in estudantes:
            lista_estudantes.append({
                "id": estudante.id,
                "nome": estudante.nome,
                "nota": estudante.nota
            })

        return lista_estudantes, 200

    except Exception as e:
        db.session.rollback()
        return {"ERRO": f"Um erro inesperado aconteceu: {e}"}, 500
    
def get_student_by_id_service(id: int) -> tuple:
    """
    Retorna um estudante baseado em seu id

    Args:
        id (int): Chave primária de um registro de estudante no banco de dados.
    Returns:
        (tuple): Um dicionário com os dados do estudante e um código de status http.
    """
    try:
        try:
            student = Student.query.get(
                int(id)
            )
        except (ValueError, TypeError):
            return {"ERRO": "O id deve ser um valor inteiro."}, 400

        mensagem = {
            "id": student.id,
            "nome": student.nome,
            "nota": student.nota
        }
        
        return mensagem, 200

    except Exception as e:
        db.session.rollback()
        return {"ERRO": f"Um erro inesperado aconteceu: {e}"}, 500