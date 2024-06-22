# 使用chatGPT生成

import random

courses = [
    {'teacher': '', 'name': '　　', 'hours': -1},  # 那一節沒上課
    {'teacher': '甲', 'name': '機率', 'hours': 2},
    {'teacher': '甲', 'name': '線代', 'hours': 3},
    {'teacher': '甲', 'name': '離散', 'hours': 3},
    {'teacher': '乙', 'name': '視窗', 'hours': 3},
    {'teacher': '乙', 'name': '科學', 'hours': 3},
    {'teacher': '乙', 'name': '系統', 'hours': 3},
    {'teacher': '乙', 'name': '計概', 'hours': 3},
    {'teacher': '丙', 'name': '軟工', 'hours': 3},
    {'teacher': '丙', 'name': '行動', 'hours': 3},
    {'teacher': '丙', 'name': '網路', 'hours': 3},
    {'teacher': '丁', 'name': '媒體', 'hours': 3},
    {'teacher': '丁', 'name': '工數', 'hours': 3},
    {'teacher': '丁', 'name': '動畫', 'hours': 3},
    {'teacher': '丁', 'name': '電子', 'hours': 4},
    {'teacher': '丁', 'name': '嵌入', 'hours': 3},
    {'teacher': '戊', 'name': '網站', 'hours': 3},
    {'teacher': '戊', 'name': '網頁', 'hours': 3},
    {'teacher': '戊', 'name': '演算', 'hours': 3},
    {'teacher': '戊', 'name': '結構', 'hours': 3},
    {'teacher': '戊', 'name': '智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']
rooms = ['A', 'B']
slots = [
    'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
    'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
    'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
    'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
    'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
    'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
    'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
    'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
    'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
    'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',
]

def generate_initial_schedule(courses, slots):
    schedule = {}
    available_slots = slots.copy()
    random.shuffle(available_slots)
    for course in courses:
        if course['hours'] > 0:
            for _ in range(course['hours']):
                if available_slots:
                    slot = available_slots.pop()
                    schedule[slot] = course
    return schedule

def calculate_conflicts(schedule):
    conflicts = 0
    teacher_slots = {}
    for slot, course in schedule.items():
        if course['teacher'] not in teacher_slots:
            teacher_slots[course['teacher']] = []
        teacher_slots[course['teacher']].append(slot)

    for teacher, slots in teacher_slots.items():
        days = set(slot[1] for slot in slots)
        if len(days) < len(slots):
            conflicts += len(slots) - len(days)
    return conflicts

def get_neighbors(schedule, courses, slots):
    neighbors = []
    for _ in range(10):
        new_schedule = schedule.copy()
        swap_slot1, swap_slot2 = random.sample(slots, 2)
        new_schedule[swap_slot1], new_schedule[swap_slot2] = new_schedule.get(swap_slot2, {'teacher': '', 'name': '　　', 'hours': -1}), new_schedule.get(swap_slot1, {'teacher': '', 'name': '　　', 'hours': -1})
        neighbors.append(new_schedule)
    return neighbors

def hill_climbing(courses, slots):
    current_schedule = generate_initial_schedule(courses, slots)
    current_conflicts = calculate_conflicts(current_schedule)
    
    while True:
        neighbors = get_neighbors(current_schedule, courses, slots)
        best_neighbor = min(neighbors, key=calculate_conflicts)
        best_neighbor_conflicts = calculate_conflicts(best_neighbor)
        
        if best_neighbor_conflicts >= current_conflicts:
            break
        current_schedule = best_neighbor
        current_conflicts = best_neighbor_conflicts

    return current_schedule

schedule = hill_climbing(courses, slots)

def print_schedule(schedule):
    for slot in slots:
        course = schedule.get(slot, {'teacher': '', 'name': '　　', 'hours': -1})
        print(f"{slot}: {course['teacher']} {course['name']}")

print_schedule(schedule)
