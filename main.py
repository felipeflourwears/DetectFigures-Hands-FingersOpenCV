import cv2
import SeguimientoManos as sm
import time
import requests

# Inicializa las variables de tiempo
start_time = time.time()
hand_present_time = 0
hand_absent_time = 0
hand_detected = False
dedos_anteriores = 0

detector = sm.detectormanos(Confdeteccion=0.75)
video_path = 'video.mp4'
#cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el cuadro, verifica la ruta del video o el formato del archivo.")
        break

    frame = detector.encontrarmanos(frame)

    cv2.rectangle(frame, (420, 225), (570, 425), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, "Dedos", (425, 420), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 5)

    manosInfo, cuadro = detector.encontrarposicion(frame, dibujar=True)
    #print(manosInfo)

    if manosInfo:
        dedos = detector.dedosarriba()
        contar = dedos.count(1)
        cv2.putText(frame, str(contar), (445, 375), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)

        if contar in [0, 1, 2, 3, 4, 5]:  
            hand_present_time = time.time() - start_time
            
            if hand_present_time >= 10 and not hand_detected:
                hand_detected_time = time.time()
                hand_detected = True
                # Continuar mostrando el contorno de los dedos durante los 10 segundos antes de reiniciar la detección
            elif hand_detected:
                if time.time() - hand_detected_time >= 10:
                    hand_detected = False
                    start_time = time.time()
                    same_fingers_time = 0  # Reiniciar el contador para la detección de la misma cantidad de dedos
            else:
                # Verificar si se mantiene la misma cantidad de dedos durante 3 segundos
                if contar == dedos_anteriores:
                    same_fingers_time = time.time() - start_time
                    if same_fingers_time >= 5 and not same_fingers_detected:
                        same_fingers_detected = True
                        # Imprimir el mensaje después de 3 segundos
                        
                        print(f"Hay {contar} dedos durante 3 segundos")
                else:
                    same_fingers_detected = False
                    start_time = time.time()
                    dedos_anteriores = contar

        else:
            hand_detected = False
            hand_absent_time = time.time() - start_time

    if hand_absent_time >= 10:
        start_time = time.time()

    cv2.imshow("Contando Dedos", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()