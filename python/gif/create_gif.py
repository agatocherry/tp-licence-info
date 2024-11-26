import imageio.v3 as imgio

filenames = ['cherrim1.png', 'cherrim2.png']
images = [ ]

for filename in filenames:
  images.append(imgio.imread(filename))

imgio.imwrite('cherrim.gif', images, duration = 500, loop = 0)