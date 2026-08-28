"""
ProcessMirror Studio
--------------------
Interactive interface for ProcessMirror.

Features:
- Create processes
- Add expected workflow steps
- Add actual workflow steps
- View processes
- Analyze process deviations
- Compare expected vs actual execution
"""

from process_mirror import ProcessMirror


class ProcessMirrorStudio:

    def __init__(self):

        self.system = ProcessMirror()

    # ----------------------------------
    # Create Process
    # ----------------------------------
    def create_process(self):

        print(
            "\n========== CREATE PROCESS ==========\n"
        )

        process_id = input(
            "Process ID: "
        ).strip()

        if not process_id:

            print(
                "\nProcess ID cannot be empty."
            )

            return

        if self.system.find_process(
                process_id):

            print(
                "\nProcess ID already exists."
            )

            return

        name = input(
            "Process Name: "
        ).strip()

        if not name:

            print(
                "\nProcess name cannot be empty."
            )

            return

        process = self.system.create_process(

            process_id,
            name

        )

        print(
            "\nProcess created successfully."
        )

        print(
            f"Process: {process['Name']}"
        )

    # ----------------------------------
    # Add Expected Step
    # ----------------------------------
    def add_expected_step(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        print(
            "\n========== ADD EXPECTED STEP ==========\n"
        )

        process_id = input(
            "Process ID: "
        ).strip()

        process = self.system.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        step = input(
            "Expected Step: "
        ).strip()

        if not step:

            print(
                "\nStep cannot be empty."
            )

            return

        self.system.add_expected_step(

            process_id,
            step

        )

        position = len(
            process["Expected Steps"]
        )

        print(
            f"\nExpected step added at "
            f"position {position}."
        )

    # ----------------------------------
    # Add Actual Step
    # ----------------------------------
    def add_actual_step(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        print(
            "\n========== ADD ACTUAL STEP ==========\n"
        )

        process_id = input(
            "Process ID: "
        ).strip()

        process = self.system.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        step = input(
            "Actual Step: "
        ).strip()

        if not step:

            print(
                "\nStep cannot be empty."
            )

            return

        self.system.add_actual_step(

            process_id,
            step

        )

        position = len(
            process["Actual Steps"]
        )

        print(
            f"\nActual step recorded at "
            f"position {position}."
        )

    # ----------------------------------
    # Add Expected Workflow
    # ----------------------------------
    def add_expected_workflow(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        process_id = input(
            "\nProcess ID: "
        ).strip()

        process = self.system.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        print(
            "\nEnter expected steps one by one."
        )

        print(
            "Press Enter on an empty step to finish.\n"
        )

        while True:

            step = input(
                "Expected Step: "
            ).strip()

            if not step:

                break

            self.system.add_expected_step(

                process_id,
                step

            )

        print(
            "\nExpected workflow updated."
        )

    # ----------------------------------
    # Add Actual Workflow
    # ----------------------------------
    def add_actual_workflow(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        process_id = input(
            "\nProcess ID: "
        ).strip()

        process = self.system.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        print(
            "\nEnter actual steps in the exact "
            "order they occurred."
        )

        print(
            "Press Enter on an empty step to finish.\n"
        )

        while True:

            step = input(
                "Actual Step: "
            ).strip()

            if not step:

                break

            self.system.add_actual_step(

                process_id,
                step

            )

        print(
            "\nActual workflow recorded."
        )

    # ----------------------------------
    # View Processes
    # ----------------------------------
    def view_processes(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        print(
            "\n========== PROCESSES ==========\n"
        )

        for process in self.system.processes:

            print(
                f"{process['ID']} | "
                f"{process['Name']}"
            )

            print(
                f"  Expected Steps: "
                f"{len(process['Expected Steps'])}"
            )

            print(
                f"  Actual Steps: "
                f"{len(process['Actual Steps'])}"
            )

            print()

    # ----------------------------------
    # Show Workflow
    # ----------------------------------
    def show_workflow(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        process_id = input(
            "\nProcess ID: "
        ).strip()

        process = self.system.find_process(
            process_id
        )

        if not process:

            print(
                "\nProcess not found."
            )

            return

        print(
            "\n========== PROCESS WORKFLOW ==========\n"
        )

        print(
            f"Process: {process['Name']}\n"
        )

        print(
            "EXPECTED WORKFLOW:"
        )

        if process["Expected Steps"]:

            for index, step in enumerate(

                    process["Expected Steps"],

                    start=1):

                print(
                    f"  {index}. {step}"
                )

        else:

            print(
                "  No expected steps."
            )

        print(
            "\nACTUAL WORKFLOW:"
        )

        if process["Actual Steps"]:

            for index, step in enumerate(

                    process["Actual Steps"],

                    start=1):

                print(
                    f"  {index}. {step}"
                )

        else:

            print(
                "  No actual steps."
            )

    # ----------------------------------
    # Analyze Process
    # ----------------------------------
    def analyze_process(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        print(
            "\n========== ANALYZE PROCESS ==========\n"
        )

        process_id = input(
            "Process ID: "
        ).strip()

        self.system.display_analysis(
            process_id
        )

    # ----------------------------------
    # Analyze All
    # ----------------------------------
    def analyze_all(self):

        if not self.system.processes:

            print(
                "\nNo processes available."
            )

            return

        results = (
            self.system.analyze_all_processes()
        )

        print(
            "\n========== ALL PROCESS ANALYSIS ==========\n"
        )

        for index, result in enumerate(
                results,
                start=1):

            print(
                f"{index}. "
                f"{result['Process']}"
            )

            print(
                f"   Completion: "
                f"{result['Completion']}%"
            )

            print(
                f"   Compliance: "
                f"{result['Compliance']}%"
            )

            print(
                f"   Status: "
                f"{result['Status']}"
            )

            print()

    # ----------------------------------
    # Main Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)

            print(
                "              PROCESS MIRROR"
            )

            print("=" * 60)

            print("1. Create Process")
            print("2. Add Expected Step")
            print("3. Add Actual Step")
            print("4. Add Expected Workflow")
            print("5. Add Actual Workflow")
            print("6. View Processes")
            print("7. Show Process Workflow")
            print("8. Analyze Process")
            print("9. Analyze All Processes")
            print("10. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.create_process()

            elif choice == "2":

                self.add_expected_step()

            elif choice == "3":

                self.add_actual_step()

            elif choice == "4":

                self.add_expected_workflow()

            elif choice == "5":

                self.add_actual_workflow()

            elif choice == "6":

                self.view_processes()

            elif choice == "7":

                self.show_workflow()

            elif choice == "8":

                self.analyze_process()

            elif choice == "9":

                self.analyze_all()

            elif choice == "10":

                print(
                    "\nThank you for using "
                    "ProcessMirror."
                )

                break

            else:

                print(
                    "\nInvalid choice. Please try again."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = ProcessMirrorStudio()

    studio.menu()
