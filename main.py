import cv2
import SeguimientoManos as sm 

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
        print(dedos)
        cv2.putText(frame, str(contar), (445, 375), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 0), 25)
    
    cv2.imshow("Contando Dedos", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()
