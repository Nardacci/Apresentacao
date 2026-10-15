# -*- coding: utf-8 -*-
"""Gera dados/dados.js a partir de conteudo.py e dos fluxos da homologação.

Uso: python3 ferramentas/montar_dados.py [pasta homologacao]
(padrão: ../labmedsys_homol/homologacao, repositório privado Nardacci/LabMedsys_homol)
Só os TÍTULOS das etapas dos fluxos são usados: as observações técnicas ficam de fora.
"""
import json, os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from conteudo import ETAPAS, GRUPOS, NORMAS, FRENTES, CENAS, RESPOSTAS

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
HOMOL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, '..', 'labmedsys_homol', 'homologacao')
EQUIPE = json.load(open(os.path.join(AQUI, 'equipe-fluxos.json'), encoding='utf-8'))

# Fluxos da equipe (Recebimento e Quarentena): fases por agrupamento de etapas
FASES_EQUIPE = {
    'recebimento': [('Estrutura e cadastros', [1, 2, 3, 4]), ('Inspeção e aprovação', [5, 6]), ('Recebimento e conferência', [7, 8]), ('Entrada e disponibilização', [9, 10, 11])],
    'quarentena': [('Parametrização e entrada', [1, 2]), ('Solicitação e amostragem', [3, 4, 5]), ('Análise', [6, 7]), ('Laudo e movimentação', [8, 9])],
}

def fluxo_homol(chave, nome, linha):
    pasta, arq = chave.split('/')
    d = json.load(open(os.path.join(HOMOL, pasta, 'fluxos', arq + '.fluxo.json'), encoding='utf-8'))
    fases = []
    for f in d['fases']:
        fases.append({'nome': f['nome'], 'etapas': [{'t': e['titulo'], 'dec': bool(e.get('decisao'))} for e in f['etapas']]})
    return {'nome': nome, 'linha': linha, 'fases': fases}

def fluxo_equipe(chave, nome, linha):
    k = chave[1:]
    passos = {s['n']: s for s in EQUIPE[k]['steps']}
    fases = [{'nome': n, 'etapas': [{'t': passos[i]['title'], 'dec': False} for i in nums]} for n, nums in FASES_EQUIPE[k]]
    return {'nome': nome, 'linha': linha, 'fases': fases}

etapas = []
total_fluxos = 0
for e in ETAPAS:
    x = {k: v for k, v in e.items() if k != 'fluxos'}
    x['fluxos'] = []
    for chave, nome, linha in e['fluxos']:
        x['fluxos'].append(fluxo_equipe(chave, nome, linha) if chave.startswith('@') else fluxo_homol(chave, nome, linha))
        total_fluxos += 1
    etapas.append(x)

# Na página, só o texto de RESPOSTAS. A origem (já tem / requisito) fica só no documento interno.
normas = [{'id': n[0], 'g': n[1], 'tema': n[2], 'norma': n[3], 'resposta': RESPOSTAS[n[0]]} for n in NORMAS]
totais = {'modulos': 9, 'fluxos': total_fluxos, 'temas': len(normas), 'grupos': len(GRUPOS)}
cenas = [{'a': c[0], 'b': c[1], 'apoio': c[2], 'modulos': c[3]} for c in CENAS]
dados = {'etapas': etapas, 'grupos': GRUPOS, 'normas': normas, 'cenas': cenas, 'totais': totais}

# Documento interno (não vai para o site): o que confirmar com o desenvolvimento da versão nova.
if len(sys.argv) > 2:
    linhas = ['# Itens a confirmar com o desenvolvimento da versão nova', '',
              'Estes itens aparecem na página "Dentro das normas da ANVISA" como capacidade do iLabPharma. Vêm de requisitos levantados na análise do legado (não existem lá). Antes de mostrar a clientes, confirmar que a versão nova os atende.', '']
    for n in NORMAS:
        if n[6]:
            linhas.append('## Tema %d · %s (%s)' % (n[0], n[2], n[3]))
            linhas += ['- [ ] ' + x for x in n[6]] + ['']
    open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(linhas))
    print('Documento interno:', sys.argv[2])
os.makedirs(os.path.join(RAIZ, 'dados'), exist_ok=True)
saida = os.path.join(RAIZ, 'dados', 'dados.js')
with open(saida, 'w', encoding='utf-8') as f:
    f.write('window.DADOS=' + json.dumps(dados, ensure_ascii=False, indent=1) + ';\n')
print('Gerado', saida, totais)
