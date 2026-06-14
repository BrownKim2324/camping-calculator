def input_float(prompt, default=None):
    while True:
        try:
            value = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ")
            if value.strip() == "" and default is not None:
                return float(default)
            return float(value)
        except ValueError:
            print("숫자를 올바르게 입력해 주세요.")


def input_int(prompt, default=None):
    while True:
        try:
            value = input(f"{prompt}{' [' + str(default) + ']' if default is not None else ''}: ")
            if value.strip() == "" and default is not None:
                return int(default)
            return int(value)
        except ValueError:
            print("정수를 올바르게 입력해 주세요.")


def calculate_total_cost(nights, people, site_fee_per_night, food_cost, fuel_cost, equipment_cost, additional_cost):
    camping_fee = nights * site_fee_per_night
    total = camping_fee + food_cost + fuel_cost + equipment_cost + additional_cost
    per_person = total / people if people > 0 else 0
    return {
        "camping_fee": camping_fee,
        "total": total,
        "per_person": per_person,
    }


def main():
    print("=== 간단한 캠핑 계산기 ===")
    nights = input_int("캠핑 기간(박)", 1)
    people = input_int("참여 인원(명)", 2)
    site_fee_per_night = input_float("사이트 1박 요금(원)", 30000)
    food_cost = input_float("식비 총액(원)", 60000)
    fuel_cost = input_float("연료/가스비 총액(원)", 10000)
    equipment_cost = input_float("장비 대여/구입비(원)", 0)
    additional_cost = input_float("기타 비용(원)", 0)

    result = calculate_total_cost(
        nights,
        people,
        site_fee_per_night,
        food_cost,
        fuel_cost,
        equipment_cost,
        additional_cost,
    )

    print("\n=== 계산 결과 ===")
    print(f"캠핑장 비용: {result['camping_fee']:.0f}원")
    print(f"전체 총 비용: {result['total']:.0f}원")
    print(f"1인당 비용: {result['per_person']:.0f}원")
    print("====================")
    print("안전한 캠핑 되세요!")


if __name__ == "__main__":
    main()
