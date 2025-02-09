import boto3
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from botocore.exceptions import NoCredentialsError

# Inicializa o cliente Rekognition
rekognition_client = boto3.client("rekognition")

# Diretórios padrão
IMAGE_DIR = Path("images").resolve()
OUTPUT_DIR = Path("output").resolve()
OUTPUT_DIR.mkdir(exist_ok=True)  # Garante que a pasta de saída existe


class CelebrityRecognizer:
    def __init__(self, image_path: Path):
        self.image_path = image_path
        self.output_path = OUTPUT_DIR / f"{image_path.stem}-detected.jpg"

    def analyze_image(self):
        """Executa a análise de celebridades na imagem usando AWS Rekognition."""
        try:
            with self.image_path.open("rb") as img:
                response = rekognition_client.recognize_celebrities(Image={"Bytes": img.read()})
            return response
        except NoCredentialsError:
            print("Erro: Credenciais da AWS não encontradas!")
            return None

    def highlight_faces(self, detected_faces: list):
        """Desenha caixas azuis ao redor das faces das celebridades detectadas."""
        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  # Usar fonte padrão para evitar problemas

        width, height = image.size

        for celeb in detected_faces:
            box = celeb["Face"]["BoundingBox"]
            left = int(box["Left"] * width)
            top = int(box["Top"] * height)
            right = int((box["Left"] + box["Width"]) * width)
            bottom = int((box["Top"] + box["Height"]) * height)

            confidence = celeb.get("MatchConfidence", 0)
            if confidence > 90:
                draw.rectangle([left, top, right, bottom], outline="blue", width=3)

                text = celeb.get("Name", "Desconhecido")
                draw.text((left, top - 15), text, font=font, fill="white")

        image.save(self.output_path)
        print(f"✅ Imagem processada e salva: {self.output_path}")


def main():
    """Executa a detecção de celebridades em múltiplas imagens."""
    images = [
        IMAGE_DIR / "bbc.jpg",
        IMAGE_DIR / "msn.jpg",
        IMAGE_DIR / "neymar-torcedores.jpg",
    ]

    for img in images:
        if not img.exists():
            print(f"⚠️ Imagem não encontrada: {img}")
            continue

        recognizer = CelebrityRecognizer(img)
        response = recognizer.analyze_image()

        if response and response.get("CelebrityFaces"):
            recognizer.highlight_faces(response["CelebrityFaces"])
        else:
            print(f"👤 Nenhuma celebridade detectada em: {img}")


if __name__ == "__main__":
    main()
