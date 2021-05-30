import vsketch
import numpy as np


class InterpolationSketch(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def coordinate_colums(self, colums_points):
        colums_points_unzipped = zip(*colums_points)
        colums_points_unzipped = list(colums_points_unzipped)
        x_tuples = colums_points_unzipped[0]
        y_tuples = colums_points_unzipped[1]
        return np.array(x_tuples), np.array(y_tuples)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a1", landscape=False)
        vsk.scale("1cm")

        all_colums_points = []

        for row in np.linspace(1, 15, 25):
            colums_points = []
            for col in range(25):
                x = row + vsk.random(0)
                y = col + vsk.random(1)
                # vsk.point(x, y)
                colums_points.append((x, y))
            all_colums_points.append(colums_points)

        for index in range(len(all_colums_points) - 1):
            current_colums_points = all_colums_points[index]
            next_colums_points = all_colums_points[index + 1]

            (
                x_coordinate_current_colum,
                y_coordinate_current_colum,
            ) = self.coordinate_colums(current_colums_points)

            x_coordinate_next_colum, y_coordinate_next_colum = self.coordinate_colums(
                next_colums_points
            )

            interpolation_steps = 5
            for interpolation_step in range(interpolation_steps):
                interpolated_x = vsk.lerp(
                    x_coordinate_current_colum,
                    x_coordinate_next_colum,
                    interpolation_step / interpolation_steps,
                )
                interpolated_y = vsk.lerp(
                    y_coordinate_current_colum,
                    y_coordinate_next_colum,
                    interpolation_step / interpolation_steps,
                )
                interpolated_coordinates = zip(interpolated_x, interpolated_y)

                # vsk.polygon(interpolated_coordinates)

                for step in interpolated_coordinates:
                    vsk.circle(step[1], step[0], step[0])
                    vsk.rotate(angle=0.001)

                    # vsk.rect(step[1], step[0], step[0], step[1])

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    InterpolationSketch.display()
