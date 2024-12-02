def is_report_safe(report: list[int]) -> bool:
    current_level = report[0]
    is_safe = True
    is_increasing = None
    for level in report[1:]:
        if abs(current_level - level) < 1 or abs(current_level - level) > 3:
            is_safe = False
            break
        if is_increasing is not None:
            if (not is_increasing and current_level < level) \
                or (is_increasing and current_level > level):
                    is_safe = False
                    break
        elif is_increasing is None:
            is_increasing = current_level < level
        current_level = level
    return is_safe

def part1(reports: list[list[int]]) -> int:
    return sum(map(is_report_safe, reports))

def part2(reports: list[list[int]]) -> int:
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
            continue
        for index in range(len(report)):
            if is_report_safe(report[:index] + report[index + 1:]):
                safe_reports += 1
                break
    return safe_reports

def run(part: int, input_data: list[str]):
    reports = []
    for line in input_data:
        levels = line.split(" ")
        reports.append([int(e) for e in levels])
    print(part1(reports) if part == 1 else part2(reports))
