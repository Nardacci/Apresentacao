# Apresentação iLabPharma: regras de trabalho

## Contexto
- **Pitch de vendas** (site estático, sem build) para apresentar o iLabPharma a clientes. Abrir pelo `index.html`. Estrutura no `README.md`.
- A apresentação antiga (jornada de oito etapas, copiada do iLabPharma) ficou em `jornada-anterior.html`, só como referência.
- Origem: copiado em 15/10/2026 de `Nardacci/iLabPharma` (`apresentacao.html`). A documentação de homologação, que alimenta o conteúdo, está em `Nardacci/LabMedsys_homol` (pasta `homologacao/`, privada) e o portal em `Nardacci/iLabPharma`. Aqui não se copia o portal.

## Decisões do responsável (15/10/2026)
1. **Foco: o sistema legado** (o LabMedSys entregue pelo fornecedor, hoje chamado iLabMedSys/iLabPharma). Não descrever a nova versão.
2. **Não mostrar ao cliente falhas, defeitos nem limitações** achados nos testes. Mostrar o que o sistema tem e o que a norma exige.
3. **Nada de segurança**: achados, acessos, senhas, chaves e strings de conexão nunca entram.
4. **Sem inventar**: todo número, nome de tela, fluxo ou regra vem da documentação (código ou documentos da equipe) e deve poder ser conferido. Na dúvida, deixar de fora ou perguntar.
5. Como o cliente não vê falhas, **não afirmar que uma função "funciona" ou "cumpre a norma"** quando os testes mostraram o contrário. Descrever o que a função faz e o que a norma pede, sem declarar conformidade.

6. **É um pitch de vendas, não uma página técnica** (15/10/2026): sem códigos, manuais nem termos de homologação. O cliente deve (a) entender como o iLabPharma funciona, (b) ver a aderência às normas da ANVISA, com o que ainda não existe indicado como "será entregue", e (c) sentir expectativa e experiência.
7. **Layout livre**: pode mudar o modelo das telas e a navegação; não é preciso seguir a apresentação antiga.
8. **Fora da apresentação** (por segurança ou por serem falhas): temas de acesso e senha (1 e 2 do diagnóstico) e de banco de dados (7). Os demais temas aparecem como "Base pronta" (a função existe) ou "Será entregue", nunca como "atende" ou "não atende".
9. **Módulos não testados** (Comercial, Rastreabilidade, OPE) podem ser descritos pelo que o código prevê.

## Como o conteúdo é montado
- `ferramentas/conteudo.py`: o texto de venda (sete etapas da jornada, 35 temas da norma, nove frentes de evolução). Editar aqui.
- `ferramentas/montar_dados.py`: lê o texto e os fluxos da homologação (`labmedsys_homol/homologacao/*/fluxos/*.fluxo.json`, só os títulos das etapas) e gera `dados/dados.js`. Os fluxos de Recebimento e Quarentena vêm de `ferramentas/equipe-fluxos.json` (documentos da equipe).
- `pitch.css` e `pitch.js` desenham a página; não têm conteúdo próprio.
- Depois de mudar `conteudo.py`: `python3 ferramentas/montar_dados.py <pasta homologacao>`.

## Convenções
- Quem conduz é analista de negócio, não desenvolvedor: português claro.
- Antes de enviar, abrir no navegador (python `http.server` + Playwright, Chromium em `/opt/pw-browsers`) e conferir: sem erro de script, sem arquivo 404, jornada completa até o fim.
- Logo: usar `assets/ilabpharma-logo-claro.svg` em fundo escuro e `ilabpharma-logo.svg` em fundo claro.
