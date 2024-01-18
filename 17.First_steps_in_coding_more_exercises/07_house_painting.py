x = float(input())
y = float(input())
h = float(input())

middle_wall = x * y
window = 1.5 * 1.5
total_middle_walls = 2 * middle_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
total_walls = 2 * back_wall - entrance
total_area = total_walls + total_middle_walls
green_paint = total_area / 3.4

roof = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)
total_area_roof = roof + roof_triangles
red_paint = total_area_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')