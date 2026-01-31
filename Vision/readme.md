# Video Feature Extraction Tool

A Python tool that analyzes video files and extracts 4 visual/temporal features:
1. **Shot Cut Detection** - Finds hard cuts between scenes
2. **Motion Analysis** - Calculates optical flow motion
3. **Text Detection** - Extracts text using EasyOCR
4. **Object Detection** - Counts people vs objects using YOLO

## File Format
- **Jupyter Notebook**: `video_analysis_tool.ipynb`
- Works in Google Colab or local Jupyter environments

## Installation

Run these commands in a cell first:

```python
# Install required libraries
!pip install opencv-python==4.13.0.90
!pip install numpy==2.0.2
!pip install easyocr==1.7.2
!pip install ultralytics==8.4.9

Usage in Google Colab
1. Upload your video file to Colab
2. Open video_analysis_tool.ipynb
3. Change the video path in the first cell:
# Change this to your uploaded video
video_file = "/content/sample.mp4"  # ← Update this
output_folder = "/content/results"
4. Run all cells sequentially (Runtime → Run all)

Usage in Local Jupyter
1. pip install notebook
2. jupyter notebook video_analysis_tool.ipynb
3. Update video path in first cell
4. Run all cells

Output
JSON file: results/video_features.json with all extracted features
Console output: Progress updates and final summary


Features Implemented
1. Shot Cut Detection
Samples 3 frames per second

Uses frame differencing (threshold: 30)

Outputs cut timestamps and statistics

2. Motion Analysis
Uses Farneback optical flow

Samples 4 frames per second

Calculates motion magnitude and variation

3. Text Detection (OCR)
Uses EasyOCR (English only)

Samples 3 frames per second

Extracts unique texts with timestamps

4. Object vs Person Dominance
Uses YOLOv8n (small model)

Samples 2 frames per second

Calculates person ratio and dominance

Notebook Structure
The notebook is organized sequentially:

Setup - Imports and path configuration

Feature 1 - Shot cut detection
Feature 2 - Motion analysis
Feature 3 - Text detection
Feature 4 - Object detection

Main function - Runs everything

Version check - Library versions used
