import cv2
import face_recognition

# Carregue a imagem do seu rosto para comparação
imagem_rosto = face_recognition.load_image_file("foto rosto.jpg")
encodings_rosto = face_recognition.face_encodings(imagem_rosto)[0]

# Inicialize a captura de vídeo da webcam
captura = cv2.VideoCapture(0)

while True:
    # Capture um quadro da webcam
    ret, quadro = captura.read()

    # Encontre todos os rostos no quadro
    rostos = face_recognition.face_locations(quadro)
    
    for rosto in rostos:
        # Extraia as codificações faciais do quadro
        encodings_quadro = face_recognition.face_encodings(quadro, [rosto])[0]

        # Compare as codificações do rosto do quadro com o seu rosto
        comparacoes = face_recognition.compare_faces([encodings_rosto], encodings_quadro)

        if True in comparacoes:
            # Se a comparação for verdadeira, é você
            nome = "leo"
        else:
            # Se não for verdadeira, não é você
            nome = "Desconhecido"

        # Desenhe um retângulo ao redor do rosto no quadro
        (top, right, bottom, left) = rosto
        cv2.rectangle(quadro, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(quadro, nome, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Exiba o quadro resultante
    cv2.imshow('Reconhecimento Facial', quadro)

    # Encerre o loop quando pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura e feche a janela
captura.release()
cv2.destroyAllWindows()
