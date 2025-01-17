import cv2
from ultralytics import YOLO

path_modelo = r"CAMINHO DO MODELO"
# Senha correta
senha_correta = ["paz", "rock", "joinha", "saudacao_vulcana"]


# Senha desafio
#senha_desafio = ["paz", "rock", "joinha", "vulcano", "vulcano","joinha","paz"]

print('Insira a senha: ')

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Verificar se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# Array com os gestos capturados
gestos_detectados = []

modelo = YOLO(path_modelo, task="detect")

while len(gestos_detectados) < len(senha_correta):
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    # Fazer a predição
    resultados = modelo.predict(frame, save=False, conf=0.5)

    # Processar os resultados
    for box in resultados[0].boxes:
        classe = int(box.cls)  # Índice da classe detectada
        gesto = modelo.names[classe]  # Nome da classe (mapeado pelo modelo treinado)
        if gesto not in gestos_detectados:
            gestos_detectados.append(gesto)
            print(f"Gesto detectado: {gesto}")

    # Exibir o feed da câmera
    try:
        frame = resultados[0].plot()
    except:
        print("NO DETECTIONS")
    cv2.imshow("Detecção de Gestos", frame)

    # Encerrar com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()

print("\nSequência detectada: ")
# Verificar se a sequência de gestos está correta
if gestos_detectados == senha_correta:
    print(gestos_detectados)
    print("Senha correta! Acesso liberado.")
else:
    print(gestos_detectados)
    print("Senha incorreta! Acesso negado.")
