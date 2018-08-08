import numpy as np
import matplotlib.pyplot as plt
def raw_loader(path='data/normal1.csv'):
  file = open(path)
  lines = file.readlines()
  res = {}
  for line in lines:
    sl = line.split(',')
    name = sl[0]
    cur_data = []
    for v in sl[1:]:
      cur_data.append(float(v))
    res[name] = cur_data
  return res

def sgn_to_img(sgn):
  dim = len(sgn)
  img = np.zeros((dim, dim))
  for i in range(dim):
    idx = round(sgn[i] * (dim - 1))
    img[dim-idx-1][i] = 255
    if idx > 0:
      img[dim-idx][i] = 125
    if idx < dim - 1:
      img[dim-idx-2][i] = 125
  return img

def sgns_to_imgs(sgns):
  imgs = []
  for sgn in sgns:
    imgs.append(sgn_to_img(sgn))
  return np.array(imgs)

def show_imgs(first):
  plt.figure(figsize=(15,5))
  plt.imshow(first)
  plt.show()
  return

if __name__ == '__main__':
  

  show_imgs(test_img)
