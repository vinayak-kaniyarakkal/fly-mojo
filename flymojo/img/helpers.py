import cv2
from PIL import Image
from pytesseract import image_to_string
from string import punctuation


def recognize_pan_data(image_array):
    pil_image = Image.fromarray(image_array)
    string_data = image_to_string(pil_image)
    if not string_data or string_data is None or string_data == '':
        return False
    string_data = string_data.replace('\n', ' ')
    special_chars = set(punctuation)
    special_chars.remove('/')
    for _char in string_data:
        if _char in special_chars:
            return False
    return string_data


def process_image(img_file_name):
    """
        Input image needs to be in 750x470 resolution
    """

    original_img = cv2.imread(img_file_name)

    # crop the portion of the image to extract the text data.
    cropped_img = original_img[110:400, 10:550]
    # cv2.imwrite('cropped_img.jpg', cropped_img)

    # perform an edge detection to extract the binary image and the edges.
    edged_img = cv2.Canny(cropped_img, 300, 400)
    # cv2.imwrite('edged_img.jpg', edged_img)

    # perform contour finding to get the contours and fill them with binary 1.
    img_contours, contours, hirarchy = cv2.findContours(edged_img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bounding_boxes = []
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        center = (x + w / 2, y + h / 2)
        if area > 100:
            x, y, w, h = x - 4, y - 4, w + 8, h + 8
            bounding_boxes.append((center, (x, y, w, h)))
            cv2.rectangle(img_contours, (x, y), (x + w, y + h), 100, -1)

    cv2.imwrite('img_contours.jpg', img_contours)

    img_contours2, contours2, hirarchy2 = cv2.findContours(img_contours.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    bounding_boxes2 = []
    recognized_params = []
    for i, contour in enumerate(contours2):
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        if area > 2000:
            x, y, w, h = x - 4, y - 4, w + 8, h + 8
            bounding_boxes2.append((center, (x, y, w, h)))
            cv2.rectangle(img_contours2, (x, y), (x + w, y + h), 200, -1)
            contour_cropped = cropped_img[y:(y + h), x:(x + w)]
            import pdb; pdb.set_trace()
            if recognize_pan_data(contour_cropped):
                recognized_params.append(recognize_pan_data(contour_cropped))

    pan_data = {'pan': '', 'dob': '', 'father_name': '', 'name': ''}
    pan_labels = ['pan', 'dob', 'father_name', 'name']
    if len(recognized_params) > 4:
        for i in range(len(recognized_params) - 4):
            pan_labels.append('data_' + str(i))

    for i, param in enumerate(recognized_params):
        pan_data.update({pan_labels[i]: param})
        if param and param.replace('/', '').isdigit():
            pan_data.update({'dob': param})

    return pan_data

img_file_name = r'C:\Users\37946\Desktop\Vinayak\rnd\flymojo\flymojo\img\sample-test-PAN5.jpg'  # 'sample-test-PAN2.jpg'
print process_image(img_file_name)
