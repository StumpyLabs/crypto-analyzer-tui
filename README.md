Crypto Analyzer TUI

This application will give you information on the top 100 coins by market cap.
There are options to see the coins in order by market cap, price, price change over 24hrs, volume, all-time low, and
all-time high.

Table of Contents

    Installation
    Usage
    Features
    Configuration
    Contributing
    Testing
    License
    Credits
    Contact

Installation
Prerequisites

    Python 3.8+
    pip
    Git
    Pandas

Installation Steps

    Clone the repository:
    bash
    git clone https://github.com/StumpyLabs/crypto-analyzer-tui.git

    Navigate to the project directory:
    bash
    cd crypto-analyzer-tui
    
    Install the required dependencies:
    bash
    pip install -r requirements.txt

Usage

    To start the project, run the following command:
    bash
    python main.py

    When in project use these commands to navigate:
    mc: market cap
    p: price
    pc: price change over 24 hours
    v: total volume
    al: all-time low
    ah: all-time high
    q: quit

Features

    Feature 1: Discover .
    Feature 2: Describe another great feature.
    Feature 3: Yet another cool feature.

Configuration

To configure the project, modify the config.yaml file located in the config/ directory. The file should look something like this:

yaml

setting_1: value1
setting_2: value2
setting_3:
  - sub_value1
  - sub_value2

Contributing

Contributions are welcome! Please follow these steps:

    Fork the project.
    Create your feature branch (git checkout -b feature/AmazingFeature).
    Commit your changes (git commit -m 'Add some AmazingFeature').
    Push to the branch (git push origin feature/AmazingFeature).
    Open a pull request.

Please make sure to update tests as appropriate.
Testing

Run the following command to execute the test suite:

bash

pytest

License

This project is licensed under the MIT License - see the LICENSE file for details.
Credits

    John Doe - Original author
    Jane Smith - Contributor
    Awesome Library - Used for the data processing engine

Contact

If you have any questions, feel free to contact me at stumpf80369@gmail.com.