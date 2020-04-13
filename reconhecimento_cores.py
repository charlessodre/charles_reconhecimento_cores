# coding=utf-8
import cv2
import numpy as np

print(cv2.__version__)

# define range colors in HSV

# vermelho
lower_red = np.array([158, 232, 147])
upper_red = np.array([198, 255, 226])

# laranja
lower_orange = np.array([175, 149, 184])
upper_orange = np.array([210, 212, 230])

# verde
lower_green = np.array([51, 107, 128])
upper_green = np.array([82, 255, 190])

# azul
lower_blue = np.array([81, 138, 133])
upper_blue = np.array([109, 219, 219])

# amarelo
lower_yellow = np.array([4, 181, 88])
upper_yellow = np.array([24, 255, 255])

# roxo
lower_purple = np.array([110, 88, 120])
upper_purple = np.array([156, 159, 201])

# rosa
lower_pink = np.array([153, 112, 183])
upper_pink = np.array([188, 174, 248])

# branco
lower_white = np.array([0, 0, 255])
upper_white = np.array([255, 255, 255])

# marrom
lower_brown = np.array([157, 74, 0])
upper_brown = np.array([223, 216, 70])


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
    min_contour_area = 500
    contourArea = cv2.contourArea(max_area)

    threshold_reached = contourArea > min_contour_area

    if threshold_reached:
        rectangle = cv2.minAreaRect(max_area)
        box = cv2.boxPoints(rectangle)
        box_int64 = np.int0(box)

        cv2.drawContours(image, [box_int64], 0, contour_color, 3)

    return threshold_reached


def color_tracking(image, color_mask, contour_color, color_name):
    contours = get_contours(color_mask)

    if len(contours) > 0:
        if draw_color_contours(image, contours, contour_color):
            moments = cv2.moments(contours[-1])
            centroid = get_moments_centroid(moments)
            # cv2.circle(frame, centroid, 5, contour_color, thickness=-1)
            cv2.putText(image, color_name, centroid, cv2.FONT_HERSHEY_PLAIN, 1, contour_color)


# Caputura o video
webcam = cv2.VideoCapture(0)
_, frame = webcam.read()

# Define as configurações para salvar o frame
output_video = "./output/saida_video.mp4"
save_frame = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 10,
                             (frame.shape[1], frame.shape[0]))

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
    white_mask = get_color_mask(frame_hsv, lower_white, upper_white)
    brown_mask = get_color_mask(frame_hsv, lower_brown, upper_brown)

    color_tracking(frame, blue_mask, (255, 0, 0), 'azul')
    color_tracking(frame, green_mask, (0, 255, 0), 'verde')
    color_tracking(frame, red_mask, (0, 0, 255), 'vermelho')
    color_tracking(frame, yellow_mask, (0, 255, 255), 'amarelo')
    color_tracking(frame, pink_mask, (255, 0, 255), 'rosa')
    color_tracking(frame, purple_mask, (255, 85, 170), 'roxo')
    color_tracking(frame, orange_mask, (0, 102, 255), 'laranja')
    color_tracking(frame, white_mask, (255, 255, 255), 'branco')
    color_tracking(frame, brown_mask, (0, 51, 102), 'marrom')

    cv2.imshow("video", frame)
    save_frame.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release all resources.
save_frame.release()
webcam.release()
cv2.destroyAllWindows()
