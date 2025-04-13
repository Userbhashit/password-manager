import os
import pytest
from pyfiglet import Figlet 
from unittest.mock import patch, mock_open
from project import welcome_user, reset, check_os
from genrate import generate, LETTERS_LOWER, LETTERS_UPPER, NUMBERS, SYMBOLS


def test_welcome_user(capfd):
    fake_username = "TestUser"

    with patch("builtins.open", mock_open(read_data=fake_username)):
        welcome_user()
        out, _ = capfd.readouterr()

        # Generate expected ASCII with pyfiglet to compare
        f = Figlet(font="standard")
        expected = f.renderText(f"Welcome  {fake_username}")

        # Check that the rendered welcome is in the output
        assert expected in out


def test_generate():
    test_cases = [
        (3, 8),   # Multiple passwords, minimum length
        (1, 12),   # Single password, medium length
        (5, 15)   # Multiple passwords, longer length
    ]
    
    for num_password, length in test_cases:
        with patch('genrate.get_length', return_value=length):
            passwords = generate(num_password)
            
            # Test correct number of passwords returned
            assert len(passwords) == num_password
            
            for pwd in passwords:
                # Test correct length for each password
                assert len(pwd) == length
                
                # Test contains at least one of each character type
                assert any(c in SYMBOLS for c in pwd)
                assert any(c in LETTERS_UPPER for c in pwd)
                assert any(c in LETTERS_LOWER for c in pwd)
                assert any(c in NUMBERS for c in pwd)
                
                # Test all characters are from allowed sets
                allowed_chars = set(SYMBOLS + LETTERS_UPPER + LETTERS_LOWER + NUMBERS)
                assert all(c in allowed_chars for c in pwd)
            
            # Test passwords are not all identical 
            if num_password > 1:
                assert len(set(passwords)) > 1


def test_reset():
    reset()

    assert (os.path.exists(".key") == False)
    assert (os.path.exists(".user") == False)
    assert (os.path.exists(".pass.db") == False)
    assert (os.path.exists(".pass") == False)

# test_os_check.py
@pytest.mark.parametrize(
    "mock_os, expected_exit",
    [
        ("Darwin", False),   # macOS (should not exit)
        ("Linux", False),    # Linux (should not exit)
        ("Windows", True),   # Unsupported OS (should exit)
        ("OtherOS", True),   # Unsupported OS (should exit)
    ]
)
def test_check_os(mock_os, expected_exit):
    with patch("platform.system", return_value=mock_os):
        if expected_exit:
            with pytest.raises(SystemExit):  # Check if the program exits
                check_os()
        else:
            check_os()  # If not expected to exit, just run the function

