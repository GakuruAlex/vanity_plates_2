# Vanity Plates #

In Massachusetts, home to havard University, it's possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones.

Requirements are:

1) All vanity plates must start with atleast two letters.

2) Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.

3) Numbers cannot be used in the middle of a plate and the first number cannot be a zero.

4) No periods or punctuation marks are allowed.


# Pre-requisite #

clone repo:

```bash
        git clone https://github.com/GakuruAlex/vanity_plates_2.git
```

cd into project dir 

```bash
    cd vanity_plates_2
```

Create a virtual env

```bash
    python3 -m venv envname
```

Activate env

```bash
    source envname/bin/activate
```

Install requirements

```bash
    pip install -r requirements.txt
```

# Usage #
A user is prompted to enter the desired plate, if plate is valid the program prints "Valid" as output otherwise "Invalid"

To run the program

```bash
    python3 vanity_plates_2.py
```
 To run the tests

 ```bash
    pytest -v
 ```