"""
ProcessMirror
-------------
File: process_mirror.py

Purpose
-------
ProcessMirror compares an expected workflow with the
workflow that actually happened.

It identifies:

- Missing steps
- Extra steps
- Steps performed in the wrong order
- Repeated steps
- Completed steps
- Process deviations
- Overall process compliance

Example:

Expected:
1. Receive Request
2. Validate Request
3. Approve Request
4. Complete Request

Actual:
1. Receive Request
2. Approve Request
3. Validate Request
4. Complete Request

Result:
- Step "Approve Request" happened too early
- Step "Validate Request" happened too late
- Process deviation detected
"""


class ProcessMirror:

    def __init__(self):

        self.processes = []

    # ----------------------------------
    # Create Process
    # ----------------------------------
    def create_process(
            self,
            process_id,
            name):

        process = {

            "ID":
                process_id,

            "Name":
                name,

            "Expected Steps":
                [],

            "Actual Steps":
                []

        }

        self.processes.append(
            process
        )

        return process

    # ----------------------------------
    # Find Process
    # ----------------------------------
    def find_process(
            self,
            process_id):

        for process in self.processes:

            if process["ID"] == process_id:

                return process

        return None

    # ----------------------------------
    # Add Expected Step
    # ----------------------------------
    def add_expected_step(
            self,
            process_id,
            step_name):

        process = self.find_process(
            process_id
        )

        if not process:

            return None

        process[
            "Expected Steps"
        ].append(
            step_name
        )

        return step_name

    # ----------------------------------
    # Add Actual Step
    # ----------------------------------
    def add_actual_step(
            self,
            process_id,
            step_name):

        process = self.find_process(
            process_id
        )

        if not process:

            return None

        process[
            "Actual Steps"
        ].append(
            step_name
        )

        return step_name

    # ----------------------------------
    # Normalize Step
    # ----------------------------------
    def normalize_step(
            self,
            step):

        return step.strip().lower()

    # ----------------------------------
    # Find Missing Steps
    # ----------------------------------
    def find_missing_steps(
            self,
            expected,
            actual):

        actual_normalized = [

            self.normalize_step(step)

            for step in actual

        ]

        missing = []

        for step in expected:

            if self.normalize_step(
                    step
            ) not in actual_normalized:

                missing.append(
                    step
                )

        return missing

    # ----------------------------------
    # Find Extra Steps
    # ----------------------------------
    def find_extra_steps(
            self,
            expected,
            actual):

        expected_normalized = [

            self.normalize_step(step)

            for step in expected

        ]

        extra = []

        for step in actual:

            if self.normalize_step(
                    step
            ) not in expected_normalized:

                extra.append(
                    step
                )

        return extra

    # ----------------------------------
    # Find Repeated Steps
    # ----------------------------------
    def find_repeated_steps(
            self,
            actual):

        counts = {}

        for step in actual:

            normalized = (
                self.normalize_step(step)
            )

            counts[normalized] = (
                counts.get(
                    normalized,
                    0
                ) + 1
            )

        repeated = []

        for step, count in counts.items():

            if count > 1:

                repeated.append({

                    "Step":
                        step,

                    "Occurrences":
                        count

                })

        return repeated

    # ----------------------------------
    # Find Order Deviations
    # ----------------------------------
    def find_order_deviations(
            self,
            expected,
            actual):

        expected_positions = {}

        for index, step in enumerate(
                expected):

            normalized = (
                self.normalize_step(step)
            )

            expected_positions[
                normalized
            ] = index

        actual_positions = []

        for index, step in enumerate(
                actual):

            normalized = (
                self.normalize_step(step)
            )

            if normalized in expected_positions:

                actual_positions.append({

                    "Step":
                        step,

                    "Expected Position":
                        expected_positions[
                            normalized
                        ],

                    "Actual Position":
                        index

                })

        deviations = []

        for item in actual_positions:

            if (

                item["Expected Position"]
                !=
                item["Actual Position"]

            ):

                deviations.append(
                    item
                )

        return deviations

    # ----------------------------------
    # Calculate Completion
    # ----------------------------------
    def calculate_completion(
            self,
            expected,
            actual):

        if not expected:

            return 0

        expected_normalized = [

            self.normalize_step(step)

            for step in expected

        ]

        actual_normalized = [

            self.normalize_step(step)

            for step in actual

        ]

        completed = 0

        for step in expected_normalized:

            if step in actual_normalized:

                completed += 1

        completion = (

            completed
            /
            len(expected_normalized)

        ) * 100

        return round(
            completion,
            2
        )

    # ----------------------------------
    # Calculate Compliance
    # ----------------------------------
    def calculate_compliance(
            self,
            expected,
            actual):

        if not expected:

            return 0

        missing = self.find_missing_steps(
            expected,
            actual
        )

        extra = self.find_extra_steps(
            expected,
            actual
        )

        order = self.find_order_deviations(
            expected,
            actual
        )

        repeated = self.find_repeated_steps(
            actual
        )

        penalty = 0

        penalty += (
            len(missing) * 20
        )

        penalty += (
            len(extra) * 10
        )

        penalty += (
            len(order) * 10
        )

        penalty += (
            len(repeated) * 5
        )

        compliance = max(
            0,
            100 - penalty
        )

        return round(
            compliance,
            2
        )

    # ----------------------------------
    # Determine Process Status
    # ----------------------------------
    def process_status(
            self,
            compliance,
            missing,
            extra,
            order):

        if not missing and not extra and not order:

            return "Fully Compliant"

        if missing:

            if compliance < 50:

                return "Major Deviation"

            return "Incomplete"

        if compliance >= 80:

            return "Minor Deviation"

        return "Major Deviation"

    # ----------------------------------
    # Analyze Process
    # ----------------------------------
    def analyze_process(
            self,
            process):

        expected = process[
            "Expected Steps"
        ]

        actual = process[
            "Actual Steps"
        ]

        missing = self.find_missing_steps(
            expected,
            actual
        )

        extra = self.find_extra_steps(
            expected,
            actual
        )

        repeated = self.find_repeated_steps(
            actual
        )

        order = self.find_order_deviations(
            expected,
            actual
        )

        completion = (
            self.calculate_completion(
                expected,
                actual
            )
        )

        compliance = (
            self.calculate_compliance(
                expected,
                actual
            )
        )

        status = self.process_status(

            compliance,
            missing,
            extra,
            order

        )

        return {

            "Process ID":
                process["ID"],

            "Process":
                process["Name"],

            "Expected Steps":
                expected,

            "Actual Steps":
                actual,

            "Missing Steps":
                missing,

            "Extra Steps":
                extra,

            "Repeated Steps":
                repeated,

            "Order Deviations":
                order,

            "Completion":
                completion,

            "Compliance":
                compliance,

            "Status":
                status

        }

    # ----------------------------------
    # Analyze All Processes
    # ----------------------------------
    def analyze_all_processes(self):

        results = []

        for process in self.processes:

            results.append(

                self.analyze_process(
                    process
                )

            )

        return results

    # ----------------------------------
    # Display Analysis
    # ----------------------------------
    def display_analysis(
            self,
            process_id):

        process = self.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        result = self.analyze_process(
            process
        )

        print(
            "\n========== PROCESS MIRROR ==========\n"
        )

        print(
            f"Process: "
            f"{result['Process']}"
        )

        print(
            f"Completion: "
            f"{result['Completion']}%"
        )

        print(
            f"Compliance: "
            f"{result['Compliance']}%"
        )

        print(
            f"Status: "
            f"{result['Status']}"
        )

        print(
            "\nExpected Steps:"
        )

        for index, step in enumerate(
                result["Expected Steps"],
                start=1):

            print(
                f"{index}. {step}"
            )

        print(
            "\nActual Steps:"
        )

        for index, step in enumerate(
                result["Actual Steps"],
                start=1):

            print(
                f"{index}. {step}"
            )

        print(
            "\nMissing Steps:"
        )

        if result["Missing Steps"]:

            for step in result[
                    "Missing Steps"]:

                print(
                    f"- {step}"
                )

        else:

            print(
                "- None"
            )

        print(
            "\nExtra Steps:"
        )

        if result["Extra Steps"]:

            for step in result[
                    "Extra Steps"]:

                print(
                    f"- {step}"
                )

        else:

            print(
                "- None"
            )

        print(
            "\nRepeated Steps:"
        )

        if result["Repeated Steps"]:

            for item in result[
                    "Repeated Steps"]:

                print(
                    f"- {item['Step']} "
                    f"({item['Occurrences']} times)"
                )

        else:

            print(
                "- None"
            )

        print(
            "\nOrder Deviations:"
        )

        if result["Order Deviations"]:

            for item in result[
                    "Order Deviations"]:

                print(
                    f"- {item['Step']}: "
                    f"expected position "
                    f"{item['Expected Position'] + 1}, "
                    f"actual position "
                    f"{item['Actual Position'] + 1}"
                )

        else:

            print(
                "- None"
            )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    system = ProcessMirror()

    # ----------------------------------
    # Create Process
    # ----------------------------------

    system.create_process(

        "P001",

        "Customer Refund Process"

    )

    # ----------------------------------
    # Expected Workflow
    # ----------------------------------

    system.add_expected_step(
        "P001",
        "Receive Request"
    )

    system.add_expected_step(
        "P001",
        "Validate Request"
    )

    system.add_expected_step(
        "P001",
        "Approve Refund"
    )

    system.add_expected_step(
        "P001",
        "Process Refund"
    )

    system.add_expected_step(
        "P001",
        "Notify Customer"
    )

    # ----------------------------------
    # Actual Workflow
    # ----------------------------------

    system.add_actual_step(
        "P001",
        "Receive Request"
    )

    system.add_actual_step(
        "P001",
        "Approve Refund"
    )

    system.add_actual_step(
        "P001",
        "Validate Request"
    )

    system.add_actual_step(
        "P001",
        "Process Refund"
    )

    system.add_actual_step(
        "P001",
        "Notify Customer"
    )

    # ----------------------------------
    # Analyze
    # ----------------------------------

    system.display_analysis(
        "P001"
    )
