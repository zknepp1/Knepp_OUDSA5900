# Project Title
AI Models for Investment Portfolio Development

# Description

This study set out to explore the role of news-driven neural networks, particularly in Recurrent Neural Networks, and building investment portfolios with the trained models. While incorporating news-related variables into Recurrent Neural Networks, the additional news variables on predictive accuracy within the models have shown to have a marginal effect. This study contributes to the field of AI and Financial Analysis as a reminder of the importance of data quality in the nature of stock price prediction. While neural networks prove to be a powerful tool for financial analysis and decision making, quantity and quality of data are crucial for building effective models.

The code in this project is divided up between the folders "no_news" and "with_news" to keep the predictions of both models separate. From the results of the study, the models that don't contain news variables are implemented in this github project.


# Installation Instructions

1. Clone repo into local directory.
2. Move to directory with: "cd Knepp_OUDSA5900"
3. Activate virtual environment: "source venv/bin/activate"
4. Install the necessary packages: "pip install -r requirements.txt"
5. Run the main file in the no_news folder: "python3 no_news/main.py"


# How to Use

Once the main program is executed, the program will ask the user for a list of stocks to put in the algorithmic trader.
Please keep in mind that the model building process is very time consuming. Make sure your machine has plenty of memory.

![image](https://github.com/zknepp1/Knepp_OUDSA5900/assets/41703755/1132876f-4271-41d9-8cf2-5ed06b641eb6)




Enter the stock labels one-by-one in all CAPS. When you are finished entering the stocks, type "EXIT"

![image](https://github.com/zknepp1/Knepp_OUDSA5900/assets/41703755/e4423011-d485-47cb-810b-ee996ee1a2a4)




If the data is entered correctly, the data is collected and the modeling process has begun.

![image](https://github.com/zknepp1/Knepp_OUDSA5900/assets/41703755/ee4e17d8-cf8b-4596-a802-0166402f983b)




Please wait till the program has finished executing and the program will spit out a suggested portfolio.
The below image is an example of the program, run on the stock labels: MOS and MMM

![image](https://github.com/zknepp1/Knepp_OUDSA5900/assets/41703755/f1660dba-4f1f-469a-8b0e-a3bcaa7a5c2f)




# Issues and Limitations
This biggest issues encountered in this project is time constraints, hardware constraints, and switching news datasets mid project. Depending on the hardware on the user's machine the program may face difficulty with training time for the models. I have tested that upward of 15 stock labels will cause the program to crash due to limited RAM. To get the results for the project, I simply divided the stock label work load into multiple sessions.







