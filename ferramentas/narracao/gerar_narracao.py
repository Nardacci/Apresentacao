"""Gera a narração da apresentação com a API de voz da OpenAI (um MP3 por trecho do roteiro).

Uso (no computador da pessoa, com a chave só na variável de ambiente, nunca em arquivo):
    set OPENAI_API_KEY=...            (PowerShell: $env:OPENAI_API_KEY = Read-Host -AsSecureString ... ver LEIA-ME.md)
    python ferramentas/narracao/gerar_narracao.py [--voz nova] [--modelo gpt-4o-mini-tts] [--so 3,4]

Lê `roteiro.json` e grava `audio/NN-id.mp3`. Trechos já gravados são pulados (apague o MP3 para refazer).
Não precisa de biblioteca extra: usa só a biblioteca padrão do Python.
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROTEIRO = AQUI / "roteiro.json"
AUDIO = AQUI / "audio"
INSTRUCOES = ("Narração em português do Brasil, voz institucional, clara e calma, ritmo moderado, "
              "como um apresentador de produto para a indústria farmacêutica. Pronuncie 'iLabPharma' "
              "como 'ai-léb-farma' e 'ANVISA' como 'anvisa'.")


def falar(texto, voz, modelo, chave):
    corpo = {"model": modelo, "voice": voz, "input": texto, "response_format": "mp3"}
    if modelo.startswith("gpt-4o"):
        corpo["instructions"] = INSTRUCOES
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps(corpo).encode("utf-8"),
        headers={"Authorization": f"Bearer {chave}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voz", default="nova", help="alloy, ash, coral, echo, fable, nova, onyx, sage, shimmer")
    ap.add_argument("--modelo", default="gpt-4o-mini-tts")
    ap.add_argument("--so", default="", help="números dos trechos, separados por vírgula (ex.: 1,5)")
    a = ap.parse_args()
    chave = os.environ.get("OPENAI_API_KEY")
    if not chave:
        sys.exit("Defina OPENAI_API_KEY na variável de ambiente (nunca em arquivo).")
    so = {int(x) for x in a.so.split(",") if x.strip()}
    AUDIO.mkdir(exist_ok=True)
    seg = json.loads(ROTEIRO.read_text(encoding="utf-8"))
    feitos = 0
    for s in seg:
        if so and s["n"] not in so:
            continue
        destino = AUDIO / f"{s['n']:02d}-{s['id']}.mp3"
        if destino.exists():
            print(f"já existe: {destino.name}")
            continue
        print(f"gerando {destino.name} ({len(s['texto'].split())} palavras)...")
        destino.write_bytes(falar(s["texto"], a.voz, a.modelo, chave))
        feitos += 1
    print(f"{feitos} trecho(s) gerado(s) em {AUDIO}")


if __name__ == "__main__":
    main()
