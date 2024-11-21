TestSSL Scanner Automation Tool

*Overview*

The TestSSL Scanner Automation Tool is designed to simplify SSL/TLS testing for multiple domains and ports. 
This tool automates the use of the testssl utility, saving results to a structured output file for easy analysis and sharing.

*Features*

Scans multiple domains and ports for SSL/TLS configurations and vulnerabilities.
Automatically saves detailed results in a testssl_scan_results.txt file.
Reduces manual effort and improves testing efficiency.

*Requirements Dependencies*

Python: Version 3.6 or higher.
Download Python

TestSSL Tool:
Download from TestSSL GitHub Repository.
Add the testssl tool to your system's PATH.

*Installation*

1. Clone or Download the Script
Clone the repository:
bash
Copy code
git clone <repository_link> Or , download the script directly as testssl_scanner.py.

2. Verify Python Installation
Ensure Python is installed by running:
bash
Copy code
python3 --version
If not installed, download and install it from https://www.python.org.

3. Install TestSSL
Download the testssl tool from the official repository.
Extract the files and add the directory to your system PATH:
Linux/Mac:
bash
Copy code
export PATH=$PATH:/path/to/testssl
Windows:
Add the path via "System Environment Variables" > "Path."

Usage

1. Prepare the Environment
Navigate to the folder containing the script:
bash
Copy code
cd <script_directory>

2. Run the Script
Execute the script to scan all configured domains and ports:
*bash
Copy code
python3 testssl_scanner.py*

3. View the Output
The results are saved in testssl_scan_results.txt in the script directory. Open this file to view detailed scan results.
Script Configuration
The script uses a dictionary to define the target domains and ports:

*python
Copy code
targets = {
    "api.example.in": [443, 2053, 2083, 2087, 2096, 8443],
    "apih.exaple.in": [443, 2053, 2083, 2087, 2096, 8443],
    # Add more domains and ports as needed
}*
To Add or Modify Targets:
Edit the targets dictionary in the script with the desired domains and ports.
Sample Output
The script produces an output file (testssl_scan_results.txt) with results like:

plaintext
Copy code
Starting testssl scan for api.prod.payglocal.in on port 443...
---------------------------------------------
Scan results for api.prod.example.in:443
- Supported Protocols: TLSv1.2, TLSv1.3
- Vulnerabilities: None found
...
---------------------------------------------
Starting testssl scan for apih.Example.in on port 8443...
Troubleshooting
Common Issues
TestSSL Not Found:

Ensure the testssl tool is installed and added to your PATH.
Verify by running testssl --version in the terminal.
Permission Denied:

Use chmod +x testssl to make the tool executable.
Script Errors:

Ensure Python 3.x is installed and used to run the script.
Contributors
Author: Anshil Dev
License
This project is licensed under the MIT License.

Feedback & Support
For any issues or suggestions, contact:

Email: [anshildev007@gmail.com]
Team Chat: [Slack/Teams/Other]
