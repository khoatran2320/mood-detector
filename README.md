# About

This project attempts to predict the attitude of a social media user based on their interactions on Twitter or Instagram.

## Built with help from

- [Tech With Tim](https://techwithtim.net/tutorials/ai-chatbot/part-4/)
- [Google Vision Tutorial](https://cloud.google.com/vision/docs/detecting-faces?authuser=1&apix_params=%7B%22resource%22%3A%7B%22requests%22%3A%5B%7B%22features%22%3A%5B%7B%22maxResults%22%3A10%2C%22type%22%3A%22FACE_DETECTION%22%7D%5D%2C%22image%22%3A%7B%22source%22%3A%7B%22imageUri%22%3A%22gs%3A%2F%2Fcloud-samples-data%2Fvision%2Fface%2Ffaces.jpeg%22%7D%7D%7D%5D%7D%7D#vision_face_detection-python)
- [Tensorflow Tutorial](https://developers.google.com/machine-learning/guides/text-classification/)
- [Code Drip](https://www.youtube.com/watch?v=d2GBO_QjRlo&t=464s)

## To run this application on your computer

#### Instagram

1. clone the repo
2. obtain Google Vision API key and credentials from [Google Cloud Console](https://console.cloud.google.com/)
3. change **InstaBot.py** scrape link to match targeted user
4. run `python3 insta/InstaBot.py` on terminal

#### Twitter

1. clone the repo
2. export your twitter account username and password and make sure they can be retrieved in **twitter/TwitterBot.py**
3. uncomment the last block of comments in **twitter/wordai.py**
4. run `python3 twitter/wordai.py` on terminal
5. you may want to re-train the model with more epochs and/or hidden layers for bettery accuracy. Just uncomment the training code, change the number of epochs and/or hidden layers, and comment the load model code

## Disclaimer

This application was built for personal use only. Data scraping may be unethical so please use with consideration and respect. Only for personal use.
