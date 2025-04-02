import pytest 

from app.module.utility.shortcut_excuter import ShortcutExecutor

@pytest.fixture
def shortcut_executor():
    return ShortcutExecutor()

@pytest.fixture
def shortcut_path():
    return "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Everything.lnk"

def test_get_process_name_by_shortcut_path(shortcut_executor, shortcut_path):
    process_name = shortcut_executor.get_process_name_by_shortcut_path(shortcut_path=shortcut_path)
    assert process_name == "Everything.exe"

def test_exec_shortcut_by_shortcut_path(shortcut_executor, shortcut_path):
    shortcut_executor.exec_shortcut_by_shortcut_path(shortcut_path=shortcut_path)
    return

def test_quit_app_by_shortcut_path(shortcut_executor, shortcut_path):
    shortcut_executor.quit_app_by_shortcut_path(shortcut_path=shortcut_path)
    return

def test_minimize_app_by_shortcut_path(shortcut_executor, shortcut_path):
    shortcut_executor.minimize_app_by_shortcut_path(shortcut_path=shortcut_path)
    return






