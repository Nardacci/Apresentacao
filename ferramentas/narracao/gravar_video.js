// Grava o vídeo da apresentação (index.html) tela a tela, com a duração de cada tela igual à do
// MP3 da narração (ferramentas/narracao/audio/NN-id.mp3) mais uma pausa. Sem áudio: o MP3 é
// juntado depois pelo montar_video.py.
//
// Uso: node ferramentas/narracao/gravar_video.js <url do index.html> <saida.webm> [duracoes.json]
//   duracoes.json: {"1": 12.3, "2": 18.0, ...} segundos por trecho (gerado pelo montar_video.py).
//   Sem o arquivo, usa 6 s por tela.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [url, saida, duracoesArq] = process.argv.slice(2);
if (!url || !saida) { console.error('uso: gravar_video.js <url> <saida.webm> [duracoes.json]'); process.exit(1); }
const duracoes = duracoesArq ? JSON.parse(fs.readFileSync(duracoesArq, 'utf8')) : {};
const PAUSA = 0.8;        // segundos de silêncio depois de cada trecho
const TROCA = 0.5;        // tempo da transição entre telas
const TOTAL = Object.keys(duracoes).length || 29;

(async () => {
  const b = await chromium.launch();
  const dir = path.dirname(path.resolve(saida));
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, recordVideo: { dir, size: { width: 1280, height: 720 } } });
  const p = await ctx.newPage();
  const erros = [];
  p.on('pageerror', e => erros.push(String(e)));
  p.on('response', r => { if (r.status() >= 400) erros.push(r.status() + ' ' + r.url()); });
  await p.goto(url);
  const marcas = [];
  let t = 0;
  for (let n = 1; n <= TOTAL; n++) {
    if (n > 1) { await p.keyboard.press('ArrowRight'); await p.waitForTimeout(TROCA * 1000); t += TROCA; }
    const dur = (duracoes[String(n)] || 6) + PAUSA;
    marcas.push({ n, inicio: t, duracao: dur });
    await p.waitForTimeout(dur * 1000);
    t += dur;
  }
  const video = p.video();
  await ctx.close(); await b.close();
  const gravado = await video.path();
  fs.renameSync(gravado, path.resolve(saida));
  fs.writeFileSync(path.resolve(saida) + '.marcas.json', JSON.stringify({ TROCA, PAUSA, marcas, erros }, null, 1));
  console.log('telas', TOTAL, 'duração', t.toFixed(1), 's', 'erros', JSON.stringify(erros));
})();
