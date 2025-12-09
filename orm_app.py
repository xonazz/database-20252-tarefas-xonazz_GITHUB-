from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('postgresql://admin:1234@localhost:5432/AtividadesBD')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Projeto(Base):
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    lider = Column(String)
    atividades = relationship("Atividade", back_populates="projeto")

class Atividade(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    projeto_id = Column(Integer, ForeignKey('projetos.id'))
    descricao = Column(String)
    projeto = relationship("Projeto", back_populates="atividades")

# Inserir atividade
nova_atividade = Atividade(projeto_id=1, descricao="Atividade via ORM")
session.add(nova_atividade)

# Atualizar líder
projeto = session.query(Projeto).filter_by(id=1).first()
if projeto:
    projeto.lider = "Líder atualizado ORM"

# Listar projetos e atividades
projetos = session.query(Projeto).all()
for p in projetos:
    for a in p.atividades:
        print(p.nome, p.lider, a.descricao)

session.commit()
