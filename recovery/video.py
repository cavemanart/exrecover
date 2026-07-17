import cv2


def validate_video(path):

    cap=cv2.VideoCapture(
        path
    )

    ok=cap.isOpened()

    cap.release()

    return ok
