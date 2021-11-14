from PIL.Image import BILINEAR
from wordcloud import WordCloud as wc
import matplotlib.pyplot as plt

#sample data dictionary 
sample_dict = {"cat": 5, "dog": 26, "catlover": 80, "dogsofinstagram": 100, "cutecat": 87 }

#create the cloud
bkgrnd_color = input("Enter background color: \n")
word_color = input("Enter word color story: \n")
# list of color options can be found here: https://matplotlib.org/stable/tutorials/colors/colormaps.html


hashtag_cloud = wc(background_color = bkgrnd_color, colormap= word_color, height = 1000, width = 1000, max_words = 10)
hashtag_cloud.generate_from_frequencies(sample_dict)

#show the cloud
plt.imshow(hashtag_cloud)
plt.axis("off")
plt.show()

