# AYR_Take_Home
This project develops a machine learning model capable of classifying text images based on the font used. The classifier can distinguish among ten different fonts, making it a valuable tool for graphic designers, typographers, and software applications needing automated font recognition. 

The project includes scripts to create font images and scripts demonstrating data wrangling, model training, and classification methods. 

Additionally, it saves the best model during training, which can be used for making predictions on new images.

<b> Setup Instructions </b>

    1.Prerequisites
        Ensure you have the following installed:

            Python 3.6+
            pip (Python package installer)
            
    2. Installation
        a. Clone the Repository
            git clone <repository_url>
            cd <repository_directory>
        b. Install Requirred packages
            pip install -r requirements.txt
            
    3. Folder Structure
        fonts: Directory containing .ttf font files used for generating test images.
        data: Directory containing the dataset used for training the model, with subdirectories for each font, each containing images of that font.     
        Test Fonts: Directory where generated test images will be saved. The images are generated using the Font image generation Script.ipynb        
        Font image generation Script.ipynb: python notebook used to generate images using fonts directory and saved in Test Fonts Directory.
        Font Classifier.ipynb: Python notebook containing scripts demonstrating data wrangling, model training, and classification methods.
        Font Classifier.py: The file used to test the saved model by providing the input image.
        top_model.keras: Final model with best weights.   
        requirements.txt: Used to install the required packages.
        Documentation.docx: This docx file contains documentation on Data Collection & Preparation and Evaluation Metrics
        
    4. Running the Script
    
        a. Generating Test Font Images: 
            i.     Test Font Generation.py - This python script file is used to generate the font images using .ttf file.
            ii.    Below are the path variables used to access the path mentioned for .ttf files and output location respectively.
                        fonts_path = 'fonts'
                        output_path = 'Test Fonts'
            iii.   By running the below script, the output images will be available in Test Fonts Directory.
                
                        python Test\ Font\ Generation.py
                
        b. Loading the saved model and Predicting Fonts on the images:
            i.     Font Classifier.py - This python script is used to load the saved model and predicting the font for the images present in Test Fonts directory.
            ii.    The input path can be changed in the script for variable "img_path='Test Fonts'"
            iii.   Please make sure that the top_model.keras is present at the root level. It will by default be present at root when cloned. 
            iv.    By running below script, the model will be loaded and will start predicting fonts for images present in Test Fonts.

                        python Font\ Classifier.py
