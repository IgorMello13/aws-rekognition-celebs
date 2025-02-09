# 🎭 AWS Rekognition - Detecção de Celebridades

Este projeto utiliza **AWS Rekognition** para detectar celebridades em imagens.

## 🚀 Como Executar

### 1️⃣ Instalar Dependências
Antes de rodar o script, instale as dependências necessárias:

```bash
pip install boto3 mypy-boto3-rekognition
```

### 2️⃣ Configurar AWS Credentials
Para utilizar o AWS Rekognition, configure suas credenciais da AWS:

```bash
aws configure
```

Você precisará fornecer:
- AWS Access Key ID
- AWS Secret Access Key
- Região padrão da AWS

### 3️⃣ Executar o Script
Basta rodar o arquivo `main.py`:

```bash
python main.py
```

O script detecta celebridades na imagem `images/celebridade.jpg` e gera um `response.json` com os detalhes.

## 📈 Exemplo de Saída

```
✅ Imagem processada e salva: output/bbc-detected.jpg
✅ Imagem processada e salva: output/msn-detected.jpg
✅ Imagem processada e salva: output/neymar-torcedores-detected.jpg

## 📌 O Que Foi Modificado?
- 🔹 **Estrutura do código** melhorada com uma classe `CelebrityRecognizer`.
- 🔹 **Quadrado ao redor das faces agora é azul** (`"blue"` em vez de `"red"`).
- 🔹 **Fonte do texto foi alterada** para `ImageFont.load_default()` para compatibilidade.
- 🔹 **Organização das pastas** agora inclui `output/` para imagens processadas.