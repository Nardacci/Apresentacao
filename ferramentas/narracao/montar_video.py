"""Monta o vídeo narrado da apresentação: mede os MP3, grava o vídeo com a duração certa por tela
(gravar_video.js) e junta a narração (ffmpeg).

Uso: python ferramentas/narracao/montar_video.py [--url http://localhost:8765/index.html] [--saida apresentacao-narrada.mp4]

Precisa de: node com playwright, ffmpeg e ffprobe no PATH, e os MP3 em ferramentas/narracao/audio/
(gerados por gerar_narracao.py). Se faltar algum MP3, a tela correspondente fica 6 s em silêncio.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
AUDIO = AQUI / "audio"


def duracao(arq):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arq)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://localhost:8765/index.html")
    ap.add_argument("--saida", default=str(AQUI / "apresentacao-narrada.mp4"))
    a = ap.parse_args()
    seg = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))
    mp3 = {}
    for s in seg:
        arq = AUDIO / f"{s['n']:02d}-{s['id']}.mp3"
        if arq.exists():
            mp3[s["n"]] = arq
    faltam = [s["n"] for s in seg if s["n"] not in mp3]
    if faltam:
        print(f"AVISO: sem narração nos trechos {faltam} (ficam 6 s em silêncio)")
    dur = {str(s["n"]): (duracao(mp3[s["n"]]) if s["n"] in mp3 else 6.0) for s in seg}
    trab = AQUI / "trabalho"
    trab.mkdir(exist_ok=True)
    (trab / "duracoes.json").write_text(json.dumps(dur, indent=1))
    webm = trab / "video.webm"
    subprocess.run(["node", str(AQUI / "gravar_video.js"), a.url, str(webm), str(trab / "duracoes.json")], check=True)
    marcas = json.loads(Path(str(webm) + ".marcas.json").read_text())
    # Trilha de áudio: cada MP3 começa no instante em que a tela aparece (adelay), tudo misturado.
    entradas, filtros, rotulos = ["-i", str(webm)], [], []
    for i, m in enumerate(marcas["marcas"]):
        arq = mp3.get(m["n"])
        if not arq:
            continue
        entradas += ["-i", str(arq)]
        k = len(entradas) // 2 - 1
        ms = int(m["inicio"] * 1000)
        filtros.append(f"[{k}:a]adelay={ms}|{ms}[a{k}]")
        rotulos.append(f"[a{k}]")
    if not rotulos:
        sys.exit("Nenhum MP3 em audio/: gere a narração antes (gerar_narracao.py).")
    filtro = ";".join(filtros) + f";{''.join(rotulos)}amix=inputs={len(rotulos)}:normalize=0[aout]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", filtro,
                    "-map", "0:v", "-map", "[aout]", "-c:v", "libx264", "-crf", "24", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", a.saida],
                   check=True)
    print("vídeo narrado:", a.saida, f"({duracao(a.saida):.0f} s)")


if __name__ == "__main__":
    sys.exit(main())
