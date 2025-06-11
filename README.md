# 🕒 Days to Hours Converter

A simple Python program that converts days into hours. The script takes user input for a number of days, validates the input, and displays the equivalent hours. The loop continues until the user types `"exit"`.

---

## 🧠 Features

- Accepts multiple day values separated by commas
- Validates input and handles:
  - Positive integers
  - Zero
  - Negative or invalid input
- Continuously prompts the user until `"exit"` is entered

---

## 💡 How It Works

- 1 day = 24 hours (conversion constant)
- You input a number like `5` and it returns:  
  `5 days are 120 hours`
- You can input multiple values like `3,5,0,-2,hello` and it will validate each

---

## 🛠️ Usage

### 1. Clone or download the script

```bash
git clone https://github.com/tjhabeeb/days-to-hours-converter.git
cd days-to-hours-converter
```

### 2. Run the script

```bash
python3 convert.py
```

Or if you saved it as `days_converter.py`:

```bash
python3 days_converter.py
```

### 3. Input example

```text
Enter a number of days: 5,10,0,-3,test
```

Output:
```
5 days are 120 hours
10 days are 240 hours
You entered a 0, please enter a positive number
This is an invalid number
You entered an invalid value, please enter an integer
```

---

## 📦 Dependencies

- Python 3.x  
(No external libraries needed)

---

## 📌 Improvements (Optional)

- [ ] Add unit tests
- [ ] Allow conversion to minutes or seconds
- [ ] Create a GUI version

---

## 🧑‍💻 Author

**Olalekan Habeeb**  
GitHub: [@tjhabeeb](https://github.com/tjhabeeb)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
