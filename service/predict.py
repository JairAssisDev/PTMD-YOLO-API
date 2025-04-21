from ultralytics import YOLO
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Load model at startup
try:
    model = YOLO("models/best.pt")
except Exception as e:
    logger.error(f"Failed to load YOLO model: {e}")
    raise

async def diagnostic(img_array):
    if img_array is None:
        return {"predictions": [], "error": "Imagem inválida ou não fornecida"}

    try:
        results = model(img_array)

        # Definir os nomes das classes
        classes = ["Normal", "Anormal"]

        # Obter a classe prevista e a probabilidade
        for result in results:
            class_id = result.probs.top1  # Índice da classe predita (0 ou 1)
            probabilities = result.probs.data.tolist()  # Lista com as probabilidades de todas as classes
            
            # Exibir a classe predita e sua probabilidade
            print(f"Classe Predita: {classes[class_id]}")
            print(f"Probabilidade: {probabilities[class_id]:.4f}")
            predictions = [{
            "class": classes[class_id],
            "confidence": float(f"{probabilities[class_id]:.4f}")}]
            return {"predictions": predictions}

    except Exception as e:
        logger.error(f"Erro: {e}")
        return {"predictions": [], "error": str(e)}