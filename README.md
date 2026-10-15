# iLabPharma · Apresentação

Pitch de vendas do iLabPharma, em uma página: **como o sistema funciona**, **aderência às normas da ANVISA** e **o que será entregue**.

## Como abrir

Site estático, sem build. Abra `index.html` no navegador (funciona também por duplo clique) ou sirva a pasta:

```
python3 -m http.server 8000
```

A fonte (Inter e Manrope) vem do Google Fonts; sem internet o texto usa a fonte padrão.

## A apresentação: um roteiro, do início ao fim

O presenter só avança: botão **Próximo** (ou seta →) em todas as telas; **Anterior** (ou seta ←) volta uma tela. A barra fixa mostra o capítulo, o progresso e o nome da próxima tela.

| Capítulo | Telas | Arquivo |
|---|---|---|
| Início | 1 | `index.html`: promessa, trilho do lote e o botão "Iniciar a apresentação" |
| Como funciona | 14 (7 etapas × visão geral e fluxos) | `funciona.html`: 37 fluxos de processo; o primeiro de cada etapa já vem aberto; botão "Ampliar o fluxo" |
| Normas da ANVISA | 7 (um grupo por tela) | `anvisa.html`: 35 exigências da RDC 658/2022 e do Guia 33/2020 e a resposta do iLabPharma |
| O que entregamos | 7 cenas | `entrega.html`: o que o cliente ganha, além do sistema |

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `index.html`, `funciona.html`, `anvisa.html`, `entrega.html`, `pitch.css`, `pitch.js` | As páginas (geradas por `montar_paginas.py`; sem conteúdo próprio) |
| `dados/dados.js` | Conteúdo, gerado |
| `ferramentas/conteudo.py` | O texto de venda: editar aqui |
| `ferramentas/montar_paginas.py` | Gera as quatro páginas HTML |
| `ferramentas/montar_dados.py` | Gera `dados/dados.js` a partir do texto e dos fluxos da homologação |
| `ferramentas/equipe-fluxos.json` | Fluxos de Recebimento e Quarentena (documentos da equipe) |
| `jornada-anterior.html` e arquivos `journey-*`, `home.*`, `app.js`, `styles.css`, `fluxo-*.html` | Apresentação anterior (copiada do iLabPharma), só como referência |
| `assets/`, `imagens/` | Logos, ilustrações e fluxogramas |

Regras de trabalho e decisões do responsável: `CLAUDE.md`.
