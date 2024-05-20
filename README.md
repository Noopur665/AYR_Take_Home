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
        Clone the repository:

            git clone <repository_url>
            cd <repository_directory>

    3. Folder Structure
        fonts: Directory containing .ttf font files used for generating test images.
        Test Fonts: Directory where generated test images will be saved.
        data: Directory containing the dataset used for training the model, with subdirectories for each font, each containing images of that font.
        Font Classifier: Jupyter notebook for data wrangling, model training, and classification.
        Font image generation Script: Jupyter notebook to create test images from fonts folder and save it to Test fonts
        top_model.keras: The best model will be saved.

    4. Generating Test Font Images
        Create Test Font Images:
            Run the script to generate images with text rendered in different fonts for testing purposes.
                
