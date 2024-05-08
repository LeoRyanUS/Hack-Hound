# Hack Hound

Hack Hound is a Python-based web security tool developed by Leo Ryan for professionals and penetration testers. It provides a comprehensive suite of features to scan web applications for vulnerabilities such as XSS, SQL injection, CSRF, path traversal, SSRF, and command injection.

## Description

Hack Hound is a powerful web security scanner designed to help professionals identify and mitigate security vulnerabilities in web applications. With its user-friendly interface and extensive range of features, Hack Hound makes it easy to conduct comprehensive security assessments and ensure the safety and integrity of web applications.

## Usage

To use Hack Hound, follow these steps:

1. **Installation**:
   - Clone the repository: `git clone https://github.com/LeoRyanUS/Hack-Hound.git`
   - Navigate to the project directory: `cd Hack-Hound`
   - Install the dependencies: `pip install -r requirements.txt`

2. **Running the Tool**:
   - Run the tool: `python hackhound.py`
   - Follow the prompts to enter the target URL and choose the type of vulnerability scan.

3. **Available Scan Types**:
   - XSS (Cross-Site Scripting)
   - SQL injection
   - Path Traversal
   - CSRF (Cross-Site Request Forgery)
   - SSRF (Server-Side Request Forgery)
   - Command Injection

4. **Comprehensive Scan**:
   - Use the `--scan-type all` option to perform a comprehensive scan for all vulnerability types.

5. **Search Engine Scan**:
   - Use the `--search-engine-scan` option to perform a comprehensive scan using a search engine.

## Terminal Instructions

When running Hack Hound from the terminal, you will be prompted to enter the target URL of the website you want to scan. You can also specify the type of vulnerability scan you want to perform using command-line options.

Follow the on-screen instructions to navigate through the scan process. Once the scan is complete, the results will be displayed in the terminal, providing details of any vulnerabilities detected.

For more information on how to use the tool and interpret the scan results, refer to the documentation provided in the "docs" folder.

## Contribution

Contributions to Hack Hound are welcome! If you'd like to contribute, please refer to the CONTRIBUTING.md file for guidelines.

For any questions or assistance, feel free to contact Leo Ryan at leoryanus@gmail.com.
