# AI-Based Linux Process Scheduler

An innovative approach to process scheduling on Linux, leveraging machine learning techniques to enhance scheduling performance by predicting optimal time quanta for processes. This project introduces a simulation model that integrates an AI-based scheduling algorithm with the Linux Completely Fair Scheduler (CFS).

## Project Overview

The AI-Based Linux Process Scheduler aims to improve the performance of the Linux scheduler by reducing context switches, optimizing turnaround time, and minimizing process wait time. The project uses machine learning to analyze the execution history of processes and predict a suitable time quantum for each process, leading to more efficient CPU utilization.

## Key Features

- **Simulation Model:** A simulation environment to test the AI-based scheduler.
- **Machine Learning Integration:** Utilizes machine learning algorithms (Decision Tree, Support Vector Machine, Random Forest) to predict time quanta.
- **Scheduler Enhancements:** Modifies the current Linux CFS scheduler to incorporate predictions and reduce overheads.
- **Performance Metrics:** Evaluates performance improvements such as reduced context switches and optimized process execution.

## Objectives

- Implement a simplified version of the Linux scheduler.
- Design a Completely Fair Scheduler (CFS) simulator.
- Integrate machine learning models to predict time quanta.
- Develop a graphical user interface (GUI) for the simulator.
- Test and validate the AI-based scheduler's performance.

## Project Environment

- **Language:** Python
- **Development Tools:** PyCharm IDE, Notepad++, GCC Compiler
- **Frameworks & Libraries:** Flask, Pandas, Scikit-Learn, Pickle

## How It Works

1. **Data Collection:** Gathers static and dynamic features of processes for training the machine learning model.
2. **Machine Learning Model:** Trains models using collected data to predict suitable time quanta.
3. **Scheduler Integration:** Modifies the Linux CFS scheduler to use predicted time quanta for processes.
4. **Simulation and Testing:** Simulates the scheduling process and measures performance improvements.

![y](https://github.com/user-attachments/assets/0d5bfc9b-0616-45fa-b95f-ba3196865700)

## Future Prospects

- Enhance the accuracy of the ML model with more data.
- Implement reinforcement learning for dynamic adjustments.
- Address limitations such as multitasking trade-offs and cold-start problems.

## How to Use

1. Clone the repository.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the scheduler simulation through the provided GUI by uploading a process data file in Excel format.
4. Analyze the simulation results displayed on the UI.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.
