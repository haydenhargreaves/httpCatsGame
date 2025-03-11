# HTTP Cat Quiz

![I am a teapot http code 418](https://http.cat/418.jpg)

## Description

This Streamlit application is a fun and educational quiz designed to test your knowledge of HTTP response codes. It utilizes the adorable `http.cat` API to display cat images corresponding to each HTTP code, making learning enjoyable.

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