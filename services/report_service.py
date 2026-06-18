from datetime import datetime


class ReportService:

    @staticmethod
    def generate_report(
        report_text
    ):

        filename = (
            f"reports/report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(report_text)

        return filename
