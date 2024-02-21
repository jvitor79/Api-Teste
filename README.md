# Api teste

Esta é uma api teste desenvolvida para fins de aprendizagem e treino da construção de api para gerenciamento de uma base de dados
de filmes e séries, afim de nomar as mesmas e dar uma nota para cada filme e episódio da série

Para isto foi utlizada as seguintes tecnologias:

- FastAPI
- SQLAlchemy
- Alembic
- Uvicorn
- Pydantic
- Supabase
- PostgreSQL

## Comandos

### Criar virtual environment

- python3 -m venv <nome_do_venv>
- source <nome_do_venv>/bin/activate

### Instalar requirements

- pip install -r requiremnts.txt

### Iniciar Api

- uvicorn src.app:main --reload

### Versionamento base de dados

- alembic revision --autogenerate -m <código_da_versão>
- alembic upgade <id_versão> (head para versão mais recente)
- alembic downgade <id_versão> (base para voltar ao estado inicial)
