# coding=utf-8
import cv2

filter_type = 'HSV'
name_window = 'image'
limits = ("min", "max")


def get_trackbar_values(filter_type, name_window, limits):
    values = []

    for i in limits:
        for j in filter_type:
            val = cv2.getTrackbarPos("{}-{}".format(j, i), name_window)
            values.append(val)

    return values

def nothing(x):
    pass

def show_trackbars(filter_type, name_window, limits):
    cv2.namedWindow(name_window)

    for i in limits:
        value = 0
        if i == "max":
            value = 255

        for j in filter_type:
            cv2.createTrackbar("{}-{}".format(j, i), name_window, value, 255, nothing)

show_trackbars(filter_type, name_window, limits)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam!")
    exit()

while True:

    _, frame = webcam.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    min_val1, min_val2, min_val3, max_val1, max_val2, max_val3 = get_trackbar_values(filter_type, name_window, limits)

    mask = cv2.inRange(hsv_frame, (min_val1, min_val2, min_val3), (max_val1, max_val2, max_val3))

    frame_result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.putText(frame_result, "Lower color (HSV): H={}, S={}, V={}".format(min_val1, min_val2, min_val3), (10, 20),
                cv2.FONT_HERSHEY_PLAIN, 1,
                (0, 255, 255))
    cv2.putText(frame_result, "Upper color (HSV): H={}, S={}, V={}".format(max_val1, max_val2, max_val3), (10, 40),
                cv2.FONT_HERSHEY_PLAIN, 1,
                (0, 255, 255))

    cv2.imshow(name_window, frame_result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release all resources.
webcam.release()
cv2.destroyAllWindows()
