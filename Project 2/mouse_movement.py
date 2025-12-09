import math
import random
import time

def human_curve(start, end, steps=50):
    """
    Creates a human-like Bezier curve path from start to end.
    """
    x1, y1 = start
    x2, y2 = end

    # Random control points to avoid robotic path
    ctrl1 = (x1 + (x2 - x1) * random.uniform(0.2, 0.4),
             y1 + abs(y2 - y1) * random.uniform(0.2, 0.4))

    ctrl2 = (x1 + (x2 - x1) * random.uniform(0.6, 0.8),
             y1 + abs(y2 - y1) * random.uniform(0.6, 0.8))

    path = []

    for t in [i / steps for i in range(steps)]:
        # Bezier quadratic curve algorithm
        x = (1 - t)**3 * x1 + 3 * (1 - t)**2 * t * ctrl1[0] + 3 * (1 - t) * t**2 * ctrl2[0] + t**3 * x2
        y = (1 - t)**3 * y1 + 3 * (1 - t)**2 * t * ctrl1[1] + 3 * (1 - t) * t**2 * ctrl2[1] + t**3 * y2

        # Add human micro-jitter
        x += random.uniform(-0.5, 0.5)
        y += random.uniform(-0.5, 0.5)

        path.append((x, y))

    return path


def human_move_mouse(page, start, end):
    """
    Moves mouse smoothly with human-like imperfections.
    """
    path = human_curve(start, end, steps=random.randint(8, 15))

    for (x, y) in path:
        page.mouse.move(x, y)
        time.sleep(random.uniform(0.001, 0.004))  # human speed variation

    # Human overshoot (humans go slightly beyond target then correct)
    if random.random() < 0.7:
        overshoot_x = end[0] + random.randint(-1, 1)
        overshoot_y = end[1] + random.randint(-1, 1)
        page.mouse.move(overshoot_x, overshoot_y)
        time.sleep(random.uniform(0.002, 0.005))
        page.mouse.move(end[0], end[1])


def human_hover(page, element):
    """Moves to element center and hovers with a pause"""

    box = element.bounding_box()
    if not box:
        return

    target = (
        box["x"] + box["width"] / 2,
        box["y"] + box["height"] / 2
    )

    # Random starting point
    start = (random.randint(10, 400), random.randint(10, 300))

    human_move_mouse(page, start, target)

    # Hover pause like a real human
    time.sleep(random.uniform(0.015, 0.045))


def human_click(page, element):
    """Hover + micro hesitation + click"""

    human_hover(page, element)

    # hesitation before click
    time.sleep(random.uniform(0.005, 0.02))

    #element.click(delay=random.randint(40, 120))  # human click delay


def human_scroll(page, amount=2000):
    """Scroll slowly like a human reading"""
    total = 0
    while total < amount:
        step = random.randint(10, 20)
        page.mouse.wheel(0, step)
        total += step
        time.sleep(random.uniform(0.005, 0.02))