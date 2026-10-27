# Narração da apresentação

Três passos: o roteiro (aqui), a voz (OpenAI, no computador da pessoa) e a montagem do vídeo.

## 1. Roteiro

`roteiro.md` (para ler) e `roteiro.json` (para os scripts): 29 trechos, um por tela, na ordem da apresentação. O texto vem de `ferramentas/conteudo.py`. Para mudar a narração, edite o `roteiro.json` (ou refaça pelo `conteudo.py`) e apague o MP3 do trecho alterado.

## 2. Voz (no computador da pessoa, com crédito na OpenAI)

A chave fica só na variável de ambiente da janela, nunca em arquivo nem no git. No PowerShell:

```powershell
$s = Read-Host "Chave da OpenAI" -AsSecureString
$env:OPENAI_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))
cd <pasta do repositório Apresentacao>
python ferramentas\narracao\gerar_narracao.py --voz nova
```

Gera `audio/NN-id.mp3` (29 arquivos, uns 100 KB cada). Para ouvir uma voz antes de gerar tudo: `--so 1` gera só o primeiro trecho; apague o MP3 e troque `--voz` (alloy, ash, coral, echo, fable, nova, onyx, sage, shimmer). Custo: cerca de 1.000 palavras, bem abaixo de um dólar no `gpt-4o-mini-tts`.

Depois, `git add ferramentas/narracao/audio` e envie o ramo: a montagem pode ser feita em qualquer máquina com os MP3.

## 3. Montagem do vídeo

Precisa de `node` com Playwright, `ffmpeg` e `ffprobe`.

```bash
python3 -m http.server 8765 &          # na pasta do repositório
python3 ferramentas/narracao/montar_video.py --saida apresentacao-narrada.mp4
```

O script mede cada MP3, grava a apresentação com cada tela durando o tempo da sua narração mais 0,8 s de pausa e junta o áudio. O resultado (1280×720, H.264 + AAC) não vai para o git: publique em `Nardacci/iLabPharma` na pasta `pitch/video/`.
