"""
Launcher script for bundled Streamlit application.
This script is used when the app is bundled as an executable.
"""
import sys
import os
import subprocess

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
    try:
        # Use streamlit run command
        subprocess.run([
            sys.executable,
            '-m',
            'streamlit',
            'run',
            app_path,
            '--server.headless',
            'true',
            '--server.port',
            '8501',
            '--server.address',
            'localhost',
            '--browser.gatherUsageStats',
            'false'
        ])
    except Exception as e:
        print(f"Error starting Streamlit: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

