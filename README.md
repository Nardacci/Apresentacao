# iLabPharma · Apresentação

Pitch de vendas do iLabPharma, em uma página: **como o sistema funciona**, **aderência às normas da ANVISA** e **o que será entregue**.

## Como abrir

Site estático, sem build. Abra `index.html` no navegador (funciona também por duplo clique) ou sirva a pasta:

```
python3 -m http.server 8000
```

A fonte (Inter e Manrope) vem do Google Fonts; sem internet o texto usa a fonte padrão.

## As páginas

1. **Início** (`index.html`): promessa, o trilho do lote e três portas para as outras páginas.
2. **Como funciona** (`funciona.html`): sete etapas, nove módulos e 35 fluxos de processo, que podem ser ampliados em tela cheia. O botão "Seguir o lote" percorre as etapas.
3. **Normas da ANVISA** (`anvisa.html`): 35 exigências da RDC 658/2022 e do Guia 33/2020, com filtro por grupo e a resposta do iLabPharma a cada uma.
4. **O que entregamos** (`entrega.html`): sete cenas sobre o que o cliente ganha, além do sistema.

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
