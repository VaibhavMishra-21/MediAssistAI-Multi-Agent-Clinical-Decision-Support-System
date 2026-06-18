from workflows.diagnosis_workflow import (
    run_medical_workflow
)

print("=" * 60)
print("MediAssistAI")
print("=" * 60)

symptoms = input(
    "\nEnter patient symptoms:\n"
)

result = run_medical_workflow(
    symptoms
)

print("\n")
print("=" * 60)
print("ANALYSIS RESULT")
print("=" * 60)

print("\nRisk Level:")
print(result["risk"])

print("\nFindings:")
print(result["findings"])

print("\nFinal Report:")
print(result["final_report"])

print("\nSaved To:")
print(result["report_file"])
