import cv2
import numpy as np

print(cv2.__version__)
# color limits in BGR
# vermelho
lower_red = np.array([170, 100, 0])
upper_red = np.array([180, 255, 255])

# verde
lower_green = np.array([28, 60, 6])
upper_green = np.array([64, 255, 192])

# azul
lower_blue = np.array([164, 45, 45])
upper_blue = np.array([247, 11, 11])

# amarelo
lower_yellow = np.array([25, 124, 124])
upper_yellow = np.array([32, 255, 255])

# rosa
lower_pink = np.array([247, 220, 247])
upper_pink = np.array([115, 38, 115])

def get_moments_centroid(moments):
    return (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))


def get_contours(color_mask):
    image, contours = cv2.findContours(color_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return image


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


def color_tracking(image, color_mask, contour_color):
    contours = get_contours(color_mask)

    if len(contours) > 0:
        draw_color_contours(image, contours, contour_color)
        moments = cv2.moments(contours[-1])
        centroid = get_moments_centroid(moments)
        cv2.circle(image, centroid, 5, contour_color, thickness=-1)

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam!")
    exit()

while True:

    ret, frame = webcam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_mask = get_color_mask(hsv, lower_blue, upper_blue)
    green_mask = get_color_mask(hsv, lower_green, upper_green)
    red_mask = get_color_mask(hsv, lower_red, upper_red)
    yellow_mask = get_color_mask(hsv, lower_yellow, upper_yellow)
    pink_mask = get_color_mask(hsv, lower_pink, upper_pink)

    color_tracking(frame, blue_mask, (255, 0, 0))
    color_tracking(frame, green_mask, (0, 255, 0))
    color_tracking(frame, red_mask, (0, 0, 255))
    color_tracking(frame, yellow_mask, (0, 255, 255))
    color_tracking(frame, pink_mask, (255, 0, 255))

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libera os recursos.
webcam.release()
cv2.destroyAllWindows()
