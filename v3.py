# Import dependencies

import os
from time import sleep, strftime
import pyautogui as pg
import pandas as pd
from PIL import ImageGrab
import logging

ORG_SIZE = (1600, 900)
DISPLAY_SIZE = pg.size()

DIFF_X = DISPLAY_SIZE[0] / ORG_SIZE[0]
DIFF_Y = DISPLAY_SIZE[1] / ORG_SIZE[1]

def key_fill(*args) -> None:
    """Types the given arguments using pyautogui."""
    pg.write(*args)

def copy(x_axis: int = 0, y_axis: int = 0, clicks: int = 3) -> str:
    """Copies text from the specified screen coordinates."""

    pg.click(x=x_axis, y=y_axis, clicks=clicks)
    sleep(0.5)  # Wait for the click action to register
    copied_text = pg.hotkey('ctrl', 'c')
    sleep(0.5)  # Wait for clipboard to update
    return copied_text

def tab(times: int = 1, interval: float = 0.3) -> None:
    """Presses the tab key a specified number of times with an interval."""
    pg.press(keys='tab', presses=times, interval=interval)

def space(times: int = 1, interval: float = 0.3) -> None:
    """Presses the space key a specified number of times with an interval."""
    pg.press(keys='space', presses=times, interval=interval)

def verify_field(expected_field: str = None, x_axis: int = 0, y_axis: int = 0) -> bool:
    """Verifies if the expected field is present on the screen."""
    if expected_field is None:
        raise ValueError("Expected field must be provided.")
        pg.alert(text="Expected field must be provided.", title="Error", button="OK")

    field = copy(x_axis=x_axis, y_axis=y_axis, clicks=3)
    if field != expected_field:
        logging.error(f"""Field verification failed. 
                      Expected: \"{expected_field}\" at ({x_axis}, {y_axis}) 
                      but the field is \"{field}\".""")
        pg.alert(text=f"""Field verification failed. 
                      Expected: \"{expected_field}\" at ({x_axis}, {y_axis}) 
                      but the field is \"{field}\".""",
                 title="Error", button=f"{field}")
        return False
    return True
    

def login_page(username: str = None, password: str = None) -> None:
    if username is None or password is None:
        raise ValueError("Username and password must be provided.")
    
    """Automates the login process by entering username and password."""

    userid_org_coord = (636, 592)
    password_org_coord = (645, 634)

    # Calculate adjusted coordinates based on display size

    uid_coord = (int(userid_org_coord[0] * DIFF_X),
                 int(userid_org_coord[1] * DIFF_Y))
    pwd_coord = (int(password_org_coord[0] * DIFF_X), 
                 int(password_org_coord[1] * DIFF_Y))

    # Verify and fill User ID field
    if not verify_field(expected_field="User ID", x_axis=uid_coord[0], y_axis=uid_coord[1]):
        raise ValueError("User ID field: Wrong Coordinates.")
        pg.alert(text="User ID field: Wrong Coordinates given.", title="Error", button="OK")
        logging.error(f"{get_timestamp()} :: User ID field: Wrong Coordinates given.")
    else:
        # To move to username entry field
        tab()
        key_fill(username)
        logging.info(f"{get_timestamp()} :: User ID field: Entered {username}.")
        sleep(0.5)

    # Verify and fill Password field
    if not verify_field(expected_field="Password", x_axis=pwd_coord[0], y_axis=pwd_coord[1]):
        raise ValueError("Password field: Wrong Coordinates.")
        pg.alert(text="Password field: Wrong Coordinates given.", title="Error", button="OK")
        logging.error(f"{get_timestamp()} :: Password field: Wrong Coordinates given.")
    else:
        # To move to password entry field
        tab()
        key_fill(password)
        logging.info(f"{get_timestamp()} :: Password field: Password {password}.")
        sleep(0.5)
    
    # Press Enter to submit the login form
    pg.press('enter')


def get_timestamp(fmt: str = "%Y-%m-%d_%H:%M:%S") -> str:
    """Return the current local time formatted using `strftime` from `time`.

    Example: `2026-01-01_15:30:12`
    """
    return strftime(fmt)


def save_screenshot(prefix: str = "screenshot", folder: str = ".", fmt: str = "%Y%m%d_%H%M%S") -> str:
    """Capture the screen and save a PNG file with a timestamped filename.

    Returns the full path to the saved image.
    """
    ts = get_timestamp(fmt)
    filename = f"{prefix}_{ts}.png"
    path = os.path.join(folder, filename)
    img = ImageGrab.grab()
    img.save(path)
    logging.info(f"Saved screenshot: {path}")
    return path

login_page(username="testuser", password="testpass")