import cv2
import numpy as np

print(cv2.__version__)

# define range color in HSV

# vermelho
lower_red = np.array([166, 174, 74])
upper_red = np.array([182, 255, 219])

# verde
lower_green = np.array([59, 0, 8])
upper_green = np.array([101, 212, 48])

# azul
lower_blue = np.array([101, 130, 80])
upper_blue = np.array([128, 255, 188])

# amarelo
lower_yellow = np.array([14, 210, 105])
upper_yellow = np.array([29, 255, 143])

# roxo
lower_purple = np.array([139, 128, 13])
upper_purple = np.array([163, 255, 237])

# rosa
lower_pink = np.array([152, 158, 124])
upper_pink = np.array([181, 228, 245])


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

    color_tracking(frame, blue_mask, (255, 0, 0), 'azul')
    color_tracking(frame, green_mask, (0, 255, 0), 'verde')
    color_tracking(frame, red_mask, (0, 0, 255), 'vermelho')
    color_tracking(frame, yellow_mask, (0, 255, 255), 'amarelo')
    color_tracking(frame, pink_mask, (255, 0, 255), 'rosa')
    color_tracking(frame, purple_mask, (255, 85, 170), 'roxo')

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release all resources.
webcam.release()
cv2.destroyAllWindows()
