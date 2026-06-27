# Projeto: Copa Cultural

## O que é
Site/app em marciofirmo.github.io/copa que, para cada jogo da Copa do Mundo 2026, mostra música tradicional e cinema dos países. Arquivo principal: copa/index.html (HTML+CSS+JS puro, sem build).

## Regras invioláveis
- NUNCA edite o index.html da RAIZ — é a página acadêmica pessoal. Só mexa em copa/index.html (e arquivos dentro de copa/).
- SEMPRE me mostre o diff/as mudanças ANTES de aplicar, e espere aprovação.
- SÓ faça commit e push depois que eu aprovar explicitamente. Branch: main.
- Não invente dados (jogos, placares, músicas, filmes). Se faltar informação, pergunte.

## Estrutura do copa/index.html
- const C = {...}: banco de países (sigla → {name, flag, trad, songs:[], films:[]}).
- const MATCHES = [...]: jogos, formato {date:"AAAA-MM-DD", t:"00h", h:"SIGLA", a:"SIGLA", s:"X x Y"}. O campo "s" só aparece quando o jogo terminou.
- const PL = {...}: link de playlist do Spotify por jogo, chave "SIGLA_A-SIGLA_B".
- const SPL = {...}: link de playlist pública REAL do Spotify por PAÍS, chave "SIGLA". Quando o jogo não tem entrada em PL, a página mostra 1 botão por país: usa SPL[país] se existir; senão cai automaticamente numa busca pública do Spotify pelo gênero (função countryPL = sp(name+trad)). Preferir sempre playlists públicas reais (OWNER/oficiais) — as geradas pelo conector nascem privadas e não abrem para visitantes. A busca da ferramenta do Spotify só devolve playlist real (OWNER/SPOTIFY_CURATED) para alguns países; para a maioria ela GERA uma privada (inútil para visitantes), por isso o fallback por busca.
- A página mostra automaticamente os jogos de hoje + 2 dias (pela data do visitante).

## Convenções
- Música: primeira do array songs[] é o destaque; demais ficam no "ver mais".
- Filme: primeiro do array films[] é o destaque.
- Manter o código sem dependências externas (roda direto no navegador).
- Português nos textos visíveis.
