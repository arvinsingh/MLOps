# MLOps Rent Prediction

## Overview
This project aims to turn ML models developed in Jupyter Notebooks into production-ready, fully operational microservices deployable in containers.

## Getting Started
### Prerequisites
- Python 3.11

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/arvinsingh/MLOps.git
   cd MLOps
   ```

2. Install dependencies:
   ```sh
   make install
   ```

### Running the Application
1. Train the model:
   ```sh
   make runner-builder
   ```

2. Run the inference service:
   ```sh
   make runner-inference
   ```