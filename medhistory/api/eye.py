import cv2
import numpy as np
import math
import base64


def check_cataract(img_str):
	data = base64.b64decode(img_str)
	if ".png" in data:
		extension = ".png"
	else:
		extension = ".jpg"
	with open("test" + extension, "wb") as f:
		f.write(data)
	img = cv2.imread("test" + extension)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	#gray = gray[20:150,70:200].copy()

	cv2.imwrite('greyScale.png',gray)
	grayscale = gray
	#ret, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC )
	ret, gray = cv2.threshold(gray, 55, 255,  cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
	# gray = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	#  cv2.THRESH_BINARY_INV,11,2 )



	gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
	gray = cv2.morphologyEx(gray, cv2.MORPH_ERODE, np.ones((2, 2), np.uint8))
	gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))

	cv2.imwrite('catagray.png',gray)

	#find contours
	threshold = cv2.inRange(gray, 250, 255)
	conimg ,contours, heirarchy = cv2.findContours(
		threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
	)
	#cv2.imwrite('cont.png',conimg)
	c = None
	sec = None
	max = 0
	smax = 0
	for contour in contours:

		if cv2.contourArea(contour) > max:
			smax = max
			sec = c
			max = cv2.contourArea(contour)
			c = contour
		elif cv2.contourArea(contour) > smax:
			smax = cv2.contourArea(contour)
			sec = contour
		if cv2.contourArea(contour)>1000000 and cv2.contourArea(contour) < 1100000:
			smax = cv2.contourArea(contour)
			sec = contour


	# c = sec
	# max = smax
	center = cv2.moments(c)


	r = math.ceil((cv2.contourArea(c) / np.pi) ** 0.5)

	r = r * 0.7
	img2 = np.zeros_like(grayscale)

	cx = int(center['m10'] / center['m00'])
	cy = int(center['m01'] / center['m00'])
	cv2.circle(img2, (cx, cy), int(r), (255, 255, 255), -1)
	res = cv2.bitwise_and(grayscale, img2)
	resized = cv2.resize(res, (256, 256))

	cv2.imwrite('resized.png',res)

	mean, std = cv2.meanStdDev(resized)


	mean = mean[0][0]
	std = std[0][0]

	U = abs((1 - std / mean))

	points = 0


	count = 0
	sum = 0

	for x in resized:
		for y in x:
			if y!=0:
				sum = sum + y
				count = count + 1


	mean = sum/count

	deltaSum = 0
	for x in resized:
		for y in x:
			if y!=0:
				deltaSum = (y - mean ) ** 2
	std = (float(deltaSum)/count)**0.5
	print mean,
	print U,
	print std
	if U > 0.17:
		points += 1
	elif U < 0.09:
		points -= 1

	if mean > 134:
		points -= 1
	elif mean < 125.31:
		points += 1

	if std < 1.59:
		points += 1
	elif std > 3.18:
		points -= 1
	return points
