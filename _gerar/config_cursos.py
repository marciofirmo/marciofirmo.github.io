# -*- coding: utf-8 -*-
"""
Configuração do repositório de material didático.

Como usar: edite este arquivo (é só dados) e rode:
    python _gerar/publicar_material.py

O script copia os PDFs com NOMES PÚBLICOS ESTÁVEIS e regenera as páginas.

Regra de ouro dos nomes: o nome público NUNCA muda quando a versão interna muda.
   aula05_acb_v8_aluno.pdf  (interno)  ->  aula-05-custo-beneficio.pdf  (público)
Assim o link que o aluno salvou continua funcionando no semestre seguinte.
"""

DROPBOX = r"C:\Users\marci\Dropbox\02. Carreira\07. UERJ\1. Ensino"

CURSOS = [
    {
        "slug": "setor-publico",
        "nome": "Economia do Setor Público",
        "codigo": "UERJ · graduação · obrigatória",
        "atualizado": "2026.1",
        "resumo": (
            "Por que, como e com que efeitos o Estado intervém na economia. "
            "O curso reconstrói a microeconomia necessária em cada tópico e traz "
            "sempre a camada brasileira: dados, instituições e casos reais."
        ),
        "nota_alunos_antigos": (
            "Este material foi revisado e ampliado em 2026.1. Se você cursou a "
            "disciplina antes, vale rever por aqui: os decks estão bem mais "
            "completos que as versões anteriores."
        ),
        "fonte": DROPBOX + r"\6. Setor Público\03. Setor Público - 2026_1 - retomada",
        "secoes": [
            {
                "titulo": "Aulas",
                "nota": "Versão para estudo, com todos os passos revelados. São os mesmos slides usados em aula.",
                "itens": [
                    {"origem": r"2. Aulas\01_Introdução\aula01_introducao_v2_aluno.pdf",
                     "publico": "aula-01-introducao.pdf",
                     "titulo": "Aula 1 — Introdução",
                     "desc": "O que é Economia do Setor Público; as quatro perguntas que organizam o curso; tamanho e forma do Estado no Brasil."},
                    {"origem": r"2. Aulas\02_Análise Normativa\aula02_normativa_v3_aluno.pdf",
                     "publico": "aula-02-analise-normativa.pdf",
                     "titulo": "Aula 2 — Análise normativa",
                     "desc": "Positivo × normativo; excedentes e eficiência; os dois Teoremas do Bem-Estar; funções de bem-estar social; o mapa das falhas de mercado. Caso: o congelamento de aluguéis de 1942."},
                    {"origem": r"2. Aulas\02_Análise Normativa\material_extra_eficiencia.pdf",
                     "publico": "material-extra-eficiencia.pdf",
                     "titulo": "Material extra — eficiência de troca",
                     "desc": "Opcional. Por que TMS = razão de preços é o coração da eficiência, e o que uma transferência lump sum muda (e o que não muda)."},
                    {"origem": r"2. Aulas\03_Externalidades\aula03_externalidades_v4_aluno.pdf",
                     "publico": "aula-03-externalidades.pdf",
                     "titulo": "Aula 3 — Externalidades",
                     "desc": "CMP × CMS e peso morto; Teorema de Coase e seus limites; imposto de Pigou, subsídios e cotas; preço × quantidade sob incerteza; tabagismo e internalidades."},
                    {"origem": r"2. Aulas\04_Bens Públicos\aula04_bens_publicos_v4_aluno.pdf",
                     "publico": "aula-04-bens-publicos.pdf",
                     "titulo": "Aula 4 — Bens públicos",
                     "desc": "Rivalidade e exclusão; a condição de Samuelson construída passo a passo; free rider e tragédia dos comuns; provisão pública e os casos brasileiros (COSIP, saneamento, segurança, SUS)."},
                    {"origem": r"2. Aulas\05_Custo-Benefício\aula05_acb_v8_aluno.pdf",
                     "publico": "aula-05-custo-beneficio.pdf",
                     "titulo": "Aula 5 — Análise de custo-benefício",
                     "desc": "O que conta como custo e como benefício; valor do tempo e valor da vida estatística; desconto e VPL; erros clássicos; o Guia ACB brasileiro e a ACB no mundo real."},
                ],
            },
        ],
        "programa": [
            ("Parte 1 — atuação governamental (gasto)",
             ["Introdução e análise normativa",
              "Externalidades",
              "Bens públicos",
              "Análise de custo-benefício",
              "Escolha pública e economia política"]),
            ("Parte 2 — taxação (receita)",
             ["Introdução à taxação",
              "Incidência: quem paga não é quem recolhe",
              "Peso morto e taxação ótima",
              "Imposto de renda; poupança e riqueza",
              "Reforma tributária brasileira",
              "Federalismo fiscal; previdência e assistência"]),
        ],
        "avaliacao": [
            ("P1 (5 pontos) — Parte 1", "31/08/2026"),
            ("P2 (5 pontos) — Parte 2", "26/10/2026"),
            ("Prova Final", "03 a 09/11/2026"),
        ],
        "avaliacao_nota": (
            "Média = P1 + P2. Acima de 7, aprovado; entre 4 e 7, Prova Final "
            "(média final = dois terços da média mais um terço da PF). "
            "Frequência mínima de 75% é exigência institucional da UERJ. "
            "As provas são sempre às segundas-feiras."
        ),
        "bibliografia": [
            ("GRUBER, J.",
             "<em>Public Finance and Public Policy</em>. Worth Publishers. Livro-texto principal."),
            ("GIAMBIAGI, F.; ALÉM, A. C.",
             "<em>Finanças Públicas: Teoria e Prática no Brasil</em>. 5. ed. Elsevier, 2015. Referência da camada brasileira."),
        ],
    },
    {
        "slug": "economia-da-educacao",
        "nome": "Economia da Educação",
        "codigo": "UERJ · graduação · eletiva",
        "atualizado": "2026.1",
        "resumo": (
            "Capital humano, retornos da educação, políticas educacionais e "
            "avaliação de impacto — com laboratórios interativos que rodam R no "
            "próprio navegador, sem instalar nada."
        ),
        "nota_alunos_antigos": "",
        "fonte": "",
        "secoes": [
            {
                "titulo": "Laboratórios interativos",
                "nota": "Rodam R direto no navegador (webR). Não precisa instalar nada: é só abrir e mexer.",
                "itens": [
                    {"link": "../laboratorio-vies-webr.html",
                     "titulo": "Laboratório do viés de variável omitida",
                     "desc": "Seis cenários mostrando quando e por que a variável omitida distorce a estimativa."},
                    {"link": "../revisao-estatistica-webr.html",
                     "titulo": "Revisão estatística interativa",
                     "desc": "Lei dos grandes números, correlação e correlação parcial, construídas na mão."},
                    {"link": "../laboratorio-tentativas-webr.html",
                     "titulo": "Laboratório das tentativas — inferência causal",
                     "desc": "Cada método consertando o viés de seleção, ao vivo."},
                    {"link": "../vies-variavel-omitida-webr.html",
                     "titulo": "Editor de código livre (webR)",
                     "desc": "Versão sem roteiro, para experimentar."},
                ],
            },
        ],
        "programa": [],
        "avaliacao": [],
        "avaliacao_nota": "",
        "bibliografia": [],
    },
    {
        "slug": "topicos-teoria-economica",
        "nome": "Tópicos em Teoria Econômica",
        "codigo": "UERJ · graduação",
        "atualizado": "",
        "resumo": "Tópicos avançados selecionados em economia aplicada e teórica.",
        "nota_alunos_antigos": "",
        "fonte": "",
        "secoes": [],
        "programa": [],
        "avaliacao": [],
        "avaliacao_nota": "",
        "bibliografia": [],
    },
]
