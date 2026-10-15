# -*- coding: utf-8 -*-
"""Gera as quatro páginas do pitch (index, funciona, anvisa, entrega) com cabeçalho e rodapé comuns.
Uso: python3 ferramentas/montar_paginas.py [pasta de saída]  (padrão: raiz do repositório)"""
import os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = sys.argv[1] if len(sys.argv) > 1 else RAIZ

NAV = [('inicio', '#inicio', 'Início'), ('funciona', '#industria', 'Como funciona'), ('anvisa', '#g0', 'Normas da ANVISA'), ('entrega', '#entrega', 'O que entregamos')]

INICIO = '''<section class="hero" id="inicio">
  <div class="hero-texto">
    <p class="kicker"><span class="ponto"></span>iLabPharma</p>
    <h1>Do insumo ao lote liberado, <em>tudo conectado.</em></h1>
    <p class="lead">O iLabPharma acompanha a produção de medicamentos e vacinas de ponta a ponta, com a Qualidade dentro de cada etapa e as exigências da ANVISA como guia.</p>
    <div class="inicio-acao">
      <a class="btn primario grande" id="comecar" href="#industria">Iniciar a apresentação <span aria-hidden="true">→</span></a>
      <p class="atalho">Use as setas <kbd>←</kbd> <kbd>→</kbd> do teclado para avançar e <kbd>F</kbd> para tela cheia.</p>
    </div>
    <ol class="roteiro" aria-label="O que você vai ver">
      <li><b>1</b> Como o iLabPharma funciona</li>
      <li><b>2</b> Dentro das normas da ANVISA</li>
      <li><b>3</b> O que entregamos</li>
    </ol>
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
  </div>
  <div class="funciona">
    <ol class="passos" id="passos" aria-label="Etapas"></ol>
    <article class="painel" id="painel" aria-live="polite"></article>
  </div>
</section>
'''

ANVISA = '''<section class="pagina" id="anvisa">
  <div class="pagina-topo">
    <p class="kicker"><span class="ponto"></span>As normas</p>
    <h1>Dentro das normas da ANVISA</h1>
    <p class="sub" id="anvisaSub"></p>
  </div>
  <div class="cobertura" id="cobertura"></div>
  <div class="filtros" id="filtros" role="tablist" aria-label="Grupos da norma"></div>
  <div class="grade-normas" id="normas"></div>
  <p class="nota">Fonte: RDC 658/2022 e Guia 33/2020 (ANVISA).</p>
</section>
'''

ENTREGA = '''<div class="cenas" id="cenas" aria-label="O que entregamos"></div>
<nav class="pontos" id="pontos" aria-label="Cenas"></nav>
'''

def view(chave, corpo, ativo=False):
    return '<div class="view" id="v-%s"%s>\n%s\n</div>' % (chave, '' if ativo else ' hidden', corpo)

def pagina_unica():
    nav = ''.join('<a href="%s" data-view="%s">%s</a>' % (h, k, t) for k, h, t in NAV)
    corpo = '\n'.join([view('inicio', INICIO, True), view('funciona', FUNCIONA), view('anvisa', ANVISA), view('entrega', ENTREGA)])
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>iLabPharma · Do insumo ao lote liberado</title>
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="iLabPharma: gestão da produção de medicamentos e vacinas, do recebimento do insumo à liberação do lote, com as exigências da ANVISA como guia.">
<link rel="icon" href="assets/ilabpharma-logo-claro.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="pitch.css">
</head>
<body data-pag="inicio">
<a class="pular" href="#funciona">Ir para o conteúdo</a>
<header class="topo" id="topo">
  <a class="marca" href="#inicio" aria-label="iLabPharma, início"><img src="assets/ilabpharma-logo-claro.svg" alt="iLabPharma"></a>
  <nav aria-label="Capítulos">%s</nav>
  <button type="button" class="tela-cheia" id="telaCheia" aria-label="Tela cheia (tecla F)" title="Tela cheia (F)">⤢ <span>Tela cheia</span></button>
</header>
<main id="conteudo">
%s
</main>
<nav class="seq" id="seq" aria-label="Roteiro da apresentação"></nav>
<script src="dados/dados.js"></script>
<script src="pitch.js"></script>
</body>
</html>
''' % (nav, corpo)

def redirecionador(destino_padrao, alvo):
    return '''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="robots" content="noindex, nofollow"><title>iLabPharma</title>
<script>location.replace('index.html' + (location.hash || '%s'));</script>
<noscript><meta http-equiv="refresh" content="0;url=index.html%s"></noscript></head>
<body><p><a href="index.html%s">Abrir a apresentação do iLabPharma</a></p></body></html>
''' % (destino_padrao, destino_padrao, destino_padrao)

arquivos = {
    'index.html': pagina_unica(),
    'funciona.html': redirecionador('#industria', 'funciona'),
    'anvisa.html': redirecionador('#g0', 'anvisa'),
    'entrega.html': redirecionador('#entrega', 'entrega'),
}
for nome, html in arquivos.items():
    open(os.path.join(SAIDA, nome), 'w', encoding='utf-8').write(html)
    print('Gerado', nome)
