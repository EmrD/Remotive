import cv2
import numpy as np
import os
import pyautogui

pyautogui.FAILSAFE = False

kurulumpath = os.path.abspath("haarcascade_frontalface_default.xml").replace("haarcascade_frontalface_default.xml", "")
face_cascade = cv2.CascadeClassifier(kurulumpath + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(kurulumpath + 'haarcascade_eye.xml')
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)


def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame


def detect_eyes(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)
    width = np.size(img, 1)
    height = np.size(img, 0)
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye


def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]
    return img


def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    return keypoints


def is_eye_centered(center, img_width):
    center_threshold = 0.1 * img_width
    if center < img_width / 2 - center_threshold:
        pyautogui.move(30, 0)
        return "Right"
    elif center > img_width / 2 + center_threshold:
        pyautogui.move(-30, 0)
        return "Left"
    else:
        return "Centered"


def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('image')
    cv2.createTrackbar('threshold', 'image', 58, 255, lambda x: None)
    first_read = True

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 5, 1, 1)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))
        if len(faces) > 0:
                # Eye center detection
            threshold = cv2.getTrackbarPos('threshold', 'image')
            face_frame = detect_faces(frame, face_cascade)
            if face_frame is not None:
                eyes = detect_eyes(face_frame, eye_cascade)
                for eye in eyes:
                    if eye is not None:
                        eye = cut_eyebrows(eye)
                        keypoints = blob_process(eye, threshold, detector)
                        for keypoint in keypoints:
                            eye_center_x = int(keypoint.pt[0])
                            eye_centered = is_eye_centered(eye_center_x, eye.shape[1])
                            cv2.putText(frame, eye_centered + " Eye", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 255, 0), 2)
            for (x, y, w, h) in faces:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                roi_face = gray[y:y + h, x:x + w]
                roi_face_clr = frame[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50))

                if len(eyes) >= 2:
                    if first_read:
                        cv2.putText(frame, "Algılamaya Başladı", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
                        first_read = False
                    else:
                        cv2.putText(frame, "Eyes open!", (70, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                else:
                    if first_read:
                        cv2.putText(frame, "No eyes detected", (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
                    else:
                        print("Blink detected")
                        pyautogui.click()
                        first_read = True

        else:
            cv2.putText(frame, "No face detected", (100, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
