import cv2
import numpy as np

print(cv2.__version__)

# define range colors in HSV

# vermelho
lower_red = np.array([168, 175, 173])
upper_red = np.array([191, 234, 255])

# laranja
lower_orange = np.array([0, 182, 45])
upper_orange = np.array([10, 222, 240])

# verde
lower_green = np.array([66, 136, 93])
upper_green = np.array([83, 236, 144])

# azul
lower_blue = np.array([101, 130, 80])
upper_blue = np.array([128, 255, 188])

# amarelo
lower_yellow = np.array([4, 181, 88])
upper_yellow = np.array([24, 255, 255])

# roxo
lower_purple = np.array([104, 107, 105])
upper_purple = np.array([131, 280, 143])

# rosa
lower_pink = np.array([160, 172, 112])
upper_pink = np.array([172, 255, 236])


def get_moments_centroid(moments):
    return (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))


def get_contours(color_mask):
    contours, _ = cv2.findContours(color_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_color_mask(hsv_image, lower_color, upper_color):
    color_mask = cv2.inRange(hsv_image, lower_color, upper_color)
    color_mask = cv2.erode(color_mask, None, iterations=2)
    color_mask = cv2.dilate(color_mask, None, iterations=2)

    return color_mask


def draw_color_contours(image, contours, contour_color):
    max_area = max(contours, key=cv2.contourArea)
    rectangle = cv2.minAreaRect(max_area)
    box = cv2.boxPoints(rectangle)
    box_int64 = np.int0(box)

    cv2.drawContours(image, [box_int64], 0, contour_color, 2)


def color_tracking(image, color_mask, contour_color, color_name):
    contours = get_contours(color_mask)

    if len(contours) > 0:
        draw_color_contours(image, contours, contour_color)
        moments = cv2.moments(contours[-1])
        centroid = get_moments_centroid(moments)
        # cv2.circle(frame, centroid, 5, contour_color, thickness=-1)
        cv2.putText(image, color_name, centroid, cv2.FONT_HERSHEY_PLAIN, 1, contour_color)


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam!")
    exit()

while True:

    ret, frame = webcam.read()

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_mask = get_color_mask(frame_hsv, lower_blue, upper_blue)
    green_mask = get_color_mask(frame_hsv, lower_green, upper_green)
    red_mask = get_color_mask(frame_hsv, lower_red, upper_red)
    yellow_mask = get_color_mask(frame_hsv, lower_yellow, upper_yellow)
    pink_mask = get_color_mask(frame_hsv, lower_pink, upper_pink)
    purple_mask = get_color_mask(frame_hsv, lower_purple, upper_purple)
    orange_mask = get_color_mask(frame_hsv, lower_orange, upper_orange)

    color_tracking(frame, blue_mask, (255, 0, 0), 'azul')
    color_tracking(frame, green_mask, (0, 255, 0), 'verde')
    color_tracking(frame, red_mask, (0, 0, 255), 'vermelho')
    color_tracking(frame, yellow_mask, (0, 255, 255), 'amarelo')
    color_tracking(frame, pink_mask, (255, 0, 255), 'rosa')
    color_tracking(frame, purple_mask, (255, 85, 170), 'roxo')
    color_tracking(frame, orange_mask, (85, 85, 255), 'laranja')

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release all resources.
webcam.release()
cv2.destroyAllWindows()
