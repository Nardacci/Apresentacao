# Apresentação iLabPharma: regras de trabalho

## Contexto
- **Pitch de vendas** (site estático, sem build) para apresentar o iLabPharma a clientes. Abrir pelo `index.html`. Estrutura no `README.md`.
- A apresentação antiga (jornada de oito etapas, copiada do iLabPharma) ficou em `jornada-anterior.html`, só como referência.
- Origem: copiado em 15/10/2026 de `Nardacci/iLabPharma` (`apresentacao.html`). A documentação de homologação, que alimenta o conteúdo, está em `Nardacci/LabMedsys_homol` (pasta `homologacao/`, privada) e o portal em `Nardacci/iLabPharma`. Aqui não se copia o portal.

## Decisões do responsável
**15/10/2026, primeira rodada**
1. **Nada de segurança**: achados, acessos, senhas, chaves e strings de conexão nunca entram. Os temas 1 e 2 (acesso e senha) e 7 (banco) do diagnóstico ficam fora.
2. **Sem inventar**: todo número, nome de tela, fluxo ou regra vem da documentação e deve poder ser conferido.
3. **É um pitch de vendas, não uma página técnica**: sem códigos, manuais nem termos de homologação. O cliente deve entender como o iLabPharma funciona, ver a aderência às normas da ANVISA e sentir expectativa e experiência. Layout livre.
4. **Nenhuma falha, defeito ou limitação** aparece. Módulos não testados (Comercial, Rastreabilidade, OPE) podem ser descritos pelo que o código prevê.

**15/10/2026, segunda rodada (corrige a primeira)**
5. **O que se vende é a versão nova.** O legado (LabMedSys, aquisição da empresa) é só referência para não construir do zero e **não será comercializado**: a página nunca fala em legado, em "será entregue" nem em "base pronta". O conteúdo do legado e os requisitos levantados descrevem o que o iLabPharma é capaz de fazer.
6. **"O que entregamos" é experiência, não lista de funções** (como a Coca-Cola não entrega refrigerante nem a Nike entrega tênis): cenas que dizem o que o cliente ganha (certeza, tranquilidade, uma só verdade, confiança, orgulho), sem números.
7. **Telas e fontes menores; quatro páginas separadas; fluxos ampliáveis** (tela cheia, zoom e arraste).

**15/10/2026, terceira rodada**
8. **A apresentação é um roteiro em linha reta, do início ao fim, sem idas e vindas**: Início, Como funciona (cada etapa em duas telas: visão e fluxos, com o primeiro fluxo já aberto), Normas da ANVISA (uma tela por grupo) e O que entregamos (cenas). Barra fixa em todas as telas com Anterior e Próximo (mostrando o nome da próxima tela) e setas do teclado. Poucos cliques; o presenter só avança.
9. **Contatos** do fecho (Sidnei e Alex Arruda) estão guardados em `homologacao/apresentacao/contatos.md` do repositório privado. **Não publicar** até o responsável mandar. O código já aceita `D.contatos` (nome, e-mail, celular) na última cena.

**Atenção:** a versão nova **não foi analisada** aqui. Os itens que vieram de requisito (e não do que o legado já faz) estão no documento interno `homologacao/apresentacao/itens-a-confirmar.md` do repositório privado `LabMedsys_homol`. **Confirmar com o desenvolvimento antes de mostrar a clientes.** Esse documento não vai para o site.

## Como o conteúdo é montado
- `ferramentas/conteudo.py`: o texto de venda (sete etapas, 35 temas da norma com `RESPOSTAS` para a página, cenas de "O que entregamos"). Editar aqui. `NORMAS` guarda a origem de cada item (já existe / requisito), só para o documento interno.
- `ferramentas/montar_paginas.py`: gera as quatro páginas HTML.
- `ferramentas/montar_dados.py`: lê o texto e os fluxos da homologação (`labmedsys_homol/homologacao/*/fluxos/*.fluxo.json`, só os títulos das etapas) e gera `dados/dados.js`. Os fluxos de Recebimento e Quarentena vêm de `ferramentas/equipe-fluxos.json` (documentos da equipe).
- `pitch.css` e `pitch.js` desenham as páginas; não têm conteúdo próprio.
- Depois de mudar `conteudo.py`: `python3 ferramentas/montar_dados.py <pasta homologacao> [arquivo do documento interno]` e, se mudar o cabeçalho, `python3 ferramentas/montar_paginas.py`.
- A cópia publicada fica em `Nardacci/iLabPharma`, pasta `pitch/`, **só com os arquivos do site** (sem `ferramentas/`, que cita o legado).

## Convenções
- Quem conduz é analista de negócio, não desenvolvedor: português claro.
- Antes de enviar, abrir no navegador (python `http.server` + Playwright, Chromium em `/opt/pw-browsers`) e conferir: sem erro de script, sem arquivo 404, jornada completa até o fim.
- Logo: usar `assets/ilabpharma-logo-claro.svg` em fundo escuro e `ilabpharma-logo.svg` em fundo claro.
