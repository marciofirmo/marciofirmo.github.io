# marciofirmo.github.io — três coisas no mesmo repositório

Este repositório hospeda **três projetos distintos**. Antes de mexer, veja em qual
você está:

| Caminho | O que é | Quem edita |
|---|---|---|
| `index.html` (raiz) | Página acadêmica pessoal | manual, com cuidado |
| `setor-publico/`, `economia-da-educacao/`, `topicos-teoria-economica/`, `curso.css` | **Repositório de material didático** | **gerado** por `_gerar/publicar_material.py` |
| `copa/` | Projeto Copa Cultural | manual |

## Regras invioláveis (valem para tudo)
- **SEMPRE mostre o diff/as mudanças ANTES de aplicar, e espere aprovação.**
- **SÓ faça commit e push depois de aprovação explícita.** Branch de publicação: `main`.
  Atenção: o clone costuma estar numa branch automática (`auto/placares-*`) — confira
  com `git branch --show-current` antes de publicar.
- **Não invente dados** (jogos, placares, músicas, filmes, números de aula). Se faltar
  informação, pergunte.

## Material didático (`setor-publico/` etc.)

**Este repositório fica fora do Dropbox, então os `CLAUDE.md` de
`02. Carreira` e de `1. Ensino` NÃO carregam aqui.** Por isso o fluxo está
escrito por extenso abaixo — não dependa de ler os outros arquivos.

### "Publica o material novo" — o que fazer

1. Se houver material novo, acrescente/ajuste o bloco dele em
   `_gerar/config_cursos.py` (só dados: título, descrição, caminho de origem no
   Dropbox, nome público).
2. `python _gerar/publicar_material.py --conferir` (simula, não escreve) e depois
   sem a flag.
3. **Verificação visual obrigatória**: suba um servidor local
   (`python -m http.server 8765`) e **olhe as páginas** antes de publicar.
4. `git add -A && git commit -m "..."`.
5. **Confira a branch**: `git branch --show-current`. O clone costuma estar numa
   `auto/placares-*` (do projeto da Copa) e **o site publica de `main`**. Se
   preciso: `git checkout main && git merge <branch> --ff-only`.
6. `git push origin main` — **só com aval explícito do Marcio**.

### Regras do material
- **Não edite os HTML de curso à mão** — são gerados; mexer neles é trabalho
  perdido na próxima geração. Mude o config.
- Os PDFs vêm do Dropbox (`02. Carreira\07. UERJ\1. Ensino\...`) e são copiados com
  **nome público estável**: `aula05_acb_v8_aluno.pdf` → `aula-05-custo-beneficio.pdf`.
  Nunca mude o nome público ao subir de versão — quebraria o link salvo pelo aluno.
- **Sem datas nas páginas**: elas valem para qualquer semestre. Datas de prova,
  pesos e formato ficam com a turma, não no site.
- **Não vão para o site** (até o Marcio liberar): listas, gabaritos/respostas,
  roteiros do professor e documentos-fonte de terceiros.

## Página acadêmica (`index.html` da raiz)
- Editar só quando o pedido for explicitamente sobre ela. É bilíngue: cada texto
  aparece em `<span class="en">` e `<span class="pt">` — **mexeu num, mexa no outro**.
- A seção `#teaching` linka para as páginas de curso; se acrescentar disciplina no
  gerador, acrescente o link aqui também.

## Projeto Copa Cultural (`copa/index.html`)
Site/app que, para cada jogo da Copa 2026, mostra música tradicional e cinema dos
países. HTML+CSS+JS puro, sem build. **Não mexa fora de `copa/` quando o assunto for
a Copa.**

## Estrutura do copa/index.html
- const C = {...}: banco de países (sigla → {name, flag, trad, songs:[], films:[]}).
- const MATCHES = [...]: jogos, formato {date:"AAAA-MM-DD", t:"00h", h:"SIGLA", a:"SIGLA", s:"X x Y"}. O campo "s" só aparece quando o jogo terminou.
- const SPL = {...}: link de playlist pública REAL do Spotify por PAÍS, chave "SIGLA". Cada jogo mostra sempre 1 botão por país (os dois times que jogam) — NÃO há playlist por jogo. Para cada país usa SPL[país] se existir; senão cai automaticamente numa busca pública do Spotify pelo gênero (função countryPL = sp(name+trad)). Preferir sempre playlists públicas reais (OWNER/oficiais) — as geradas pelo conector nascem privadas e não abrem para visitantes. A busca da ferramenta do Spotify só devolve playlist real (OWNER/SPOTIFY_CURATED) para alguns países; para a maioria ela GERA uma privada (inútil para visitantes), por isso o fallback por busca.
- A página mostra automaticamente os jogos de hoje + 2 dias (pela data do visitante).

## Convenções
- Música: primeira do array songs[] é o destaque; demais ficam no "ver mais".
- Filme: primeiro do array films[] é o destaque.
- Manter o código sem dependências externas (roda direto no navegador).
- Português nos textos visíveis.
