# 📁 Estrutura de Pastas do Projeto - Reconhecimento Facial via RTSP

Este documento descreve a estrutura de diretórios e arquivos utilizada no projeto, com o objetivo de manter a organização, facilitar a manutenção e garantir padronização entre os desenvolvedores.

---

## 🌲 Estrutura Geral

```
/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── camera.py
│   ├── queues.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── stream.py
│   └── detectors/
│       ├── __init__.py
│       └── face_detector.py
├── tests/
├── config.py
├── .env.example
├── .gitignore
├── requirements.txt
└── docs/
    ├── structure.md
    ├── changelog.md
    └── routes.md
```

---

## 🔍 Detalhamento por Pasta

### `/app`

* Onde reside toda a lógica da aplicação.
* **main.py**: inicializa o servidor, as rotas e configurações.
* **config.py**: centraliza configurações reutilizáveis (como caminhos, thresholds, etc.).

### `/routes`

* Cada rota é isolada por funcionalidade.
* Exemplo: `routes/face_detect.py`, `routes/compare.py`.

### `/detectors`

* Implementações como MTCNN, RetinaFace ou InsightFace.
* Normalmente centralizado em um módulo de abstração comum.

### `/embeddings`

* Cálculo de vetores faciais (512 ou 1024 dimensões).
* Comparações de similaridade, normalização, clustering.

### `/database`

* Conexões com PostgreSQL, tabelas e acesso com SQLAlchemy ou psycopg2.
* Pode conter scripts para criação de tabelas e versionamento.

### `/services`

* Regras de negócio específicas, por exemplo:

  * Registro de logs faciais
  * Criação de perfil de usuário
  * Controle de acessos por câmera

### `/static`

* Imagens recebidas dos streams
* Rosto alinhado, desconhecido, confirmado
* Pode conter miniaturas exibidas na UI

### `/tests`

* Scripts com testes unitários para os módulos do sistema.
* Uso preferencial de `pytest`.

---

## 📌 Observações Finais

* Toda nova pasta criada deve ser documentada aqui.
* Toda nova função crítica deve estar mapeada em `/docs/constants.md` e/ou `/docs/dependencies.md`.
* O diretório `.venv/` não deve ser versionado.

Se essa estrutura for alterada, o arquivo `structure.md` deve ser **obrigatoriamente atualizado**.
