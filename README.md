# HTTP Cat Quiz


<div align="center">

[![Run Pytest Tests](https://github.com/haydenhargreaves/httpCatsGame/actions/workflows/pytest.yml/badge.svg)](https://github.com/haydenhargreaves/httpCatsGame/actions/workflows/pytest.yml)
[![Build and Push Docker Image](https://github.com/haydenhargreaves/httpCatsGame/actions/workflows/docker-build.yml/badge.svg)](https://github.com/haydenhargreaves/httpCatsGame/actions/workflows/docker-build.yml)

![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

![I am a teapot http code 418](https://http.cat/418.jpg)
</div>



## Description

This Streamlit application is a fun and educational quiz designed to test your knowledge of HTTP response codes. It utilizes the adorable `http.cat` API to display cat images corresponding to each HTTP code, making learning enjoyable.

**A demo of this app can be found [here](https://httpcats.streamlit.app).**

## Features

* **Quiz Format:** Presents multiple-choice questions about HTTP response codes.
* **Interactive UI:** Uses Streamlit's `st.radio` for interactive question selection.
* **Score Tracking:** Calculates and displays the user's score upon submission.
* **Visual Feedback:** Provides "Correct" or "Incorrect" feedback for each question.
* **Cat Images:** Displays cat images from `http.cat` corresponding to the correct HTTP response codes.
* **Session State:** Uses `st.session_state` to maintain the quiz state across reruns, preventing data loss.
* **Caching:** Uses `@st.cache_data` to improve performance by caching the loading of images.

## Getting Started

### Prerequisites

* Python 3.6+
* Streamlit (`streamlit`)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Install the required packages:

    ```bash
    pip install streamlit
    ```

### Running the Application

1.  Navigate to the directory containing the Streamlit app.
2.  Run the application using Streamlit:

    ```bash
    streamlit run app.py
    ```

    (replace `app.py` with the name of your streamlit file)

3.  Open your web browser to the displayed URL (usually `http://localhost:8501`).

### Running the Test

1.  Navigate to the directory containing the Streamlit app.
2.  Ensure `pytest` is installed.

    ```bash
    pip install pytest
    ```
    
3.  Run the tests using pytest.

    ```bash
    pytest
    ```


## Automated Deployment with Ansible

This project includes Ansible playbooks to automate the deployment of the HTTP Cat Quiz on a DigitalOcean Droplet.
The IP will be automaticall applied when the playbooks are ran, to ensure a constant location for connection and DNS setup.

### Setup

1.  **Install Ansible:** If you don't have Ansible installed, follow the instructions on the [official Ansible documentation](https://www.google.com/search?q=https://docs.ansible.com/installation_guide/index.html).

2.  **Install the DigitalOcean Collection for Ansible:**

    ```bash
    ansible-galaxy collection install community.digitalocean
    ```

3.  **Configure DigitalOcean API Token:** Ensure you have a DigitalOcean API token with write access. You can create one in your DigitalOcean control panel under "API".

4.  **Create an Inventory File (e.g., `inventory/hosts.yml`):**

    ```yml

    all:
      vars:
        ansible_connection: ssh
      hosts:
        <name>:
          ansible_user: <user>
          domain: <domain>
          hostname: <hostname>
    ```


### Running the Playbooks

1.  **Create a new DigitalOcean Droplet:**

    Navigate to the directory containing the Ansible playbooks and run:

    ```bash
    ansible-playbook create_droplet.yml
    ```

    **Note:** You might need to adjust the `create.py` script in `src/droplet/` to configure the droplet size, region, and other parameters according to your needs.

2.  **Setup the Droplet and Deploy the Application:**

    Once the droplet is created and its IP address is assigned (this process is handled by `createdroplet.yml`), you can run the playbook to install necessary packages (Docker) and deploy the HTTP Cat Quiz:

    ```bash
    ansible-playbook playbooks/setup_droplet.yml
    ```

    Replace `<your_droplet_ip>` with the actual IP address of your newly created droplet.

3.  **Upgrade the Droplet (Optional):**

    To perform a system upgrade on your droplet:

    ```bash
    ansible-playbook playbooks/update_droplet.yml
    ```

### Playbook Descriptions

  * **`playbooks/create_droplet.yml`:** This playbook uses a local Python script (`src/droplet/create.py`) to create a new DigitalOcean Droplet. It then waits for the droplet to become available and assigns a public IP address using another local script (`src/droplet/assign.py`). **Note:** You might need to customize the Python scripts in `src/droplet/` with your DigitalOcean API token and desired droplet specifications.
  * **`playbooks/setup_droplet.yml`:** This playbook targets the newly created Droplet (or any specified host in your inventory). It performs the following actions:
      * Ensures essential packages like `vim`, `wget`, `btop`, and `docker.io` are installed.
      * Deploys the HTTP Cat Quiz application as a Docker container using the `ghcr.io/haydenhargreaves/httpcatsgame:master` image.
      * Starts the Docker container and configures it to restart automatically unless stopped.
      * Publishes the container's port 8501 to the host's port 80, making the application accessible via HTTP on the droplet's IP address.
  * **`playbooks/update_droplet.yml`:** This playbook targets the specified host and performs a full system upgrade (`dist-upgrade`), updates the package cache, and reboots the server if necessary. It also removes any unused dependencies.

### Code Structure

  * **`playbooks/setup_droplet.yml`:** Ansible playbook to provision and configure a DigitalOcean Droplet for deployment.
  * **`playbooks/create_droplet.yml`:** Ansible playbook to create a new DigitalOcean Droplet and assign an IP address.
  * **`playbooks/update_droplet.yml`:** Ansible playbook to upgrade the packages on a remote host.
  * **`src/droplet/create.py`:** Python script used by `createdroplet.yml` to interact with the DigitalOcean API to create a droplet. **(Note: You might need to configure this script)**
  * **`src/droplet/assign.py`:** Python script used by `createdroplet.yml` to interact with the DigitalOcean API to get the IP address of the created droplet. **(Note: You might need to configure this script)**

### Dependencies

  * Ansible
  * `community.digitalocean` Ansible collection (for DigitalOcean interaction)
  * Docker (for containerization on the deployed server)

**Note:** Remember to fill your `.env` file with the required fields, the required fields are defined in the Python source code!

## Code Structure

* **`app.py`:** Contains the main Streamlit application code, including quiz generation, user interaction, and score calculation.
* **`codes.py`:** Contains functions for generating random HTTP codes, retrieving code messages, and creating quiz options.
* **`test/test_main.py`:** Contains all the test for the application, which can be run with `pytest`.

## Usage

1.  The application will display a series of multiple-choice questions about HTTP response codes.
2.  Select your answer for each question using the radio buttons.
3.  Click the "Submit Answers" button to check your answers and see your score.
4.  After submission, you will see your score and feedback for each question, including cat images corresponding to the correct HTTP response codes.

## Dependencies

* Streamlit (`streamlit`)
* Python's `random` module
* Python's `typing` module
