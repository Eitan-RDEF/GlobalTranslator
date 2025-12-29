import sys
import os
import traceback

# Global exception handler to keep window open
def show_error_and_wait(type, value, tb):
    print("\n" + "="*60)
    print("CRITICAL ERROR OCCURRED")
    print("="*60)
    traceback.print_exception(type, value, tb)
    print("="*60)
    input("Press Enter to exit...")

sys.excepthook = show_error_and_wait

try:
    from streamlit.web import cli as stcli
except ImportError as e:
    print(f"Failed to import Streamlit: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

# Get the directory where the executable is located
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    # PyInstaller sets _MEIPASS to the temp folder where files are extracted
    base_path = sys._MEIPASS
    app_path = os.path.join(base_path, 'app.py')
    # Ensure we're in the right directory
    os.chdir(base_path)
else:
    # Running as script
    base_path = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(base_path, 'app.py')

# Run Streamlit
if __name__ == '__main__':
    # Prepare arguments for Streamlit
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless", "true",
        "--server.port", "8501",
        "--server.address", "localhost",
        "--browser.gatherUsageStats", "false",
        "--global.developmentMode", "false",
    ]
    
    # Run Streamlit directly
    sys.exit(stcli.main())

