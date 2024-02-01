**Predictive Models for Mortality, Major Bleeding, and Venous Thromboembolism**

_Overview_
This Django project provides predictive models for Mortality (M), Major Bleeding (MB), and Venous Thromboembolism (VTE). The models utilize input features provided through a web interface and return predictions based on pre-trained machine learning models.

_Project Structure_
m.html: Template for Mortality prediction results.
mb.html: Template for Major Bleeding prediction results.
vte.html: Template for VTE prediction results.
main.html: Main page template with links to different prediction pages.

_Dependencies_
Django
pandas
joblib
scikit-learn

_Installation_
Install the required dependencies using the following command:
pip install Django pandas scikit-learn joblib

Clone the repository:
git clone https://github.com/buttawb/MB-VTE-Prediction-.git

Navigate to the project directory:
cd your-repo

Run the Django development server:
python manage.py runserver
Access the web interface by visiting http://127.0.0.1:8000/ in your web browser.

Usage
Visit the main page at http://127.0.0.1:8000/.
Click on the respective links to access Mortality, Major Bleeding, and VTE prediction pages.
Enter the required input parameters and submit the form.
View the prediction results on the corresponding result pages (m.html, mb.html, vte.html).

_Model Files_
S.pkl: Pre-trained model file for Mortality prediction.
MB.pkl: Pre-trained model file for Major Bleeding prediction.
VTE.pkl: Pre-trained model file for VTE prediction.

_Important Notes_
Ensure that the necessary model files (S.pkl, MB.pkl, VTE.pkl) are present in the project directory.
Input validation is limited, and the application assumes valid numerical inputs. Additional validation can be added based on specific requirements.
Feel free to explore and adapt the project based on your needs. If you have any questions or issues, please don't hesitate to reach out to the project maintainers.

Disclaimer: This project is for educational and demonstration purposes. It is important to understand the limitations and considerations associated with predictive models in a real-world medical context. Consultation with medical professionals is advised for any decision-making based on the predictions provided by the models.
