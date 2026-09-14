# Multi-Disease Dataset Audit

Automated structural audit of the four raw datasets before preprocessing and model training.

## Diabetes

- Rows: 768
- Columns: 9
- Target: `Outcome`
- Target found: True
- Duplicate rows: 0

### Columns

- `Pregnancies`
- `Glucose`
- `BloodPressure`
- `SkinThickness`
- `Insulin`
- `BMI`
- `DiabetesPedigreeFunction`
- `Age`
- `Outcome`

### Missing Values

- None detected by pandas.

### Suspicious Values

- None detected.

### Target Distribution

- `0`: 500
- `1`: 268

## Heart

- Rows: 303
- Columns: 14
- Target: `num`
- Target found: True
- Duplicate rows: 0

### Columns

- `age`
- `sex`
- `cp`
- `trestbps`
- `chol`
- `fbs`
- `restecg`
- `thalach`
- `exang`
- `oldpeak`
- `slope`
- `ca`
- `thal`
- `num`

### Missing Values

- `ca`: 4
- `thal`: 2

### Suspicious Values

- None detected.

### Target Distribution

- `0`: 164
- `1`: 55
- `2`: 36
- `3`: 35
- `4`: 13

## Ckd

- Rows: 400
- Columns: 25
- Target: `class`
- Target found: True
- Duplicate rows: 0

### Columns

- `age`
- `bp`
- `sg`
- `al`
- `su`
- `rbc`
- `pc`
- `pcc`
- `ba`
- `bgr`
- `bu`
- `sc`
- `sod`
- `pot`
- `hemo`
- `pcv`
- `wbcc`
- `rbcc`
- `htn`
- `dm`
- `cad`
- `appet`
- `pe`
- `ane`
- `class`

### Missing Values

- `age`: 9
- `bp`: 12
- `sg`: 47
- `al`: 46
- `su`: 49
- `rbc`: 152
- `pc`: 65
- `pcc`: 4
- `ba`: 4
- `bgr`: 44
- `bu`: 19
- `sc`: 17
- `sod`: 87
- `pot`: 88
- `hemo`: 52
- `pcv`: 71
- `wbcc`: 106
- `rbcc`: 131
- `htn`: 2
- `dm`: 2
- `cad`: 2
- `appet`: 1
- `pe`: 1
- `ane`: 1

### Suspicious Values

- None detected.

### Target Distribution

- `ckd`: 250
- `notckd`: 150

## Breast Cancer

- Rows: 569
- Columns: 31
- Target: `Diagnosis`
- Target found: True
- Duplicate rows: 0

### Columns

- `radius1`
- `texture1`
- `perimeter1`
- `area1`
- `smoothness1`
- `compactness1`
- `concavity1`
- `concave_points1`
- `symmetry1`
- `fractal_dimension1`
- `radius2`
- `texture2`
- `perimeter2`
- `area2`
- `smoothness2`
- `compactness2`
- `concavity2`
- `concave_points2`
- `symmetry2`
- `fractal_dimension2`
- `radius3`
- `texture3`
- `perimeter3`
- `area3`
- `smoothness3`
- `compactness3`
- `concavity3`
- `concave_points3`
- `symmetry3`
- `fractal_dimension3`
- `Diagnosis`

### Missing Values

- None detected by pandas.

### Suspicious Values

- None detected.

### Target Distribution

- `B`: 357
- `M`: 212

