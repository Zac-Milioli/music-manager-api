# music-manager-api
Desenvolvimento de uma API para artistas rascunharem e salvarem suas ideias produções.

Possui CI (testes unitários, linter e merge automático na master em caso sucesso) implementado.

Python é obrigatório para a utilização deste software.

## Instalação dos pacotes necessários
```
pip install -r requirements.txt
```

## Execução
```
python main.py
```

## Documentação e testes manuais
Ao executar o sistema, é gerada a documentação automática que pode ser acessada diretamente pelo navegador.

> http://localhost:8000/docs (Permite testar a API)
> http://localhost:8000/redoc (Somente documentação)

### Recomenda-se o uso de um venv. Para tal:
```
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```
