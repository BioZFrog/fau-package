import argparse
import os
from pathlib import Path


LOG_FILE = Path.home() / '.todo_logger' / 'log.txt'
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

UNCHECKED_PREFIX = '[ ] '
CHECKED_PREFIX = '[x] '
DISPLAY_UNCHECKED = '☐ '
DISPLAY_CHECKED = '✔ '

def add_task(task: str) -> None:
    task_text = task.strip()
    if not task_text:
        print('Cannot add an empty task.')
        return

    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{UNCHECKED_PREFIX}{task_text}        -- {os.getcwd()}\n")
    print(f"Added task: {task_text}")


def tick_task(index: int) -> None:
    if not os.path.exists(LOG_FILE):
        print('No tasks file found.')
        return

    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]

    if index < 1 or index > len(lines):
        print(f'Index out of range: {index}')
        return

    original = lines[index - 1]
    if original.startswith(CHECKED_PREFIX):
        print(f'Task {index} is already ticked.')
        return

    task_text = original[len(UNCHECKED_PREFIX):] if original.startswith(UNCHECKED_PREFIX) else original
    lines[index - 1] = f"{CHECKED_PREFIX}{task_text}"

    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

    print(f'Ticked task {index}: {task_text}')


def clear() -> None:
    if not os.path.exists(LOG_FILE):
        print('No tasks file found.')
        return

    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        file.write('')
    print('Cleared all tasks.')


def tick_last_task() -> None:
    if not os.path.exists(LOG_FILE):
        print('No tasks file found.')
        return

    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]

    if not lines:
        print('No tasks yet.')
        return

    tick_task(len(lines))

def show_tasks() -> None:
    if not os.path.exists(LOG_FILE):
        print('No tasks yet.')
        return

    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]

    if not lines:
        print('No tasks yet.')
        return

    for index, line in enumerate(lines, start=1):
        if line.startswith(CHECKED_PREFIX):
            display_line = DISPLAY_CHECKED + line[len(CHECKED_PREFIX):]
        elif line.startswith(UNCHECKED_PREFIX):
            display_line = DISPLAY_UNCHECKED + line[len(UNCHECKED_PREFIX):]
        else:
            display_line = DISPLAY_UNCHECKED + line

        print(f"{index}. {display_line}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Todo list manager')
    parser.add_argument('--add', metavar='TASK', nargs=argparse.REMAINDER, help='Add a task')
    parser.add_argument('--tick', metavar='INDEX', nargs='*', type=int, help='Tick task by index')
    parser.add_argument('--clear', action='store_true', help='Clear all tasks')
    args = parser.parse_args()

    if args.add is not None:
        task = ' '.join(args.add).strip()
        add_task(task)
    elif args.tick is not None:
        if not args.tick:
            tick_last_task()
        else:
            for index in args.tick:
                tick_task(index)
    elif args.clear:
        clear()
    else:
        show_tasks()


if __name__ == '__main__':
    main()