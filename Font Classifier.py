from keras.models import load_model
import os

model = load_model('top_model.keras')

img_path='Test Fonts'

def rev_conv_label(label):
    labels = [
        'AguafinaScript', 'AlexBrush', 'Allura', 'alsscrp', 'Canterbury',
        'GreatVibes', 'Holligate Signature', 'I Love Glitter', 'James Fajardo', 'OpenSans'
    ]
    return labels[label]


# Process each image in the directory
for image_file in os.listdir(img_path):
    try:
    
        # Construct full image path
        full_path = os.path.join(img_path, image_file)
    
        # Open, convert to RGB, and convert to array
        pil_im = PIL.Image.open(full_path).convert('RGB')
        pil_im = pil_im.resize((105, 105))
        org_img = img_to_array(pil_im)
        org_img = np.expand_dims(org_img, axis=0)  # Model expects a batch of images

        # Normalize the image
        org_img = org_img.astype('float') / 255.0

        # Predict the font
        y = model.predict(org_img)
        y = np.argmax(y, axis=1)  # Get the index of the max log-probability
        label = rev_conv_label(y[0])  # Convert numerical label to actual font name

        # Plot and annotate image with predicted label
        fig, ax = plt.subplots()
        ax.imshow(pil_im, cmap='gray')
        ax.axis('off')  # Hide axes
        ax.text(5, 5, label, color='blue', bbox=dict(facecolor='white', alpha=0.75, edgecolor='none', boxstyle='round,pad=0.5'))
        plt.show()
    except:
        None