# Apresentação iLabPharma: regras de trabalho

## Contexto
- Site estático (sem build) que apresenta o sistema a clientes: jornada de oito etapas e fluxogramas. Abrir pelo `index.html`. Estrutura no `README.md`.
- Origem: copiado em 15/10/2026 de `Nardacci/iLabPharma` (`apresentacao.html`). A documentação de homologação, que alimenta o conteúdo, está em `Nardacci/LabMedsys_homol` (pasta `homologacao/`, privada) e o portal em `Nardacci/iLabPharma`. Aqui não se copia o portal.

## Decisões do responsável (15/10/2026)
1. **Foco: o sistema legado** (o LabMedSys entregue pelo fornecedor, hoje chamado iLabMedSys/iLabPharma). Não descrever a nova versão.
2. **Não mostrar ao cliente falhas, defeitos nem limitações** achados nos testes. Mostrar o que o sistema tem e o que a norma exige.
3. **Nada de segurança**: achados, acessos, senhas, chaves e strings de conexão nunca entram.
4. **Sem inventar**: todo número, nome de tela, fluxo ou regra vem da documentação (código ou documentos da equipe) e deve poder ser conferido. Na dúvida, deixar de fora ou perguntar.
5. Como o cliente não vê falhas, **não afirmar que uma função "funciona" ou "cumpre a norma"** quando os testes mostraram o contrário. Descrever o que a função faz e o que a norma pede, sem declarar conformidade.

## Convenções
- Quem conduz é analista de negócio, não desenvolvedor: português claro.
- Antes de enviar, abrir no navegador (python `http.server` + Playwright, Chromium em `/opt/pw-browsers`) e conferir: sem erro de script, sem arquivo 404, jornada completa até o fim.
- Logo: usar `assets/ilabpharma-logo-claro.svg` em fundo escuro e `ilabpharma-logo.svg` em fundo claro.
