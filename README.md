## ⌨️ Gistia's Engineer Assessment

- Implemented the Data analysis using Python and Pandas as the data manipulation library

- Option (a.) was chosen from the [2.] section of the Assessment. Since Pandas is being used to read the dataset

- The main code is in the `src/assets_parser.py` file
    - A constants file `src/config/constants` is used to store the constants used in the code, such as the Google Sheets URL and the Column names
    - It also uses the `src/util/get_google_sheets_csv_url.py` to transform the Dataset URL into a CSV version readable by Pandas

### ⚙️ How to run
- Clone the repository `git clone https://github.com/lucasmsa/gistia-engineer-assessment.git`
- Install the dependencies `pip install -r requirements.txt`
- Run the code `python src/assets_parser.py`