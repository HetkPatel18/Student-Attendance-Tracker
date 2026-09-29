import tracker

def ask_number(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            return int(val)
        print("Enter a valid whole number.")

def main():
    courses = tracker.load_data()

    while True:
        print("\n=== Student Attendance Tracker ===")
        print("1. View Attendance Dashboard")
        print("2. Add a Subject")
        print("3. Log Today's Classes")
        print("4. Check Bunks & Warnings")
        print("5. Delete a Subject")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            if not courses:
                print("No subjects added yet.")
                continue
            print(f"\n{'Code':<8} {'Subject':<18} {'Total':<8} {'Attended':<10} {'Pct':<8}")
            print("-" * 52)
            for c in courses:
                pct = tracker.get_percentage(c["attended"], c["total"])
                print(f"{c['code']:<8} {c['name'][:16]:<18} {c['total']:<8} {c['attended']:<10} {pct}%")

        elif choice == "2":
            code = input("Course Code: ").strip().upper()
            if tracker.find_course(courses, code):
                print("Subject already exists.")
                continue
            name = input("Subject Name: ").strip()
            total = ask_number("Total classes held: ")
            attended = ask_number("Classes attended: ")
            if attended > total:
                print("Attended classes cannot be more than total classes.")
                continue
            courses.append({"code": code, "name": name, "total": total, "attended": attended})
            tracker.save_data(courses)
            print(f"Added {code} successfully.")

        elif choice == "3":
            code = input("Enter Course Code: ").strip()
            target = tracker.find_course(courses, code)
            if not target:
                print("Subject not found.")
                continue
            att = ask_number("Attended today: ")
            miss = ask_number("Missed today: ")
            target["attended"] += att
            target["total"] += (att + miss)
            tracker.save_data(courses)
            new_pct = tracker.get_percentage(target["attended"], target["total"])
            print(f"Updated. Current percentage: {new_pct}%")

        elif choice == "4":
            if not courses:
                print("No subjects available.")
                continue
            print("\n--- Compliance Report (75% Criteria) ---")
            for c in courses:
                pct = tracker.get_percentage(c["attended"], c["total"])
                print(f"\n{c['code']} - {c['name']}: {pct}%")
                if pct >= 75.0:
                    bunks = tracker.calculate_safe_bunks(c["attended"], c["total"])
                    print(f"  You can safely bunk {bunks} class(es).")
                else:
                    needed = tracker.calculate_needed_classes(c["attended"], c["total"])
                    print(f"  Warning: Attend next {needed} class(es) to hit 75%.")

        elif choice == "5":
            code = input("Enter Course Code to delete: ").strip()
            target = tracker.find_course(courses, code)
            if target:
                courses.remove(target)
                tracker.save_data(courses)
                print(f"Deleted {code}.")
            else:
                print("Subject not found.")

        elif choice == "6":
            print("Session saved. Bye!")
            break

if __name__ == "__main__":
    main()