import cv2,numpy as np
img=cv2.imread("dipawali-wallpapers.png",1)
cv2.imshow("image",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
def swap_cols(arr, frm, to):
    arr[:,[frm, to]] = arr[:,[to, frm]]
for i in range(int(img.shape[1]/2)):
    for j in range(img.shape[2]):
        swap_cols(img, i,img.shape[1]-i-1)
cv2.imshow("image",img)
cv2.waitKey(1000)
cv2.imwrite("sangam.png",img)
#get_ipython().run_line_magic('pinfo', 'cv2.imshow')





