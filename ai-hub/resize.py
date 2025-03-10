import cv2
import sys

def resize_image(image_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    # Find nearest multiples of 32
    new_w = 640 #(w // 32) * 32
    new_h = 640 #(h // 32) * 32

    if new_w != w or new_h != h:
        print(f"Resizing image from ({w}, {h}) to ({new_w}, {new_h})")
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
        cv2.imwrite(image_path, img)
    else:
        print("Image dimensions are already valid.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize.py <image_path>")
        sys.exit(1)
    resize_image(sys.argv[1])