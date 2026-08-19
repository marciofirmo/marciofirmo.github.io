# -*- coding: utf-8 -*-
"""
Gera as páginas de material didático do site a partir de config_cursos.py.

    python _gerar/publicar_material.py            # gera tudo
    python _gerar/publicar_material.py --conferir # só confere, não escreve

O que faz:
  1. copia cada PDF da pasta de trabalho (Dropbox) para {slug}/ com NOME PÚBLICO ESTÁVEL;
  2. regenera {slug}/index.html;
  3. escreve curso.css (estilo compartilhado, alinhado ao index.html do site);
  4. relata o que copiou, o que já estava igual e o que NÃO encontrou.

Nada é publicado: depois de rodar, confira e faça commit/push você mesmo.
"""
import os
import shutil
import sys
import datetime
import html

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

from config_cursos import CURSOS  # noqa: E402

CONFERIR = "--conferir" in sys.argv
HOJE = datetime.date.today().strftime("%d/%m/%Y")

CSS = """/* Estilo das páginas de curso — alinhado ao index.html do site.
   Gerado por _gerar/publicar_material.py; não edite à mão. */
:root{
  --bg:#fdfdfc; --fg:#222; --muted:#666; --rule:#e4e4e0;
  --link:#1a4f7a; --link-hover:#0e3552; --maxw:740px;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font:18px/1.6 Georgia,"Times New Roman",serif;
  padding:2rem 1.2rem 4rem;
}
.wrap{max-width:var(--maxw);margin:0 auto}
a{color:var(--link);text-decoration:none}
a:hover{color:var(--link-hover);text-decoration:underline}
.voltar{font-size:.85rem;color:var(--muted);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
h1{font-size:2rem;margin:1.4rem 0 .2rem;line-height:1.2}
.codigo{color:var(--muted);font-size:1rem;margin:0 0 1rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
h2{font-size:1.3rem;margin:2.4rem 0 .8rem;font-weight:600;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
h3{font-size:1rem;margin:1.6rem 0 .6rem;color:var(--muted);
  text-transform:uppercase;letter-spacing:.06em;font-weight:600;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
p{margin:.6rem 0}
hr{border:0;border-top:1px solid var(--rule);margin:2.6rem 0 0}
.aviso{border-left:3px solid var(--rule);padding:.1rem 0 .1rem 1rem;
  margin:1.4rem 0;color:#3a3a3a;font-size:.95rem}
.item{margin:1.3rem 0;padding-bottom:1.1rem;border-bottom:1px solid var(--rule)}
.item:last-child{border-bottom:0}
.item .tit{font-weight:700}
.item .desc{font-size:.95rem;color:#3a3a3a;margin:.25rem 0 .4rem}
.item .baixar{font-size:.85rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.secao-nota{font-size:.9rem;color:var(--muted);margin:-.3rem 0 1rem}
table.datas{border-collapse:collapse;font-size:.95rem;margin:.6rem 0}
table.datas td{padding:.3rem 1.4rem .3rem 0;border-bottom:1px solid var(--rule)}
table.datas td.q{color:var(--muted);white-space:nowrap}
ul.prog{margin:.3rem 0 1rem 1.1rem;padding:0;font-size:.95rem}
ul.prog li{margin:.2rem 0}
.bib{font-size:.95rem;margin:.5rem 0}
footer{margin-top:2.4rem;font-size:.82rem;color:var(--muted);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
@media(max-width:640px){ body{font-size:17px} h1{font-size:1.7rem} }
"""


def e(txt):
    return html.escape(str(txt), quote=False)


def pagina_curso(c, itens_ok):
    """Monta o HTML da página de um curso."""
    p = []
    a = p.append
    a('<!DOCTYPE html>')
    a('<html lang="pt-BR">')
    a('<head>')
    a('<meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width, initial-scale=1">')
    a('<title>%s — Marcio Gold Firmo</title>' % e(c["nome"]))
    a('<meta name="description" content="Material da disciplina %s. '
      'Slides, programa e avaliação.">' % e(c["nome"]))
    a('<link rel="stylesheet" href="../curso.css">')
    a('</head>')
    a('<body>')
    a('<div class="wrap">')
    a('<div class="voltar"><a href="../#teaching">&larr; Marcio Gold Firmo — ensino</a></div>')
    a('<h1>%s</h1>' % e(c["nome"]))
    a('<p class="codigo">%s</p>' % e(c["codigo"]))
    if c.get("resumo"):
        a('<p>%s</p>' % e(c["resumo"]))
    if c.get("nota_alunos_antigos"):
        a('<div class="aviso">%s</div>' % e(c["nota_alunos_antigos"]))

    # --- material ---
    for sec, itens in itens_ok:
        if not itens:
            continue
        a('<h2>%s</h2>' % e(sec["titulo"]))
        if sec.get("nota"):
            a('<p class="secao-nota">%s</p>' % e(sec["nota"]))
        for it in itens:
            destino = it.get("publico") or it.get("link")
            a('<div class="item">')
            a('  <div class="tit">%s</div>' % e(it["titulo"]))
            if it.get("desc"):
                a('  <div class="desc">%s</div>' % e(it["desc"]))
            rot = "Abrir &rarr;" if it.get("link") else "Baixar o PDF &rarr;"
            a('  <div class="baixar"><a href="%s">%s</a></div>' % (e(destino), rot))
            a('</div>')

    # --- programa ---
    if c.get("programa"):
        a('<h2>Programa</h2>')
        for titulo, topicos in c["programa"]:
            a('<h3>%s</h3>' % e(titulo))
            a('<ul class="prog">')
            for t in topicos:
                a('  <li>%s</li>' % e(t))
            a('</ul>')

    # --- avaliação ---
    if c.get("avaliacao"):
        a('<h2>Avaliação</h2>')
        a('<table class="datas">')
        for o_que, quando in c["avaliacao"]:
            a('  <tr><td>%s</td><td class="q">%s</td></tr>' % (e(o_que), e(quando)))
        a('</table>')
        if c.get("avaliacao_nota"):
            a('<p class="secao-nota">%s</p>' % e(c["avaliacao_nota"]))

    # --- bibliografia ---
    if c.get("bibliografia"):
        a('<h2>Bibliografia</h2>')
        for autor, ref in c["bibliografia"]:
            a('<p class="bib"><strong>%s</strong> %s</p>' % (e(autor), ref))

    if not any(itens for _, itens in itens_ok):
        a('<h2>Material</h2>')
        a('<p class="secao-nota">Em preparação.</p>')

    a('<hr>')
    a('<footer>Última atualização: %s. '
      'Dúvidas e correções são bem-vindas — escreva para o professor.</footer>' % HOJE)
    a('</div>')
    a('</body>')
    a('</html>')
    return "\n".join(p) + "\n"


def main():
    print("=" * 66)
    print("PUBLICAR MATERIAL DIDÁTICO" + ("  [modo conferência]" if CONFERIR else ""))
    print("=" * 66)

    faltando = []
    for c in CURSOS:
        print("\n### %s  (/%s/)" % (c["nome"], c["slug"]))
        destino_dir = os.path.join(SITE, c["slug"])
        if not CONFERIR:
            os.makedirs(destino_dir, exist_ok=True)

        itens_ok = []
        for sec in c.get("secoes", []):
            ok = []
            for it in sec["itens"]:
                if it.get("link"):          # material que já mora no site
                    ok.append(it)
                    print("   link   %s" % it["titulo"])
                    continue
                origem = os.path.join(c["fonte"], it["origem"])
                if not os.path.isfile(origem):
                    print("   FALTA  %s\n          -> %s" % (it["titulo"], origem))
                    faltando.append((c["nome"], it["titulo"], origem))
                    continue
                destino = os.path.join(destino_dir, it["publico"])
                igual = (os.path.isfile(destino)
                         and os.path.getsize(destino) == os.path.getsize(origem))
                if not CONFERIR and not igual:
                    shutil.copy2(origem, destino)
                mb = os.path.getsize(origem) / 1048576.0
                print("   %s %s  (%.1f MB)  -> %s"
                      % ("=" if igual else "COPIA", it["titulo"][:38].ljust(38), mb, it["publico"]))
                ok.append(it)
            itens_ok.append((sec, ok))

        if not CONFERIR:
            with open(os.path.join(destino_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(pagina_curso(c, itens_ok))
            print("   pagina -> %s/index.html" % c["slug"])

    if not CONFERIR:
        with open(os.path.join(SITE, "curso.css"), "w", encoding="utf-8") as f:
            f.write(CSS)
        print("\ncurso.css escrito.")

    print("\n" + "-" * 66)
    if faltando:
        print("ATENÇÃO — %d arquivo(s) não encontrado(s):" % len(faltando))
        for curso, tit, caminho in faltando:
            print("  · [%s] %s\n      %s" % (curso, tit, caminho))
    else:
        print("Todos os arquivos configurados foram encontrados.")
    print("Depois de conferir, faça: git add -A && git commit && git push")


if __name__ == "__main__":
    main()
