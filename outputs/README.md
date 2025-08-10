# Output Folder

Transcription results are automatically saved here.

## File Types Generated

### Text Files (.txt)
- **Format**: `{original_filename}_transcription.txt`
- **Content**: Clean, readable transcription text
- **Use Case**: Simple text output, copy-paste friendly

### JSON Files (.json)
- **Format**: `{original_filename}_detailed.json`  
- **Content**: Complete transcription data with metadata
- **Includes**: 
  - Segmented text with timestamps
  - Word-level confidence scores
  - Processing metadata
  - Audio file information

## Sample Outputs

The sample files demonstrate different types of transcription results:
- Business meetings
- Educational content  
- Interview transcripts
- Multi-language support

## Output Structure

```
outputs/
├── sample_meeting_transcription.txt     # Clean text
├── sample_meeting_detailed.json        # Full metadata
├── sample_interview_transcription.txt  # Clean text
├── sample_interview_detailed.json      # Full metadata
└── sample_lecture_transcription.txt    # Clean text
```