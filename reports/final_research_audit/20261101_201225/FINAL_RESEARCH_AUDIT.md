# Final Research Audit

- Created: 20261101_201225
- Technical checks passed: 4/5
- Overall technical checks: REVIEW REQUIRED

## Repeated cross-validation
- Configurations: 24
- Fold evaluations: 600

## CKD diagnostics
- Rows: 400
- Features: 24
- Missing feature cells: 1012
- Duplicate feature rows: 0

## Class imbalance
- diabetes: {'0': 500, '1': 268} (majority/minority ratio: 1.866)
- heart: {'0': 164, '1': 139} (majority/minority ratio: 1.180)
- ckd: {'0': 150, '1': 250} (majority/minority ratio: 1.667)
- breast_cancer: {'0': 357, '1': 212} (majority/minority ratio: 1.684)

## Technical checks
- repeated_cross_validation: PASS
- research_validation: PASS
- class_imbalance_audit: REVIEW REQUIRED
- existing_training_evidence: PASS
- pytest: PASS
- frontend_build: REVIEW REQUIRED

## Limitations
- CKD's near-perfect cross-validation scores require source-level and independent-dataset investigation.
- Repeated cross-validation is internal validation, not external clinical validation.
- Class stratification does not itself correct class imbalance.
- No clinical deployment or diagnostic claim is established by these experiments.

This audit does not establish clinical validity or prove the absence of data leakage.