import cv2

def process_image(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blur, 50, 150)

    resized = cv2.resize(edges, (640,480))

    # cv2.imwrite(image_path.split(".")[0]+"gray.jpg", gray)
    # cv2.imwrite(image_path.split(".")[0]+"blur.jpg", blur)
    # cv2.imwrite(image_path.split(".")[0]+"edges.jpg", edges)
    cv2.imwrite("output/resized.jpg", resized)

    return resized