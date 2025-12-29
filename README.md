# 🌍 Global Translator

A professional Streamlit application for translating large Word documents, PDFs, and text files using OpenAI's GPT models. The app intelligently chunks documents while preserving sentence and paragraph boundaries, ensuring high-quality translations.

## Features

- 📄 **Multi-Format Support**: Upload and translate Word (`.docx`), PDF (`.pdf`), and Text (`.txt`) files
- 🤖 **AI-Powered Translation**: Uses OpenAI's GPT-4.1-mini model for accurate translations
- 📝 **Smart Chunking**: Automatically splits documents into 2000-5000 word chunks (configurable)
- ✨ **Sentence-Aware**: Never splits sentences or paragraphs during chunking
- 🎨 **Format Preservation**: Maintains paragraph structure and styles (Word output)
- ⚙️ **Configurable**: Customize target language, source language, and chunk size via UI
- 🌐 **50+ Languages**: Support for professional translations in any language

## Prerequisites

- Python 3.10 or higher
- OpenAI API key

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (Development mode only):
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Development vs Production Modes

The application supports two modes:

### Development Mode (Default)
- **Detection**: Automatically detected when running as Python script
- **API Key Source**: `.env` file
- **Usage**: For developers working with the source code
- **Setup**: Create `.env` file with your API key

### Production Mode (Standalone Executable)
- **Detection**: Automatically detected when running as bundled executable (`.exe` file)
- **API Key Source**: User input in the app's Settings sidebar
- **Usage**: For end users who receive the standalone application
- **Setup**: Users enter their API key directly in the app interface
- **Note**: No `.env` file needed - the app will prompt users to enter their API key in the UI

The app automatically detects which mode it's running in and adjusts accordingly. When you create the standalone executable, users won't need to create any `.env` files - they'll simply enter their API key in the Settings section of the app.

## Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to the URL shown in the terminal (typically `http://localhost:8501`)

3. **Configure settings** (optional):
   - Set source and target languages in the sidebar
   - Adjust chunk size if needed (2000-5000 words, default: 3500)
   - Add translation instructions if needed

4. **Upload a document**:
   - Click "Upload Document"
   - Select your `.docx`, `.pdf`, or `.txt` file

5. **Translate**:
   - Click "Translate Document"
   - Wait for processing to complete
   - Download your translated Word document (always outputs as `.docx`)

## Configuration

### Environment Variables (Development Mode Only)

In development mode, edit the `.env` file to customize:

- `OPENAI_API_KEY`: Your OpenAI API key (required in dev mode)
- `OPENAI_MODEL`: Model to use (default: `gpt-4.1-mini`)
- `DEFAULT_TARGET_LANGUAGE`: Default target language (default: `English`)
- `DEFAULT_CHUNK_SIZE`: Default chunk size in words (default: `3500`)

**Note**: In production mode (standalone executable), users enter their API key directly in the app's Settings sidebar. Environment variables are not used in production mode.

### Application Settings

You can also modify `config.py` to change default application settings.

## How It Works

1. **Document Extraction**: The app extracts text from Word, PDF, or text files while preserving paragraph structure. For PDFs, only text-based PDFs are supported (not scanned images).

2. **Smart Chunking**: Documents are split into configurable chunks (2000-5000 words), ensuring:
   - Sentences are never split
   - Paragraphs are preserved when possible
   - Chunks respect natural text boundaries

3. **Translation**: Each chunk is translated using OpenAI's API with a professional translation prompt.

4. **Document Reconstruction**: Translated chunks are reassembled into a new Word document (`.docx`) with preserved paragraph structure.

## File Format Support & Limitations

### Supported Formats

- **Word Documents (`.docx`)**: Full support with paragraph style preservation
- **Text Files (`.txt`)**: Full support, outputs as Word document
- **PDF Files (`.pdf`)**: Text-based PDFs only (see limitations below)

### PDF Limitations

⚠️ **Important PDF Limitations:**

- **Text-based PDFs only**: The app works best with PDFs that contain actual text (not scanned images)
- **Scanned PDFs**: Image-based/scanned PDFs are not supported - text extraction will be limited or fail
- **Multi-column layouts**: PDFs with multiple columns may have text extracted in incorrect reading order
- **Images**: Images in PDFs are automatically excluded from extraction
- **Complex layouts**: Tables, complex formatting, and embedded objects may not be preserved
- **Encrypted PDFs**: Password-protected PDFs are not supported

**How to check if your PDF is text-based:**
- Try to select and copy text from the PDF
- If you can select text → text-based (works well)
- If you cannot select text → scanned/image-based (won't work well)

**Recommendations:**
- Use single-column PDFs for best results
- Convert scanned PDFs to text-based PDFs using OCR software first
- For best quality, use Word documents (`.docx`) when possible

## Project Structure

```
GlobalTranslator/
├── app.py              # Main Streamlit application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .env                # Your environment variables (create this)
├── LICENSE             # MIT License
└── README.md           # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Model Limitations & Technical Details

### Model: GPT-4.1-mini

The application uses OpenAI's `gpt-4.1-mini` model for translation. This model offers a balance between performance, cost, and quality for translation tasks.

**Key Limitations:**
- **Context Window**: The model has a large context window (up to 1,047,576 tokens), but processing very large documents in a single request can lead to:
  - Increased latency and processing time
  - Higher costs per request
  - Potential quality degradation for extremely long texts
  - Risk of hitting rate limits or timeout issues

- **Output Token Limit**: The model has a maximum output token limit per response (typically 16,384 tokens). This is why documents are chunked - to ensure each translation response stays within the output limit. If a chunk's translation would exceed this limit, the translation may be truncated or fail.

- **Translation Quality**: While `gpt-4.1-mini` provides excellent translation quality for most use cases, it may not match the performance of larger, more expensive models (like GPT-4) for:
  - Highly technical or specialized terminology
  - Complex literary texts with nuanced language
  - Documents requiring deep cultural context understanding

- **Rate Limits**: OpenAI API has rate limits that may affect processing of very large documents or high-volume usage.

### Why 2000-5000 Word Chunk Size? (Default: 3500)

The chunk size is configurable between 2000-5000 words (default: 3500) and was chosen to balance:

- **Token Efficiency**: ~1 word ≈ 1.3 tokens, leaving room for prompts and longer translation output
- **Output Limit**: Ensures translated output stays within the model's output token limit (~16,384 tokens per response)
- **Quality**: Smaller chunks maintain better contextual coherence and preserve sentence/paragraph boundaries
- **Cost**: Efficient token usage while allowing error recovery if one chunk fails
- **Performance**: Faster processing, better progress tracking, reduced timeout risk

### How "Never Splits Sentences or Paragraphs" Works

The chunking algorithm uses a hierarchical approach:

1. **Paragraph-Level**: Documents are processed paragraph by paragraph. If adding a paragraph would exceed the chunk limit, the current chunk is saved and a new one starts.

2. **Sentence-Level** (only when a single paragraph exceeds chunk size): Uses regex `(?<=[.!?])\s+` to split by complete sentences only, never mid-sentence.

3. **Reconstruction**: Translated chunks are reassembled in order, with paragraph styles preserved. Split paragraphs maintain their original style across chunks.

## Pricing Information

The application uses OpenAI's API. Pricing for `gpt-4.1-mini` (as of 2024):
- **Input**: $0.40 per 1M tokens
- **Output**: $1.60 per 1M tokens

**Example costs:**
- Small (5,000 words): ~$0.015
- Medium (20,000 words): ~$0.062
- Large (50,000 words): ~$0.154

Output tokens are typically 20-30% more than input tokens. For current pricing, visit [OpenAI's Pricing Page](https://openai.com/api/pricing/).

## Important Notes

- The app uses OpenAI's API, which requires an active API key and may incur costs based on usage
- Large documents may take several minutes to translate depending on size and API response times
- Translation quality depends on the source/target languages and text complexity
- Monitor your OpenAI API usage to track costs
- **Output format**: All translations are output as Word documents (`.docx`), regardless of input format

## Troubleshooting

**Error: "Please set OPENAI_API_KEY in your .env file"**
- Make sure you've created a `.env` file from `.env.example`
- Verify your API key is correctly set in the `.env` file

**Translation fails**
- Check your OpenAI API key is valid and has sufficient credits
- Verify your internet connection
- Check the OpenAI API status

**Document formatting issues**
- The app preserves paragraph styles, but complex formatting (tables, images, etc.) is not supported
- PDFs with complex layouts may lose formatting
- Images are automatically excluded from extraction

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

For issues or questions, please open an issue on the repository.

