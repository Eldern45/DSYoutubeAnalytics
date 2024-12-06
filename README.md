# DSYoutubeAnalytics
### Analysing YouTube trends and training a video category prediction model

YouTube currently stands as one of the most popular platforms for video content consumption. YouTube's "trending" section highlights videos that have captured widespread attention in a specific region. Considering the immense popularity of the platform, and the fact that users' activity is what defines what videos will be trending, conclusions on broader societal interests could be made by looking at the YouTube trends. Analyzing the data from two major markets, the US and the UK, meaningful insights into media consumption and culture could be gathered. Such a project would have many benefits, ranging from what topics are currently captivating public attention of a country's media users, to helping creators align their content strategies with relevant topics. This project will seek to derive insights into viewing habits, content characteristics, and trends over time.


#### How to build and set project (with VSCode):
1. Download the project and open the project folder with VSCode.
2. Press Ctrl + Shift + P and type _"Python: Create Environment"_ (functionality was checked with Python 3.12.6)
3. VSCode will offer you to install dependencies from requirements.txt. If not, open the terminal and install them yourself with _pip install -r requirements.txt_.
4. For running Jupyter notebook files, you should install the offered extensions. After that, select the kernel (your created .venv).
5. To be able to run the prediction app, run all cells from the prediction.ipynb file. It will take 5-10 minutes. It will create _random_forest_model.pkl_, which is necessary for running the application.
6. Congratulations, you are all set!
