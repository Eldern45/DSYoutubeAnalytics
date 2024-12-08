# Project G2: YOUTUBE TRENDS
Analysing YouTube trends and training a video category prediction model

### TEAM:
Timofei Šinšakov (Gr 7)
Natalja Frantikova (Gr 4)
Andrei Potrebin (Gr 2)

### Motivation and goal

YouTube currently stands as one of the most popular platforms for video content consumption. YouTube's "trending" section highlights videos that have captured widespread attention in a specific region. Considering the immense popularity of the platform, and the fact that users' activity is what defines what videos will be trending, conclusions on broader societal interests could be made by looking at the YouTube trends. Analyzing the data from two major markets, the US and the UK, meaningful insights into media consumption and culture could be gathered. Such a project would have many benefits, ranging from what topics are currently captivating public attention of a country's media users, to helping creators align their content strategies with relevant topics. This project will seek to derive insights into viewing habits, content characteristics, and trends over time.

**The overall objective could be described in three distinct goals:**
1) Train a machine learning model to predict the category of a trending video based on its text attributes (title, tags and description).
2) Compare content in US and UK: we wanted to find out in what ways the trending videos of the two countries differed, and what differences were significant (p < 0.05).
3) Understand the temporal evolution of audience interests: we wanted to investigate which themes were popular during specific time periods.

### How to build and set project (with VSCode):
**IMPORTANT NOTE:** The datasets are not included in the repository. You need to download the necessary files [from this source](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv). The needed files are: US_category_id.json, US_youtube_trending_data.csv, GB_category_id.json, GB_youtube_trending_data.csv.

1. Download the project and open the project folder with VSCode.
2. Press Ctrl + Shift + P and type _"Python: Create Environment"_ (functionality was checked with Python 3.12.6)
3. VSCode will offer you to install dependencies from requirements.txt. If not, open the terminal and install them yourself with _pip install -r requirements.txt_.
4. For running Jupyter notebook files, you should install the offered extensions. After that, select the kernel (your created .venv).
5. To be able to run the prediction app, run all cells from the prediction.ipynb file. It will take 5-10 minutes. It will create _random_forest_model.pkl_, which is necessary for running the application.
6. Congratulations, you are all set!

### Guide to the repo contents:

3 Jupyter notebooks, each corresponding to one goal (see goals above).
* prediction.ipynb - a notebook where the prediction model was trained, tuned (for finding the best hyperparameters), and tested.
* comparison.ipynb - a notebook where trending videos from US and UK were compared. Contains tables where videos are ranked by different metrics (views, days in trends, likes), visualization of video categories and popular tags, binomial tests and more.
* Goal3.ipynb - a notebook where temporal analysis of trends was conducted.
Two JSON files from Kaggle which map each content category ID to the name of the category.
* GB_category_id.json - for the categories of the UK video dataset. Technically it is redundant since all the categories here are also included in the US category JSON, and that additionally has one more category.
* US_category_id.json - for the categories of the US video dataset.
Files related to category prediction model
* predict_app.py - a simple tkinter app where you can play around with the model. Enter the title, tags, and description of a hypothetical video and see what category the model predicts. Note that the tested accuracy is 85.7%, some categories are predicted more successfully than others, and there is some subjectivity in what category is best to choose.
* requirements.txt - build requirements. See the build guide above.
* vectorizer.pkl - a serialized version of a vectorizer object used in prediction.ipynb.
Other
* G2_report.pdf - a longer report explaining the goals and datasets in more detail, following CRISP-DM. (HW 10).
