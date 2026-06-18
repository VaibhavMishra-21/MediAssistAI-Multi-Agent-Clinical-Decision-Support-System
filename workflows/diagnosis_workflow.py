from agents.symptom_agent import SymptomAgent
from agents.risk_agent import RiskAgent
from agents.cardiology_agent import CardiologyAgent
from agents.pulmonology_agent import PulmonologyAgent
from agents.neurology_agent import NeurologyAgent
from agents.psychology_agent import PsychologyAgent
from agents.supervisor_agent import SupervisorAgent

from services.report_service import ReportService


symptom_agent = SymptomAgent()
risk_agent = RiskAgent()

cardiology_agent = CardiologyAgent()
pulmonology_agent = PulmonologyAgent()
neurology_agent = NeurologyAgent()
psychology_agent = PsychologyAgent()

supervisor_agent = SupervisorAgent()


def run_medical_workflow(symptoms):

    findings = symptom_agent.analyze(symptoms)

    risk = risk_agent.evaluate(symptoms)

    cardiology = cardiology_agent.analyze(symptoms)

    pulmonology = pulmonology_agent.analyze(symptoms)

    neurology = neurology_agent.analyze(symptoms)

    psychology = psychology_agent.analyze(symptoms)

    final_report = (
        supervisor_agent.generate_final_report(
            cardiology,
            pulmonology,
            neurology,
            psychology,
            risk
        )
    )

    report_file = ReportService.generate_report(
        final_report
    )

    return {
        "findings": findings,
        "risk": risk,
        "cardiology": cardiology,
        "pulmonology": pulmonology,
        "neurology": neurology,
        "psychology": psychology,
        "final_report": final_report,
        "report_file": report_file
    }
