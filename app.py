# 授業一覧
# 各授業は辞書で管理する
# {
#     "name": "情報数学",
#     "assignments": ["レポート1", "レポート2"]
# }
subjects = []


def register_subject() :
    """授業を登録する"""

    subject_name = input("授業名を入力してください: ").strip()

    if subject_name == "" :
        print("エラー：授業名を入力してください。")
        return

        subjects.append({
            "name": subject_name,
            "assignments" : []
            })

        print("授業を登録しました。")


        def register_assignment() :
        """課題を登録する"""

        if len(subjects) == 0 :
            print("エラー：授業が登録されていません。先に授業を登録してください。")
            return

            print("\n===== 授業一覧 =====")

            for i, subject in enumerate(subjects, start = 1) :
                print(f"{i}. {subject['name']}")

                subject_number = input("課題を登録する授業番号を入力してください: ").strip()

                if subject_number == "" :
                    print("エラー：授業番号を入力してください。")
                    return

                    if not subject_number.isdigit() :
                        print("エラー：数字を入力してください。")
                        return

                        subject_index = int(subject_number) - 1

                        if subject_index < 0 or subject_index >= len(subjects) :
                            print("エラー：存在しない授業番号です。")
                            return

                            assignment_name = input("課題名を入力してください: ").strip()

                            if assignment_name == "":
print("エラー：課題名を入力してください。")
return

subjects[subject_index]["assignments"].append(assignment_name)

print("課題を登録しました。")


def show_list() :
    """授業ごとの課題一覧を表示する"""

    print("\n===== 登録一覧 =====")

    if len(subjects) == 0 :
        print("授業が登録されていません。")
        return

        for i, subject in enumerate(subjects, start = 1) :

            print(f"\n{i}. {subject['name']}")

            if len(subject["assignments"]) == 0 :
                print("  課題なし")
            else:
for j, assignment in enumerate(subject["assignments"], start = 1) :
    print(f"  {j}. {assignment}")

    print()


    def main() :

    while True :

        print("==== メニュー ====")
        print("1. 授業登録")
        print("2. 課題登録")
        print("3. 一覧表示")
        print("4. 終了")

        choice = input("選択してください: ").strip()

        if choice == "1":
register_subject()

elif choice == "2" :
    register_assignment()

    elif choice == "3" :
    show_list()

    elif choice == "4" :
    print("終了します。")
    break

        else:
print("エラー：1～4を入力してください。")


main()