FastTag System
Overview
The FastTag System is a toll payment solution that leverages QR code technology for vehicle identification and transaction recording. It includes:

A QR Code Generator GUI built with Tkinter that generates and stores QR codes for vehicles.
A QR Code Scanner utilizing a camera to decode QR codes, identify vehicles, and record transactions in a MySQL database.
Features
QR Code Generation: Create unique FastTags for each vehicle with relevant details (Owner Name, Vehicle Number, Mobile Number, Vehicle Type) stored in a MySQL database.
QR Code Scanning: Capture and decode FastTags in real-time using OpenCV and Pyzbar libraries. Automatically identify the vehicle type, apply toll charges, and log transactions.
Database Integration: All vehicle and transaction data is securely stored in a MySQL database.
Technologies Used
Languages: Python
Libraries:
cv2 (OpenCV): For camera and image processing.
pyzbar: For decoding QR codes.
qrcode: For generating QR codes.
tkinter: For building the GUI.
Pillow: For handling image resizing.
MySQL Connector: For interacting with the MySQL database.
Database: MySQL
Project Structure
QR Code Generator GUI:
Generates and saves FastTags (QR codes) containing vehicle information.
Inserts vehicle details and FastTag codes into the MySQL database.
QR Code Scanner:
Captures QR codes using a camera, decodes them, and retrieves vehicle information.
Charges toll fees based on vehicle type and logs the transaction in the database.
