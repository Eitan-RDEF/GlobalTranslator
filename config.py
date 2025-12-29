"""
Configuration file for Global Translator application.
"""
import os

class Config:
    """Application configuration settings."""
    
    # OpenAI Model Configuration
    MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    
    # Translation Settings
    DEFAULT_TARGET_LANGUAGE = os.getenv("DEFAULT_TARGET_LANGUAGE", "English")
    DEFAULT_CHUNK_SIZE = int(os.getenv("DEFAULT_CHUNK_SIZE", "3500"))
    
    # Chunking Settings
    MIN_CHUNK_SIZE = 3000
    MAX_CHUNK_SIZE = 4000
    
    # API Settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Application Settings
    APP_TITLE = "Global Translator"
    APP_DESCRIPTION = "Professional document translation using AI"

