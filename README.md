# Body Posture Comparison Tool using MediaPipe and PyQt5

A sophisticated computer vision application that leverages MediaPipe's pose estimation capabilities and Dynamic Time Warping (DTW) algorithm to analyze and compare human body movements between video sequences. This tool is specifically designed for analyzing cricket bowling techniques before and after injuries, as well as tracking progress in yoga poses over time.

![Example Graph](image4.gif)

## Example Outputs

### Cricket Bowling Analysis

Comparison of bowling actions showing temporal alignment of key joint angles:

![Bowling Analysis](image6.gif)

Detailed error visualization highlighting specific phases of movement discrepancy:

![Error Analysis](image8.gif)

### Yoga Pose Comparison

Comparison of similar but technically different yoga poses with landmark detection:

![Yoga Analysis](screenshot1.png)

## Technical Overview

### Core Technologies

- **MediaPipe Pose (v0.8+)**: Utilizes Google's MediaPipe framework for real-time pose landmark detection, tracking 33 key body points with high precision. The implementation filters out facial landmarks to focus exclusively on body posture analysis.

- **Dynamic Time Warping (DTW)**: Implements FastDTW algorithm with cosine distance metrics to compare temporal sequences of body poses, allowing for non-linear alignment of movements performed at different speeds.

- **PyQt5 GUI Framework**: Provides a responsive user interface with real-time video processing, interactive controls, and integrated matplotlib visualizations for immediate feedback.

- **OpenCV**: Handles video capture, frame processing, and visualization of pose landmarks with custom angle calculations.

### Technical Features

- **Pose Landmark Detection**: Captures 33 key body points per frame using MediaPipe's ML-powered pose estimation model.

- **Angle Calculation**: Computes joint angles between connected body segments (shoulders, elbows, knees, etc.) for precise biomechanical analysis.

- **Real-time DTW Comparison**: Calculates frame-by-frame similarity scores between reference and subject videos using FastDTW algorithm.

- **Error Visualization**: Generates dynamic plots showing error metrics and movement discrepancies over time.

- **Customizable Frame Rate**: Adjustable processing speed via slider control for detailed analysis of rapid movements.

- **Video Selection Interface**: Integrated file dialog for selecting and comparing any two video sources.

## System Architecture

The application follows a modular architecture:

1. **Pose Detection Module** (`pose_module.py`): Encapsulates MediaPipe integration with custom angle calculation and visualization methods.

2. **Movement Comparison Engine** (`move_comparison.py`): Implements the DTW algorithm for comparing pose sequences between videos.

3. **PyQt5 Application Layer** (`FinalBowling.py`/`BowlingComparisionFinal.py`): Provides the user interface, real-time processing, and visualization components.

## Installation

### Prerequisites

- Python 3.8+ (recommended for optimal MediaPipe compatibility)
- Webcam (for live capture comparison, optional)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/subhashbs36/Body-posture-comparision-tool-using-pyqt5.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Body-posture-comparision-tool-using-pyqt5
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

The application relies on the following key libraries:

- **MediaPipe**: ML framework for pose estimation
- **PyQt5**: GUI framework
- **OpenCV**: Computer vision operations
- **FastDTW**: Optimized Dynamic Time Warping implementation
- **SciPy**: Scientific computing (used for distance calculations)
- **Matplotlib**: Data visualization

```bash
# Full dependency list
pip install opencv-python-headless mediapipe PyQt5 numpy matplotlib scipy fastdtw
```

## Usage

### Running the Application

1. Launch the main application:
   ```bash
   python FinalBowling.py
   ```

2. Use the "Select Videos" button to choose two videos for comparison:
   - **Reference Video**: A benchmark performance (e.g., pre-injury bowling technique)
   - **Comparison Video**: The technique to analyze (e.g., post-injury bowling action)

3. The application will:
   - Process both videos through MediaPipe's pose estimation pipeline
   - Calculate and display joint angles on both video streams
   - Apply DTW algorithm to compare pose sequences
   - Generate real-time error graphs showing movement discrepancies

### Interface Controls

- **Pause/Play**: Toggle video processing
- **FPS Slider**: Adjust processing speed
- **Clear Graph**: Reset visualization data
- **Select Videos**: Choose new video files for comparison

## Technical Applications

### Sports Biomechanics Analysis

- **Injury Prevention**: Detect subtle changes in bowling technique that may lead to injuries
- **Rehabilitation Monitoring**: Track recovery progress by comparing pre and post-injury movements
- **Performance Optimization**: Identify technical inefficiencies in athletic movements

### Yoga and Fitness Assessment

- **Pose Accuracy Measurement**: Quantify alignment accuracy in yoga poses
- **Progress Tracking**: Monitor improvements in form and technique over time
- **Instructor Feedback**: Provide objective metrics for pose corrections

### General Motion Analysis

- **Ergonomic Assessment**: Analyze workplace movements for injury risk
- **Physical Therapy**: Track patient progress during rehabilitation exercises
- **Dance and Performance Arts**: Compare choreography execution against reference performances

## Technical Limitations and Considerations

- MediaPipe pose estimation works best with unobstructed, well-lit subjects
- DTW algorithm complexity increases with video length (FastDTW optimization mitigates this)
- Processing speed depends on hardware capabilities (CPU/GPU)
- Occlusion handling is limited by MediaPipe's single-view estimation capabilities

## Future Technical Enhancements

- **3D Pose Estimation**: Upgrade to MediaPipe's 3D landmark detection for depth analysis
- **Multi-person Tracking**: Add support for comparing synchronized movements of multiple subjects
- **Machine Learning Classification**: Implement pose classification models for automatic technique assessment
- **Temporal Segmentation**: Automatic detection and segmentation of movement phases
- **Cloud Integration**: Remote storage and analysis capabilities for team environments
- **Biomechanical Metrics**: Advanced joint force and torque calculations

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and send pull requests.

When contributing code, please follow these guidelines:
1. Maintain consistent code style with the existing codebase
2. Add appropriate documentation for new features
3. Include unit tests for new functionality
4. Ensure compatibility with the existing architecture

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
