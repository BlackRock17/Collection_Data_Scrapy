# Data Collection with Scrapy

This project aims to extract data from the website https://desktop.bg/computers-all using Scrapy. Follow the steps below to set up the project and collect the data.

---

# Steps to Start the Project

1. Create a new folder on your local machine where you want to store the project.
   
2. Open a terminal and navigate to the newly created folder. Clone the project from GitHub using the following command:
    ###git clone https://github.com/BlackRock17/Collection_Data_Scrapy.git###

3. After successful cloning, navigate to the project folder:
    ###cd Collection_Data_Scrapy###

4. Create a virtual environment (venv) for the project to isolate the dependencies:
    ###python -m venv venv###
   
5. Then activate the virtual environment:
  - For Windows:
         ###venv\Scripts\activate###
  - For Unix or MacOS:
         ###source venv/bin/activate###

6. Install the required packages listed in the requirements.txt file:
      ###pip install -r requirements.txt###
   
7. Navigate to the spiders folder within the project. The path may vary depending on the directory where you cloned the project. For example:
      ###cd data_collection\data_collection\spiders###
   
8. Start the data collection process using Scrapy:
      ###scrapy crawl computers###
   
9. Wait for the data collection process to complete. This may take around 5-7 minutes, depending on your internet speed and computer performance.

10. After the process is finished, a file named 'computers.db' will appear in the spiders folder, containing the collected data.
    
11. You should now have all the available computer configurations from the website 'https://desktop.bg/computers-all' in the database, excluding duplicates.
    I noticed that the database contains fewer computers than those on the website.
    After personally reviewing the data, I found that some computers and their configurations are repeated, with the only difference being the price and the presence of promotions.
    Due to this reason, the records in the database differ, as the code I have written does not allow duplicate entries.

---

# Note on Starting Scrapy
    
Despite the Scrapy documentation recommending starting the project from the main directory (in my case, D:\scrapy_project\Collection_Data_Scrapy\data_collection),
I encountered an error indicating a missing module whenever I tried. After watching several tutorials online, I noticed that everyone starts Scrapy after navigating to the spiders folder.
Therefore, I have shown this approach in step 6 of the instructions.

---

# Next Steps
        
After successfully extracting the data, you can proceed to the Django project (Computers_API).
You will find detailed information on how to start it in its README file.

Link to Computers_API: ###https://github.com/BlackRock17/Computers_API.git###

If you have any questions, feel free to contact me via email at lyyubo@gmail.com or by phone at 0895028398.
