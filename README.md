# iLabPharma · Apresentação (Process Experience)

Apresentação interativa do iLabPharma para clientes: uma jornada de oito etapas, do cadastro da indústria até o produto acabado, com fluxogramas dos processos.

Origem: copiada em 15/10/2026 do repositório `Nardacci/iLabPharma` (a antiga página inicial, hoje `apresentacao.html` lá). Esta cópia é independente: mudanças aqui não alteram o portal de homologação.

## Como abrir

Site estático, sem build. Abra `index.html` no navegador, ou sirva a pasta:

```
python3 -m http.server 8000
```

e acesse `http://localhost:8000`. A fonte (Inter e Manrope) vem do Google Fonts; sem internet o texto usa a fonte padrão.

## Navegação

1. **Início:** abertura com o botão "Iniciar jornada".
2. **Jornada:** passa por "Seguir" e "Continuar". Etapas: Indústria, Fábrica, Medicamento, Produção, Controle da Qualidade, Garantia da Qualidade, Produto Acabado.
3. **Fluxos:** cada etapa tem um item "Fluxo" que abre o fluxograma em tela cheia (`fluxo-*.html`), com zoom pela roda do mouse, duplo clique, `+` / `-` e `0` para voltar.
4. **Menu lateral** (visão de processos): Mapa de Processos, Processos, Módulos, Glossário e Sobre o Projeto.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `index.html` | Página única da apresentação |
| `app.js`, `home.js`, `journey*.js` | Lógica e conteúdo das telas e da jornada (os arquivos `-v4`, `-fix` e `stage*` são camadas sobrepostas, carregadas na ordem do `index.html`) |
| `styles.css`, `home.css`, `journey*.css` | Estilos |
| `fluxo-*.html` | Visualizador de cada fluxograma (zoom e arraste) |
| `assets/` | Logo e ilustrações SVG |
| `imagens/` | Fluxogramas e telas do sistema em PNG |

## Pendências conhecidas (levantadas na cópia)

- O logo SVG tem a palavra "Pharm" em cor escura e some no fundo escuro da abertura e do cabeçalho.
- As imagens `imagens/Sistema - *.png` não são usadas por nenhuma tela.
- O código foi sobreposto em camadas (vários `journey-*` que corrigem os anteriores); vale consolidar antes de crescer o conteúdo.
