# iLabPharma · Apresentação

Pitch de vendas do iLabPharma, em uma página: **como o sistema funciona**, **aderência às normas da ANVISA** e **o que será entregue**.

## Como abrir

Site estático, sem build. Abra `index.html` no navegador (funciona também por duplo clique) ou sirva a pasta:

```
python3 -m http.server 8000
```

A fonte (Inter e Manrope) vem do Google Fonts; sem internet o texto usa a fonte padrão.

## A página

1. **Início:** promessa, três números e o trilho do lote, que percorre as sete etapas sozinho.
2. **Como funciona:** sete etapas (Indústria, Materiais e armazenagem, Medicamento e fabricação, Controle da Qualidade, Garantia da Qualidade, Documentos, Produto acabado até o cliente), com o que o sistema faz, o resultado, as ligações com outros módulos e **35 fluxos de processo** desenhados na própria página. O botão "Seguir o lote" percorre as etapas.
3. **Normas da ANVISA:** 35 pontos da RDC 658/2022 e do Guia 33/2020, com filtro por grupo e por situação. Cada ponto mostra o que o iLabPharma já oferece e a próxima entrega.
4. **Evolução:** nove frentes de entrega, ligadas aos pontos da norma que fecham.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `index.html`, `pitch.css`, `pitch.js` | A página (sem conteúdo próprio) |
| `dados/dados.js` | Conteúdo, gerado |
| `ferramentas/conteudo.py` | O texto de venda: editar aqui |
| `ferramentas/montar_dados.py` | Gera `dados/dados.js` a partir do texto e dos fluxos da homologação |
| `ferramentas/equipe-fluxos.json` | Fluxos de Recebimento e Quarentena (documentos da equipe) |
| `jornada-anterior.html` e arquivos `journey-*`, `home.*`, `app.js`, `styles.css`, `fluxo-*.html` | Apresentação anterior (copiada do iLabPharma), só como referência |
| `assets/`, `imagens/` | Logos, ilustrações e fluxogramas |

Regras de trabalho e decisões do responsável: `CLAUDE.md`.
