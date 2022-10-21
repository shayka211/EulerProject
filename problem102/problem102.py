from EulerProject.useful_functions import get_list_of_sets_from_text_separated_by_commas




def triangle_containment(A, B, C, point):
    outer_point_from_triangle = (max(A[0], B[0], C[0])+1, max(A[1], B[1], C[1])+1)
    number_of_intersections = 0
    if is_lines_intersecting_in_range_of_points(A, B, point, outer_point_from_triangle):
        number_of_intersections +=1
    if is_lines_intersecting_in_range_of_points(A, C, point, outer_point_from_triangle):
        number_of_intersections += 1
    if is_lines_intersecting_in_range_of_points(B, C, point, outer_point_from_triangle):
        number_of_intersections += 1
    return number_of_intersections % 2 ==1





def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        return [px, py]


# A is of the following A=(3,5)
def is_lines_intersecting_in_range_of_points(A, B, C, D):
    M = findIntersection(A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1])
    return point_in_the_middle_of_two_points(A, B, M) and point_in_the_middle_of_two_points(C, D, M)


def point_in_the_middle_of_two_points(X, Y, M):
    return min(X[0], Y[0]) <= M[0] <= max(X[0], Y[0]) and min(X[1], Y[1]) <= M[1] <= max(X[1], Y[1])


def solve_problem_102():
    url = r"C:\Users\shay\PycharmProjects\pythonProject\EulerProject\problem102\p102_triangles.txt"
    list_of_all_sets = get_list_of_sets_from_text_separated_by_commas(url)
    count = 0
    for lis in list_of_all_sets:
        A = (lis[0], lis[1])
        B = (lis[2], lis[3])
        C = (lis[4], lis[5])
        if triangle_containment(A, B, C, (0, 0)):
            count += 1
    print(count)


if __name__ == "__main__":
    solve_problem_102()
