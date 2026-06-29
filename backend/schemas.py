from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    avatar: str

class TemaCreate(BaseModel):
    nome: str

class PerguntaCreate(BaseModel):
    enunciado: str
    tipo: str
    tema_id: int

class AlternativaCreate(BaseModel):
    descricao: str
    correta: bool
    pergunta_id: int

class RespostaCreate(BaseModel):
    usuario_id: int
    pergunta_id: int
    alternativa_id: int
    tentativa_id: int

class TentativaCreate(BaseModel):
    usuario_id: int

class LoginRequest(BaseModel):
    email: str
    senha: str

