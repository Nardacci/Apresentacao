# -*- coding: utf-8 -*-
"""Gera as quatro páginas do pitch (index, funciona, anvisa, entrega) com cabeçalho e rodapé comuns.
Uso: python3 ferramentas/montar_paginas.py [pasta de saída]  (padrão: raiz do repositório)"""
import os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = sys.argv[1] if len(sys.argv) > 1 else RAIZ

NAV = [('inicio', 'index.html', 'Início'), ('funciona', 'funciona.html', 'Como funciona'), ('anvisa', 'anvisa.html', 'Normas da ANVISA'), ('entrega', 'entrega.html', 'O que entregamos')]

def pagina(chave, titulo, descricao, corpo, extra_body=''):
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' class="ativo" aria-current="page"' if k == chave else '', t) for k, h, t in NAV)
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s</title>
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="%(descricao)s">
<link rel="icon" href="assets/ilabpharma-logo-claro.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="pitch.css">
</head>
<body data-pag="%(chave)s">
<a class="pular" href="#conteudo">Ir para o conteúdo</a>
<header class="topo" id="topo">
  <a class="marca" href="index.html" aria-label="iLabPharma, início"><img src="assets/ilabpharma-logo-claro.svg" alt="iLabPharma"></a>
  <nav aria-label="Páginas">%(nav)s</nav>
</header>
<main id="conteudo">
%(corpo)s
</main>
%(extra)s
<script src="dados/dados.js"></script>
<script src="pitch.js"></script>
</body>
</html>
''' % dict(titulo=titulo, descricao=descricao, chave=chave, nav=nav, corpo=corpo, extra=extra_body)

RODAPE = '''<footer class="rodape">
  <img src="assets/ilabpharma-logo-claro.svg" alt="iLabPharma">
  <p>Inteligência aplicada à gestão da produção laboratorial de medicamentos e vacinas.</p>
</footer>'''

INICIO = '''<section class="hero" id="inicio">
  <div class="hero-texto">
    <p class="kicker"><span class="ponto"></span>iLabPharma</p>
    <h1>Do insumo ao lote liberado, <em>tudo conectado.</em></h1>
    <p class="lead">O iLabPharma acompanha a produção de medicamentos e vacinas de ponta a ponta, com a Qualidade dentro de cada etapa e as exigências da ANVISA como guia.</p>
    <nav class="portas" id="portas" aria-label="Conheça o iLabPharma"></nav>
  </div>
  <div class="hero-trilho" aria-label="A jornada do lote">
    <p class="trilho-rotulo">Siga o lote</p>
    <ol class="trilho" id="trilho"></ol>
    <div class="trilho-card" id="trilhoCard" aria-live="polite"></div>
  </div>
</section>
''' 

FUNCIONA = '''<section class="pagina" id="funciona">
  <div class="pagina-topo">
    <p class="kicker"><span class="ponto"></span>Como funciona</p>
    <h1>Entenda como o iLabPharma funciona</h1>
    <p class="sub">Sete etapas, nove módulos integrados. Escolha uma etapa ou deixe o lote percorrer o caminho.</p>
    <button class="btn" id="tocar" type="button" aria-pressed="false"><span id="tocarIco" aria-hidden="true">▶</span> <span id="tocarTxt">Seguir o lote</span></button>
  </div>
  <div class="funciona">
    <ol class="passos" id="passos" aria-label="Etapas"></ol>
    <article class="painel" id="painel" aria-live="polite"></article>
  </div>
</section>
''' + RODAPE

ANVISA = '''<section class="pagina" id="anvisa">
  <div class="pagina-topo">
    <p class="kicker"><span class="ponto"></span>As normas</p>
    <h1>Dentro das normas da ANVISA</h1>
    <p class="sub">Para cada exigência da RDC 658/2022 e do Guia 33/2020, como o iLabPharma responde.</p>
  </div>
  <div class="cobertura" id="cobertura"></div>
  <div class="filtros" id="filtros"></div>
  <div class="grade-normas" id="normas"></div>
  <p class="nota">Fonte: RDC 658/2022 e Guia 33/2020 (ANVISA).</p>
</section>
''' + RODAPE

ENTREGA = '''<div class="cenas" id="cenas" aria-label="O que entregamos"></div>
<nav class="pontos" id="pontos" aria-label="Cenas"></nav>
'''

paginas = {
    'index.html': pagina('inicio', 'iLabPharma · Do insumo ao lote liberado', 'iLabPharma: gestão da produção de medicamentos e vacinas, do recebimento do insumo à liberação do lote, com as exigências da ANVISA como guia.', INICIO),
    'funciona.html': pagina('funciona', 'Como funciona · iLabPharma', 'Como o iLabPharma acompanha o lote do insumo à liberação, etapa por etapa, com os fluxos de cada processo.', FUNCIONA),
    'anvisa.html': pagina('anvisa', 'Normas da ANVISA · iLabPharma', 'Como o iLabPharma responde a cada exigência da RDC 658/2022 e do Guia 33/2020.', ANVISA),
    'entrega.html': pagina('entrega', 'O que entregamos · iLabPharma', 'O que o iLabPharma entrega além do sistema.', ENTREGA),
}
for nome, html in paginas.items():
    open(os.path.join(SAIDA, nome), 'w', encoding='utf-8').write(html)
    print('Gerado', nome)
