# Complexity, Cost, Social Relevance and Health Concern

## Complexity

MediPredict AI has moderate-to-high technical complexity because it combines four disease-specific machine learning classification tasks in one platform. Each dataset has different feature types, missing-value patterns and target representations. The project additionally compares six machine learning algorithms for each disease and requires preprocessing, evaluation, model selection, serialization, backend integration and user-interface development. Preventing data leakage and maintaining reproducibility further increase the engineering requirements. A modular architecture reduces this complexity by separating data loading, preprocessing, modelling, prediction and presentation. This allows individual disease modules to be tested independently while maintaining one unified application architecture.

## Cost

The project is designed as a low-cost academic research system. Python, Pandas, NumPy, Scikit-learn, XGBoost, Flask, React and related development tools can be used without mandatory commercial software licences. Public datasets are used for experimentation. Development can be performed on existing computing hardware without dedicated medical equipment. The planned web application targets free hosting tiers where suitable for academic demonstration. Browser-native voice functionality is preferred to avoid recurring third-party voice API costs. Therefore, the major project cost is development time, computing resources and documentation rather than software licensing.

## Social Relevance

A unified health-risk prediction interface demonstrates how machine learning can be applied to structured healthcare-related information. Bringing multiple disease prediction tasks into one educational platform can improve awareness of data-driven healthcare technologies and provide an academic demonstration for students and researchers. The platform can demonstrate responsible communication of model uncertainty and limitations. Its social relevance should not be confused with clinical validation. The system is not designed to replace medical professionals or provide definitive diagnoses. Its primary contribution is educational and research-oriented: demonstrating a reproducible machine learning workflow for multiple health-related prediction problems within one accessible software platform.

## Health Concern

Healthcare prediction systems require particular caution because users may interpret incorrect predictions as medical facts. MediPredict AI therefore presents outputs as preliminary risk predictions rather than confirmed diagnoses. Multiple evaluation metrics will be used instead of relying only on accuracy. Input validation, appropriate preprocessing and leakage prevention are necessary to reduce technical errors. Dataset limitations and the absence of clinical validation must also be communicated clearly. Users should not change medication or treatment based solely on the application's output. Professional healthcare advice remains necessary for diagnosis and treatment. The project is intended primarily for academic research, demonstration and exploration of machine learning methods.
